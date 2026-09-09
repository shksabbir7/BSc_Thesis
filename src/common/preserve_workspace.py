"""Create and verify non-destructive preservation assets; never ingest results.

The working-copy archive is diagnostic backup, not a new scientific release.
No extraction is performed. Original raw files are opened read-only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from src.common.seed import set_seed


def digest(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def git(*args: str) -> str:
    return subprocess.check_output(["git", "-C", str(ROOT), *args]).decode("utf-8")


def verify(manifest_path: Path) -> None:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for asset in manifest["assets"]:
        path = manifest_path.parent / asset["filename"]
        if path.stat().st_size != asset["bytes"] or digest(path) != asset["sha256"]:
            raise ValueError(f"Asset identity mismatch: {path.name}")
        if path.suffix == ".zip" and "members" in asset:
            expected = {row["path"]: row for row in asset["members"]}
            with zipfile.ZipFile(path) as archive:
                if len(archive.namelist()) != len(expected) or set(archive.namelist()) != set(expected):
                    raise ValueError(f"Member set mismatch: {path.name}")
                for name, row in expected.items():
                    with archive.open(name) as stream:
                        actual = hashlib.file_digest(stream, "sha256").hexdigest()
                    if actual != row["sha256"] or archive.getinfo(name).file_size != row["bytes"]:
                        raise ValueError(f"Member identity mismatch: {name}")
        print(f"VERIFIED {path.name}", flush=True)


def pack(output: Path, name: str, files: list[tuple[Path, str]], standing: str) -> dict:
    destination = output / name
    members = []
    with zipfile.ZipFile(destination, "x", zipfile.ZIP_DEFLATED,
                         compresslevel=1, strict_timestamps=False) as archive:
        for source, relative in sorted(files, key=lambda row: row[1]):
            if source.is_symlink() or not source.is_file():
                raise ValueError(f"Not a regular source file: {source}")
            if source.suffix.lower() in {".md", ".txt", ".json", ".jsonl", ".csv", ".py", ".js", ".ts", ".yaml", ".yml", ".html", ".log", ".xml"}:
                content = source.read_bytes()
                if re.search(rb"(?:AIza[0-9A-Za-z_-]{35}|gh[pousr]_[0-9A-Za-z]{30,}|github_pat_[0-9A-Za-z_]{40,}|-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----)", content):
                    raise ValueError(f"Credential-like content requires review: {relative}")
            row = {"path": relative, "bytes": source.stat().st_size, "sha256": digest(source)}
            archive.write(source, relative)
            if source.stat().st_size != row["bytes"] or digest(source) != row["sha256"]:
                raise ValueError(f"Source changed while packaging: {relative}")
            members.append(row)
    print(f"PACKED {name}: {len(members)} files", flush=True)
    return {"filename": name, "bytes": destination.stat().st_size,
            "sha256": digest(destination), "scientific_standing": standing, "members": members}


def main() -> None:
    set_seed()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--s5-archives", type=Path)
    parser.add_argument("--verify", type=Path)
    args = parser.parse_args()
    if args.verify:
        verify(args.verify)
        return
    if not args.output or not args.s5_archives:
        parser.error("--output and --s5-archives are required when creating assets")
    output = args.output.resolve()
    # Keep the output away from every input tree and refuse reuse.
    if output.parent != ROOT / "backup-release" or output.exists():
        parser.error("Use a new directory directly under backup-release/")
    output.mkdir(parents=True)
    head = git("rev-parse", "HEAD").strip()
    candidates = set(git("ls-files", "-z").split("\0"))
    candidates.update(git("ls-files", "--others", "--exclude-standard", "-z").split("\0"))
    exclude = {".git", ".claude", ".venv", ".pnpm-store", ".pytest_cache", ".tmp", "backup-release"}
    sources = []
    for name in sorted(candidates - {""}):
        parts = Path(name).parts
        path = ROOT / name
        if parts[0] in exclude or name.startswith("tmp/s5_posthoc_clean/"):
            continue
        if path.name.startswith(".env") and path.name != ".env.example":
            continue
        if any(part in {"node_modules", "__pycache__", ".git"} for part in parts):
            continue
        if path.is_file():
            sources.append((path, name))
    runtime = []
    for folder in ("data/raw", "data/cleaned", "data/annotation", "data/rag", "artifacts/verifier_b"):
        runtime.extend((p, p.relative_to(ROOT).as_posix()) for p in (ROOT / folder).rglob("*") if p.is_file())
    assets = [pack(output, "working-copy-diagnostic.zip", sources, "diagnostic_working_copy_not_scientific_ingestion"),
              pack(output, "restore-data-models.zip", runtime, "preservation_copy_original_standing_unchanged")]
    # These identities come from docs/s5_archive_manifest.md, not filenames alone.
    final_archives = [
        ("final_22124a8/s5_checkpoint.zip", "bd29b7a387df8c09f36d2c5be93f661c41d80ed66245027af3996f86e45a0ed2", "22124a816e5ecc9d6fa59c957bd939cfd311a28a", 5400),
        ("postrun_366df8c/s5_bn_postrun_results_complete.zip", "2270bdd0b3a4bbc88258c991648d463eb215b23cd17e3cdd298372eb1bbc499f", None, 5400),
    ]
    import shutil
    for relative, expected, commit, rows in final_archives:
        source = args.s5_archives / relative
        if digest(source) != expected:
            raise ValueError(f"Registered archive mismatch: {source.name}")
        destination = output / source.name
        shutil.copyfile(source, destination)
        member_commits = {}
        with zipfile.ZipFile(source) as archive:
            for name in archive.namelist():
                if name.endswith(".json"):
                    payload = json.loads(archive.read(name))
                    if isinstance(payload, dict):
                        provenance = payload.get("_provenance", {})
                        if provenance.get("git_commit"):
                            member_commits[name] = provenance["git_commit"]
        assets.append({"filename": source.name, "bytes": destination.stat().st_size,
                       "sha256": expected, "producing_commit": commit, "rows": rows,
                       "member_producing_commits": member_commits,
                       "scientific_standing": "final"})
    diagnostics = [(p, p.relative_to(args.s5_archives).as_posix())
                   for p in (args.s5_archives / "diagnostic_510a95c").rglob("*") if p.is_file()]
    assets.append(pack(output, "s5-superseded-diagnostics.zip", diagnostics, "diagnostic"))
    snapshot_path = output.parent / "environment-restoration.json"
    snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
    shutil.copyfile(snapshot_path, output / snapshot_path.name)
    freeze_path = output / "requirements-restoration.txt"
    freeze_path.write_text("\n".join(snapshot["pip_freeze"]) + "\n", encoding="utf-8", newline="\n")
    for path in (output / snapshot_path.name, freeze_path):
        assets.append({"filename": path.name, "bytes": path.stat().st_size,
                       "sha256": digest(path), "scientific_standing": "diagnostic_preservation_environment_not_final_run"})
    manifest = {"created_utc": datetime.now(timezone.utc).isoformat(),
                "packaging_base_commit": head, "packaging_worktree_dirty": bool(git("status", "--porcelain")),
                "source_note": "Working files are preserved as found, including existing uncommitted drafts and diagnostic results. This is not an integrity audit or promotion of those results.",
                "deleted_tracked_paths": git("ls-files", "--deleted").splitlines(),
                "excluded": ["credentials", "virtual environment", "node_modules", "agent worktrees", "tmp/s5_posthoc_clean duplicate checkout", "external Hugging Face model cache"],
                "assets": assets}
    manifest_path = output / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    verify(manifest_path)


if __name__ == "__main__":
    main()

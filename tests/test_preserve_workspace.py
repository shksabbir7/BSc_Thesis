import json
import zipfile

import pytest

from src.common.preserve_workspace import digest, pack, verify


def test_preservation_roundtrip_and_tamper_detection(tmp_path):
    source = tmp_path / "input.txt"
    source.write_text("Original evidence", encoding="utf-8")
    row = pack(tmp_path, "backup.zip", [(source, "data/input.txt")], "diagnostic")
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps({"assets": [row]}), encoding="utf-8")
    verify(manifest)
    assert source.read_text(encoding="utf-8") == "Original evidence"
    with (tmp_path / "backup.zip").open("ab") as stream:
        stream.write(b"changed")
    with pytest.raises(ValueError, match="Asset identity mismatch"):
        verify(manifest)


def test_duplicate_zip_members_rejected_even_with_matching_asset_hash(tmp_path):
    source = tmp_path / "input.txt"
    source.write_text("Evidence", encoding="utf-8")
    row = pack(tmp_path, "backup.zip", [(source, "input.txt")], "diagnostic")
    archive_path = tmp_path / "backup.zip"
    with zipfile.ZipFile(archive_path, "a") as archive:
        with pytest.warns(UserWarning):
            archive.writestr("input.txt", "Evidence")
    row.update(bytes=archive_path.stat().st_size, sha256=digest(archive_path))
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps({"assets": [row]}), encoding="utf-8")
    with pytest.raises(ValueError, match="Member set mismatch"):
        verify(manifest)


def test_existing_archive_not_overwritten(tmp_path):
    archive = tmp_path / "backup.zip"
    archive.write_bytes(b"existing backup")
    with pytest.raises(FileExistsError):
        pack(tmp_path, "backup.zip", [], "diagnostic")
    assert archive.read_bytes() == b"existing backup"

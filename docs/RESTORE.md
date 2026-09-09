# Restore this thesis on another machine

The Git repository and its Release assets serve different purposes. Clone the
repository for committed code, configs, chapters, figures, results and frozen
splits. Download the preservation assets for data, trained Verifier-B and the
original generation archives. A clone alone cannot run the full workflow.

## Locate and verify the backup

Repository: <https://github.com/alphapie77/BSc_Thesis>

Release assets: <https://github.com/alphapie77/BSc_Thesis/releases>

Use the release identified in `docs/STATUS.md`; do not assume a release has
been uploaded merely because locally prepared files exist. Download its
`manifest.json` and all named assets into one directory. In a fresh clone:

```powershell
git clone https://github.com/alphapie77/BSc_Thesis.git
cd BSc_Thesis
git config core.hooksPath .githooks
python src/common/preserve_workspace.py --verify C:/Downloads/thesis-backup/manifest.json
```

The verifier checks whole-file SHA-256 and sizes, plus the exact member set,
per-file sizes and hashes of the newly packaged ZIPs. It extracts nothing.
The original S5 ZIP identities are checked against the existing registered
hashes; passing a backup check is not a new scientific ingestion audit.

`working-copy-diagnostic.zip` preserves the local working files as they stood
when packaging, including unfinished chapters, conference work, presentations,
and uncommitted analyses. It is **not the source tree of the release tag** and
does not promote unreviewed results. Extract it to a separate empty directory,
then compare any desired work with the clone before incorporating it. The
manifest lists tracked deletions so missing files are not mistaken for loss.
The committed baseline remains recoverable from the recorded base commit.

## Data and trained artifacts

Inspect `restore-data-models.zip` in a separate staging directory. It contains
the original workbook, cleaned tables, annotation files, the R1 Chroma index
and trained Verifier-B files. Member paths specify their original repo-relative
locations. Restore needed files only into missing destinations; never overwrite
an existing raw file, frozen split or audited result. `data/raw/` stays read-only
for all repository scripts. Initial raw-data placement is an operator action.

The workbook's identity must be:

```text
SHA-256 8f972734fc3629427cdf8d01716aa817f7b325410b2fdd0f26cbc2e68506db9f
bytes   195186
```

Its actual filename uses spaces; the old `data/raw/README.md` example uses
underscores. Follow the manifest and `docs/dataset_card.md`, not that example.
Never regenerate `data/splits/split_map_v1.json`.

Keep `s5_checkpoint.zip`, `s5_bn_postrun_results_complete.zip` and
`s5-superseded-diagnostics.zip` outside the live results/resume directories.
See `docs/s5_archive_manifest.md` for their scientific standing. Do not unpack
an archive over `results/` or rerun the frozen 5,400-case experiment as setup.

## Python and frontend dependencies

The local preservation environment was Python 3.13.3 on Windows. The release
includes `environment-restoration.json` and a `requirements-restoration.txt`
derived from its `pip_freeze`. These describe the preservation-time environment,
not the final Kaggle run. The tracked `requirements.lock.txt` is older and must
not be relabelled as the current runtime or hand-edited.

```powershell
py -3.13 -m venv .venv
.venv/Scripts/python.exe -m pip install -r C:/Downloads/thesis-backup/requirements-restoration.txt
.venv/Scripts/python.exe -m pytest tests/test_split_map.py tests/test_s4_index.py tests/test_demo.py
.venv/Scripts/python.exe -m src.agents.build_index --config configs/s4_index.yaml --dry-run
```

The dependency install on a clean new machine must still be tested. Some
packages are platform-dependent; a Windows freeze is not a Linux environment
specification. For a historical scoring step, use that step's own recorded
runtime and producing commit, not the preservation environment.

Node.js 22 or later is required by the Windows launcher. Install the frontend
from its committed lockfile:

```powershell
cd interface
npm ci
cd ..
```

Do not commit `.venv`, `node_modules`, caches, local logs or credentials.

## Restore LaBSE and start the optional live demo

The Hugging Face cache is outside the thesis directory and is not in the backup.
The observed local LaBSE cache revision was
`836121a0533e5664b21c7aacc5d22951f2b8b25b`. Download that revision before using
the offline launcher, using the restored Python environment:

```powershell
.venv/Scripts/python.exe -c "from src.common.seed import set_seed; set_seed(); from huggingface_hub import snapshot_download; snapshot_download('sentence-transformers/LaBSE', revision='836121a0533e5664b21c7aacc5d22951f2b8b25b')"
```

The application requests the model by repository name, so ensure that the
cache's `main` reference resolves to that revision before offline startup.
If a newer revision is cached, do not silently substitute it; resolve the
cache/configuration explicitly and revalidate the index.

If the restored Chroma index is incompatible with the installed Chroma version,
build a new index in a separate checkout from the restored cleaned data using:

```powershell
.venv/Scripts/python.exe -m src.agents.build_index --config configs/s4_index.yaml --index-only
```

This mode checks the existing scientific manifest and does not rewrite it.
Gold-300 and R2 must remain absent from retrieval.

Create `.env` from `.env.example` and supply a new server-side Google API key.
Secrets are intentionally absent from backups. Run `start_demo.cmd`; the
launcher verifies artifact readiness before opening the UI. Verifier-B is only
for offline scoring and must never be loaded into the live loop. Hosted model
availability and API access can change; a preserved repository cannot guarantee
future hosted responses or reproduce their bytes.

## Updating the archive later

Commit reviewed source changes and keep the frozen results unchanged. Create
a new release/version for new preservation assets; never replace a verified
archive silently. Run `env_snapshot.py --out` into a new backup directory so
the historical environment/result files are not overwritten. Package into a
new directory beneath `backup-release/` with `preserve_workspace.py`, verify
it, and record the uploaded release identity in STATUS in the same commit as
the lab-notebook entry. Local caches can be cleaned only after the required
backup files have been downloaded and verified successfully.

The preservation choice was checked with two Consensus searches targeting
2025–2026. Klonoff et al. (2026), *Research Code Sharing in Support of Gold
Standard Science*, confirmed the need to pair versioned code with the data
snapshot and environment; it did not change the scientific pipeline. See
`docs/related_work.md` and `docs/references.bib`.

GitHub's own documentation supports distributing large binaries as Release
assets: <https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github>.

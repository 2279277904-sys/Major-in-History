# Image Processing Skill

A local Codex Skill for CPU background removal, transparent PNG cutouts, and
deterministic subject placement on an exact-size or exact-aspect-ratio canvas.

The default model is `birefnet-general`. The implementation always passes an
explicit allowlisted model to rembg and never silently falls back to BRIA.

## Supported platform

- Windows x64
- PowerShell 5.1 or later
- CPython 3.12
- CPU inference
- Codex desktop or another Codex installation with personal Skills support

The current MVP processes one image per invocation and outputs transparent PNG
only. GPU acceleration, batch processing, solid backgrounds, and JPEG/WebP
output are outside this release.

## Features

- Local inference after initial dependency and model downloads
- Exact pixel-size or aspect-ratio layout
- EXIF orientation handling and Lanczos resampling
- Low-memory soft-edge color decontamination
- Reusable rembg sessions and explicit model selection
- Atomic output writes with no overwrite by default
- Structured JSON output and stable exit codes
- Full Windows x64 CPython 3.12 dependency lock with wheel SHA-256 hashes
- Independent SHA-256 verification of the default model

## Install on a new computer

Clone the repository:

```powershell
git clone https://github.com/liweier12/image-processing-skill.git
cd image-processing-skill
```

Create the local virtual environment, install the hash-locked dependencies,
and download `birefnet-general`:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\image-processing\scripts\setup.ps1
```

The setup script looks for the Codex-bundled Python 3.12 by default. If it is
not discovered automatically, pass another CPython 3.12 executable:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\image-processing\scripts\setup.ps1 `
  -BasePython "<path-to-python-3.12.exe>"
```

Install the Skill as a Junction in the current user's personal Codex Skills
directory:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\image-processing\scripts\install-skill.ps1
```

Restart Codex after the first installation.

### Storage and network

A fresh default installation needs approximately 1.5 GB before temporary
download caches: about 0.46 GB for the Python environment and 0.93 GB for the
default General model. Setup requires internet access. After the model and
packages are present, normal processing can run offline.

Optional models are downloaded locally when first selected and are never
synchronized through Git.

## Keep computers in sync

On each computer, update the clone with:

```powershell
git pull --ff-only
```

The installed Junction points to the clone, so source updates are immediately
visible to Codex. Run `setup.ps1` again when `requirements.lock` changes. Each
computer maintains its own `.venv` and `.models` directories.

## Usage

Invoke the Skill in Codex with `$image-processing`, or call the entry point:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass `
  -File .\image-processing\scripts\process-image.ps1 `
  --input "<input-image>" `
  --output "<output.png>" `
  --width 1200 `
  --height 1200
```

Use `--aspect-ratio 3:4` instead of width and height when only a ratio is
required. See `image-processing/references/cli-contract.md` for the complete
JSON and exit-code contract.

## Privacy

Image processing runs locally. User images, generated outputs, model files,
virtual environments, logs, local agent state, and common private-data formats
are ignored by Git. A tracked-file privacy audit runs in CI and can be run
locally before staging:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\privacy-audit.ps1
```

An ignore rule is not a security boundary: always inspect the exact staged
file list and diff before committing.

## Development

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD = "1"
.\image-processing\.venv\Scripts\python.exe -m pytest -q -p no:cacheprovider `
  --basetemp .\.test-venv\pytest-temp
```

The direct runtime and validation dependencies are declared in
`image-processing/requirements.in`. The committed lock is platform-specific
and must be regenerated for Windows x64 CPython 3.12 when dependencies change.

## Security

Report suspected vulnerabilities through GitHub private vulnerability
reporting, not through a public issue. See `SECURITY.md`.

## License scope

Repository-authored code and documentation are MIT licensed. Third-party
packages and model weights retain their own terms. This repository does not
contain or redistribute model weights. See `THIRD_PARTY_NOTICES.md` and
`image-processing/references/model-licenses.md` before redistribution or
commercial deployment.

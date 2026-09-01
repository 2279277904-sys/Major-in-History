param(
    [string]$BasePython,
    [switch]$SkipModelDownload
)

$ErrorActionPreference = "Stop"
$skillRoot = Split-Path -Parent $PSScriptRoot
$venvDir = Join-Path $skillRoot ".venv"
$venvPython = Join-Path $venvDir "Scripts\python.exe"
$requirements = Join-Path $skillRoot "requirements.lock"
$modelsDir = Join-Path $skillRoot ".models"
$defaultModel = Join-Path $modelsDir "birefnet-general.onnx"
$defaultModelSha256 = "58f621f00f5d756097615970a88a791584600dcf7c45b18a0a6267535a1ebd3c"

if (-not $BasePython) {
    $BasePython = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
}
if (-not (Test-Path -LiteralPath $BasePython -PathType Leaf)) {
    throw "Codex bundled Python was not found at '$BasePython'. Pass -BasePython explicitly."
}
if (-not (Test-Path -LiteralPath $requirements -PathType Leaf)) {
    throw "Pinned requirements are missing: '$requirements'."
}

$version = & $BasePython -c "import sys; print('.'.join(map(str, sys.version_info[:3])))"
if ($LASTEXITCODE -ne 0 -or -not $version.StartsWith("3.12.")) {
    throw "Python 3.12 is required; found '$version'."
}

if (-not (Test-Path -LiteralPath $venvPython -PathType Leaf)) {
    & $BasePython -m venv $venvDir
    if ($LASTEXITCODE -ne 0) { throw "Failed to create the local virtual environment." }
}

& $venvPython -m pip install --disable-pip-version-check --only-binary=:all: --require-hashes -r $requirements
if ($LASTEXITCODE -ne 0) { throw "Dependency installation failed." }
& $venvPython -m pip check
if ($LASTEXITCODE -ne 0) { throw "Installed dependency validation failed." }

New-Item -ItemType Directory -Path $modelsDir -Force | Out-Null
$env:REMBG_HOME = $modelsDir
$env:U2NET_HOME = $modelsDir

if (-not $SkipModelDownload) {
    & $venvPython -c "from rembg.sessions.birefnet_general import BiRefNetSessionGeneral; print(BiRefNetSessionGeneral.download_models())"
    if ($LASTEXITCODE -ne 0) { throw "Failed to download or validate birefnet-general." }
    if (-not (Test-Path -LiteralPath $defaultModel -PathType Leaf)) {
        throw "Model setup completed without '$defaultModel'."
    }
    $actualModelSha256 = (Get-FileHash -LiteralPath $defaultModel -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($actualModelSha256 -ne $defaultModelSha256) {
        throw "birefnet-general SHA-256 mismatch. Expected '$defaultModelSha256'; found '$actualModelSha256'."
    }
}

& $venvPython -c "import onnxruntime, PIL, rembg; print('environment ready')"
if ($LASTEXITCODE -ne 0) { throw "Installed environment validation failed." }

Write-Output "Setup complete: $skillRoot"

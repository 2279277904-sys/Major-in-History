$ErrorActionPreference = "Stop"

$skillRoot = Split-Path -Parent $PSScriptRoot
$pythonExe = Join-Path $skillRoot ".venv\Scripts\python.exe"
$modelsDir = Join-Path $skillRoot ".models"

if (-not (Test-Path -LiteralPath $pythonExe -PathType Leaf)) {
    $payload = [ordered]@{
        status = "error"
        code = "environment_error"
        message = "Local environment is missing. Run scripts/setup.ps1 first."
        elapsedMs = 0
    }
    $payload | ConvertTo-Json -Compress
    exit 3
}

$env:REMBG_HOME = $modelsDir
$env:U2NET_HOME = $modelsDir
& $pythonExe (Join-Path $PSScriptRoot "process_image.py") @args
exit $LASTEXITCODE

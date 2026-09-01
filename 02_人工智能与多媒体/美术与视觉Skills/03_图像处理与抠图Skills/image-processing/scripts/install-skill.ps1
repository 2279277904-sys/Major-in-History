param([switch]$Force)

$ErrorActionPreference = "Stop"
$sourceSkill = (Resolve-Path -LiteralPath (Split-Path -Parent $PSScriptRoot)).Path
$sourcePython = Join-Path $sourceSkill ".venv\Scripts\python.exe"
$sourceManifest = Join-Path $sourceSkill "SKILL.md"
$skillsRoot = Join-Path $env:USERPROFILE ".codex\skills"
$destination = Join-Path $skillsRoot "image-processing"
$expectedPrefix = [IO.Path]::GetFullPath($skillsRoot).TrimEnd('\') + '\'
$destinationFull = [IO.Path]::GetFullPath($destination)

if (-not $destinationFull.StartsWith($expectedPrefix, [StringComparison]::OrdinalIgnoreCase)) {
    throw "Refusing to install outside the personal Codex skills directory."
}
if (-not (Test-Path -LiteralPath $sourceManifest -PathType Leaf)) {
    throw "Skill manifest is missing: '$sourceManifest'."
}
if (-not (Test-Path -LiteralPath $sourcePython -PathType Leaf)) {
    throw "Skill environment is missing. Run scripts/setup.ps1 before installation."
}

New-Item -ItemType Directory -Path $skillsRoot -Force | Out-Null
if (Test-Path -LiteralPath $destination) {
    if (-not $Force) {
        throw "Destination already exists: '$destination'. Use -Force to back it up first."
    }
    $stamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $backup = "$destination.backup-$stamp"
    if (Test-Path -LiteralPath $backup) { throw "Backup destination already exists: '$backup'." }
    Move-Item -LiteralPath $destination -Destination $backup
    Write-Output "Existing destination backed up to: $backup"
}

New-Item -ItemType Junction -Path $destination -Target $sourceSkill | Out-Null
$installed = Get-Item -LiteralPath $destination
if ($installed.LinkType -ne "Junction") { throw "Installation did not create a Junction." }
Write-Output "Installed Junction: $destination -> $sourceSkill"

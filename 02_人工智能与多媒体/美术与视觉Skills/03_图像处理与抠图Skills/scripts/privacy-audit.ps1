param([string]$RepositoryRoot = (Split-Path -Parent $PSScriptRoot))

$ErrorActionPreference = "Stop"
$root = (Resolve-Path -LiteralPath $RepositoryRoot).Path
$tracked = @(& git -C $root ls-files --cached --others --exclude-standard)
if ($LASTEXITCODE -ne 0) { throw "Unable to enumerate tracked files." }

$forbiddenExtensions = @(
    ".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".tif", ".tiff", ".heic",
    ".pdf", ".onnx", ".log", ".csv", ".xls", ".xlsx", ".db", ".sqlite", ".sqlite3",
    ".pem", ".key", ".pfx", ".p12", ".kdbx"
)
$forbiddenNames = @(".env", "id_rsa", "id_ed25519")
$textPatterns = [ordered]@{
    "Windows absolute path" = "(?i)[a-z]:\\"
    "User home path" = ("(?i)(?:/" + "Users/|/" + "home/)[^/\s<>]+")
    "Private key" = "-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"
    "GitHub token" = "(?i)(?:ghp_|github_pat_)[a-z0-9_]+"
    "OpenAI token" = "(?i)sk-[a-z0-9_-]{16,}"
    "AWS access key" = "AKIA[0-9A-Z]{16}"
    "Email address" = "(?i)[a-z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?(?:\.[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)+"
}

$failures = [System.Collections.Generic.List[string]]::new()
foreach ($relative in $tracked) {
    $extension = [IO.Path]::GetExtension($relative).ToLowerInvariant()
    $name = [IO.Path]::GetFileName($relative).ToLowerInvariant()
    if ($extension -in $forbiddenExtensions -or $name -in $forbiddenNames) {
        $failures.Add("Forbidden tracked file: $relative")
        continue
    }
    $fullPath = Join-Path $root $relative
    $content = Get-Content -LiteralPath $fullPath -Raw -ErrorAction Stop
    foreach ($entry in $textPatterns.GetEnumerator()) {
        if ($content -match $entry.Value) {
            $failures.Add("$($entry.Key) found in: $relative")
        }
    }
}

if ($failures.Count -gt 0) {
    $failures | Sort-Object -Unique | ForEach-Object { Write-Error $_ }
    throw "Privacy audit failed with $($failures.Count) finding(s)."
}

Write-Output "Privacy audit passed for $($tracked.Count) publishable file(s)."

param(
    [Parameter(Mandatory = $true)]
    [ValidateNotNullOrEmpty()]
    [string]$Message
)

$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot

git add --all
if ($LASTEXITCODE -ne 0) { throw 'git add failed' }

git diff --cached --quiet
if ($LASTEXITCODE -eq 0) {
    Write-Output 'No changes to synchronize.'
    exit 0
}
if ($LASTEXITCODE -ne 1) { throw 'git diff failed' }

git commit -m $Message
if ($LASTEXITCODE -ne 0) { throw 'git commit failed' }

git push origin HEAD:main
if ($LASTEXITCODE -ne 0) { throw 'git push failed; the local commit is retained.' }

git status --short --branch
if ($LASTEXITCODE -ne 0) { throw 'git status failed' }

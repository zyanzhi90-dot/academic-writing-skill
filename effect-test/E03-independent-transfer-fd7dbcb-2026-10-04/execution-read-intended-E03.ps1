$OutputEncoding = [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$records = @(
$lines = @(Get-Content -LiteralPath 'D:\桌面\正文writing skill\effect-test\E03-independent-transfer-fd7dbcb-2026-10-04\coordinator\intended-inputs\inputs\task.md' -Encoding UTF8)
[pscustomobject]@{path='inputs/task.md';lines=@($lines | ForEach-Object { '{0}' -f $_ });line_count=$lines.Count}
$lines = @(Get-Content -LiteralPath 'D:\桌面\正文writing skill\effect-test\E03-independent-transfer-fd7dbcb-2026-10-04\coordinator\intended-inputs\inputs\scientific-facts.md' -Encoding UTF8)
[pscustomobject]@{path='inputs/scientific-facts.md';lines=@($lines | ForEach-Object { '{0}' -f $_ });line_count=$lines.Count}
$lines = @(Get-Content -LiteralPath 'D:\桌面\正文writing skill\effect-test\E03-independent-transfer-fd7dbcb-2026-10-04\coordinator\intended-inputs\inputs\personal-experience.txt' -Encoding UTF8)
[pscustomobject]@{path='inputs/personal-experience.txt';lines=@($lines | ForEach-Object { '{0}' -f $_ });line_count=$lines.Count}
$lines = @(Get-Content -LiteralPath 'D:\桌面\正文writing skill\effect-test\E03-independent-transfer-fd7dbcb-2026-10-04\coordinator\intended-inputs\inputs\core-requirements.txt' -Encoding UTF8)
[pscustomobject]@{path='inputs/core-requirements.txt';lines=@($lines | ForEach-Object { '{0}' -f $_ });line_count=$lines.Count}
)
ConvertTo-Json -InputObject @($records) -Depth 6

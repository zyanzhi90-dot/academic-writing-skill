$OutputEncoding = [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$records = @(
$lines = @(Get-Content -LiteralPath 'C:\Users\user2\AppData\Local\Temp\e03-independent-abstract-transfer-mtvjs6vq\materials\inputs\task.md' -Encoding UTF8)
[pscustomobject]@{path='inputs/task.md';lines=@($lines | ForEach-Object { '{0}' -f $_ });line_count=$lines.Count}
$lines = @(Get-Content -LiteralPath 'C:\Users\user2\AppData\Local\Temp\e03-independent-abstract-transfer-mtvjs6vq\materials\inputs\scientific-facts.md' -Encoding UTF8)
[pscustomobject]@{path='inputs/scientific-facts.md';lines=@($lines | ForEach-Object { '{0}' -f $_ });line_count=$lines.Count}
$lines = @(Get-Content -LiteralPath 'C:\Users\user2\AppData\Local\Temp\e03-independent-abstract-transfer-mtvjs6vq\materials\inputs\personal-experience.txt' -Encoding UTF8)
[pscustomobject]@{path='inputs/personal-experience.txt';lines=@($lines | ForEach-Object { '{0}' -f $_ });line_count=$lines.Count}
$lines = @(Get-Content -LiteralPath 'C:\Users\user2\AppData\Local\Temp\e03-independent-abstract-transfer-mtvjs6vq\materials\inputs\core-requirements.txt' -Encoding UTF8)
[pscustomobject]@{path='inputs/core-requirements.txt';lines=@($lines | ForEach-Object { '{0}' -f $_ });line_count=$lines.Count}
)
ConvertTo-Json -InputObject @($records) -Depth 6

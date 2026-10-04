$OutputEncoding = [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$records = @(
$lines = @(Get-Content -LiteralPath 'C:\Users\user2\AppData\Local\Temp\polishing-aqgf6xmc\materials\inputs\task.md' -Encoding UTF8)
[pscustomobject]@{path='inputs/task.md';lines=@($lines | ForEach-Object { '{0}' -f $_ });line_count=$lines.Count}
$lines = @(Get-Content -LiteralPath 'C:\Users\user2\AppData\Local\Temp\polishing-aqgf6xmc\materials\inputs\scientific-facts.md' -Encoding UTF8)
[pscustomobject]@{path='inputs/scientific-facts.md';lines=@($lines | ForEach-Object { '{0}' -f $_ });line_count=$lines.Count}
$lines = @(Get-Content -LiteralPath 'C:\Users\user2\AppData\Local\Temp\polishing-aqgf6xmc\materials\inputs\personal-experience.txt' -Encoding UTF8)
[pscustomobject]@{path='inputs/personal-experience.txt';lines=@($lines | ForEach-Object { '{0}' -f $_ });line_count=$lines.Count}
$lines = @(Get-Content -LiteralPath 'C:\Users\user2\AppData\Local\Temp\polishing-aqgf6xmc\materials\inputs\core-requirements.txt' -Encoding UTF8)
[pscustomobject]@{path='inputs/core-requirements.txt';lines=@($lines | ForEach-Object { '{0}' -f $_ });line_count=$lines.Count}
$lines = @(Get-Content -LiteralPath 'C:\Users\user2\AppData\Local\Temp\polishing-aqgf6xmc\materials\inputs\abstract-writing-method.txt' -Encoding UTF8)
[pscustomobject]@{path='inputs/abstract-writing-method.txt';lines=@($lines | ForEach-Object { '{0}' -f $_ });line_count=$lines.Count}
$lines = @(Get-Content -LiteralPath 'C:\Users\user2\AppData\Local\Temp\polishing-aqgf6xmc\materials\inputs\current-draft.md' -Encoding UTF8)
[pscustomobject]@{path='inputs/current-draft.md';lines=@($lines | ForEach-Object { '{0}' -f $_ });line_count=$lines.Count}
)
ConvertTo-Json -InputObject @($records) -Depth 6

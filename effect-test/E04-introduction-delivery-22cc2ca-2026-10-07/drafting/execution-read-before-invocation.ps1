$OutputEncoding = [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$records = @(
$lines = @(Get-Content -LiteralPath 'C:\Users\user2\AppData\Local\Temp\drafting-csgds3bw\materials\inputs\task.md' -Encoding UTF8)
[pscustomobject]@{path='inputs/task.md';lines=@($lines | ForEach-Object { '{0}' -f $_ });line_count=$lines.Count}
$lines = @(Get-Content -LiteralPath 'C:\Users\user2\AppData\Local\Temp\drafting-csgds3bw\materials\inputs\scientific-facts.md' -Encoding UTF8)
[pscustomobject]@{path='inputs/scientific-facts.md';lines=@($lines | ForEach-Object { '{0}' -f $_ });line_count=$lines.Count}
$lines = @(Get-Content -LiteralPath 'C:\Users\user2\AppData\Local\Temp\drafting-csgds3bw\materials\inputs\personal-experience.txt' -Encoding UTF8)
[pscustomobject]@{path='inputs/personal-experience.txt';lines=@($lines | ForEach-Object { '{0}' -f $_ });line_count=$lines.Count}
$lines = @(Get-Content -LiteralPath 'C:\Users\user2\AppData\Local\Temp\drafting-csgds3bw\materials\inputs\core-requirements.txt' -Encoding UTF8)
[pscustomobject]@{path='inputs/core-requirements.txt';lines=@($lines | ForEach-Object { '{0}' -f $_ });line_count=$lines.Count}
$lines = @(Get-Content -LiteralPath 'C:\Users\user2\AppData\Local\Temp\drafting-csgds3bw\materials\inputs\introduction-method.txt' -Encoding UTF8)
[pscustomobject]@{path='inputs/introduction-method.txt';lines=@($lines | ForEach-Object { '{0}' -f $_ });line_count=$lines.Count}
$lines = @(Get-Content -LiteralPath 'C:\Users\user2\AppData\Local\Temp\drafting-csgds3bw\materials\inputs\current-author-adjustment.txt' -Encoding UTF8)
[pscustomobject]@{path='inputs/current-author-adjustment.txt';lines=@($lines | ForEach-Object { '{0}' -f $_ });line_count=$lines.Count}
$lines = @(Get-Content -LiteralPath 'C:\Users\user2\AppData\Local\Temp\drafting-csgds3bw\materials\inputs\background-facts.md' -Encoding UTF8)
[pscustomobject]@{path='inputs/background-facts.md';lines=@($lines | ForEach-Object { '{0}' -f $_ });line_count=$lines.Count}
$lines = @(Get-Content -LiteralPath 'C:\Users\user2\AppData\Local\Temp\drafting-csgds3bw\materials\inputs\citation-facts.md' -Encoding UTF8)
[pscustomobject]@{path='inputs/citation-facts.md';lines=@($lines | ForEach-Object { '{0}' -f $_ });line_count=$lines.Count}
$lines = @(Get-Content -LiteralPath 'C:\Users\user2\AppData\Local\Temp\drafting-csgds3bw\materials\inputs\accepted-abstract.en.txt' -Encoding UTF8)
[pscustomobject]@{path='inputs/accepted-abstract.en.txt';lines=@($lines | ForEach-Object { '{0}' -f $_ });line_count=$lines.Count}
)
ConvertTo-Json -InputObject @($records) -Depth 6

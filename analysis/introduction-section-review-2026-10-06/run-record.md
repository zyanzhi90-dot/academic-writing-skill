# 本轮读取与提交记录

- 日期：2026-10-06；项目：academic-writing-skill。
- 启动分支：`main`；`git pull --ff-only origin main` 成功，返回 `Already up to date.`；基线：`623b055879967c7e8bc6528b213b00f96baaee0d`。
- 启动工作区已存在作者对《核心要求.txt》的修改。该文件与另外两份作者要求均按当前内容读取；本轮不改写作者输入，启动读取时的 SHA-256 见 `source-provenance.json`。
- 通过现有共用范例索引的四个 PDF 定义定位 B15–B18。本轮直接重新打开原 PDF，不使用既有分析报告或效果测试输出作为结论依据。
- `read_sources.py` 使用 PyMuPDF 1.28.2 提取原始页面文本块、坐标及页码；Poppler `pdftoppm` 以 140 dpi 渲染 P17、P05、Fuzzy2023 各前两页与 ESO2017 前三页，均成功。
- 逐篇读取完整页面文本，并通过图像查看工具查看全部九张页面图像。由双栏与段首缩进确认跨栏／跨页续段、贡献列表以及下一节边界。Introduction 中正文段落分别为 9、9、4、9；贡献条目分别为 0、3、3、3。
- 整理后的全节英文与原块 ID 对应保存在四个 `*-introduction.md` 和 `curated-introductions.json`。只恢复版面；行末断词处理记录在 `layout-normalization.json`。整理时按页面图像校正右栏坐标门限，并保留 error-integral、time-delay、multiple-output 等恰逢行末的语义连字符；原始提取文件始终保留。
- `source-audit.json` 记录来源覆盖核对：按阅读顺序连接所选文本块，与全部整理单元去除版面空白后内容一致；40 个单元无内容删漏。四份 PDF、三份作者要求及两个索引文件的 SHA-256 与实际读取时一致。
- 同步前已跟踪文件的差异仅为启动时已有的《核心要求.txt》作者更新；本轮新增材料全部在本目录。没有改动 Skill、执行器或既有分析／测试记录，没有安装、写作／润色会话、效果测试或 E04 对照。
- 按项目 `AGENTS.md`，以 `./sync.ps1 -Message "Analyze complete B15-B18 Introduction organization"` 提交并推送本目录及已存在的作者要求更新。提交后在会话中核对工作区与本地／远端主分支，最终状态以 Git 和同步输出为准。

交付报告为 `report.md`。本轮的原文事实、默认取向和单篇特殊处理分开记录；提交后停止，交负责人对照出版 PDF 验收。

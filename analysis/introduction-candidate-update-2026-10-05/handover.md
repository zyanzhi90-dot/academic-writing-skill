# 引言候选改造交接

本轮已把 P17／A06、P05／A07、Fuzzy2023／A02、ESO2017／A04 的引言学习依据落实到候选按需范例层。P17 保持默认表达锚点，其他三篇按作者当前科学关系补充。Writing 详细引言指南中的真实技术继承、组织顺序和句式示意冲突已就地协调。改造只涉及五个候选文件；两端入口、工作流、科学英文核心及原有22张范例卡保留。

工作起点为 `54f9e39773e92c8ced719d4bcd4d01db6195980b`，本地与 `origin/main` 一致且工作区干净。依据为该提交的 [分析报告](../introduction-learning-2026-10-05/report.md)、四篇完整引言副本及最新《核心要求.txt》《我自己的经验和做法.txt》。作者输入与历史分析未改动；`root1.pdf` 的先前缺失状态未被替代版本补齐，本轮也没有用 E04 评价生成规则。

## 实际改动与执行动作

| 文件／位置 | 具体问题、所作修改 | 改变的读取／写作判断及预期作用 |
|---|---|---|
| [新增 Shared 引言范例](../../skill-candidate/nature-shared/core/robotics-introduction-examples.md)，Selection／B15–B18 | 已有 A 卡只有摘要，B01 是全文接口，不能代替四篇整节引言。新增四张 B 卡，包含整节段落推进、25处原文引文、页码／段首／DOI及迁移分析 | 读当前任务相关的实际段落及连续英文，用于作者自己的设计理由、作用、对象交接和保证。先按 P17 取默认英文，再选补充，不要求全部卡片或原 PDF |
| [共用范例索引](../../skill-candidate/nature-shared/core/robotics-writing-examples.md)，权威范围／Introduction reference selection／Source conventions／引言任务行 | 原引言任务只指 B02／B03；“cards below”为单文件权威。新增任务链接及 P17 默认选择，说明任务链接卡也是权威范例，区分旧卡与新引言来源 | Writing 和 Polishing 沿已有共同入口发现同一份引言证据；原 B02／B03及摘要选例仍可使用，不复制两份范例或新增工作流 |
| [Shared 入口](../../skill-candidate/nature-shared/SKILL.md)，robotics examples 段 | 原说明只把 `robotics-writing-examples.md` 认作 sole example authority，和新任务链接结构冲突。改为索引自身的卡片及 task-linked references | 使已有 Shared 依赖说明允许按索引读取新卡；项目报告和 PDF 仍是可选回查，不成为正常使用必需材料 |
| [Shared manifest](../../skill-candidate/nature-shared/manifest.yaml)，core.on_demand | 新资源须在 Shared 声明中可核对。登记由共用索引选择的引言参考及 B15–B18 范围 | 声明资源及读取条件，保持 `always_load: []`；没有把四篇加成两端常驻依赖或新增顶层路由 |
| [Writing 详细引言指南](../../skill-candidate/nature-writing/references/introduction.md)，Goal／logic map／backward question／Forward story／Section Skeleton | 原图将所有前作设为 SOTA failure，问题预设无成熟方案，顺序标为必须依次写，且 skeleton 有 Experiment。改为前作能力及条件、具体未解决问题，明确可选组织及贡献所需评价预览 | 防止制造缺口，允许 P17、Fuzzy、ESO 的局部动机—设计后继续解释另一条件；不设固定段数、段末gap、列表或结果报告配额。主指南仍保留原有不同组织 variants |
| 同一 Writing 指南，Prior work and the present advance／Not Recommended rationale | 原警告要求即使实际增量也不要这样写，另有 shallow／incremental 并列评价。改为如实说明继承及改变的条件／机制，删除无助贡献的开发历史，并以机制／范围是否清楚评估表述 | 让实际改进保持科学真实，同时交代为何需要、如何起作用；不为 novelty 隐藏前作或夸大失效范围 |
| 同一 Writing 指南，Opening／Pipeline Version 3–4 句式示意 | Given／Inspired／Considering 起句与已有完整主谓及分词开头约束冲突，This leads to ... and achieves ... 易将不同作用合并。改为有科学主语及限定动词的输入／原因／设计句，要求 named design 的支持关系 | 保留输入、技术继承和设计理由，使用符合作者要求的具体实现；复用共用检查，不另设句法规则。原文示例文件作为来源证据保留，不改历史摘录，其文字明确不能覆盖共用表达约束 |

上述作用是改动的设计理由，尚不是实测写作收益。新增卡片包含完整段落及明确标注的连续句组，保留四篇的不同组织。源文 Here、分词开头、分号、语言错误和科学概括保留在引文中并给出迁移边界；作者新稿沿既有表达与科学保障实现。没有从源文继承 DMP／NN／BLF／ESO 作为作者必选技术，也没有把三条贡献、九段、双组件、roadmap 或实验清单固化。

## 两端实际文件读取路径

两端现有 `SKILL.md` 和 manifest 中的 robotics 条件均已指向共用索引，没有修改它们。对机器人中心引言的实现链为：

`nature-writing 或 nature-polishing/SKILL.md → 本端 manifest 与原有 core／intro／language／journal fragments → nature-shared/core/robotics-writing-examples.md 的共用说明及引言任务链接 → robotics-introduction-examples.md 的 Selection 和所选 B15–B18`。

Writing 引言另沿其已有路径读 `references/introduction.md`。两端继续按原条件读取 `robotics-main-text.md`，并从 `always_load` 读取 `scientific-expression.md`；Polishing 继续诊断后选例、使用自身输出与检查，不新增 Writing 交接或生成步骤。

[implementation-check.json](implementation-check.json) 记录本地候选及候选单独复制到临时位置后的真实文件读取、SHA-256和所选文本指纹。核对任务轴和选卡是显式解析的，不是模型自然语言路由测试。原始文件字节为完整性核对而读取，记录另区分用于当前任务的共用说明／所选卡片及未选卡片；这不声称模型只关注所选文本。

每端分别核对默认 B15、中文任务／学习条件补充 B16、联合性能补充 B17、传感／补偿补充 B18；另外核对机器人摘要和非机器人引言不引入新参考。临时环境只有候选三包，没有项目分析或原 PDF。所有必需读取均在候选内完成；四个 PDF 链接在该环境不可用，是可选回查而非执行依赖。索引与新增范例也通过实际 PowerShell `Get-Content -Raw -Encoding UTF8` 核对内容。

这证明声明路径和文件可读取、内容自足且可以按既有索引选择；不证明自主模型实际选卡、采用英文、检查可靠或写作质量稳定。

## 来源与候选完整性核对

[quote-provenance.json](quote-provenance.json) 将25处引文逐项对应到 `54f9e39` 已核对原文的论文、段落和 PDF 块，所有引文为完整原段或连续片段，无科学改写。两处 Fuzzy 首段非连续摘录已明确标注分隔。四份 PDF 哈希与此前来源记录一致。Git 源文与工作副本只可能有 LF／CRLF 排版差异，按换行规范化核对，未覆盖历史源文。

候选完整性核对保留原22张卡的全文，保留全部其他候选文件，新增文件仅一份。三个包的 skill-creator `quick_validate.py`、manifest 所声明路径、严格 UTF-8 与 relocated-candidate 文件读取均完成；这些是实施完整性核对，不是效果测试。核对程序复用已有 manifest 检查函数，未运行其会写历史记录的主入口。新证据均放在本目录。

[candidate-files.json](candidate-files.json) 记录本轮完成实施核对后的全部候选内容哈希，作为改造内容冻结依据。版本标签保留原值，实际候选身份由本轮提交及内容指纹确定。冻结后不以本轮材料补写效果验收。

## 效果待验与验收边界

| 项目 | 本轮状态 | 尚需何种证据 |
|---|---|---|
| Drafting | 未运行／未评价 | 隔离正常请求下是否按科学关系选择英文，首次输出是否忠实且解释贡献必要关系 |
| 无逐句反馈 Polishing | 未运行／未评价 | 是否独立发现并修正实际问题，同时保留已经成立的科学含义和符合作者风格的表达 |
| 组合交付 | 未运行／未评价 | 各阶段首次输入／输出／读取记录分别保留后，最终交付的必要性、科学忠实与具体英文 |
| 迁移及稳定性 | 未评价 | 新任务及重复执行的独立证据，不能把这四篇已知范例或 E04 个案补记通过 |

效果核对如获后续授权，应只给写作端正常使用的候选及声明依赖、作者原始科学材料与标准请求，单独保存各阶段首次输出和读取记录，不输入本交接的诊断或预期答案。负责人本轮可以先独立验收改动与来源；读路径核对和实施完成不代替效果。

本轮未安装 Skill、未调用模型或效果测试、未修改历史输出、未推进其他章节。提交同步后停止。

# E01 Abstract 独立 Drafting 复测记录

本轮以 `gpt-6.1-sol / high` 在全新独立会话中只执行一次摘要起草，原样保存英文摘要、中文翻译及执行者最终交付的附加内容。所有中间消息和工具返回另存于原始事件日志。未挑选重跑结果、润色、反馈修订或人工改写输出，未修改或安装 Skill，未推进其他部分。本记录只核对运行、隔离和留存，不评价稿件科学表达或英文质量。

## 冻结材料

- [materials/inputs/task.md](materials/inputs/task.md)：本轮 Abstract-only 任务，不额外指定主要参考、摘要结构、句数或句式。参考选择和表达要求由冻结 Skill 及作者输入提供。
- [materials/inputs/scientific-facts.md](materials/inputs/scientific-facts.md)：已验收 `effect-test/E01-abstract-materials-2026-10-02/科学事实包.md` 的原样字节副本。
- [materials/inputs/personal-experience.txt](materials/inputs/personal-experience.txt)：项目《我自己的经验和做法.txt》的原样字节副本。
- `materials/skill-candidate/`：从提交 `11e900cc53ccee25f5f9d6b93971551b87f2e87a` 的 Git blob 提取 nature-writing 与 nature-shared，99文件逐字节一致，无隔离改写。版本为 writing `1.5.1-rc.5`、shared `1.6.1-rc.4`；本轮不提供 Polishing 包。
- `materials/文献资料/`：当前学习目录的21篇 PDF 原样副本。`materials/analysis/reading/`：仅从这21篇当前 PDF 使用 `pdftotext -raw -enc UTF-8` 新提取的对应文本，保留261个 PDF 页标记，无提取警告、无文字润色。15篇现存旧论文沿用原 P 编号，6篇新增论文按 PDF 文件名定位；不复制已删除论文的旧提取文本，也不改项目原提取目录。

合计144个允许文件：99候选文件、3输入、21 PDF、21提取文本。完整19张候选范例卡可用，不排除 A06／B01。冻结候选中保留的历史正文引文及来源声明不改；3条指向旧测试材料中论文 PDF 的可选链接未额外补入本次材料，当前21篇目录可用，旧测试目录及其输出／评价不在允许输入范围。摘要所用四篇主要参考的当前 PDF 均在本次学习目录内。

逐文件哈希、来源、PDF—提取文本对应关系、工具哈希、准备时项目提交及保护快照见 [frozen-materials.json](frozen-materials.json)。不复制目标原文、目标提取文本、来源定位、准备／诊断／评价材料、旧输出及其表达衍生材料。本 README、运行工具及留存记录也不进入写作材料目录。

## 独立会话与唯一调用

复用已验收 E01 首次运行方式，使用项目外新建的材料目录、全新 `codex exec --ephemeral --ignore-user-config --ignore-rules` 会话。禁用自动项目说明、网络搜索、53个发现的现装 Skill 入口及 plugins、remote_plugin、apps、hooks、memories、multi_agent；本次进程限制不改用户配置或现装文件。CLI 为 `codex-cli 0.159.2`，指定模型 `gpt-6.1-sol`、推理 `high`，无模型替换或自动重跑。执行提示要求 UTF-8 读取，先读范例共用说明和索引，再按需选择卡片及原文；未在提示中指定参考卡片或写法。

隔离依据为独立材料目录、自动加载限制、允许文件边界及实际命令核对；不宣称操作系统层面的目录外读权限隔离。原始记录反映执行行为，不把提示要求当作实际遵循证明。

[execute_once.py](execute_once.py) 仅在本次新目录中作必要适配：候选提交、推理设置及当前21篇文本准备。复用既有 P17 工具的哈希、清单、CLI 定位与收集函数；旧工具仅供留存端调用，没有交给写作执行者，未调用旧写作任务或读取旧稿，旧记录不改。`prepare` 拒绝覆盖材料，`run` 拒绝已存在的 `drafting/`，只调用一次；唯一调用退出码 **0**，耗时 **213.70秒**。

## 输出及证据文件

| 文件 | 留存内容 |
|---|---|
| [drafting/first-output.md](drafting/first-output.md) | 首次完整最终交付的原样输出，不删改附加内容 |
| [drafting/execution-prompt.txt](drafting/execution-prompt.txt)、[execution-command.json](drafting/execution-command.json) | 冻结执行提示及完整参数 |
| [drafting/frozen-run.json](drafting/frozen-run.json) | 候选、模型／推理、144材料哈希、提示、CLI及执行工具哈希、唯一调用序号 |
| [drafting/events.jsonl](drafting/events.jsonl)、[stderr.txt](drafting/stderr.txt)、[run-meta.json](drafting/run-meta.json) | 原始事件、工具返回、中间消息、错误流及运行状态 |
| [drafting/loaded-files.json](drafting/loaded-files.json) | 实际读取／检索文件、哈希、命令及未解析／目录外读取项 |
| [drafting/loading-audit.json](drafting/loading-audit.json) | 返回源文范围、完整卡片与标题检索的区别、UTF-8文本对照及原始日志哈希 |
| [verification.json](verification.json) | 材料、运行副本、原项目及现装文件不变性；首次输出与终端最终消息一致性 |

首次输出为 **2,930字节**，SHA-256 为 `67883ac7702ea71efbaf782a85a68cb046e0533de73359d1e300044b6db38c99`，与原始事件中的最终交付消息一致，仅不计末尾换行。没有第二次写作调用或备选结果。

## 实际加载与留存核对

23条材料读取命令全部退出成功，涉及3输入和17候选文件。实际读取 Writing 入口、manifest、always-load 保障、manuscript、algorithmic、abstract、generic、zh-to-en／en 及摘要深度参考；未加载正文模块，未直接回查 PDF 或提取文本。

共用范例先返回说明与索引，再按需返回卡片内容。完整 A02／A03／A06 已返回；其他卡片的标题检索不算完整读取，未完整预加载全部卡片。1,297个带编号的返回行与冻结 UTF-8 源文一致，无未映射编号返回或文本差异；具体范围和命令在 loading-audit.json 中原样留存。未发现显式目录外材料读取，未解析读取命令为空。记录证明材料实际返回，不证明参考已有效转化为达标表达。

冻结材料、运行副本、已追踪原项目文件、六个现装 W/P/S 目录及冻结执行工具哈希均一致。目录内 `.gitattributes` 使用 `* -text`，保留输入、PDF、提取文本、首次输出和日志的原始字节。材料合格、实施完成及实际输出达标仍为不同状态；本轮只完成唯一一次运行及留存核对，提交同步后停止，供负责人阅读验收。

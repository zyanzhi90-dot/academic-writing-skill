# E01 Abstract 独立 Drafting 复测（d78be2d）

本轮只执行一次独立摘要起草，原样保存完整英文摘要、中文翻译及执行者附加内容。未重跑、筛选、润色、反馈修订或人工改写，未修改或安装 Skill，未推进其他 section。本记录只核对运行、隔离、实际加载与留存，写作效果交负责人验收。运行跨2026-10-02／03（Asia/Shanghai）；目录按准备日期保留。

## 冻结输入及隔离

- 候选提交：`d78be2dc583d32a590453c329dd504d3886b6ede`。`materials/skill-candidate/` 中 writing／shared 的100个文件与该提交 Git blob 逐字节一致，版本分别为 `1.5.1-rc.6`／`1.6.1-rc.5`；没有隔离改写，不提供 Polishing 包。
- [任务](materials/inputs/task.md)、[科学事实包](materials/inputs/scientific-facts.md)、[个人经验](materials/inputs/personal-experience.txt)：事实包与当前项目经验文件保留原始字节。任务不额外指定参考论文、开头、句数、结构或句式，参考选择和英文实现由 Skill 决定。
- 参考：当前21篇学习 PDF 加 P04／P06／P19 三份归档 PDF，共24篇，分别从对应 PDF 新提取24份带页标记的 UTF-8 文本，不复制旧测试提取或表达衍生材料。20张范例卡全部可按需读取。
- 归档隔离：仅复制三份 PDF 到新材料目录中候选声明的相对位置，文件与 `20c7839` 对应原文逐字节一致。新目录的 `materials/effect-test/` 下仅有这三份 PDF，没有旧测试输出、日志、输入、评价或元数据；候选链接和内容保持原样。14条范例 PDF 来源及12条正文 PDF 来源均在允许目录内可解析。
- 全部151个允许文件（100候选、3输入、24 PDF、24提取文本）的哈希、来源、归档对照和保护快照见 [frozen-materials.json](frozen-materials.json) 与 [preflight.json](preflight.json)。目标原文、目标提取、来源定位、旧稿、反馈、诊断、评价及其表达衍生材料不进入材料目录；运行记录和本说明也不提供给写作端。

采用项目外新建、仅含允许材料的目录和全新 `codex exec --ephemeral --ignore-user-config --ignore-rules` 会话。仅调用显式指定的冻结 nature-writing；本次调用禁用自动项目说明、网络搜索、发现的现装 Skill 入口及 plugins／remote_plugin／apps／hooks／memories／multi_agent，不改现装文件或用户配置。隔离证据为材料边界、自动加载限制和实际读取核对，不宣称操作系统层面的目录外读取权限隔离。

## 唯一运行与原样输出

模型参数 `gpt-6.1-sol`，推理 `high`，CLI `codex-cli 0.159.2`，调用序号1；退出码 **0**，耗时 **215.50秒**。本轮运行工具仅在新目录适配候选提交、归档 PDF 隔离与提取；复用既有收集函数，不调用旧写作任务。`prepare`／`run` 均拒绝覆盖或第二次调用。

- [drafting/first-output.md](drafting/first-output.md)：唯一首次完整最终交付，2789字节，SHA-256 `588fdf65c449e7eb0f9c96b36fa53704d455a7d337914bc46e845cdced4f33af`；与原始事件最后交付消息一致，仅不计末尾换行。
- [execution-prompt.txt](drafting/execution-prompt.txt)、[execution-command.json](drafting/execution-command.json)、[frozen-run.json](drafting/frozen-run.json)：冻结提示、完整执行参数、输入／工具哈希和版本。
- [events.jsonl](drafting/events.jsonl)、[stderr.txt](drafting/stderr.txt)、[run-meta.json](drafting/run-meta.json)：原始事件、中间消息、全部工具返回、错误流及运行状态，未删改。
- [loaded-files.json](drafting/loaded-files.json)、[loading-audit.json](drafting/loading-audit.json)、[verification.json](verification.json)：实际读取、返回范围对照及保留核对。

## 实际加载与留存核对

26条材料读取／检索命令全部退出成功，涉及3输入和18候选文件。实际读取入口、manifest、always-load 共用保障（含 scientific-expression）、manuscript、algorithmic、abstract、generic、zh-to-en／en 及摘要深度参考；未读取正文模块或直接回查 PDF／提取文本。共用说明与任务索引先返回，随后完整返回 A06、A04、A02、A07；其他卡片标题检索不算完整读取，未整库预加载。此记录仅说明材料实际返回，不判定参考已有效转化为达标表达。

本次25条 Get-Content 命令返回未编号文本，1条 rg 返回带编号标题。新目录的 [collect_loading.py](collect_loading.py) 仅适配这种返回方式：从显式 Select-Object 范围恢复位置，并将每个返回行与冻结 UTF-8 文本核对；共1398行一致，无文本差异或未映射编号返回。范围和命令原样留存，不用提示要求替代实际加载证据。未发现显式目录外材料读取或未解析读取命令。

材料、运行副本、全部准备时已追踪项目文件和六个现装 W/P/S 包哈希保持一致，执行工具哈希不变；来源库、候选源文件及历史测试记录均未改。`.gitattributes` 的 `* -text` 保留输入、输出和日志原始字节。材料可用、执行留存完成与实际写作效果达标分别记录；本轮不作质量结论，提交同步后停止。

# E01 Abstract 独立 Drafting 复测（c8396e9）

本轮只运行一次全新独立摘要起草，原样保存完整英文摘要、中文翻译及执行者附加内容。不挑选重跑、润色、反馈修订或人工改写，不修改或安装 Skill，不推进其他 section。本记录只核对运行、隔离、加载与留存，不评价稿件科学表达、翻译或英文质量。

## 冻结输入与隔离

- 候选提交：`c8396e9e15b3306c56573325ff634dd0ea50cc1f`。`materials/skill-candidate/` 中 writing／shared 的100个文件与提交 Git blob 逐字节一致，未作隔离改写；manifest 版本为 `1.5.1-rc.6`／`1.6.1-rc.5`，不提供 Polishing 包。
- [任务](materials/inputs/task.md)、[科学事实包](materials/inputs/scientific-facts.md)、[个人经验](materials/inputs/personal-experience.txt)：已验收 E01 中文事实包和当前项目经验文件的原样字节副本。任务与执行提示沿用既有通用内容，不额外指定参考、开头、结构、句数或句式，不加入失败诊断／修订提示。参考选择、信息取舍和具体英文由 Skill 决定。
- 参考资料：当前21篇学习 PDF 和单独复制的 P04／P06／P19 三份归档 PDF，共24篇；从这些 PDF 新提取24份 UTF-8 文本，共307个 PDF 页标记，无提取警告或文字润色。20张范例卡均可按需读取。
- 归档隔离：仅复制三份 PDF 到新材料目录中候选声明的相对位置，与 `20c7839` 对应原文逐字节一致。新目录 `materials/effect-test/` 下只有三份 PDF，未复制历史测试输出、输入、日志、评价或元数据；归档文本另从 PDF 新提取。14条范例 PDF 来源和12条正文 PDF 来源在隔离目录内可解析，不改候选链接。
- 全部151个允许文件（100候选、3输入、24 PDF、24提取文本）的哈希、PDF—文本对应、原文对照和保护快照见 [frozen-materials.json](frozen-materials.json) 与 [preflight.json](preflight.json)。目标原文／提取文本、来源定位、旧稿、反馈、诊断、评价及其表达衍生材料不进入材料目录；执行记录、运行工具及本说明也不提供给写作端。

采用项目外新建的纯材料目录及 `codex exec --ephemeral --ignore-user-config --ignore-rules` 新会话，显式调用冻结 nature-writing。当前调用禁用自动项目说明、发现的现装 Skill 入口、网络搜索及 plugins／remote_plugin／apps／hooks／memories／multi_agent，不改变现装文件或用户配置。隔离依据是材料边界、自动加载限制和实际命令核对，不宣称操作系统层面的目录外读取权限隔离。

## 唯一运行与原始留存

指定模型 `gpt-6.1-sol`、推理 `high`，CLI `codex-cli 0.159.2`，调用序号1；退出码 **0**，耗时 **184.15秒**。运行工具复用既有机制，仅在新副本中改候选提交和运行目录前缀；任务／提示逻辑不改，收集工具原样复用。`prepare` 拒绝覆盖材料，`run` 拒绝第二次调用。

| 文件 | 留存内容 |
|---|---|
| [drafting/first-output.md](drafting/first-output.md) | 完整首次最终交付，英文摘要、中文翻译和附加内容原样保留 |
| [execution-prompt.txt](drafting/execution-prompt.txt)、[execution-command.json](drafting/execution-command.json)、[frozen-run.json](drafting/frozen-run.json) | 冻结执行提示、完整参数、输入／CLI／工具哈希与版本 |
| [events.jsonl](drafting/events.jsonl)、[stderr.txt](drafting/stderr.txt)、[run-meta.json](drafting/run-meta.json) | 原始事件、中间消息、工具返回、错误流及运行状态 |
| [loaded-files.json](drafting/loaded-files.json)、[loading-audit.json](drafting/loading-audit.json)、[verification.json](verification.json) | 实际读取、返回范围对照及保留核对 |

首次输出 **2909字节**，SHA-256 `daea301f1a6abaf7abc4610d38bf5edb634a57570c1e2e749851b3a35e7ed305`，与原始事件最后交付消息一致，仅不计末尾换行。运行中没有第二次写作调用、反馈或人工修改。

## 实际加载与留存核对

26条读取／检索命令全部退出成功，涉及3输入和18候选文件。实际读取 Writing 入口、manifest、always-load 保障（含 scientific-expression）、manuscript、algorithmic、abstract、generic、en／zh-to-en 和摘要深度参考；未读取正文模块或直接回查 PDF／提取文本。

共用说明和任务索引先返回，再完整返回 A06、A02、A07；其他卡片／分区标题检索不计完整卡片读取，未整库预加载。1393个带编号的返回源文行与冻结 UTF-8 文本一致，无文本差异或未映射编号返回，26条命令均显式 UTF-8 读取；原始命令、范围和返回保留在日志及 loading-audit.json。未发现显式目录外材料读取或未解析读取命令。记录证明材料实际返回，不证明模仿已转化为达标表达。

材料副本、运行副本、准备时全部已追踪项目文件、六个现装 W/P/S 包和冻结执行工具哈希保持一致，首次输出与原始日志未改。`.gitattributes` 的 `* -text` 保留输入、输出、PDF和日志原始字节。本次只完成运行与留存核对，材料、实施加载和写作效果三个状态分开记录；质量由负责人验收。提交同步后停止。

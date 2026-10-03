# E01 Abstract 独立 Drafting 复测（c2c0953）

本轮仅完成唯一一次全新独立摘要起草及运行／隔离／留存核对。完整首次最终交付原样保存，不重跑、挑选、润色、反馈修订或人工改写，不修改或安装 Skill，不推进其他 section。英文表达、科学内容及中文翻译质量由负责人验收；本记录不作质量判断。

## 冻结材料与输入边界

- 候选提交：`c2c09537e4f1f944eb8a8aa82cbc7ecf5203b6a7`。`materials/skill-candidate/` 的 nature-writing／nature-shared 共100个文件取自该提交，逐字节等于 Git blob，副本未修改。manifest 版本为 `1.5.1-rc.6`／`1.6.1-rc.5`；Polishing 不属于本次写作端必要依赖，未提供。
- [当前任务](materials/inputs/task.md)、[科学事实包](materials/inputs/scientific-facts.md)、[个人经验](materials/inputs/personal-experience.txt)：已验收 E01 中文事实包及原样经验的字节副本。任务／执行提示沿用既有通用逻辑，不额外指定参考、开头、结构、句数、句式或加入失败修订提示；具体选择由冻结 Skill 决定。
- 按需参考：当前21篇学习 PDF 和 P04／P06／P19 三份单独复制的归档原文；全部24篇各新提取一份显式 UTF-8 文本，共307个 PDF 页标记，无提取警告或文字改写。20张范例卡均可按需读取。
- 归档保持候选声明的相对位置，其字节与 `20c7839` 原文一致。新材料目录 `materials/effect-test/` 下仅有三份 PDF；未复制历史输入、稿件、运行记录、评价或元数据。目标论文原文／提取文本、来源定位、旧稿、反馈、诊断、评价及表达衍生材料不进入材料目录。
- 共151个允许文件（100候选、3输入、24 PDF、24文本）的哈希和 PDF—文本对应见 [frozen-materials.json](frozen-materials.json)；启动前核对见 [preflight.json](preflight.json)。项目外临时运行副本与此快照一致，写作端只接收该材料目录，运行工具和记录不供其读取。

使用 `codex exec --ephemeral --ignore-user-config --ignore-rules` 新会话；本次调用禁用自动项目说明、发现的现装 Skill 入口、网络搜索及 plugins／remote_plugin／apps／hooks／memories／multi_agent，不改用户配置或现装文件。隔离证据为材料边界、自动加载限制及原始命令核对；不宣称操作系统层面的目录外读取权限隔离。

## 唯一运行与留存

模型参数 `gpt-6.1-sol / high`，CLI `codex-cli 0.159.2`。独立线程 `01a0fffd-48d7-7c90-b217-d6c50cbe8aa3`，一次 turn／一次调用；退出码 **0**，耗时 **216.69秒**。运行工具的新副本仅替换候选提交和临时目录前缀，任务／提示逻辑原样复用；`prepare` 拒绝覆盖材料，`run` 拒绝第二次调用。新收集器仅补识别实际出现的 `rg --encoding utf-8`，修正日志的 UTF-8 标记，不改变输出或原始日志。

| 路径 | 原样留存内容 |
|---|---|
| [drafting/first-output.md](drafting/first-output.md) | 执行者首次最终交付全文，含英文摘要、中文翻译及附加内容 |
| [execution-prompt.txt](drafting/execution-prompt.txt)、[execution-command.json](drafting/execution-command.json)、[frozen-run.json](drafting/frozen-run.json) | 提示、模型／推理及隔离参数，输入、运行工具和 CLI 哈希／版本 |
| [events.jsonl](drafting/events.jsonl)、[stderr.txt](drafting/stderr.txt)、[run-meta.json](drafting/run-meta.json) | 原始事件、中间消息、命令返回、错误流及运行结果 |
| [loaded-files.json](drafting/loaded-files.json)、[loading-audit.json](drafting/loading-audit.json)、[verification.json](verification.json) | 实际读取文件、返回范围／文本对照、输出及保留范围核对 |

首次输出 **2628字节**，SHA-256 `7a3ca0c8db8519e17ff41b86d2b0bbf74d4d47eab131764c2584b6348a363fa6`；与原始事件最终交付消息一致，仅不计末尾换行。`* -text` 属性保存输入、输出和日志的原始字节。未筛选其他结果、改变稿件或另行生成翻译。

## 实际加载与保留核对

26条读取／检索命令均成功，涉及3个输入及18个候选文件。实际读取 nature-writing 入口、manifest、always-load（含 scientific-expression）、manuscript、algorithmic、abstract、generic、en／zh-to-en 及摘要深度参考。未读取正文模块，未直接回查 PDF／提取文本；它们保持可用，但不能据此声称已读取。

共用说明／任务索引（1–144行）先返回，再完整返回 A02、A05、A06、A07。标题检索不计完整卡片读取，未整库预加载。1438个实际返回源文行与冻结 UTF-8 文本一致，无文本差异或未映射编号返回；25条 Get-Content 命令及1条 `rg --encoding utf-8` 均显式指定 UTF-8。实际源文件哈希等于冻结快照，候选快照等于指定提交；未发现显式目录外材料读取或未解析的读取命令。原始日志保留命令、顺序及返回内容；这些记录不证明表达已经达标。

材料副本、运行副本、准备时全部已追踪项目文件、六个现装 W/P/S 包及冻结执行工具保持哈希一致。候选源文件、baseline、历史稿件、日志、已验收事实包和经验均不改。新记录目录是本轮唯一项目变更范围。完成提交同步后停止，交负责人验收写作效果。

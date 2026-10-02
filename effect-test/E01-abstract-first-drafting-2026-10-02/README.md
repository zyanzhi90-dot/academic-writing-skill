# E01 Abstract 首次独立 Drafting 记录

本轮只执行一次摘要 Drafting，原样保存英文摘要、中文翻译及执行者交付的附加内容，供负责人和用户阅读。未润色、反馈修订、筛选或人工改写输出，未推进其他部分，未修改或安装 Skill；本记录只核对运行与留存，不评价科学表达或英文质量。

## 冻结输入与候选

- `materials/inputs/task.md`：当前 Abstract-only 任务，不指定参考名单、句式或摘要展开顺序。
- `materials/inputs/scientific-facts.md`：[已验收 E01 中文科学事实包](../E01-abstract-materials-2026-10-02/科学事实包.md)的原样副本。支持细节按摘要需要取舍，不要求全部写入。
- `materials/inputs/personal-experience.txt`：《我自己的经验和做法.txt》的原样副本。
- `materials/skill-candidate/`：直接从提交 `20c78392931c07c0d5c3784fad26c833ae4d1ccf` 的 Git blob 提取 nature-writing 与 nature-shared，共99个文件，逐文件字节一致，无隔离改写。版本分别为 writing `1.5.1-rc.4`、shared `1.6.1-rc.3`；Polishing 不属于本次任务。
- `materials/文献资料/`、`materials/analysis/reading/`、`materials/analysis/extracted/`：P01–P19 的原样 PDF 与两种提取文本，共57个文件，供按需调用。完整19张范例卡均可用，未排除 A06、B01。

逐文件来源和 SHA-256、准备时项目提交、候选提交及保护文件快照见 [frozen-materials.json](frozen-materials.json)。候选使用提交中的 LF 字节，保留已验收中文输入的原始字节，不依赖工作区换行转换产生的哈希。

## 独立执行环境

项目外的全新临时材料目录只复制上述159个允许文件。不复制目标原文、来源定位、准备／评价材料、旧稿或其表达衍生材料，也不复制本 README、冻结记录、运行脚本或其他执行记录。任务与提示没有传入目标原文英文、诊断、预期答案或旧输出。

使用全新 `codex exec --ephemeral --ignore-user-config --ignore-rules` 会话，不恢复旧会话。模型固定为 `gpt-6.1-sol`，推理固定为 `medium`；工作目录固定为项目外材料目录，自动项目说明读取及网络搜索关闭。通过本次进程的 `skills.config` 禁用53个已发现现装 Skill 入口，并关闭插件、远程插件、apps、hooks、记忆及多代理功能，未修改现装文件或用户配置。逐入口禁用依据 [OpenAI 官方 Skill 配置说明](https://learn.chatgpt.com/docs/build-skills#enable-or-disable-local-codex-skills)。工具参数核对未调用写作模型。

执行提示要求文本显式按 UTF-8 读取，先读取范例共用说明与任务索引，再按需选择卡片和原文；材料读取使用明确绝对路径及范围。隔离依据是独立材料目录、自动加载限制、允许文件边界和实际命令核对；不宣称操作系统层面的目录外读权限隔离。原始事件保留实际行为，不将提示要求视为执行证明。

## 执行与保存

本轮专用 [execute_once.py](execute_once.py) 仅作必要适配；复用已验收 P17 首次运行工具中的哈希、清单和记录收集函数。该旧脚本只供记录工具调用，没有交给写作执行者，也未调用其准备／写作函数或读取旧稿。现有共用工具及全部旧测试记录不改。

本次依次执行 `prepare`、`run`、`collect`。`run` 拒绝已经存在的 `drafting/` 目录，无自动重跑或覆盖逻辑。唯一写作调用退出码为 **0**，耗时 **140.36秒**。

| 文件 | 留存内容 |
|---|---|
| [drafting/first-output.md](drafting/first-output.md) | CLI 原样保存的首次完整终端交付，不拆分、删改或另写摘要 |
| [drafting/execution-prompt.txt](drafting/execution-prompt.txt)、[execution-command.json](drafting/execution-command.json) | 执行提示、完整参数及本次加载限制 |
| [drafting/frozen-run.json](drafting/frozen-run.json) | 候选提交、模型／推理、全部材料哈希、提示与执行脚本哈希、CLI 版本及二进制哈希、唯一调用序号 |
| [drafting/events.jsonl](drafting/events.jsonl)、[stderr.txt](drafting/stderr.txt)、[run-meta.json](drafting/run-meta.json) | 原始事件、错误流、退出状态和耗时 |
| [drafting/loaded-files.json](drafting/loaded-files.json) | 实际读取／检索文件、哈希、命令和未解析／目录外读取项 |
| [drafting/loading-audit.json](drafting/loading-audit.json) | 模型可见的返回行范围、标题检索与完整卡片读取的区别、UTF-8 返回内容核对及原始记录文件哈希 |
| [verification.json](verification.json) | 冻结材料、运行副本、原项目文件及现装 Skill 不变性、首次输出与最终事件一致性 |

首次输出为 **3,530字节**，SHA-256 为 `a1e812e6aa84401c227e6f14ed553ccc7ae8ef83294b8462449a0c246787f409`，与事件日志中的最终交付消息一致（仅不计末尾换行）。没有选择第二份结果。

## 实际加载与留存核对

共23条读取命令，全部退出成功，涉及3个输入文件和17个候选文件。实际加载包含 Writing 入口、manifest、always-load 共用及本地保障、manuscript、algorithmic、abstract、zh-to-en 与 en、generic，以及摘要深度参考。共用范例先返回第1–156行（说明与索引），随后检索卡片标题，最后返回第159–196行（完整 A01、A02、A03）及第221–232行（完整 A06）。标题检索涉及的其他卡片只返回标题，不计为完整卡片读取。

未直接回查 PDF 或提取文本，未读取正文模块。全部显式材料读取均位于独立目录内；自动解析未遗漏读取命令。1307个带编号的返回源文行与冻结 UTF-8 源文一致（核对时只消除返回行的 CRLF 终止符）。原始事件保留每次命令、输出和范围；这证明相关材料实际返回，不证明参考英文已成功转化为达标表达。

冻结材料及运行副本、已追踪原项目文件和六个现装 W/P/S 目录的哈希核对均一致，执行脚本与所复用的收集脚本也保持冻结时字节。目录使用 `* -text`，保留材料、首次输出和日志的原始字节。

材料合格、候选实施完成与摘要实际输出达标仍为不同状态。本轮只完成唯一一次运行及证据留存，不给出质量通过结论，提交同步后停止，供共同阅读验收。

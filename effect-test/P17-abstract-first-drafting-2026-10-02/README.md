# P17 Abstract 首次独立 Drafting 记录

本轮仅执行摘要起草及中文翻译一次，供负责人和用户共同阅读。未提前写其他部分，未评价、筛选或人工修改生成稿，未修改或安装候选 Skill。

## 输入与版本

- `materials/inputs/task.md`：冻结的当前摘要任务。
- `materials/inputs/scientific-facts.md`：已验收中文事实包的原样副本。
- `materials/inputs/personal-experience.txt`：个人经验原样副本。
- `materials/skill-candidate/`：从 `e126a659d77195f79416815db6ddb5827e60588e` 提取的 nature-writing 与 nature-shared，共 99 个必要依赖文件；没有安装到现装 Skill 目录。
- `materials/文献资料/`、`materials/analysis/reading/`、`materials/analysis/extracted/`：其余 18 篇论文的原样材料，可按需参照具体英文及回查上下文；参考论文的科学内容不能增加作者事实。

文件版本、来源与逐文件 SHA256 见 `frozen-materials.json`。运行目录是项目外的独立临时目录，仅复制 `materials/` 的内容；没有复制本记录、隔离差异、来源定位、证据报告、旧输出或评价。

## 隔离差异

只对两个候选副本作必要处理，详细差异在 `version-isolation.diff`，不交给写作执行者：

1. `nature-shared/core/robotics-writing-examples.md`：移除 A06、B01 全部引文及分析、P17 来源链接；同步删除对应索引指向，将可用卡片及论文数量调整为 17 张、18 篇。其余卡片的英文、定位与取舍说明保持原样，共用范例调用、风格协调、内部表达核查等规则保留。
2. `nature-shared/core/robotics-main-text.md`：仅移除 P17 验证分组的具体例证与 P17 链接，保留通用原则及其他论文例证。摘要任务仍按原入口排除正文模块；本项用于避免副本残留被意外读取。

其余 97 个候选依赖文件与冻结提交字节相同。P17 PDF、两种提取文本及其分析未进入材料目录，A06、B01 也不再存在。其他论文原文中的参考文献条目仍属于那些论文，没有额外清理或改写其内容。

## 执行与记录

使用 `execute_once.py prepare` 准备材料，`execute_once.py run` 启动一次全新 CLI 会话，`execute_once.py collect` 汇集加载与保存证据。该脚本为本轮专用必要适配；已有运行工具和旧记录不变。运行阶段拒绝已存在的 `drafting/` 目录，不能覆盖首次执行或自动重跑。

模型为 `gpt-6-sol`，推理为 `medium`。沿用此前 CLI 的独立 `exec --ephemeral --ignore-user-config` 执行方式；本轮仅增加项目外工作目录、非 Git 目录支持、禁用自动项目说明读取及网络搜索，明确限定可读材料范围。具体 CLI 版本、二进制哈希、配置、完整参数和执行提示均保存于运行记录。隔离方式是独立材料目录、提示中的访问限制及实际命令核对；不宣称操作系统层面的读权限隔离。

- `drafting/first-output.md`：CLI 原样保存的首次完整输出，包含其交付的英文摘要及中文翻译；保留全部附加说明，不人工删改。
- `drafting/execution-prompt.txt`、`execution-command.json`、`frozen-run.json`：执行提示、完整命令及冻结设置。
- `drafting/events.jsonl`、`stderr.txt`、`run-meta.json`：原始事件、错误流与退出状态。
- `drafting/loaded-files.json`：实际读取／检索的文件、对应命令、退出状态及未能自动解析的读取命令；原始日志保留具体范围和输出。检索或范围读取不等于完整文件读取。
- `verification.json`：输入、运行副本、候选源文件、已追踪项目文件及现装 Skill 的不变性，首次输出与终端消息的一致性；只核对运行和记录，不评价英文质量或科学表达。

## 本次运行状态

唯一一次执行退出码为 0，耗时 82.43 秒。首次输出为 2,674 字节，SHA256 为 `eca6d00b0add46cd2c4e5eb1d3e474884a3b1ee3efed0721aa204dc9c9f62c2f`，与原始事件中的最终交付消息一致（仅不计末尾换行）。输入、运行副本、已追踪项目文件及现装 Skill 的哈希核对均一致。

日志记录 26 条读取／检索命令，均退出成功，涉及 3 个输入文件和 18 个候选依赖文件。实际加载包含入口、manifest、共用保障、摘要分支、中文到英文及英文语言规则、research 与 algorithmic 分支、摘要深度参考及共用范例。共用范例文件被整份读取，随后对部分摘要卡片作范围读取；未读取正文模块，也没有直接回查 PDF 或提取文本。全部显式材料读取均在独立目录内，未发现目录外读取，自动解析未遗漏读取命令；完整原始事件仍是核对依据。

本目录使用 `* -text` 保留冻结文件和首次输出的原始字节。材料合格、候选实施完成与摘要实际输出达标是不同状态；本轮不作实际写作质量通过判定，交付后停止，等待共同阅读验收。

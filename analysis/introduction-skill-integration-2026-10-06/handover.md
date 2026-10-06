# 机器人 Introduction 三层学习接入候选：实施交付

## 基线与范围

本轮开始核对并 fetch `origin/main`；本地、跟踪分支和实时远端均为已验收的 `177d720dcae4131f653c9dee3194e781f824946c`，工作区干净。提交前再次查询远端仍为该提交。

依据当前《核心要求.txt》《我自己的经验和做法.txt》《引言写作方法.txt》、已验收的整节／段落／表达学习稿以及共用 `scientific-expression.md`，只调整候选的机器人 Introduction 路径。P17 保持默认组织与表达锚点，P05、Fuzzy2023、ESO2017 按科学关系补充。实际对象、事实、条件、比较、设计和保证由作者研究决定。

本轮使用 skill-creator 的渐进读取与包完整性核对方法，仅用于候选本地组织；没有安装 Skill，没有生成或润色 E04，没有运行效果测试，没有改变执行器。

## 改动与依据

| 位置 | 具体改动 | 依据与作用 |
| --- | --- | --- |
| Shared `core/robotics-introduction-examples.md` | 沿用原路径，改为选择与调用索引；七类科学关系连接三层材料，并共同指导 Drafting／Polishing。保留 B15–B18 来源身份、页码和适用关系。 | 学习不止于“加载过范例”：先确定作者主线和各段任务，再按需要读完整英文、连续关系及具体实现。 |
| Shared `core/robotics-introduction-section.md` | 接入六项已验收整节任务及 24 个完整英文块，增设检索锚点。 | 领域价值进入问题、各段任务、已有能力与条件、设计理由和作用、设计连接、贡献回收。 |
| Shared `core/robotics-introduction-paragraphs.md` | 接入九个完整段落及逐句推进表，增设检索锚点。 | 当前句接住什么、增加什么、如何让下句继续；保留前后段上下文及段首／段末责任。 |
| Shared `core/robotics-introduction-expression.md` | 接入 26 组表达及 32 个英文块，使用候选内三层链接。 | 主语—动作—对象、真实句式和搭配；重点调用 `In [xx], …`、同一文献续句、设计紧接作用及输入输出交接。 |
| Shared `core/robotics-writing-examples.md` | 引言选择与任务索引指向正向学习入口；补充按标题和完整示例边界读取；说明引言适配身份。 | 按需读取与当前段落科学关系相符的英文及分析，保持现有摘要与正文卡片。 |
| Writing／Polishing `static/fragments/section/intro.md` | 在各自现有入口顶部加机器人领域调用说明，使用相同共享入口与三层材料。 | Writing 在既有论证和段落规划步骤确定主线／任务；Polishing 先检查科学推进，再用同一英文修复受影响处。 |
| Shared `core/robotics-main-text.md` | 引言段落指向同一材料；Introduction 贡献联系设计及受支持作用／保证。 | 避免把原“design and evaluation”直接变成引言需要展开本研究实验的要求；独立 Related Work 的原设计与评价联系保留。 |
| Shared `manifest.yaml` | 声明三个按需资源并更新原入口条件。 | 三层材料可在独立候选目录读取，未加入 always-load。 |
| Writing `manifest.yaml`、`references/introduction.md` | 深层一般引言指南用于剩余的作者需求；机器人默认先走共享三层学习。 | 保留一般主题、期刊和其他 section 能力，同时明确当前机器人引言的默认组织来源。 |

三份候选学习资源的英文块、分析表和示例／页码标记与验收稿相同。只改候选内链接、来源审计查询入口和检索锚点。65 个英文块全部保留；没有重新总结四篇，没有改动已验收逻辑、段落推进或表达。出版原句选取与基于原文的适配仍明确区分。

原共享引言文件中的出版原文及来源差异按基线 Git 字节完整保存于 [audit/previous-robotics-introduction-examples.md](audit/previous-robotics-introduction-examples.md)。四篇已核验原文、PDF、适配对应表及历史学习稿保留原样。默认三层学习不依赖项目 `analysis/`，来源差异不随选择入口作为默认模仿内容加载。对应关系与文件哈希见 [audit/learning-resource-provenance.json](audit/learning-resource-provenance.json)。

## 起草与复核的共同要求

共同索引将实际操作接入现有工作流：作者科学主线和各段任务 → 按关系选取适用完整段落与连续句 → 选取并调整主语、动词、句式和普通学术用词 → 检查科学与英文实现 → 按原输出格式交付。

开篇第一句说明大领域的价值或重要性，随后逐步进入具体研究需要。后续段首直接命名当前科学对象、问题、路线或职责。具体文献先说明用了什么方法实现什么相关能力，再用同一文献的机制、输出或作用续句继续需要的科学关系。已有能力及其相关条件支持设计的采用理由，设计紧接具体作用或保证；多个设计按职责和共同输出连接，贡献回收前文已建立的需要。

方法信息按其引言论证作用选择：解释采用理由、职责和接口所需的概念关系进入引言，算法步骤、公式推导、控制律细节和参数进入 Method。本研究实验任务、设置、基线清单及结果默认进入 Experiments／Results；只有承担必要科学论证功能的本研究经验信息，才在引言保留其任务和证据范围。两端应用同一取舍，仍保留受作者科学支持的能力与作用关系。

这些是运行调用与取舍要求。三份学习正文继续只提供已验收的正向组织与英语实现；不混入历史诊断，不预置 E04 科学主线或逐句修法。不固定段数、设计位置、句序或每段末尾的 gap。科学问题不能用范例事实补齐。

## E04 对照依据：历史输入，不是本轮结果

本轮只读 `effect-test/E04-introduction-delivery-253dae3-2026-10-05/` 的首次 Drafting、独立 Polishing、任务输入和加载记录。既有阶段结果与报告保持原样。

| 实际历史观察 | 本轮落实 |
| --- | --- |
| 首稿首句为 `Behavior cloning learns robot manipulation policies from demonstrations through supervised learning.`；独立润色首句为 `Robot manipulation policies learned from demonstrations must generate precise actions while preserving the multiple valid ways in which a task can be completed.`。均直接进入具体学习任务。 | 将领域价值首句要求接到两端真实 intro 入口与 E01–E03，P17 I01／ESO I01 提供完整推进。 |
| 两份首次英文各九段，`In [` 均为零；主要以方法名开句说明能力。 | 选择表将具体文献及续句连接 P05 I02、P17 I04 和 E05–E13、E18；两端复核具体实现，保留作者文献身份。 |
| 两稿 P09 展开八项仿真、四项实机、基线与任务清单；P02、P03 使用本研究 pushing 和训练观察推进。 | 由共同入口承担本研究实验信息必要性判断，默认在实验／结果章节展开；必要论证信息仍按作者证据及适用范围处理。 |
| 训练／推理与 receding-horizon 段包含预测、执行、重新观察等连续内部步骤，同时也已有设计作用和 `also depends on` 的衔接。 | 保留已成熟的职责与接口关系，明确引言概念层面的选择；不以删去设计理由或全部接口信息来解决实现步骤展开。 |
| 两端实际已返回核心、intro、共享正文、公共索引和旧 Selection，仍出现上述偏差。 | 明确材料使用和生成／复核任务，而非仅增加“读取范例”的声明。 |

旧加载记录的具体返回：

| 旧卡片范围 | Drafting | 独立 Polishing |
| --- | --- | --- |
| B15：54–194 | 141 行，完整非空内容 | 141 行，完整非空内容 |
| B16：195–311 | 117 行，完整非空内容 | 96 行，部分内容 |
| B17：312–401 | 2 行标题，未完整返回 | 0 行 |
| B18：402–552 | 2 行标题，未完整返回 | 0 行 |

旧公共索引较宽的行范围还返回了部分摘要卡片。因此本轮按标题、完整学习单元边界定位，保存选中单元的实际读取记录。历史返回只能证明访问了哪些文本，不能证明模型理解、采用或完成内部复核。也没有把四篇全部读取设成新要求。

## 完整性与入口核对

执行 [check_integration.py](check_integration.py)：声明路径存在；共享入口及新资源的候选内链接和锚点解析；三层 65 个英文块、分析表和来源标记与验收稿一致；旧 22 张 A／B 卡片及摘要选择保持一致；其余候选文件、两端轴映射、always-load、核心工作流、语言规则和脚本保持基线内容；原 PDF、作者输入和 E04 保持原样。

读取链在两端均为：`SKILL.md` → manifest 与 always-load（包含原 `scientific-expression.md`）→ 当前 intro／paper-type／language／journal 片段 → 共用机器人索引及正文层 → 原共享引言路径 → 选中科学关系的整节、段落、表达完整单元。intro 中的 `../nature-shared/…` 明确相对技能根目录解析。两端使用同一共享材料与范围要求。

核对记录覆盖 Writing／Polishing 各自 `en`、`zh-to-en` 的四种已手动解析 Introduction 请求。中文路径同时读取既有英文片段。将三包复制到项目外临时目录后，重复读取，文件与选中单元的哈希一致；临时目录随后清理。这是包搬移和实际文件读取核对，不是安装、执行器运行或模型自主路由测试。

三包均通过 skill-creator `quick_validate.py`；`git diff --check` 通过。命令及结果见 [run-record.md](run-record.md)，实际读取、哈希和保持项见 [audit/verification.json](audit/verification.json)。

这些检查支持实施完整性与声明／读取路径一致性。未验证模型能否自主正确选择、实际采用或交付成熟引言，不补记效果、迁移、可靠遗漏检测或稳定性通过。提交同步后停止，交负责人独立验收。

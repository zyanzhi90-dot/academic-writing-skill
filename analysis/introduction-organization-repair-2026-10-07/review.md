# 机器人 Introduction 整节决策与当前作者输入修复

本轮仅实施静态修改，未安装候选、运行效果测试、生成或润色新稿。下一轮自主首次全文才可判断实际效果。

## 基线与依据

开始时工作区干净；fetch 后本地 HEAD、origin/main 及 GitHub main 均为 `712c86a5dcbb6e7f2ec1df8f1e7a40bffff47c20`。实施基座为已验收候选 `447c0c4165afb7fdc08a0458d534042a8704dc94`，效果依据为 [E04 首次记录](../../effect-test/E04-introduction-delivery-447c0c4-2026-10-07/报告.md)。

本轮读取当前《核心要求.txt》《我自己的经验和做法.txt》《引言写作方法.txt》、两端 Introduction 片段、共享索引及三层正向材料，并沿 E04 的实际输入、返回内容、公开决策和两阶段首次全文定位。历史材料仅用于这里的开发审计。

最新明确指令要求贡献引导及编号列项，并从当前 Introduction 全文排除本研究实验信息；它优先于旧的实验规则撤销调整。历史输入、成稿和评价保持原样。此前科学忠实、领域价值入口、真实文献能力及适用英文的有效部分继续保留；旧记录的整体通过结论不能代替本轮目标或未来效果判断。

## 可观察的失效位置

下表段句编号来自 [原样输出索引](../../effect-test/E04-introduction-delivery-447c0c4-2026-10-07/coordinator/output-index.json)。公开决策来自 [Writing 返回](../../effect-test/E04-introduction-delivery-447c0c4-2026-10-07/drafting/execution-agent-messages.json) 与 [Polishing 返回](../../effect-test/E04-introduction-delivery-447c0c4-2026-10-07/polishing/execution-agent-messages.json)。

| 环节 | 已证实事实 | 有依据的定位与限度 |
|---|---|---|
| 输入与路由 | [实际加载记录](../../effect-test/E04-introduction-delivery-447c0c4-2026-10-07/loading-summary.json)显示两端 Introduction 片段、专用索引和整节材料实际返回。原冲突 generic 未返回，读取边界保持。 | 不是入口找不到材料；本轮不再调整执行器、路由或读取边界。材料返回也不能证明成稿已经实行相应关系。 |
| 整节规划 | Writing `item_29/38` 提到多模态、历史与未来联合生成、能量与得分学习、生成与执行职责。`item_39` 却把后部连续分给“序列与执行、视觉计算、架构选择、总体贡献”。Polishing `item_31` 保留相近后部展开。 | 存在局部采用理由，但段落任务组合仍形成连续方法概览。需要在现有科学主线规划中先确定实际贡献及其所需论证，再选择后部仍承担科学任务的信息，而不是按组件补齐段落。八段本身不是错误，不设置替代段数。 |
| 研究现状到核心设计 | Writing P04-S05：`These studies establish diffusion modeling as a relevant approach to behavior generation.` 紧接 P04-S06：`In this paper, we propose Diffusion Policy for learning robot manipulation policies from demonstrations.` Polishing P04 结束于同期扩散模仿工作，P05 即提出本文策略。 | 文献应用的相关性与本文需要之间缺少整节层面的充分收束。P1–P3 已建立表示条件、历史与未来联合动作的区别、对比训练及归一化估计等关系；不能删掉这些有效能力与需要，也不能虚构既有工作缺陷。后文 P05 的响应新观测、P06 的视觉计算、P07 的动作时间变化有局部理由，但不能让这些后部说明代替核心设计出现前的需要论证。 |
| 范例选择与贡献形式 | 两端完整返回 E24 的框架—职责—作用连续句。E25 仅返回起始锚点行，正文和分析未返回；E26 未返回。整节层 P05/Fuzzy 的完整贡献列项已经返回。两阶段 P08 都没有贡献引导与逐项回收。 | 不能说列项范例不存在或完全未提供。可观察到的是表达层选到了总体框架实现，未读取列项的具体实现；原整节与段落调用说明允许连续段或列项，两端未把前文需要映射到具体贡献项。当前选择入口须明确区分 P17 的科学内容回收与 P05/Fuzzy 的引导、编号形式。 |
| 结尾与全文取舍 | Writing P08-S01 总结框架，S03–S05 转入八项仿真、四个 benchmark、四项实机任务及设计研究和验证证据。前文 P02-S08、P05 的受控推物观察、P07 的测试架构优势也属本研究信息。Polishing `item_30` 明确“将实验信息放在贡献收束处”，`item_31` 明确“最后收束验证证据”；P08-S03–S05 新增 46.9%、比较动作空间及 95%/20 次试验，P03-S06 新增本研究 IBC 比较波动。 | 不只是结尾数字问题。旧正常输入撤销了默认实验排除，因此不能把本轮新增边界假记为旧会话违反当时明文要求。当前需在规划、保留/新增选择和交付复核共同执行最新作者范围，不能只删结尾数字或给原总结编号。文献 [3] 的既有精度能力仍属于引用工作的真实能力，应按论证需要保留。 |

以上事实支持修改整节任务选择、贡献范例调用、方法信息选择及全文复核；不支持推断隐藏检查过程、确定唯一模型原因或认定清除某个入口即保证效果。

## 最小修改及实际决策接点

| 文件 | 修改与作用 |
|---|---|
| [Writing intro.md](../../skill-candidate/nature-writing/static/fragments/section/intro.md) | 在既有步骤 1–3 先按当前信息取舍收束文献能力、条件与研究需要，再从实际贡献及对应需要决定段落任务；步骤 4 只保留承担采用理由、职责、接口与贡献任务的方法内容，合并仅延长组件概览的描述。贡献结尾读取 E25 和适用 E26；步骤 7–8 检查完整现状到设计的过渡、后部方法用途、贡献与前文关系及全文取舍。 |
| [Polishing intro.md](../../skill-candidate/nature-polishing/static/fragments/section/intro.md) | 在既有 diagnosis 中先核对整节需要到设计及后部论证用途，保留有效文献能力；从前文需要与设计职责恢复实际贡献，读取相同列项实现。交付复核覆盖保留、替换与新增全文，不仅检查改动句的事实和语法。 |
| [共享索引](../../skill-candidate/nature-shared/core/robotics-introduction-examples.md) | 把信息选择放进主线建立，按实际需要与职责规划贡献，再选段落；贡献检索把 E25/E26 的引导与列项和 P17 I08/E24 的职责—作用内容分开对应。现有 Drafting/Polishing 分别落实需要收束、方法用途与全文取舍，避免只加一个优先级声明。 |
| [整节层](../../skill-candidate/nature-shared/core/robotics-introduction-section.md)、[段落层](../../skill-candidate/nature-shared/core/robotics-introduction-paragraphs.md)、[表达层](../../skill-candidate/nature-shared/core/robotics-introduction-expression.md) | 仅修当前贡献形式的适用说明和调用说明：P17 保留主要组织与表达锚点、为项内职责和作用提供内容，P05/Fuzzy 提供贡献引导与列项实现。所有英文证据块和逐句分析表保持原样，其余科学主线与搭配不改。 |
| [robotics-main-text.md](../../skill-candidate/nature-shared/core/robotics-main-text.md) | 把原本同时覆盖 Introduction/Related Work 的段落或列项选择范围收窄到独立 Related Work；Introduction 转用专用索引当前贡献形式与取舍。保留其他 section 指导，避免同一实际返回入口继续提供相冲突的贡献选择。 |
| [引言写作方法.txt](../../引言写作方法.txt)、[current-author-adjustment.txt](../../current-author-adjustment.txt)、[AGENTS.md](../../AGENTS.md) | 更新当前作者的需要收束、方法用途、全文实验信息边界和实质贡献列项。新增根目录正常作者调整文件；AGENTS 将下一轮输入准备明确绑定到当前根目录作者文件及新 override 副本、新哈希，避免历史 override 被继续当作当前输入。执行器本身不改。 |

这些修改没有给出 E04 专用主线、段序、替换句或预定贡献数量。分段和组合仍由作者科学关系决定。P17 的运动建模条件与多示教能力组合、生成运动到可靠执行的依赖关系，P05 的相对运动与动力学条件、Fuzzy 的性能与收敛需要及相应贡献项，继续提供可替换科学内容的成熟组织与连续英文。参考论文的控制事实或保证不成为作者事实。

## 下一轮有效作者输入

新的机器人 Introduction 记录应冻结当前根目录三份作者文件及根目录 `current-author-adjustment.txt`，把该调整文件原样复制到新记录及其 `inputs/current-author-adjustment.txt`，重新记录作者文件哈希。复用经确认的科学、背景、引用与摘要材料时，不复用历史 override 作为当前要求。新调整文件只包含正常作者要求，没有历史 failure、已知测试句、预拟科学主线或修法。

历史 E04 的 `current-author-adjustment.txt`、输入副本、首次输出、加载与公开返回记录均不改动；它们仍可用于审计当时输入和决策，不能覆盖当前作者边界。

## 静态核对与结论边界

静态核对结果见 [verification.json](verification.json)：候选改动限于上述七个 Introduction 接点；三层英文证据和逐句分析未变；两端非机器人选择入口及相容指导未变；执行器、其他 section、摘要、科学事实、历史输出和原有语境表达判据未变。专用索引本地文件与锚点仍可解析，`git diff --check` 通过。

实施结论：当前两端的正常入口已连接同一整节决策、贡献实现与信息选择，下一轮作者输入准备已有当前权威来源。效果结论：本轮没有新自主输出，不能证明模型会按修改后的决定完成整节、正确压缩方法、形成实质贡献或在全文排除本研究验证内容，也不能证明迁移或稳定性。后续独立首次效果验证判断实际完成程度。

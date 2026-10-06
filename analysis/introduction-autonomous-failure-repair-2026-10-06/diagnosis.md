# Introduction 自主失效定位与最小修改依据

远端、origin/main 与本地起点均为 `50d77287873375de04c851a6840f3fb06588ef84`。诊断复用 ee74b27 E04 的原样输入、两阶段 events.jsonl、公开规划、英文首次输出及阶段差异；作者旧实验取舍表述按该目录 current-author-adjustment.txt 处理。原记录和已验收三层材料保持不变。

## 已证实事实与发生环节

| 环节 | 实际证据 | 可以确认的判断 |
| --- | --- | --- |
| 要求适用与路由 | 两端均选择 intro、机器人主体、generic journal；Writing 后改 algorithmic。两端 scientific-expression.md 完整返回；Intro fragment 的 item_13 返回完整文件。 | 不是未识别 Introduction 或漏读作者要求。algorithmic 是论文类型，generic 是期刊轴，二者均不能把机器人引言改为 generic 引言。类型文件的全文证据链相容，不修改它。 |
| 范例选择与科学含义适配 | Writing item_22 返回共享入口，item_27/29/32 返回包含 P17 I01、E01–E03 的完整正向内容。item_26 公开规划却写“从示范学习的价值”推进。 | 规划把研究路线的价值当成领域入口。P17 I01 的应用 → 适应性 → 学习 → LfD → 运动建模具有不同科学层级，不能只凭 valuable 判断功能匹配。失效已经出现在规划/功能适配，随后生成沿用。 |
| 生成 | Writing P01-S01 为 “Robot learning from demonstrations is a valuable approach to acquiring manipulation skills.”；P04-S02 后半句为 “while [5] learned log-density gradients …”。 | 首句从示范学习路线切入；文献编号被用作学习动作的主体。后者与要求中明确科学主体的表达不符；应落实每个分句中的方法/模型/研究身份，不能仅检查整句有主语或 In [xx]。 |
| 润色适用判断 | Polishing item_18/24/25/31 返回同一入口、完整领域段落及 E01–E03。item_19/33 规划聚焦动作表示、视觉编码、架构理由，最终 P01-S01 原样保留。 | 润色对原开篇的任务判断没有纠正。已保留句仍须与所选完整范例的科学责任比较，不能把“保留准确内容”当作其满足作者组织目标的依据。 |
| 润色改写与交付复核 | 原 Writing P03-S06 主语是 “An alternative representation”；Polishing 改为 “Learning the distribution gradient offers a way …”。P04-S02 的 “while [5] learned …” 保留。Polishing item_8 完整返回表达核心。 | 动名词开句是在润色重写中新增，不是只从首稿继承；协调分句科学身份问题也没有纠正。需把所选成熟构造、科学主体和作者偏好落实到每次替换及保留句的既有复核，而非增加同义规则或更大格式检查表。 |

公开消息仅反映可见决策，不能证明隐藏检查执行顺序或内部注意力分配。原样证据摘录和哈希见 evidence.json；完整上下文仍以旧 events.jsonl 为准。

## generic 指导逐项判断

| 原路径/内容 | 冲突或相容性 | 最小处置 |
| --- | --- | --- |
| 两端 intro.md 的强制 funnel：exact unknown → research question → study route；Writing 的四段安排和要求选择 pipeline variant | 与按作者科学依赖安排段落、设计位置及贡献不一致。四段虽标 one possible，强制选变体仍增加另一套组织决策。 | 移到 intro-general.md，仅其他科学主体按需读取；机器人默认 fragment 只返回领域入口和同一三层资源路径。 |
| Writing task-then-application、open-with-challenge；深层 references/introduction.md 任务/挑战先行与实现步骤、创新先于理由 | 与本轮领域价值入口、充分理由后设计及概念层展开冲突。上轮深层 reference 未读取，不能称其导致已发生失败。 | 切断机器人 Introduction 对这些 general 深层指南及 example bank 的结构性默认入口；保留文件供原适用范围读取。 |
| Writing Here we show；两端的 Results 摘要/数字默认排除 | 与当前表达偏好或撤回的实验排除规则冲突。 | 随 generic 文件隔离，不在机器人入口新增替代取舍规则。 |
| Nature corpus 的假定读者已知领域重要性、快速问题 funnel、问题优先创新、晚出现答案 | 与当前机器人领域价值入口和科学任务决定设计位置冲突。上轮 journal=generic 未读该 corpus，无本次因果证据。 | 两端 router/manifest 中仅将机器人 Introduction 排除出该 corpus 的组织调用范围；保留其他 section 与非机器人调用。 |
| 文献能力和条件、明确已知→设计承接、科学问题不等于作者方法缺席、段落组共同承担任务、保持技术条件与证据范围 | 与正向三层材料相容。 | 在两端默认 fragment 保留；类型、语言、科学表达核心及机器人正文规则不改。 |

generic 全文同载是已证实的上下文冲突，可能增加组织选择竞争；没有对照实验能把它认定为首句错误的唯一原因。文学编号主体与新增动名词开句在局部适配及交付复核发生，不能全部归因于 generic。

## 修改与证据关系

1. 两端 intro.md 使用现有按需读取机制分开机器人和其他主体的组织资源；general 文件保留原有内容，避免改变其他学科能力。router/manifest 同步限定深层 generic/Nature 引言入口。执行器、模型设置、摘要、其他 section 不变。
2. 共享入口的既有规划选择处用 P17 I01 说明范例各科学层级的功能匹配，指向原有完整 I01/E01–E03；不提供 E04 的开篇、主线或段序。
3. 既有英文适配处明确每个分句的科学对象对应，使用已验收文献连续句及 subject–action–object 分析；既有润色复核处覆盖保留句与新增替换句，保持构造及科学作用。这是选择、适配和复核决策的接点修补，不修改三层内容或全局表达规则。

待验证的是以上接点能否在一次自主生成和独立润色中产生全文对齐，以及润色是否仍产生新冲突。静态完整性、实际返回和个别句型吻合都不能回答这一问题。修改冻结后按原机制各调用一次；无论效果结论如何均原样交付，不继续修至通过。

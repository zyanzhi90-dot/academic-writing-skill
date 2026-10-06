# Robotics writing examples — common use and expression checks

## Scope and reading order

For nature-writing and nature-polishing when robotics is the central scientific
subject: abstracts, body sections, whole-manuscript reasoning, standalone
paragraphs, and feedback revisions, including Chinese-to-English work. Exclude
incidental robotics, title-only, submission administration, and layout tasks.
This is a shared reference, not a separate workflow or an approval stage.

Read these common instructions and the task index, then the relevant cards,
including their English context, syntax analysis, transfer conditions, and
selection notes. Read text inputs, instructions, cards, and source extractions
explicitly as UTF-8: use `Get-Content -Encoding UTF8` in PowerShell or
`read_text(encoding="utf-8")` in Python. Do not load every card or PDF by default. Abstract-only tasks
select A cards without loading `robotics-main-text.md`; body tasks retain that
module and select B cards. Mixed abstract/body work uses both as needed. For
whole-manuscript reasoning start with B01/B13; for a free paragraph select by
its stated scientific purpose without forcing a section assignment.

The cards here and in task-linked references are the authoritative example text. They contain enough
context and guidance for candidate-package use without the project plan,
evidence report, or raw corpus. Project links and PDFs are optional source
lookups: use the card locator to consult the full paper and surrounding
paragraphs when fine distinctions
need checking or a card does not cover the required realization. If sources
are unavailable, use the card's supported scope or mature general guidance;
do not invent a quotation or scientific premise. For abstracts, read A06 first
as the default language-style anchor, then select matching main or supplemental
passages from the abstract index. The task index is a retrieval
aid, not a substitute for reading the actual English.

## Author meaning and reference coordination

First establish what the author intends to say in the current part: objects,
actions, evidence, conditions, comparisons, and conclusions. Reuse clear author
material and the existing Terminology Ledger; clarify only consequential
ambiguities. An omitted experiment in the input does not establish that the
research never performed it. Example facts, guarantees, and evidence strength
must not enter the author's manuscript as their own findings.

Select a few high-quality, style-matched main reference papers by examining
their actual passages for clear, concise, plain expression and fit to the
author's scientific content, preferences, and existing draft. Use them to
sustain the manuscript's organization and English style. Treat general and
Nature-style organization patterns as options where they fit this content;
current venue requirements remain binding. Supplement with better local realizations from
other papers. Choose relevant excerpts directly; no reference approval gate
or prescribed set is required. Carry the choices and useful tendencies in the
current manuscript context across parts: opening functions, focus of subjects,
object handoffs and transitions, order of conditions and results, and ordinary
collocations. No extra style document is required. Reconcile a supplemental
construction with the manuscript's terminology, person, tense, and local
information order rather than importing an inconsistent voice. Do not imitate
hedging strength, voice ratios, or sentence lengths irrespective of evidence.
Retain accurate choices within the author's established style. Grammatical
validity alone does not justify a departure from the author's requirements.

## Use during drafting, polishing, and feedback

Support discussion of the overall argument, immediate drafting of a specified
section or paragraph group, and feedback on an existing part. These are entry
points, not mandatory sequential confirmations. The six levels (manuscript,
section, paragraph, consecutive sentences, sentence, phrase/word) are views of
the current scope, not six approval stages.

For Drafting, start from the selected main references' actual English passages:
their paragraph development, first-sentence function, consecutive-sentence
progression, subject–predicate constructions, clause patterns, information
order, and ordinary collocations. Map the author's intended scientific relations
onto suitable realizations, retaining mature natural constructions where they
fit. Replace all source-specific scientific content with the author's own
objects, operations, facts, conditions, comparisons, and conclusions. Select,
combine, and adjust these realizations; use supplemental references where they
offer a better local expression consistent with the manuscript's style.
Do not reduce this to
function labels, fixed fill-in templates, or post-draft synonym replacement.
Reuse suitable mature expression without inventing wording for novelty; the
facts and logical relations must be the author's own. Respect shared ethics
for distinctive borrowed material.

For Polishing, first locate the actual failure at the relevant levels, then
start the repair from a matching reference's actual English realization and
adapt it to the author's meaning and established style. Preserve accurate
expressions and alternatives that satisfy that style. A useful example can improve a local clause
without importing its entire paragraph structure or all its wording. Before
retaining a combination from multiple examples, recheck agents, objects,
temporal order, cause, conditions, and scope in the resulting text.

For feedback, edit the requested part and only its necessary dependencies.
Retain the reference choices and terminology unless the author redirects
them; explain a necessary scope extension. Repeat the checks below on the
affected phrases, sentences, and contextual links, not an automatic full
rewrite or a new outline approval.

## Internal expression and context check before delivery

Apply the loaded `scientific-expression.md` internal phrase-to-sentence-to-context
check during generation and before delivery. It owns common syntax, explicit
object naming, technical/action roles, conditions, comparison strength, grammar,
and contextual checks; do not maintain a second general checklist here.

Compare adapted expression units with the relevant main or supplemental English:
check that paragraph progression, sentence relationships, syntax, and ordinary
wording actually use suitable source realizations within the author's style,
not just their function labels. Check that changed objects and relations remain
explicit, necessary conditions
have identifiable scope, comparisons keep like objects, and combinations add
no cumbersome phrasing or repetition without an argument function. Recheck the
affected sentences and paragraph after fixing a unit. Examples are not word
blacklists, required connectives, sentence-length targets, paragraph quotas,
or active/passive ratios. Apply the common core's distinction between errors,
awkward expression, author-style departures, and variants within that style.
Deliver checked prose in the requesting skill's format; the internal audit
does not need to appear as a checklist. Put unresolved scientific questions,
input-status explanations, and reference-choice notes in author notes outside
the manuscript. Do not write descriptions of the supplied notes into prose.


## Abstract reference selection

以 A06（*Robot Learning System Based on Adaptive Neural Control and Dynamic Movement Primitives*）作为默认摘要语言风格锚点：借鉴明确的主语—动作—对象、普通学术搭配和连续句的对象交接，不要求当前研究也有两个组件。A07（*Composite-Learning-Based Adaptive Neural Control for Dual-Arm Robots With Relative Motion*）新增为核心模仿对象，提供反复命名科学对象、设计—作用推进、分析及验证的实际英文。A02（*Fixed-Time Fuzzy Control of Uncertain Robots With Guaranteed Transient Performance*）、A04（*Extended State Observer-Based Integral Sliding Mode Control for an Underwater Robot With Unknown Disturbances and Uncertain Nonlinearities*）和 A05（*Human-Like Adaptation of Force and Impedance in Stable and Unstable Interactions*）仍是主要参考。根据当前科学内容选择、组合，并与 A06 的主要语言习惯协调；不需要每次读完五篇或复刻一个全段。A01、A03 按需补充合适的局部英文，不作为默认整体语言模型。

A08（*Residual Reinforcement Learning for Robot Control*）按需补充已有方法互补、任务分工到信号组合的摘要写法；其正文 B14 说明耦合优化和比较结果如何接作用解释。不改变 A06 默认锚点或上述主要参考分工。

摘要的信息取舍、方法优势、长度及验证表达由当前 `section/abstract.md` 承担，通用句法和对象清晰度由两端共同加载的 `scientific-expression.md` 承担。本文件提供实际英文和取舍，供两层规则按需适配，不另维护一套摘要或通用规范。

## Introduction reference selection

机器人中心的引言起草、结构调整、润色或相关反馈，按当前科学内容读取
[引言范例的选择说明与索引](robotics-introduction-examples.md#selection)，
以 B15／P17／A06 的适用段落及具体英文为默认表达锚点，再按任务关系选择
B16／P05／A07、B17／Fuzzy2023 或 B18／ESO2017 补充。
该索引连接已验收的整节、段落与表达学习材料：先根据作者科学内容确定主线与
段落任务，再按当前关系读取完整英文、连续句分析与具体表达，逐段选择、组合
和调整；Polishing 用同一材料复核科学推进与英文实现。
引言材料中的英文明确标为原文选取或基于原文的适配，保留页码与来源身份。
三个层级按需进入，可脱离项目报告使用。沿用本文件的主参考协调、既有工作流
及共用表达检查；方法概念与本研究实验信息的取舍由该引言索引共同指导两端。
按标题定位本文件的共用说明、引言选择与任务索引，再定位选中学习节的完整
边界，读取其英文、上下文和分析表，使实际读取对应当前引言任务。

## Source conventions

A cards use the author's current abstract selections and retained local illustrations. B cards in this file retain the earlier body evidence and source IDs; task-linked Introduction learning identifies original selections and explicitly marked adaptations separately. PDF pages count from the first file page; cards give sections, paragraph opening words, and ranges. Source links identify current PDFs or an unchanged archived PDF where a retained source has left the active corpus; an archive link does not make that paper a current main abstract reference. Existing extracted texts are optional under `../../../analysis/reading/Pxx.txt`; named additions are located by their PDF links. For A cards and body cards in this file, quotations only join layout line breaks and repair end-of-line hyphenation and ligatures. An ellipsis marks an omission; text on either side is not evidence of consecutive-sentence progression. Source grammar and evidence-strength issues remain in selection notes. Abstracts, body, captions, equations, and cross-section links are distinguished.

## 任务索引与六层覆盖

| 当前任务 | 优先卡片 | 主要层级与选择条件 |
|---|---|---|
| 整体思路与证据分工 | B01、B13 | 全文／Section：双组件与构造依赖；与作者已有思路核对，不强制相同章序 |
| 摘要 | A06 默认语言锚点；A07 核心对象／验证实现；A02、A04、A05 主要参考；A01、A03、A08 按需补充 | Paragraph 至 Phrase／Word，并核对全文承诺；按本文贡献选择具体英文及信息取舍，不强制同一结构 |
| 引言／文献段落组 | [B15 默认表达锚点；B16–B18 按需补充](robotics-introduction-examples.md#selection) | 整节任务、完整段落、连续句与具体表达：按作者任务、信息条件、性能目标或组件依赖选读正向实例，生成与复核使用同一材料 |
| 方法段／公式前后 | B04、B06、B07；组合控制按需 B14 | Paragraph／连续句／Sentence：目的到输入输出、新条件到修正、目标到公式解释 |
| 科学决策的理由 | B05 | Paragraph 至 Phrase／Word：已有可行路线、实际限制、方法选择 |
| 条件保证／判据 | B08、B09 | Section／连续句／Sentence：前提与结论、上下界及修正判据的范围 |
| 比较结果 | B10、B12；作用解释按需 B14 | Paragraph 至 Phrase／Word：指标、对照、统计地位、消融控制与解释范围 |
| Discussion／Conclusion | B11 | 全文／Section／Paragraph／Sentence：综合、已知研究限制与结论回收 |

Use the common instructions above during generation and before delivery; select relevant cards rather than reading all examples.

## 摘要

### A01｜双交互目标：先界定新设置，再分条件说明方法

**功能／定位。** [P11] PDF p.1，Abstract 全段，首词 “Previous works”。上文题名限定 human-guided robots 与 unknown environments；摘要最后接 Index Terms，未混入引言。适用于已有两类控制目标在同一任务中发生耦合的摘要。

> Previous works have developed impedance control to increase safety and improve performance in contact tasks, where the robot is in physical interaction with either an environment or a human user. This article investigates impedance learning for a robot guided by a human user while interacting with an unknown environment. We develop automatic adaptation of robot impedance parameters to reduce the effort required to guide the robot through the environment, while guaranteeing interaction stability. For nonrepetitive tasks, this novel adaptive controller can attenuate disturbances by learning appropriate robot impedance. Implemented as an iterative learning controller, it can compensate for position dependent disturbances in repeated movements. Experiments demonstrate that the robot controller can, in both repetitive and nonrepetitive tasks: first, identify and compensate for the interaction, second, ensure both contact stability (with reduced tracking error) and maneuverability (with less driving effort of the human user) in contact with real environments, and third, is superior to previous velocity-based impedance adaptation control methods.

**组织与句法。** 首句以 previous works 为主语，`either … or …`限定已有设置；次句将人引导与未知环境接触放入同一句，不先贴“研究不足”标签。第三句以作者为主语、adaptation 为设计对象，`to reduce … while guaranteeing …`表示同时处理两个目标。第四句用任务条件作入口，第五句以实施方式承接同一 controller；最后一句把两项抽象目标分别绑定 tracking error 和 driving effort。

**可迁移实现。** 用旧设置与新设置的区别承接贡献；再按作者确有的条件区分方法，而不是逐模块清点。Drafting 需要明确“谁与谁交互、什么条件改变、哪个指标对应哪个目标”；Polishing 检查是否把交互对象、新条件或指标关系写散。`reduce the effort required to …`、`compensate for … disturbances`有具体受事，可按真实对象使用。

**取舍与变体。** `novel`、`superior`不作为必学词；末句并列项目的语法不完全平行（can identify／ensure／is superior），不迁移。保证需有作者证明条件，不能因摘要如此写就无条件使用 guaranteeing。也可将任务分支压成一个条件复句；无需仿照末句的三项长列举。

### A02｜固定时间模糊控制：关键设计直接接其保证

**功能／定位。** [Fuzzy2023] *Fixed-Time Fuzzy Control of Uncertain Robots With Guaranteed Transient Performance*，PDF p.1／印刷页1041，Abstract 全段，首词 “In this article”；下接 Index Terms。TFS 31(3)，2023，DOI `10.1109/TFUZZ.2022.3194373`。完整摘要按空白分词约102词，供信息量比较，不是篇幅或句数规格。

> In this article, an adaptive fixed-time fuzzy control scheme is proposed for an uncertain robot manipulator with user-defined performance. A novel symmetrical barrier Lyapunov function is designed based on the error conversion mechanism and the performance function such that the tracking errors will not violate the prescribed output constraints. A novel adaptive law is constructed and incorporated into the fixed-time controller design such that all the closed-loop signals can be bounded and achieve practical fixed-time convergence regardless of the initial conditions. Finally, the feasibility and superiority of the proposed scheme are demonstrated based on simulation and experimental studies using a Baxter robot.

**组织与句法。** 首句把控制方案、对象和性能要求放在一起，没有长背景铺垫。接着以 `A … barrier Lyapunov function` 和 `A … adaptive law` 为具体主语，`is designed based on … such that …`、`is constructed and incorporated into … such that …`分别连接设计依据、设计动作与作用。最后从方法转到模拟和实机验证，不展开实验设置清单。两项设计各自承担不同保证，不是同一句性能宣传反复出现。

**可迁移实现。** 当作者确有误差约束、控制律或自适应律贡献时，可直接借鉴“设计对象＋构造动作＋必要依据／用途”的句法，把优势落实为对应误差或信号的性质。`based on …`交代依据，`incorporated into …`说明加入哪个设计，`such that …`连接受支持的结果；不要求同时使用这三个短语。设计较多时仅保留使优势可辨的关系，不按正文小节逐个展开。

**取舍与变体。** 保留 `practical fixed-time convergence` 与 `prescribed output constraints` 的技术区别，不把实用收敛改成精确零误差。正文定理1（PDF p.4）要求初始误差在性能边界内，并分别给跟踪误差收敛和闭环信号有界；源文摘要将二者压在一个 `such that` 中，本稿须使各保证的对象和必要条件清楚。原文 `novel`、`superiority` 不提供本稿比较证据；结尾按实际结果表达，不照搬自评。主动设计句或自然被动句均可；不能为模仿本段的短篇幅删除必要条件。

### A03｜判据贡献：把判别操作写到具体可计算量

**功能／定位。** [P18] PDF p.1，Abstract 全段，首词 “The stability criterion”。正文 §IV–V 分别展开竖直及 6-D 判据；摘要不是某一具体定理的完整条件集。

> The stability criterion is critical for the design of legged robots’ motion planning and control algorithms. If these algorithms cannot theoretically ensure legged robots’ stability, we need many trials to identify suitable parameters for stable locomotion. However, most existing stability criteria are tailored to robots driven solely by legs and cannot be applied to thruster-assisted legged robots. Here, we propose a stability criterion for a thruster-assisted underwater hexapod robot by finding maximum and minimum allowable thruster forces and comparing them with the current thrusts to check its stability. On this basis, we propose a method to increase the robot’s stability margin by adjusting the value of thrusts. This process is called stability enhancement. The criterion uses the optimization method to transform multiple variables such as attitude, velocity, acceleration of the robot body, and the angle and angular velocity of leg joints into one kind of variable (thrust) to judge the stability directly. In addition, the stability enhancement method is straightforward to implement because it only needs to adjust the thrusts. These provide insights into how multiclass forces such as inertia force, fluid force, thrust, gravity, and buoyancy affect the robot’s stability.

**组织与句法。** 第一至三句依次给判据用途、缺少理论判别的代价、驱动形式变化。贡献句的 `by finding … and comparing …`把“判据”落实为边界计算和当前量比较。`On this basis`从判别引出调节；单独的短定义句让 stability enhancement 有固定指称。后句以 criterion 为主语解释多变量归约，而非只用 effective 描述性能。

**可迁移实现。** 判据摘要可以围绕“判断对象、许可范围、判别动作、由此可做的调节”组织，适用于真正具有该计算关系的作者结果。Polishing 检查 allowed／current 等修饰是否区分边界与实际值，不能把它们合成笼统 thrust。短命名句无需为凑句长扩写。

**取舍与变体。** 原文宽泛 `critical`、`most existing … cannot`及末句 insights 不提供独立证据。第七句变量清单较长，另一稿可只保留决定可理解性的量。该摘要未给实验结果：这是实际变体，不能推出“所有判据摘要可省验证”。也不能从摘要中缺少定理条件推断保证无条件；B09 的正文条件更具体。

### A04｜观测器与滑模控制：区分估计、控制与验证的对象

**功能／定位。** [ESO2017] *Extended State Observer-Based Integral Sliding Mode Control for an Underwater Robot With Unknown Disturbances and Uncertain Nonlinearities*，PDF p.1／印刷页6785，Abstract 全段，首词 “This paper develops”；下接 Index Terms。TIE 64(8)，2017，DOI `10.1109/TIE.2017.2694410`。完整摘要约148词。

> This paper develops a novel integral sliding mode controller (ISMC) for a general type of underwater robots based on multiple-input and multiple-output extended-state-observer (MIMO-ESO). The difficulties associated with the unmeasured velocities, unknown disturbances, and uncertain hydrodynamics of the robot have been successfully solved in the control design. An adaptive MIMO-ESO is designed not only to estimate the unmeasurable linear and angular velocities, but also to estimate the unknown external disturbances. An ISMC is then designed using Lyapunov synthesis, and an adaptive gain update algorithm is introduced to estimate the upper bound of the uncertainties. Rigorous theoretical analysis is performed to show that the proposed control method is able to achieve asymptotical tracking performance for the underwater robot. Experimental studies are also carried out to validate the effectiveness of the proposed control, and to show that the proposed approach performs better than a conventional potential difference (PD) control approach.

**组织与句法。** 首句命名控制器、机器人对象及其依赖的观测器，第二句概括被处理的问题。第三句将观测器作主语，用 `is designed … to estimate …`列出两类估计对象；第四句换到控制器及自适应增益算法，`using …`说明设计方法，`to estimate the upper bound of …`明确算法用途。最后分别由理论分析和实验研究承载结论，使设计、保证和实际比较可区分。对象转换有功能依据，不靠频繁代词维持表面连贯。

**可迁移实现。** 对作者自己的多组件方法，借鉴具体主语和设计／用途搭配，说明哪个对象提供估计、哪个对象控制、哪个量的边界被调整。只保留与关键优势有关的分工，摘要不需解释观测器或控制器的全部内部步骤。理论结果与实验比较分别匹配作者支持的保证、对照及指标；可以压缩来源第二句宽泛的“问题已解决”，把所处理问题直接接到方法优势。

**取舍与变体。** 引文保留原貌，但其 `potential difference (PD)` 不能作为术语范例：正文 §V.B（PDF p.8／6792）的对照采用位置误差及其导数、Kp／Kd 增益，对应通常的 proportional–derivative（PD）控制，而非电势差。本稿先核实实际控制器再命名。理论跟踪通常用 `asymptotic tracking` 表达，并保留当前作者的证明条件；`unmeasured` 与 `unmeasurable` 也应按传感和材料区分。`novel`、`successfully solved`、`rigorous` 和无指标的 `performs better` 不代替本稿证据。自然并列或分句均可，但不照搬整句的多项长串。

### A05｜力与阻抗学习：用机制和比较突出方法优势

**功能／定位。** [P09] *Human-Like Adaptation of Force and Impedance in Stable and Unstable Interactions*，PDF p.1／印刷页918，Abstract 全段，首词 “This paper presents”；下接 Index Terms。TRO 27(5)，2011，DOI `10.1109/TRO.2011.2158251`。完整摘要约111词。

> This paper presents a novel human-like learning controller to interact with unknown environments. Strictly derived from the minimization of instability, motion error, and effort, the controller compensates for the disturbance in the environment in interaction tasks by adapting feedforward force and impedance. In contrast with conventional learning controllers, the new controller can deal with unstable situations that are typical of tool use and gradually acquire a desired stability margin. Simulations show that this controller is a good model of human motor adaptation. Robotic implementations further demonstrate its capabilities to optimally adapt interaction with dynamic environments and humans in joint torque controlled robots and variable impedance actuators, without requiring interaction force sensing.

**组织与句法。** 首句直接给控制器和交互任务。第二句的主体仍是 controller，`compensates for … by adapting …`把控制动作及其实现方式接起来；开头交代设计依据，没有展开学习更新步骤。第三句以已有控制器为比较对象，在同一句给新的可处理设置及稳定裕度。最后 `Simulations show …` 与 `Robotic implementations … demonstrate …`区分人类适应模型的检验和机器人实现，`without requiring …`限制实现对传感的依赖。方法优势由可处理情况、稳定裕度和传感需求承载，而非只称性能更好。

**可迁移实现。** 直接参照控制器作主语、具体动词接作用对象和方式的英文；本文关键设计可用其机制解释优势，再接与已有方法的真实比较。`compensates for … by adapting …`、`can deal with …`、`without requiring …`只有在相应动作、能力和前提确实属于作者工作时才能适配。模拟和实机的结论按各自对象紧凑交代，不要求所有作者都安排这两类证据。

**取舍与变体。** 该摘要的信息选择紧凑，但第二句的分词开头不是固定样式；本稿可以把设计依据放在清楚的有限动词句中，保留其作用关系。末句同时列环境、平台和传感条件，本稿只保留与贡献相关且会影响理解的部分。`strictly`、`a good model`、`optimally` 需要本稿自己的定义和支持，不作为成熟语言的必用词。比较范围和稳定裕度不可无条件迁移，必要条件不能为压缩篇幅而丢失。

### A06｜默认摘要语言锚点：明确对象、普通句法与句间交接

**功能／定位。** [P17] *Robot Learning System Based on Adaptive Neural Control and Dynamic Movement Primitives*，PDF p.1／印刷页777，Abstract 全段，首词 “This paper proposes”；下接 Index Terms。TNNLS 30(3)，2019，DOI `10.1109/TNNLS.2018.2852711`。完整摘要约154词。它是作者指定的默认语言风格起点，不要求其他研究具有同样组件或全文结构。

> This paper proposes an enhanced robot skill learning system considering both motion generation and trajectory tracking. During robot learning demonstrations, dynamic movement primitives (DMPs) are used to model robotic motion. Each DMP consists of a set of dynamic systems that enhances the stability of the generated motion toward the goal. A Gaussian mixture model and Gaussian mixture regression are integrated to improve the learning performance of the DMP, such that more features of the skill can be extracted from multiple demonstrations. The motion generated from the learned model can be scaled in space and time. Besides, a neural-network-based controller is designed for the robot to track the trajectories generated from the motion model. In this controller, a radial basis function neural network is used to compensate for the effect caused by the dynamic environments. The experiments have been performed using a Baxter robot and the results have confirmed the validity of the proposed methods.

**贡献与内容选择。** §I（PDF p.2／778）、§III.A–B（pp.3–5／779–781）和 §VI（p.10／786）支持两条设计及其系统整合：用 GMM 编码多示教数据、GMR 估计同一个 DMP 的非线性函数，使本文所比较的原始单示教方法无法整合的特征进入一个运动模型；为生成轨迹配备 RBFNN 自适应跟踪控制，补偿不确定动力学（正文以未知负载为例），使学习运动能够实际执行。DMP、GMM／GMR 和 RBFNN 是已有工具；多示教学习增强及生成—跟踪整合才是这里的贡献，时空缩放是所用表示的能力，不另算新算法。

**组织与句法。** 首句的 `considering both motion generation and trajectory tracking`提出系统的两项职责。接着 `DMPs are used to model …`先建立表示对象，`Each DMP`说明趋向目标的稳定运动基础；这为使用 DMP 提供理由，并为 `are integrated to improve the learning performance of the DMP, such that …`交代改进对象。该句把 GMM／GMR 的组合设计接到多示教特征利用，保留足以解释优势的信息，不展开密度估计与回归步骤。`The motion generated from the learned model can be scaled …`承接学习输出的能力，随后 `is designed … to track the trajectories generated from the motion model`把同一输出交给控制器；`Besides`的科学联系在这次交接。`In this controller`再把 RBFNN 的 `is used to compensate for …`定位到刚命名的控制器，说明它为何能处理实际执行中的动力学影响。明确的对象重复和普通用途句法维持连续论述；`During`定位示教阶段，不用模糊代词替代不同方法对象。

**支持与范围。** §V（PDF pp.7–10／783–786）的两组 Baxter 实验分别检验负载下的神经控制与 DMP 模型的泛化、多示教学习，所以末句收束两条设计，保留平台而省去关节、负载数值和倾倒／画图流程。正文 §IV.C 有有界输入下闭环信号半全局一致有界、误差趋于不变集的分析，摘要未单列证明句；生成运动的稳定性质、实际跟踪分析和实机观察各有对象，不能由 `dynamic environments`推成任意扰动完全消除，也不能把实验当作无条件零误差保证。

**可迁移实现。** 从这些具体英文和对象交接开始，把用途、输入输出及可实现的能力完整替换成作者事实；单方法摘要同样可借鉴其普通主语—谓语和搭配，不必引入第二个问题或组件。若本文确有运动生成与跟踪，才借鉴系统功能分工。Polishing 核查生成性质、控制保证及执行观察是否混为一谈；不能将 motion can be scaled 写成任意实际任务均成功。选定合适句式后检查有意义的词组及前后关系，不按源文逐句填空。

**取舍与变体。** 学其主要语言习惯，不把每个源词都视为最优：`enhanced`、`more features` 和 `confirmed the validity` 未在摘要中给出具体比较或发现，本文有关键设计优势或结果时应直接表达它。源文每个组件的细节也不是配额；可从 A02 借鉴设计接保证、A04 借鉴估计与控制分工、A05 借鉴机制与比较的压缩。DMP、GMM／GMR、RBFNN、Baxter 和生成能力均属于来源事实，不自动迁入本稿。被动与主动、条件位置及必要句长均可按作者科学含义调整。

### A07｜核心模仿对象：明确命名对象，设计—作用—分析—验证推进

**功能／定位。** [P05] *Composite-Learning-Based Adaptive Neural Control for Dual-Arm Robots With Relative Motion*，PDF p.1／印刷页1010，Abstract 全段，首词 “This article presents”；下接 Index Terms。TNNLS 33(3)，2022，DOI `10.1109/TNNLS.2020.3037795`。作者认可其整段组织和具体英文；与 A06 默认语言锚点协同，不替换其他已认可主要参考。

> This article presents an adaptive control method for dual-arm robot systems to perform bimanual tasks under modeling uncertainties. Different from the traditional symmetric bimanual robot control, we study the dual-arm robot control with relative motions between robotic arms and a grasped object. The robot system is first divided into two subsystems: a settled manipulator system and a tool-used manipulator system. Then, a command filtered control technique is developed for trajectory tracking and contact force control. In addition, to deal with the inevitable dynamic uncertainties, a radial basis function neural network (RBFNN) is employed for the robot, with a novel composite learning law to update the NN weights. The composite learning is mainly based on an integration of the historic data of NN regression such that information of the estimate error can be utilized to improve the convergence. Moreover, a partial persistent excitation condition is employed to ensure estimation convergence. The stability analysis is performed by using the Lyapunov theorem. Numerical simulation results demonstrate the validity of the proposed control and learning algorithm.

**贡献与内容选择。** §I（PDF p.2／1011）明列三项：未知动力学下执行非对称相对运动任务的双臂神经控制框架；把权值估计误差信息引入更新律的复合学习，以改善估计性能；在该估计框架中引入 PPE，放宽传统 PE 要求。命令滤波、RBFNN、PPE 概念和局部激活性质都有既有来源，不因各占一句就成为本文发明的基础工具。§II.A 同页的一臂抓持物体、另一臂沿物体表面用工具运动，解释了相对运动区别及轨迹／接触力控制为何必要。

**组织与句法。** 首句用 `to perform … under modeling uncertainties`连接方法、对象、任务与难点；紧接的 `relative motions between … and …`把泛称双臂任务限定到真实区别。该区别决定 `The robot system is first divided into …`中的两种职责，继而由 `is developed for trajectory tracking and contact force control`交代实现目标，不展开坐标系、约束方程或滤波步骤。`to deal with … dynamic uncertainties`回接首句难点，RBFNN 的 `with … to update the NN weights`引出作者的学习律。下一句重复命名 `The composite learning`，用 `is mainly based on an integration of the historic data … such that information of the estimate error can be utilized …`把历史回归数据、估计误差信息和收敛作用连起来，兑现学习优势；§III.B（pp.6–7／1015–1016）的辅助误差构造及更新律(48)支持这条关系，摘要省去积分辅助量、遗忘因子和投影细节。随后 PPE 接到 `estimation convergence`，同时呈现条件放宽的贡献和估计结论的限定。最后 `The stability analysis is performed by using …`与 `Numerical simulation results demonstrate …`分别提供理论与数值支持；具体名词的重复维持对象身份，连接词不能替代这些技术关系。

**支持与范围。** Theorem 1（PDF p.6／1015）在 PPE 及相应控制条件下保证跟踪误差、受激励权值的估计误差趋于原点小邻域，接触力误差有界；`ensure estimation convergence`不能解读成全部权值无条件精确辨识。Lyapunov 工具名称也不能替代必要条件。§IV（pp.7–10／1016–1019）以 PID、普通神经学习控制和本文方法的数值比较支持控制与学习效果，所以末句明确这两个贡献对象，省去机器人参数、曲线编号和权值变化细节；它没有实机证据。

**可迁移实现。** 可直接借鉴方法／对象开篇、`is divided into …`、`is developed for …`、`is employed … to …`、`is based on … such that …` 及分析／验证的普通句法，把科学内容全部替换为作者自己的。写下一句前确定当前动作属于哪个系统、方法、学习过程或分析，必要时重复其名称；不能只用 learned 等状态修饰代替对象类别。摘要验证默认优选本段的 `Numerical simulation results demonstrate …` 和 A04 的 `Experimental studies are also carried out to …`，分别适配实际观察结论与研究目的；前者的结果不能由后者的目的推出。按证据命名结果对象和支持的性质，不统一套成 validity 结尾。

**取舍与变体。** 模仿其信息推进和普通英文，不把双臂分解、NN、历史数据、激励条件或 Lyapunov 分析迁入其他研究。原文的分系统冒号、长目的从句及多项并列不是必学形式；按通用核心拆解过载信息，保留条件的作用域。多个设计无需照抄本段的逐项篇幅，本文贡献及摘要目的决定取舍。`novel`、`inevitable`、`improve the convergence` 和 `validity` 需对应本稿自己的对象及支持；估计收敛、运动跟踪和闭环稳定不能互换。理论分析与数值模拟不自动成为实机实验，主动／被动及更具体的验证陈述均可保留。

### A08｜互补方法：从已有能力与难点到任务分工和信号组合

**功能／定位。** [RRL2019] *Residual Reinforcement Learning for Robot Control*，ICRA 2019，pp.6023–6029，DOI `10.1109/ICRA.2019.8794127`。采用本地出版版 PDF p.1／6023 的完整 Abstract，下接 §I；与作者 arXiv:1812.03201v2 的摘要经版面断词、连字及换行规范化后相同。正文页码以下均指出版版；核验文本为 `../../../analysis/reading/RRL2019.txt`，版本依据见 `../../../analysis/RRL2019-example-addition-2026-10-04/source-basis.md`。按需补充，不替换 A06 的默认语言锚点。

> Conventional feedback control methods can solve various types of robot control problems very efficiently by capturing the structure with explicit models, such as rigid body equations of motion. However, many control problems in modern manufacturing deal with contacts and friction, which are difficult to capture with first-order physical modeling. Hence, applying control design methodologies to these kinds of problems often results in brittle and inaccurate controllers, which have to be manually tuned for deployment. Reinforcement learning (RL) methods have been demonstrated to be capable of learning continuous robot controllers from interactions with the environment, even for problems that include friction and contacts. In this paper, we study how we can solve difficult control problems in the real world by decomposing them into a part that is solved efficiently by conventional feedback control methods, and the residual which is solved with RL. The final control policy is a superposition of both control signals. We demonstrate our approach by training an agent to successfully perform a real-world block assembly task involving contacts and unstable objects.

**贡献与内容选择。** §I（p.1／6023）、§III.A–B（p.3／6025）及 §VIII（p.6／6028）把主要贡献落实为固定反馈控制与可学习残差相加的控制方法：已有控制结构处理机器人几何目标，交互学习修正接触、摩擦及物体动力学。机器人与物体耦合，式(5)的组合输入仍须针对完整任务回报优化，不能把两项职责当作互不影响的优化问题。TD3、阻抗控制、神经网络和经验回放是已有工具；样本效率、错位适应及仿真到实机是该方法的支持，不另拆成多项基础算法发明。§VII（p.6／6028）明确有同期独立的 residual policy learning 工作，本文重心在真实接触任务训练，不能据标题宣称首创一切残差学习。

**整段与连续句。** S1 的 `by capturing the structure with explicit models`先给常规控制的能力与依据；S2 `However … contacts and friction, which are difficult to capture …`保持同一控制问题，指出何种任务成分超出简单建模。S3 的 `Hence`只把这个难点接到 `these kinds of problems`下的控制器性能和部署调节，并非所有反馈控制均不可靠。S4 用 `have been demonstrated to be capable of learning … from interactions …, even for …`引入已有 RL 的互补能力，仍回接接触／摩擦。因而 S5 `by decomposing them into …`提出本文的职责安排时，两部分已有选择理由；不是先列工具再自称融合创新。S6 的 `The final control policy is a superposition of both control signals`把概念分工落实为相加输入，`both`有明确的两个先行对象，不能替换成前一模块输出交给后一模块的串联关系。S7 `We demonstrate our approach by training an agent to …`接真实任务证据，`involving contacts and unstable objects`回到前述难点；`unstable`修饰物体，不是闭环控制器。

**支持与取舍。** 摘要为解释互补设计保留常规控制能力、接触难点、已有 RL 能力及组合关系，未展开 TD3、回放、奖励公式或调参步骤；也未列全部实验。§VI（pp.4–6／6026–6028）以样本／最终表现、错位插入、控制噪声及固定侧块迁移支持作用。出版摘要只说明成功任务，不报告具体对照数字；本文有关键比较时可以用准确结果替换这一概括。§III.A 的指数稳定论述限于忽略学习残差且子空间可稳定化的基准误差系统，不是完整学习闭环定理；实机噪声只测偏置，千步迁移只适用于固定侧块。不能从 `demonstrate`推出无条件稳定、安全或普适成功。

**可迁移实现与变体。** 当作者确有已有方法互补关系，可从整段的“能力依据—任务难点—另一能力—职责安排—具体组合—验证”及这些连续句法出发，替换作者自己的对象、动作、作用和证据。`by`须分别承担真实机制、设计方式或验证方式，`which`须指向正确对象；配合 B14 核查分工是否仍受耦合约束。若读者已知背景，可直接提出方法，保留必要作用和组合关系；不把前三句设为配额。`very efficiently`、`brittle and inaccurate`和`have been demonstrated`各需作者材料支撑；不为模仿制造既有工作的缺陷或引用。成熟表达适用时直接沿用，原文背景铺垫及泛称成功并非必须照搬的长度或结尾。

## 正文：全文与章节组织

### B01｜双组件系统：正文结构、验证分组和摘要承诺互相对应

**功能／定位。** [P17] PDF p.1 Abstract／§I，p.2 §II，pp.3–4 §III，pp.5–7 §IV，pp.7–10 §V，p.10 §VI。这是全文与章节证据，不能当作同段连续句。

| 原文位置 | 信息与后续用途 |
|---|---|
| 摘要／引言 | 区分 motion generation 与 trajectory tracking；A06 的轨迹输出交给控制器 |
| §II Basic Model of Discrete Movement | 先交代 DMP 的动态结构，供 §III 的多示教估计使用 |
| §III Learning of the Motion Model | Problem Description → Learning From Multiple Demonstrations，得到可生成运动的模型 |
| §IV Adaptive Neural Control | Dynamics Description → RBFNN → Controller Design，支持闭环分析 |
| §V Experiments | 分别测试 NN controller 和 DMP motion model，随后 pouring／drawing 检验模型用途 |
| §VI Conclusion | 回收运动学习与跟踪，不新增实验 |

**原文短上下文。** p.7 §V 首段：

> The proposed system is tested by two groups of experiments: the test of the NN-based controller and the test of the DMP-based motion model.

p.7 §V.A 首两句：

> In this group of experiments, the performance of NN learning is tested, which compensates for the uncertain manipulator dynamics caused by the payload. The experiments are performed on the Baxter robot that has two seven degrees-of-freedom arms.

**具体实现。** 章节不是按“先讲方法、再堆实验”分隔：DMP 的输出成为控制器 reference；验证节首句先声明证据分工，再进入硬件与工况。该开头承担 section roadmap，不是性能主张。Drafting 可用作者的“任务／对象／支持证据”安排章节和小节；Polishing 检查实验标题与本节测试对象是否一致。

**取舍与变体。** 不学 `performance … is tested, which compensates`的含混回指，应明确是 NN learning／controller 补偿动力学，而非 performance。系统不必须每模块一个实验。另一合理顺序是 P09 p.4 §III 先仿真、p.7 §IV 后证明、p.8 §V 实机；实读这些标题确认顺序，保证与证据对应才是可迁移关系。

### B13｜章节入口：指出前节产物如何支撑当前构造

**功能／定位。** [P12] PDF p.8 §IV “Learning a GAS ADS With Predefined Position Constraint”首段；上文 §III 已学习 NEUM，后文 §IV.A 从原 ADS 学习起步。

> In this section, we first learn an original ADS ˙x = o(x) with a desired equilibrium point, i.e., o(0) = 0, using a modified Gaussian process regression (GPR) algorithm [47]. Then, we introduce an approach to formulate a GAS ADS by combining the original ADS and the NEUM learned in the previous section. Except for considering the global stability, we further show that we can add a predefined position constraint to the learned ADS, which may be valuable for some robotic tasks. Moreover, we analyze the generalization ability of the learned ADS in areas away from the demonstration area by utilizing the flexibility of the NEUM.

**组织与句法。** 首句交代本节新输入；第二句明确 previous section 的产物和当前输入如何组合。第三句增加约束，第四句才转向示教区外分析。`original ADS`、`GAS ADS`、`learned ADS`修饰对应构造状态，不能为了不重复改成无法回指的同义词。

**可迁移实现。** 对复杂方法章节可先给短路线图：当前新对象、已有对象、组合后性质、分析范围。Drafting 只预告本节实际内容；Polishing 删纯粹“本节提出一种方法”的空引导，必要时写出先后依赖，而非增加连接词。

**取舍与变体。** `Except for considering`表达附加关系不够自然，不作为搭配学习；may be valuable 是潜在用途，不能改为已证价值。若当前小节对象已由标题和前段充分定义，可以直接从条件或定义开始，无需每节都再写 roadmap。同一论文的章节导读和摘要承担不同功能，不应逐句重复。

## 正文：段落展开与连续句

### B02｜文献段：通过观测输入和控制动作比较路线

**功能／定位。** [P11] PDF p.2 §I.A “Control of Human–Robot Interaction”，段首 “Facing uncertain human behaviors”。首三句为相邻句；下面另列的段末句与它们相隔数条方法，不能拼成四句连续链。§I.B 随后改谈环境侧，§I.C 才合并问题。

> Facing uncertain human behaviors, a number of works estimate the human impedance or intention to dynamically adjust the robot’s impedance parameters for efficient and stable interaction. For instance, it has been proposed to regulate the robot impedance using muscle activity measured with surface electromyography, although the underlying control is limited by the large signal variability and neural constraints [1], [2]. To address these limitations, several approaches used the force and position information of the human limb, which can be directly measured by sensors, to infer their impedance and adjust the robot’s impedance correspondingly [3], [4].

**同段后续上下文。** 后面依次讨论其他 intention／impedance 推断、velocity heuristic、probability／time-series、改 reference trajectory 等路线，最后一句是：

> However, previous works do not explicitly consider concurrent interactions between the robot, human operator, and environment.

**组织与句法。** 首句由不确定的人体行为引出该段比较范围；`For instance`给具体信号路线，although 限定信号方案；`To address these limitations`引出可直接测量的力／位置。关系从句限定传感可测的是 force/position information，主句的 infer 作用于 impedance，测量与推断没有混同。段内后来也有 alternative 控制动作，而非每句都说“旧方法失败”。

**可迁移实现。** Drafting 文献段落组时按“什么输入、推断什么、改哪个控制量、在哪个设置有效”选择相关信息；Polishing 检查比较项是否同层及量的来源是否改变。具体可用的关系是 `use measured force and position … to infer impedance`，前提是作者文献确有这些观测与推断。

**取舍与变体。** 原文整段较长，不迁移作者逐项罗列的篇幅。这里的 previous works 是该文综述集合，不能推广为当前全部文献，更不能从作者未提供某篇信息制造 gap。可分成 EMG／测力位置与 motion-based 两段，只要段落组的比较任务完整；独立 Related Work 和 Introduction 内文献段都合理。

### B03｜贡献段：由耦合矛盾许可设计动作

**功能／定位。** [P11] PDF p.3 §I.C “Contributions … Human–Robot–Environment Interaction”首段全段；前面两组文献分别处理人机和环境交互，后段再讨论学习如何用于 carving／grinding／polishing。

> Different from the aforementioned works that considered either the interaction between robot and environment, or the interaction between robot and human, we will consider here both the human operator and the environment. We will design a robot controller that automatically infers the intention of the human and adapts to an uncertain environment by learning the resulting impedance to improve the task performance. It is not a simple combination of two controllers for robot–environment interaction and human–robot interaction, as the two control objectives can be contradictory, leading to a conflicting trade-off between maneuverability and contact stability as discussed above. Our idea is to maintain the robot’s maneuverability by inferring the human intent while only introducing additional impedance to deal with the environmental disturbance and, thus, ensure contact stability. As a result, both the maneuverability and the contact stability can be ensured during the human–robot–environment interaction, and the conflict between the human effort and the task performance is addressed.

**组织与句法。** 五句分别转换设置、设计动作、不能简单组合的理由、应对该理由的机制、目标回收。`as … can be contradictory`给具体原因；`by inferring … while …`明确两条动作的不同职责。主语由 we 到 it／objectives／our idea／two goals，变化服从论证焦点。

**可迁移实现。** 贡献并非堆两个模块：先明确组合会遇到什么技术冲突，再用实际设计解释如何处理它。Polishing 追问“our idea”的动作是否回应上一句的冲突；若作者仅组合模块而没有冲突证据，不借用这个否定句型。

**取舍与变体。** future `we will`是作者行文偏好，本稿可用 we develop／the controller adapts 等已完成设计的叙述。最后句保证须回到实际模型和证明，不复制为无条件能力；conflicting trade-off 有语义重复。连续段落与有内容的贡献列点都是合理实现，不能据此固定贡献段长度或第一人称比例。

### B04｜方法段：四种主语，连续的估计—应用对象链

**功能／定位。** [P01] PDF p.2 §II.A “EMG-Based Variable Stiffness Estimation”首段全段；前一节入口说明该模块的位置，后一段才给人臂刚度坐标变换式 (1)。

> This modality is developed to enable the robot to learn a proper stiffness regulation strategy from the human tutor during demonstrations. To do so, the human tutor’s limb endpoint stiffness is estimated first. The EMG signals extracted from the tutor’s arm are used to monitor the muscle activation for the stiffness estimation. Subsequently, the estimated human endpoint stiffness profile is transferred to the robot as the gains in the joint impedance controller.

| 句位 | 主语／谓语与信息顺序 | 为下句提供什么 |
|---|---|---|
| 1 | modality → is developed → 学习目的／示教阶段 | 要学习的是刚度调节策略 |
| 2 | limb endpoint stiffness → is estimated first | 必须先得到估计量 |
| 3 | EMG signals → are used to monitor → activation／估计用途 | 估计所依据的信号角色 |
| 4 | estimated stiffness profile → is transferred … as gains | 估计输出变为控制器参数 |

**可迁移实现。** 先确定目的与待估计对象，交代输入及观测量，再写输出的下游用途；各句可变换主语和语态。Drafting 不需要四句齐全，但不能把 EMG 当成直接测刚度。Polishing 查看 monitor／estimate／transfer 是否作用于正确对象；`as gains in … controller`表示参数映射，不等于把物理刚度直接“施加”给机器人。

**学习性改述。** 在上述已给事实内，可将末两步写为：`EMG signals are used to monitor muscle activation for endpoint stiffness estimation. The estimated stiffness profile is then mapped to the gains of the robot’s joint impedance controller.` 这保留观测、估计用途与参数映射，删去原段的宽泛评价。它只演示两个操作的清楚表达，不能代替当前作者缺失的估计模型或把任务内容直接复制进其他稿件。

**取舍与变体。** proper、enable 等宽词非必选；当题目和前文已清楚，可直接以待估计量或信号开头。主动实现可明确 signal-processing／estimation model 的施事者，但需要作者确有该模型；不能仅为改被动句而补造步骤。这是信息链，不是要求每句保持相同语法主语。

### B05｜方法选择段：承认解析路线，再说明实验测定理由

**功能／定位。** [P19] PDF p.5 §V “Stability Region”第二段全段，首词 “The stability region”。前一短段设定研究对象，后文才给线性情形与具体实验参数。

> The stability region in the impedance parameters space could be estimated analytically (see, e.g., [24]). However, many authors have observed that the actual bounds of the stability region are dependent on the robot’s hardware and, in the case of interaction with a human operator, also on the impedance of the human arm, which cannot be accurately modeled and evaluated [19], [20]. A further complication here is represented by the null-space stability for the presence of redundant DOFs [30]. Therefore, in this study, the stability region has been found experimentally.

**组织与句法。** 首句说明可行理论路线而非立即否定它；第二句以 many authors 归属已有观察，并把人臂依赖放在交互条件中；第三句引入冗余 DOF 额外问题；第四句仍以 stability region 为对象，experimentally 区分测定途径。However 是范围转折，further complication 是新增障碍，Therefore 是方法选择的结论。

**可迁移实现。** Drafting 先写作者为何未沿用一条原本可行的路线，理由应涉及真实对象和条件；Polishing 将空泛“therefore we propose”改为可回指具体限制的决定。`estimated analytically`与`found experimentally`不是风格同义词。

**取舍与变体。** 可将长第二句拆成硬件依赖与人机条件两句，只要归属及作用域保留。`is represented by`和`for the presence of`较重，不是推荐固定搭配；可以选择直接 complication arises from 等普通实现，但须保持零空间问题。没有该类限制时，可直接给方法，不要求每段都先否定解析路线。

### B06｜扩展段：新任务条件改变系数，再修改已有控制律

**功能／定位。** [P11] PDF p.5 §IV 首段全段。段落从左栏底连续到右栏顶；回看 PDF 确认不是两个段落。§III 是非重复任务自适应控制，后续式 (19) 才写新的扰动形式。

> When the robot performs a repetitive task, the environment has spatial periodicity, thus, the disturbance can be considered as a function of the position as discussed in [26]. To further elaborate, instead of constant matrices, coefficients of the disturbance are spatially periodic, i.e., their values are the same for the same position in different iterations. We modify here the adaptive impedance control proposed in Section III for repetitive tasks, making it suitable for space-related disturbances with varying coefficients. The subscript s is used for space-related variables and time-related variables are without s. The subscript i of a variable denotes its iteration number.

**组织与句法。** 任务条件首句 → 系数的同位置跨迭代含义 → 修正 §III 控制 → 索引定义。第二句不是再说一次 repetitive，而是将第一句条件落实到系数；第三句明确修改对象；两个短定义供下一式使用。

**可迁移实现。** 适用于同一方法在新条件下的扩展。Drafting 把“什么条件变了、哪个对象因此变了、旧方法哪处要改”写清；Polishing 检查是否只靠 When／thus 建立不存在的因果。`same position in different iterations`比只写 spatially periodic 更具体，只有作者模型如此定义时才使用。

**取舍与变体。** 重复任务不普遍意味着环境空间周期，不能迁移为机器人领域事实；首句是本研究设置。原文逗号串连与 `We modify here`字序不作优选句型。短索引句可保留，也可按变量定义合并；当不涉及迭代，没有理由加入这套下标。非重复与重复条件的重复用于标识不同保证，不能按无用词删去。

### B07｜公式前后：将建模假设、目标和权衡留在同一段

**功能／定位。** [P16] PDF p.3 §III.A “Reference Trajectory Shaping”首段、式 (5) 及紧随解释；此前 §II 已定义动力学，后续式 (6) 用阻抗模型求解代价。以下前引三句为连续句，后引在式 (5) 后，不能去掉公式当作四句直接相邻。

> While interacting with the human, the robotic exoskeleton will track a new trajectory that deviates from the desired trajectory, which is due to the human subject’s intention. In general, the human intention can be represented by the new trajectory, namely reference trajectory. Considering the decrease in the interaction force and the convergence of the tracking errors in the meantime, we assume that the adaption to the desired trajectory is to minimize the following cost function:

**式 (5) 后的局部解释：**

> Then, there is a balance between the human force and the error of the reshaped trajectory.

**组织与句法。** 首句为交互情境，次句命名本文的意图表示，第三句把 force 与 error 双目标对应到 minimize cost，并用 we assume 标记建模决定。公式后不是重列参数，而是说明权衡含义；具体 R／G 权重仍在式后的定义中。

**可迁移实现。** Drafting 将作者选择的表示与双目标交代在公式前，公式后说代价结构意味着什么；Polishing 修复“裸公式”或不明所以的优化，而不添加作者未提出的优化问题。`represented by … reference trajectory`是模型表示，不能自动写成已直接测得人的意图。

**取舍与变体。** 原文 which 回指、adaption／in the meantime 和泛化 `In general`不作为标准表达；具体稿可改成明确的模型内陈述。公式作用若已由上段解释，例行等式无需重复动机。这组证据不能推导每段必须“目标—公式—解释”齐套。

## 正文：条件保证、比较与结尾

### B08｜定理句：约束、方法和保证相邻而不混同

**功能／定位。** [P08] PDF p.5 §III Theorem 1 全陈述（不含随后 Proof）；前面式 (35)／(36) 定义控制器与自适应律，(11)／(12) 在前文定义约束。

> Theorem 1: For the unknown robot manipulator in (1), when the initial conditions are within the output constraints in (11) and (12), the tracking error ei in (10) can be fixed-time convergent without violating the constraints when the NN controller in (35) and the adaptive law in (36) are employed. Moreover, all the closed-loop signals in the system are GUUB.

**组织与句法。** For 指系统域，第一个 when 指初值域；tracking error 是被断言 fixed-time 的对象；第二个 when 指采用的控制器／自适应律。末句改谈 all closed-loop signals 的 GUUB，是另一个保证，而非固定时间的同义换说。

**可迁移实现。** Drafting 先确定保证对象、条件和方法，写在同一语义单位内；Polishing 可将初值条件独立成句，下一句明确用 under those conditions／under the stated controller 等回接，不能切断适用范围。`without violating the constraints`修饰同一跟踪保证，需要保留。

**取舍与变体。** 原文 can be fixed-time convergent 不必照搬为优选语法。长句也不是质量证明，若符号关系易读可保留，若过载可拆；不用 30 词阈值判断。finite-time、fixed-time、GUUB 与 SGUUB 是不同性质，不进行“更高级词”替换。此卡学习陈述组织，未复算定理。

### B09｜上下界的物理后果与跨节判据修正

**功能／定位。** [P18] PDF p.8 §IV “Vertical-Thrust-Based Stability Criterion and Enhancement”开头第二段全段，后续优化求最大／最小推力；同页 Remark 5 在 §V 前。前段的四句连续；Remark 与新标题是跨节关系。

> When the vertical thrust is too large, the robot may fall due to the support leg’s torque limit. When the vertical thrust is too small, the forward and lateral contact forces may not be sufficient to suppress the robot’s inertial and fluid forces, resulting in the support leg slipping. Setting the appropriate vertical thrusts is necessary so the robot will not fall or slip. We need to find the maximum/minimum vertical thrusts that can be applied to the robot body without losing stability.

**Remark 5 的连续前五句：**

> Although it possesses the above advantages, the criterion in this section only uses vertical thrust. Once the robot cannot maintain the prescriptive balance by adjusting the vertical thrust, the criterion regards that the robot is unstable. However, the robot may still be stable when using the 6-D thrust. That said, the criterion is slightly conservative. Thus, we need to use the 6-D thrust to improve its necessity and the accuracy of judging the robot’s stability.

随后另说恒定 relaxation 的限制，再进入 §V “6-D-Thrust-Based Stability Criterion and Enhancement”。

**组织与句法。** 句首条件对举给两种不同失败后果，第二句的 resulting in 指向支撑腿打滑，不是第一句的跌落。前段末句从这两个后果导出允许推力范围。Remark 将“竖直调整失败”与“所有推力都不可行”区分，随后新章节扩大判据输入。

**可迁移实现。** Drafting 按作者确有的上下界分别写条件与后果，再引出区间／判别量。Polishing 防止将两方向压成“增加推力提高稳定性”。必要性、充分性和可行范围须按实际定理表达；可以用两个短条件句，也可合成对比复句。

**学习性改述。** Remark 中的关键区别可以直接说：`Failure of the vertical-thrust test does not rule out stability with six-dimensional thrust.` 这里没有断言六维推力必定能稳定，只保留原文的可能可行性；后文仍需给作者实际构造的判据和条件。它是特定原文关系的另一实现，不是所有“旧方法失败”都能套用的反驳句。

**取舍与变体。** 原文 `regards that`、`prescriptive balance`、`improve its necessity`不作默认搭配；应澄清判据保守性／适用范围，不能借润色改变数学性质。跨节扩展不是普通句间衔接范例。Remark 的必要条件重复承载不同判据，不能机械删去。

### B10｜结果段：先区分指标，再限定趋势和解释

**功能／定位。** [P19] PDF p.11 §VII.D “Variable Versus Constant Impedance”，段首 “For the sake of completeness”，全段。前文已交代五名受试者、Fig.15 的 H／路径长度误差、Table I 的 t-test；本段只比较 high／low constant damping，不是 variable 与 constant 的全部结论。

> For the sake of completeness, the results of the comparison between high and low constant damping parameters have also been reported. By observing Fig. 15 and Table I, the advantage of using high damping parameters for accuracy appears clear and statistically significant. The execution time improves when low damping is adopted since the robot become lighter and easier to move (see Fig. 16). However, the result on the execution time is not statistically significant: This is probably because the subjects were instructed to prefer accuracy over speed during the execution of the task, which has led to a higher dispersion of the data related to execution time.

**组织与句法。** 首句界定这是一项补充比较，次句将 high damping 的精度与图／表绑定；第三句换 execution time 及 low damping 条件，第四句 immediately 限定同一指标的统计地位，再用 probably 提解释。换主语正好体现换指标，不能把两句合成“总体更好”。

**可迁移实现。** Drafting 报两个方向不同的指标时，让 comparator／metric／condition 同位，统计限定贴近所属指标；Polishing 让“时间更短”保留为未显著趋势，解释留在可能层。更直接的指标名来自前文定义，不可以仅凭 accuracy 猜误差方向或指标值。

**学习性改述。** 本段的两项发现可分别写成：`High damping produced significantly better accuracy in this comparison. The execution-time improvement with low damping was not statistically significant.` 这里没有推断阻尼必然造成结果，也没有把趋势删掉；前文仍需保留真实比较设置和指标定义。解释是否另写一句由当前任务决定，不强制在每个结果段都添加原因。

**取舍与变体。** `For the sake of completeness`与图表全套复述未必值得占主文；若是次要比较可按本稿意义压缩。`robot become`的语法错误不迁移。该段 since 的因果比证据可能更强，末句 `which has led`也偏确定，应按作者实验设计决定能否保留。紧邻上一段的 “guarantees the best performance”不作为优选表达：这个指标与统计分离的段落是学习对象，不全盘认可整节措辞。

### B12｜组件比较：固定输入后才能解释消融差异

**功能／定位。** [P06] PDF p.12 §IV.C “Ablation Study”开头的比较目的与固定因素段，随后列两种 variant。此前 §IV 给两主控制器任务结果；本小节明确要区分 sZFT 重建与 directional adaptation。

> In addition to the two main controllers, we performed an ablation study to isolate the contributions of the reconstructed sZFT (Section III-A) and the directional impedance adaptation (Section III-E).

> Importantly, the nominal ZFT was kept fixed throughout the ablation study. It was generated from simple kinesthetic demonstrations and was not optimized for the two tasks and pegs. Videos illustrating the kinesthetic teaching procedure for the parkour and peg-in-hole tasks are provided on the project website.

**结果上下文。** 原文随后区分 uniform adaptation＋reconstructed sZFT、directional adaptation＋nominal ZFT 两变体，报告前者两场景失败；后者 parkour 停止，圆柱 peg 达 30/30，但方形和星形失败。最后推断是针对这些设置的 directional factors 来源，不是所有机器人控制的充分必要性定理。

**组织与句法。** 小节首句给比较目的与两待分离组件；下一段以 nominal ZFT 为主语说明固定因素，再追溯生成来源和未优化状态。句子的 fixed／not optimized 是作者明确报告的实验控制，不是执行者从没有材料猜出来的研究限制。

**可迁移实现。** Drafting 只有作者提供消融时才交代改动与保持因素；Polishing 核查结果归因是否与消融设置一致。`kept fixed throughout …`、`generated from … demonstrations`是实验控制与来源的具体搭配，需要真实支持。

**取舍与变体。** 不把消融写成每篇必须补做的实验，不复制网址信息来证明因果。原文结尾 must／insufficient 不能自动扩大到其他任务。即使保留数字，也应同时保留成功和失败条件，不择取 30/30 作普适成功。

### B11｜结尾：作者支持的限制与有边界的回收

**功能／定位。** 两种实现。第一组 [P19] PDF p.12 §VIII 最后一段全段，首词 “Another important issue”；随后 §IX 首段回到冗余策略与合作书写实验。第二组 [P04] PDF p.9 §IV Example 2 末段，首词 “Compared with Example 1”。这是两个不同片段，不是一条连续句链。

**P19：**

> Another important issue is that our study does not include a rigorous stability proof, for both fixed and variable impedance parameters. As a matter of fact, although the experimental results provide significant and useful guidelines, these cannot be easily generalized to any kind of robot and task.

**紧随的 §IX 首三句：**

> In this paper, the problem of Cartesian impedance control of a redundant robot arm executing a cooperative task with a human has been addressed. In particular, redundancy has been used to keep robot’s natural behavior as close as possible to the desired impedance behavior, by decoupling the end effector equivalent inertia. This allows easily finding a region in the impedance parameter space where stability is preserved.

**P04 的结果／潜在用途：**

> Compared with Example 1, the new stability measure reduces the minimum cost from 0.72 to 0.50. Loop shaping improves performance, and complementary stability parlays knowledge of the environment into further performance gains. The latter result is robust to realistic environmental uncertainty; an exact model is not required to reap benefits. Though not demonstrated here, this approach also provides a means of controller design when the environment may be nonpassive.

**组织与句法。** P19 明说研究未含严格证明，再界定实验指南的推广边界；Conclusion 改做问题、策略和作用回收，没有把限制段逐句再播。P04 从当前对照结果转到模型要求，再用 Though not demonstrated here 将另一用途放在未展示层。

**可迁移实现。** 科学限制必须是作者证据中的研究事实，缺输入只进入作者说明。Drafting／Polishing 在结尾保留会改变推断的边界，但每次出现应承担新作用；Discussion 综合、Conclusion 压缩回收，不在两处复制同一适用域清单。定理条件若限制新的保证，仍需要邻接保留。

**取舍与变体。** P19 significant and useful 不能替代具体范围，`cannot be easily generalized`需要本稿作者支持。P04 parlays／reap benefits 比本项目要求的朴素表达更修辞化，不列入推荐搭配；该文的明确 demonstrated 边界可学。独立 Discussion、实验内局部讨论、直接 Conclusion 均可能合理，按本文确需的解释选择。

### B14｜组合控制：职责分工接耦合优化，比较结果接作用解释

**功能／定位。** [RRL2019] 出版版 §III.A（PDF p.3／6025），式(5)及基准误差动态讨论之后的完整相邻三句；§VI.A（p.4／6026）首段前三句。前一处接控制组合为何仍需整体优化，后一处接所比较设计怎样减少从零学习的负担；不是同一连续段落。与 A08 共用原件和核验文本。

> The residual controller πθ(sm, so) can now be used to maximize the reward term g(so) in (4). Since the control sequence (5) enters (1) through the dynamics of sm and sm is in fact the control input to the dynamics of so, we cannot simply use the a-priori hand-engineered feedback controller to achieve zero error of sm and independently achieve the control objective on so. Through the coupling of states we need to perform an overall optimization of (5), whereby the hand-engineered feedback controller provides internal structures and eases the optimization related to the reward term f(sm).

> First, we compare residual RL and pure RL without a hand-engineered controller on the insertion task. Fig. 2 shows in simulation and real-world that residual RL achieves a better final performance and requires less samples than RL alone, both in simulation and on physical hardware. Unlike residual RL, the pure RL approach needs to learn the structure of the position control problem from scratch, which explains the difference in sample efficiency.

**组织与句法。** 方法段先以 `The residual controller … can now be used to …`接前文职责；第二句 `Since …, we cannot … independently …`立即说明机器人状态 sm 与物体状态 so 的耦合为什么使独立完成两目标的直观理解失效。第三句 `Through the coupling of states … overall optimization …, whereby …`把该约束接到具体优化对象，同时保留基准结构仍能简化学习的作用。不能只摘第一句说学习仅优化物体奖励，也不能把 `overall`删成两个分别最优的控制器。比较段的 `we compare … on the insertion task`先确定对象与任务，`Fig. 2 shows … better … less … than …`报告两个实际指标，`Unlike … from scratch, which explains …`再将样本区别接到已有位置控制结构的作用；解释承接所测结果，不是另报未经比较的总体优越性。

**可迁移实现与范围。** 作者确有耦合设计时，可借 `Since …`、`Through …, whereby …`或拆开的成熟用途句法，明确什么相互作用决定了哪项设计、该设计保留了什么优势。比较有支持的作用解释时，可沿用这组三句的比较对象—结果—作用关系；把变量、图号、任务、指标及原因全部换成作者事实。原文 `less samples`的可数名词搭配在新文用 `fewer samples`；`in simulation and real-world`及重复的两类平台表述也按准确、自然的当前句意整理，原引文保留。只有实测结果才用 `shows`，结构作用不能由普通相关性推成唯一因果；不迁入本文的指数稳定条件、千步数量或未经保证的安全性。读者已经知道比较设置时可省开头，条件较多时可拆句，不要求复刻原句长。

## 选择范例时的边界

本组22张任务卡保留多类正文实现，摘要以作者认可的五篇为主要参考并按需补充局部写法；不对整篇论文作统一优劣评分，也不把某卡片视为最佳答案。部分原文有宽泛自评、长信息串或术语问题，卡片已明确取舍。理论和实验内容仅为写作关系定位，未复算公式、统计或推广性能；“可回查、能指导表达”仍不等于实际 Drafting／Polishing 已提高能力。没有适配作者当前任务的卡片时，保留成熟通用规则，说明证据不足，不硬套相似词句。

[P01]: <../../../文献资料/A_DMPs-Based_Framework_for_Robot_Learning_and_Generalization_of_Humanlike_Variable_Impedance_Skills.pdf>
[P05]: <../../../文献资料/Composite-Learning-Based_Adaptive_Neural_Control_for_Dual-Arm_Robots_With_Relative_Motion.pdf>
[P04]: <../../../effect-test/E01-abstract-first-drafting-2026-10-02/materials/文献资料/Complementary_Stability_and_Loop_Shaping_for_Improved_HumanRobot_Interaction.pdf>
[P06]: <../../../effect-test/E01-abstract-first-drafting-2026-10-02/materials/文献资料/Diffusion-Based Impedance Learning for Contact-Rich Manipulation Tasks.pdf>
[P08]: <../../../文献资料/Fixed-Time_Neural_Control_of_Robot_Manipulator_With_Global_Stability_and_Guaranteed_Transient_Performance.pdf>
[P09]: <../../../文献资料/Human-Like_Adaptation_of_Force_and_Impedance_in_Stable_and_Unstable_Interactions.pdf>
[P11]: <../../../文献资料/Impedance_Learning_for_Human-Guided_Robots_in_Contact_With_Unknown_Environments.pdf>
[P12]: <../../../文献资料/Learning_a_Flexible_Neural_Energy_Function_With_a_Unique_Minimum_for_Globally_Stable_and_Accurate_Demonstration_Learning.pdf>
[P16]: <../../../文献资料/Physical_HumanRobot_Interaction_of_a_Robotic_Exoskeleton_By_Admittance_Control.pdf>
[P17]: <../../../文献资料/Robot_Learning_System_Based_on_Adaptive_Neural_Control_and_Dynamic_Movement_Primitives.pdf>
[P18]: <../../../文献资料/Stability_Criterion_and_Stability_Enhancement_for_a_Thruster-Assisted_Underwater_Hexapod_Robot.pdf>
[P19]: <../../../effect-test/E01-abstract-first-drafting-2026-10-02/materials/文献资料/Variable_Impedance_Control_of_Redundant_Manipulators_for_Intuitive_HumanRobot_Physical_Interaction.pdf>
[Fuzzy2023]: <../../../文献资料/Fixed-Time_Fuzzy_Control_of_Uncertain_Robots_With_Guaranteed_Transient_Performance.pdf>
[ESO2017]: <../../../文献资料/Extended_State_Observer-Based_Integral_Sliding_Mode_Control_for_an_Underwater_Robot_With_Unknown_Disturbances_and_Uncertain_Nonlinearities.pdf>
[RRL2019]: <../../../文献资料/Residual_Reinforcement_Learning_for_Robot_Control.pdf>

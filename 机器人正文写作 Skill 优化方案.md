# 机器人论文正文写作 Skill 优化方案（待验收，不实施）

**范围与状态（2026-09-29）。** 本文只提出对现有 Nature 写作／润色 Skill 的正文能力改进，**未修改或安装 Skill**。证据来自用户提供的 19 篇论文及已补证的[《机器人论文正文写作证据分析》](机器人论文正文写作证据分析.md)。论文编号、PDF 页码和章节均在那里可回查；“PDF p.”是文件页，不是印刷页。这组材料以控制、阻抗、人机交互为主，8 篇来自 *IEEE Transactions on Robotics*，另有会议与预印本；“多篇出现”是候选写法的证据，不能直接证明其英文优于其他写法，也不能覆盖机器人所有子领域。

## 1. 实际基座与加载关系

本轮读取的是当前磁盘文件，不以先前摘要替代。`C:\Users\user\.agents\skills\nature-writing\manifest.yaml` 为 **1.5.0**，`nature-polishing\manifest.yaml` 为 **6.6.0**，`nature-shared\manifest.yaml` 为 **1.6.0**。`C:\Users\user\.codex\skills\academic-research-suite\SKILL.md` 的 Codex 适配器为 **0.1.28**，其 `manifest.json` 标明上游快照 `94436237913091d4739870159d241660527e8338`。ARS 的正文相关入口是 `ars/academic-paper/WORKFLOW.md`，再分发到 `structure_architect_agent.md`、`argument_builder_agent.md`、`draft_writer_agent.md` 等；它没有被 Nature 两个 Skill 调用，本案只作规则对照，不引入其多阶段科研流程。

| 路径（均相对对应 Skill 根目录） | 实际加载 | 本案关系 |
|---|---|---|
| `nature-writing/SKILL.md` → `manifest.yaml` → `always_load` | 每次写作加载共享 `reader-workflow`、`paper-type-taxonomy`、`ethics`、`terminology-ledger`，以及本地 `core/stance`、`core/workflow`、`core/output-format` | 论证、证据边界、术语及段落规则的上游 |
| `nature-polishing/SKILL.md` → `manifest.yaml` → `always_load` | 同一共享四文件及本地 `core/stance`、`core/failure-modes`、`core/output-format` | 先诊断结构后润色的上游 |
| 两者按 `paper_type`、`section`、`language`、`journal` 轴加载 | 写作另有 `task` 轴；正文用 `task=manuscript`；`section` 写作叫 `experiments`，润色叫 `results` | 改动要落到会被调用的 fragment 或路由，不能只添参考文档 |
| 两个 `SKILL.md` 的正文条件分支 | Results／主文压缩时加载 `nature-shared/core/main-text-discipline.md`；任何 Discussion 加载 `discussion-argument-language.md`；Nature Portfolio Introduction／Results／Abstract 分别加载三个 `nature-*` 共享文件；完整润色另加载 `consistency-sweep.md` | 通用与 Nature 专属规则已经分层，不需要重造主文分配与证据保障 |
| `references/` | 根据 manifest `on_demand` 或对应 fragment 指令选择 | `nature-writing/references/paragraph-flow.md`、`introduction.md` 等及 `nature-polishing/references/section-moves.md`、`phrasebank-playbook.md`、`style-guardrails.md` 并非每次默认加载 |

**冲突的实际位置。** `nature-writing/static/fragments/section/experiments.md` 在通用 section fragment 内直接要求读取 Nature 专属的 `nature-results-discussion.md` 三种 archetype，可能使 `journal=generic` 的机器人控制稿沿用 Nature 发现型故事；两个 router 本身则只在 Nature Portfolio 目标时条件加载该共享文件。`nature-polishing/static/fragments/language/en.md` 的“`<= 30` words”是硬上限；写作 `language/en.md` 为 10–30 词目标。`nature-writing/static/core/workflow.md` 与写作英语 fragment 把“每段恰好一个 job”“首句必为主题／主张”写为硬性操作。`nature-shared/core/nature-introduction.md` 的连续结尾段和快速漏斗明确是 Nature Portfolio 默认，不是所有机器人期刊规则。

## 2. 取舍总则和六层覆盖

**优先序建议：** 作者材料与可核查科学事实、目标期刊明确要求、现有共享完整性保障、机器人语境细化、Nature 语料启发式、通用措辞偏好。机器人细化只修饰正文的写法选择，不能覆盖证据真实性、术语、统计、报告或伦理要求。所谓“删去”优先指**删除或取消某条硬性指令的适用性**，不是删除整个既有 Skill 的其他功能。19 篇未出现某项规则，不构成删除理由。

| 层级 | 已有支持 | 实际空缺或冲突 | 拟处理项 |
|---|---|---|---|
| 全文 | 论证链、证据分配、Results 与 Discussion 分工、前后对齐 | 控制保证、系统部件与验证的对应关系尚未显式识别 | R1、R2 |
| Section / Subsection | paper-type、section fragment、Nature 结果推进 | generic 机器人稿可能被 Nature archetype 强套；润色缺独立 Related Work 路由 | R2、R3、R4 |
| Paragraph | 一段一主旨、证据配置、主文必要性 | “恰好一个 job”“首句必主张”过硬，公式前后段和文献比较段未细化 | R5、R6 |
| 连续句 | 相邻句须有关系、Discussion sentence-function audit | 跨句对象接力、旧条件→新限制→修正动作未成为可操作检查 | R7 |
| Sentence | 主谓宾、单命题、证据强度 | 主语／语态／条件范围和公式句未按技术任务选择，固定词数可能破坏保证陈述 | R8、R9 |
| Phrase / Word | terminology ledger、证据动词和 phrasebank | 技术搭配的角色、同物同名／异物异名、限定词邻接未充分操作化 | R10、R11 |

下列 R 项为**拟实施的具体规则表述**，并非已生效文本。证据中的 P 编号链接及定位见证据报告第八节。每项均注明条件和例外，避免把观察变成模板。

## 3. 逐项文件建议

### R1｜保留：证据与修改范围保障

**文件／加载：** 两个 Skill 的 `static/core/stance.md`、写作 `static/core/workflow.md`、润色 `static/core/failure-modes.md`、共享 `core/ethics.md` 与 `core/terminology-ledger.md`（四项共享规则均 `always_load`）；`core/main-text-discipline.md` 是 Results／主文任务条件加载。**判断：保留原规则，不重写。** 不编造结果、引用、机制或新颖性；先定论证和证据边界；建立术语表；修改尽量局部；主文保留改变结论的限制。这些都直接服务本项目。P19 PDF p.11 §VII.D 把未显著时间趋势与准确性优势区分，P18 p.8 §IV–V 区分两种推力判据，P12 pp.1–2 §I 区分 ADS/N-ADS，均说明证据边界与命名控制的必要性。Drafting 用来限制可写主张；Polishing 用来阻止把限定、条件或术语润掉。现有共享层已足够，**不另造第二套真实性规则**。

### R2｜修改：让控制／系统论文的全文证据链由承诺驱动

**文件／加载：** `nature-writing/static/fragments/paper_type/algorithmic.md` 和 `methods.md`、`section/experiments.md`；`nature-polishing/static/fragments/paper_type/algorithmic.md`、`section/results.md`，均由 `paper_type`／`section` 轴加载。**问题：** 现有“能力梯级／实验 ladder”能组织比较，却没有要求把控制保证、假设、算法部件与验证对象逐一对应；若套用发现型 escalation，仿真、证明、实机可能被误排成普适递进。**拟文：** “对控制、机器人学习或多模块系统稿，先列任务与假设、声称的保证或能力、支撑它的设计／证明、实际测试及边界。按依赖关系或待判别的条件组织小节；理论、仿真和实机各承担其能支持的主张，不规定固定顺序，也不要求每个模块都有独立实验。” **依据：** P15 pp.2–8 §II–IV 目标—控制—稳定性—Baxter 对应；P08 pp.2–8 §II–V 约束与收敛—仿真／实验；P17 p.7 §V 把两组实验分别对应控制器与运动模型；P09 pp.4–8 仿真在证明前，构成顺序例外。**Drafting：** 先做“承诺／条件／证据”映射再排章节。**Polishing：** 用映射诊断错位或重复，保持已由证明支持的保证与仅由实验观察支持的性能差异。

**同项加载冲突修正：** `nature-writing/static/fragments/section/experiments.md` 的“Load `nature-results-discussion.md` for the three archetypes”改成“仅当目标为 Nature Portfolio 且发现／能力验证叙事确实适用时加载；其他目标先按 paper type 与证据问题选择结构”，与 router 的目标期刊条件一致。Nature 专属共享文件本身保留。P19 pp.7–11 §VII 按四个对比轴、P18 pp.11–17 按仿真和地形实机结果组织，说明不宜默认三 archetype。

### R3｜增强：Introduction 文献段的比较轴与段间交接

**文件／加载：** `nature-writing/static/fragments/section/intro.md`、`related-work.md` 与 `nature-polishing/static/fragments/section/intro.md`；对应 `section` 轴，深例 `nature-writing/references/introduction.md` 保持按需。**问题：** 基座已说“综合而非罗列”“精确缺口”，却没给机器人稿怎样从驱动、接触、状态假设或双交互目标建立段间关系。**修正后的拟文：** “先确定与本研究决定相关的比较轴，例如观测信号、控制对象、接触条件、稳定保证或泛化范围。完成同一比较任务的**段落组**应让读者看清已有方法实现了什么、依赖什么条件、留下什么与本文有关的缺口，以及该缺口为何引出本研究决定；单段只承担其实际需要的部分。段间承接可以通过继续同一对象、转向另一条件或合并两线问题实现，不要求每段末尾制造缺口或过渡句。贡献段点明本研究回应哪一缺口，设计动作与后续验证各自对应哪一条件。允许先给任务情景，也允许先给数学分类；不强制四段或单一漏斗速度。” **依据：** P11 pp.2–3 §I.A–C 的人机／机环境两线与双目标冲突；P12 pp.1–3 §I 的 N-ADS／ADS 表示、保证与代价；P18 pp.1–4 §I 的物理假设比较；P01 pp.1–2 §I 的位置→刚度→泛化链。**例外：** 目标期刊为 Nature Portfolio 时，仍加载 `nature-shared/core/nature-introduction.md`，其快速收束可优先作为目标期刊表达，但不能抹去理解判据所必需的技术条件。**Drafting：** 先确定段落组的比较轴与必要承接再成文。**Polishing：** 检查段落组能否共同完成已知、条件、缺口与设计意义的交代，只修复真实跳跃。

### R4｜增强：Related Work 的润色入口

**文件／加载：** 在 `nature-polishing/manifest.yaml` 的 `section.values` 增加 `related-work: static/fragments/section/related-work.md`，新增同名短 fragment；router `SKILL.md` 的 section 轴说明纳入该值。写作侧已有 `section/related-work.md`，不另建。**问题：** 润色侧的 `section` 轴目前无 Related Work，单独提交该节只能落到 generic 或误套 Introduction；`references/section-moves.md` 的 Literature Review 按需且不自动路由。**修正后的拟文：** “先辨明独立 Related Work 与 Introduction 内文献段的任务。完成同一比较任务的段落组按相关技术轴交代已有能力、适用条件、剩余缺口及其与本文设计或验证的关系；单段按实际功能只承担必要部分，不强制在每段末尾写限制或过渡。保留公平归属，不用‘所有既有方法皆失效’制造空缺。若期刊要求把相关工作并入 Introduction，则沿 intro 规则而非强制独立节。” **依据：** P19 p.2 §I 指向独立 §II Related Works；P11 pp.2–3 §I.A/B 将相同功能放在 Introduction 内。**Drafting：** 使用已有写作 fragment。**Polishing：** 新路由确保独立节能触发正确诊断；若无独立节，此 fragment 不加载。

### R5｜修改：段落按“主导推理任务”而非恰好一个标签

**文件／加载：** `nature-writing/static/core/workflow.md` 步骤 3、7（`always_load`），`static/fragments/language/en.md`（语言轴）；`nature-polishing/static/fragments/language/en.md`（语言轴）；深参考 `nature-writing/references/paragraph-flow.md` 按需。**问题：** “Each paragraph must do exactly one job”“The first sentence is the topic / claim”过硬。P01 方法段为了一个刚度估计任务同时交代目的、输入、输出；P19 结果段为了一个比较同时含条件、观察、限定。**拟文：** “每段应有一个可辨认的**主导问题或对象**；为完成它可以相邻呈现目的、操作、证据、解释、限制。首句可以是任务条件、对象定义、问题或主张，只要读者能迅速判断本段为何存在。若引入独立问题或读者必须跨段寻找支撑，再拆段。用段末的新条件、未解限制或输出，与下一段形成必要交接。” **依据：** P01 p.2 §II.A 的目的→估计→EMG→增益；P19 p.11 §VII.D 的准确性／时间分指标及未显著限定；P18 p.8 §IV 的上下界物理后果。**Drafting：** 段落卡片写“主导问题+必要功能”，不机械分句。**Polishing：** 只在主导问题改变或证据跑散时拆段；不为满足 TEEL 重写正确的方法说明。

### R6｜增强：方法、定理、结果段各有可核查的局部句链

**文件／加载：** `nature-writing/static/fragments/section/method.md`、`experiments.md`；`nature-polishing/static/fragments/section/methods.md`、`results.md`，由 `section` 轴加载。**拟文：** “方法／公式段：先给引入量的任务与已知条件，再给变换或控制律，再指明产物供哪一步使用；已清楚定义的例行等式无需重复动机。定理段：保证与初值、系统、控制律及约束同一语义单位出现；长句可拆，但条件不得与结论失联。结果段：给测试条件和参照，再给观察及指标，最后给该证据许可的局部推断；统计不确定性紧随它修饰的指标。” **问题：** 基座分别有“动机／机制／证据”和“观察／条件／量”，却缺少公式与保证句的邻接规则；硬句长可能使前提断裂。**依据：** P16 p.3 §III.A 力和误差双目标→代价函数→平衡解释；P08 p.5 §III Theorem 1 的条件—保证，p.8 §V.B 的误差区间和比较器约束；P19 p.11 §VII.D 的未显著时间趋势。**Drafting：** 对符号首次出现与定理做前后句检查。**Polishing：** 把裸公式、裸数值或错位限定修到读者可判别的局部关系；不捏造条件。

### R7｜增强：连续句追踪“技术对象如何被下一句消费”

**文件／加载：** `nature-writing/static/core/workflow.md` 步骤 7（`always_load`）与 `nature-polishing/static/core/failure-modes.md`（`always_load`）；详细操作可放下述共享机器人正文模块。**拟文：** “对每组相邻句标出前句产生的技术对象、前提或尚未解决的限制，问下一句是否沿用、变换、检验或限定它。若只靠 *however/therefore* 维持表面联系，补出具体变化或删连接词。跨节标题两侧的承接单独检查，不能假装为同段连续句。” **问题：** 现有“每句与上一句有关系”过泛，无法识别对象链错乱或伪因果。**依据：** P01 p.2 §II.A 的四种语法主语但同一刚度信息链；P11 p.5 §IV 的新任务条件→空间周期系数→控制律修正；P19 p.5 §V 的解析可行→实际边界→实验测定。P04 p.4 §III 至 p.7 §IV 与 P18 p.8 §IV–V 仅作跨节例。**Drafting：** 用输入／输出接力组织新句。**Polishing：** 找“上一句谈参数、下一句无故改谈方法优势”的跳跃；允许显式新对象引入。

### R8｜删除硬词数上限，修改单句实现规则

**文件／加载：** `nature-polishing/static/fragments/language/en.md`（删除“`Keep every sentence at <= 30 words`”和“不足 10 词原则上不用完整句”的硬性门槛）；`nature-writing/static/fragments/language/en.md`（把“10–30 words”改为提醒而非目标区间）。两者均语言轴加载。**问题：** 固定计数无法区分命名、数学条件、参照和补充信息，可能诱导把保证前提切到远处或为凑下限扩写。语料只支持在核查逻辑负载后拆句，没有统一阈值证据。**拟文：** “按命题负荷、条件位置和读者能否回指对象判断句长。优先让技术对象、动作、量和适用条件形成一个可核查命题；当独立主张各自需要证据时拆句，拆后保留前提与结论的显式连接。短定义句和长定理句均可合理存在；词数仅作发现异常的提示，不作合格门槛。” **依据：** P08 p.5 §III Theorem 1 同句含初值、控制律和约束；P11 p.3 §I.C 把不能合并两控制器的原因放在复合句；P18 p.8 §IV 用两句短条件分别说明过大／过小推力。**Drafting：** 不按目标词数填充或截断。**Polishing：** 将过载句按可独立验证的命题拆分，同时保留限定。**例外：** 投稿指南有明确句长或无障碍可读性要求时依其要求。

### R9｜增强：主语、语态与信息顺序的选择测试

**文件／加载：** 两个 Skill 的 `static/fragments/language/en.md`，并在 `zh-to-en.md` 交叉引用英文规则；语言轴加载。**拟文：** “先确定句子的焦点是作者的设计动作、被估计／变换的技术量、实验观察、已有研究归属，还是定理的条件。用能让焦点承担可核查谓语的主语；需要归属设计决定时可用 *we*，需要追踪技术量或保证时可用对象主语／被动句。条件和参照靠近受其限定的命题；语态转换不得改变施事者或把推断说成直接测量。” **问题：** 基座的 SVO／单命题／‘we only when suits’缺少机器人正文的操作判断。**依据：** P01 p.2 §II.A 四句语法主语转换；P11 p.3 §I.C 的 *we* 与 *objectives*；P19 p.5 §V 的稳定区域与已有作者归属；P08 p.5 定理条件。**Drafting：** 先定对象和动作再选主动或被动。**Polishing：** 检查主语换位是否改变技术对象、因果或责任。**边界：** 不强制同一段主语相同，不强制主动／被动比例。

### R10｜增强：术语表加入“角色与相邻搭配”，不造词库

**文件／加载：** `nature-shared/core/terminology-ledger.md` 已在两个 manifest `always_load`；建议**只加机器人正文适用的小段或可选字段**，保留原通用术语表。与下述领域模块的 phrase／word 检查合用。**拟文：** “对机器人稿中决定保证或实验解释的词，必要时记下：它指代的物理／数学对象、是测量／估计／输入／输出／参数／判据中的哪一种、允许的动词搭配、不可互换的邻近术语。润色时逐项核对谓词是否改变数据来源、保证类型或控制作用。” **问题：** 当前 ledger 锁定名称，但未显式记录 *estimate*、*measure*、*map*、*guarantee* 对对象的不同操作。**依据：** P01 p.2 §II.A 的 EMG 监测→刚度估计→剖面映射为增益；P12 pp.1–2 §I 的 N-ADS／ADS；P18 pp.8–11 的 vertical／6-D thrust；P02 与 P08 的 finite-time／fixed-time 并非风格同义词。**Drafting：** 输入术语旁记其角色和可写动作。**Polishing：** 不为避免重复把数学对象或保证类型改名。**例外：** 首次全称／缩写、语法变形、文献原称允许，但关系须明晰；不把本语料动词列为禁／必用词表。

### R11｜修改：通用措辞偏好降为证据核查，不自动替换

**文件／加载：** `nature-polishing/static/fragments/section/results.md` 与 `discussion.md` 的示例谓词；`nature-writing/static/fragments/section/experiments.md` 和 `discussion.md` 的示例谓词；`nature-polishing/references/phrasebank-playbook.md`、`section-moves.md`、`style-guardrails.md` 是按需参考。**问题：** “was detected／achieved”与“may reflect／suggests”只是功能示例，若机械替换会错改保证、观察和解释；phrasebank 的“Recent years…”、`to our knowledge` 等也不能被当作默认更优。**拟文：** “示例词仅在命题类型吻合时选用。先判别句子是在给定义、模型假设、数学保证、观察、统计比较、可能解释还是未检验用途，再选动词和限定语。对 *improve, outperform, significant, guaranteed* 必须指明指标、参照、条件及证据类型；不能以语气词代替缺失的证据。” **按需文件的相应修补：** 将 `section-moves.md` 的开场短语标为非默认例句；将 `style-guardrails.md` 中把 `first` 改为 `to our knowledge` 的“safer replacements”表述改为“先核实检索范围和相邻工作，否则删去首次主张”；将 `phrasebank-playbook.md` 的“每段通常最多一个指示词开头”改为“检查代词所指对象是否明确，重复只在造成空泛衔接时删减”。**依据：** P19 p.11 §VII.D 时间趋势未显著而准确性比较显著；P04 p.9 §IV 未展示用途有明示限定；P08 p.8 §V.B 区分跟踪表现与输出约束。**Drafting：** 从命题类型选谓词。**Polishing：** 对通用升级词做证据回查，保留作者已设边界。**例外：** 某些期刊语言偏好可覆盖风格词，但不能覆盖真值。

### R12｜保留 Nature 专属规则，但只在目标与证据相容时应用

**文件／加载：** 两个 router 对 `nature-shared/core/nature-introduction.md`、`nature-results-discussion.md`、`nature-abstract.md` 的 Nature Portfolio 条件加载；两个 Skill 的 `static/fragments/journal/*`；`nature-writing/static/fragments/section/intro.md` 的 Nature summary paragraph 与典型四段描述。**判断：** Nature 专属文件保留；将四段、连续结尾段、快速漏斗和发现型结果 archetype 明确为“可选起点／目标期刊偏好”，不因 19 篇非 Nature 稿没采用而删除。**拟文：** “在 Nature Portfolio 目标上先核对期刊／文章类型，再使用共享 Nature 叙事建议；当机体约束、证明条件或必要技术分类需要较长铺垫时，以可理解的技术前提为优先，不为压缩而删去可检验条件。机器人非 Nature 目标默认不用 Nature 独有段数、标题和发现链。” **依据：** P18 pp.1–4 §I 的多类判据与物理假设；P12 pp.1–3 §I 的表示分类；P19 pp.7–11 §VII 的四对比轴；P01 p.2 §I 与 P18 p.4 §I.B 的贡献清单。**Drafting：** 按目标和论文类型选路线。**Polishing：** 不将已清楚的技术 Introduction 机械改成四段通用漏斗；仍可删无关历史。**例外：** 目标期刊当前稿约或编辑要求有优先权。

### R13｜不采纳 ARS 的强制模板，有限借鉴证据映射

**文件／加载：** ARS `ars/academic-paper/WORKFLOW.md` → `agents/structure_architect_agent.md`、`argument_builder_agent.md`、`draft_writer_agent.md`，只在 ARS 路由调用，Nature 基座**不加载**。**判断：** `structure_architect` 的 section→evidence assignment 和 `argument_builder` 的 claim–evidence–reasoning 对 R2 的“承诺／条件／证据”映射有补充提示，但 Nature 写作 `core/workflow.md`、共享 `main-text-discipline.md` 已覆盖主要机制；不复制 ARS 的 agent 角色或九阶段流程。`draft_writer_agent.md` 的 TEEL、英文 120–200 词／段、每节至少三段、≥80% 段落 TEEL 属其工作流局部门槛，与 P01 方法段、P11 文献分组和 P19 结果段的功能差异不相容，**不移植**。这不是删改 ARS 本身。Drafting／Polishing 都只保留一张轻量的承诺与证据映射，不增加新科研审批或代理流程。

## 4. 建议的组织与加载实现

1. **下一轮实施时**，拟新增 `nature-shared/core/robotics-main-text.md`，只容纳 R2、R3、R5–R11 中跨 Drafting／Polishing 共用的领域判断：承诺—条件—证据链、Introduction 比较轴、局部句链、主语／谓词／限定／命名测试。每条附 P 编号、PDF 章节与页码、短原文锚及可打开的项目论文路径，确保离开本报告仍可回查；另写适用条件及反例。不复制现有伦理、统计或全文流程，也不收入未经证实的固定句型。共享文件是领域细化，非独立 Skill。
2. **实际调用**：在两个 `SKILL.md` 的步骤 4 增加同一条件分支，并在各自 `manifest.yaml` 的 `references.on_demand` 登记路径 `../nature-shared/core/robotics-main-text.md`：当用户材料或目标稿**确属机器人控制、学习、操作或物理交互的正文 Drafting／Polishing**时，在本地 `paper_type`、`section` fragment 与必要共享通用规则之后、英语句子润色之前加载；仅投稿材料、图、排版、非机器人稿不加载。全文或混合章节只加载一次。两个入口都需测试“实际读到文件”，不能只增加 manifest 行。
3. `nature-shared/manifest.yaml` 的 `core.on_demand` 同步登记该共享模块；`nature-shared/SKILL.md` 说明它是由两个正文 Skill 请求的可选文件。按现有 shared 机制调用，而非把新文件塞进所有任务的 `always_load`。本地 section、language fragment 仍负责各自的 Drafting／Polishing 动作，不在共享文件中重复两套流程。
4. **规则冲突优先序写进两个 router 分支：** 期刊硬性要求和作者可核查材料优先；共享伦理、术语及证据边界优先；机器人模块只细化默认结构和语言，不准改事实；Nature 风格为适用目标的偏好，不强制覆盖控制条件。对 `nature-writing/section/experiments.md` 的无条件 Nature 文件引用按 R2 修正。若两个规则在句长、首句功能或段数上冲突，按 R5、R8 的功能检验执行，且记录所用例外。
5. **不触碰其他功能。** 保留 submission-package、LaTeX 排版、期刊格式、抽象／标题等文件及其路由；本方案只限定正文任务加载，不以机器人语料未涉及为由删除它们。拟新增润色 Related Work fragment 只在确有独立 Related Work 节时加载。

## 5. 实施顺序与输出验收

**实施顺序（本轮执行候选版）：** ① 冻结证据 ID 与定位并保存原版；② 修 R2、R5、R8 的现有硬规则及冲突；③ 写共享机器人正文模块并接入两个 router／manifest；④ 添润色 Related Work 入口及本地 R3、R6、R9–R11 操作；⑤ 核对两个入口、相对路径、条件加载、非机器人路由和原有保障。Drafting／Polishing 的实际输出比较属于**下一轮效果验收**，本轮只准备测试要求，不以加载成功代替写作效果。

**验收材料必须是作者任务输入和实际输出，不用‘规则可加载’代替效果。** 可从 19 篇构造**脱离原句的事实卡**，分别注明任务、系统、假设、已知结果、缺失数据，避免把论文原段抄作答案。相同输入跑旧版和候选版，人工盲评并逐点记录：

| 场景与输入 | Drafting／Polishing 输出须通过的检查 | 对应层级 |
|---|---|---|
| F1：提供完整研究事实包（系统、任务、假设、技术路线、理论保证、仿真与实机结果、比较对象、边界）；起草或重构整篇正文 | 检验章节安排是否由主张与证据关系驱动；每项核心主张能回指对应证明或实验；跨节限制与新方案连续推进；结论回收开头承诺并区分已证与未证范围。该项检查全文组织，不用 D1–P3 的局部表现替代 | 全文、Section、跨节推进、结论 |
| D1：类似 P11 的人引导与环境接触双目标，给已有两线工作、冲突与设计决定；写 Introduction 和 Related Work 片段 | 相关工作按可比技术轴归组；段落组共同说明已有能力、条件、缺口与设计意义，单段只承担必要部分；贡献解释为何不能简单相加；不虚构“首次”或无证优势 | Section、Paragraph、连续句 |
| D2：类似 P18 的腿＋推进器判据，给模型假设、垂直与六维推力判据和验证范围；写方法／结果衔接 | 保证与条件对应；两判据不混同；修正判据由前一判据的具体局限引出；仿真与实物仅支持各自结论 | Section、连续句、Sentence、Phrase |
| P1：类似 P19 的两指标结果，准确性有证据，时间仅趋势且未显著；润色结果段 | 保留条件、比较对象及“not statistically significant”；解释仍是假设；不得把时间趋势升级成已证优势 | Paragraph、Sentence、Phrase |
| P2：类似 P01 的 EMG→刚度估计→阻抗增益方法段，故意混用 measure/estimate/apply；润色 | 纠正测量／估计／施加的谓词；语法主语可变但对象链不断；不增造传感量或控制作用 | 连续句、Sentence、Phrase |
| P3：类似 P08 的初值约束与固定时间保证，提供长定理句和短定义句；润色 | 句法更易核查而前提没有离开保证；不为 30 词上限机械拆句，也不把 fixed-time 改 finite-time | Sentence、Phrase |

**判定办法（下一轮执行）：** 每个输出先逐项核对事实卡与论文原文，标记编造、技术对象混淆、保证越界、限定丢失为**阻断缺陷**；再用六层清单评估全文论证顺序、章节与证据对应、跨节推进、结论回收、段间交接、相邻句对象接力、单句条件位置和英文技术搭配。比较旧版与候选版时，要求 F1 与 D1–P3 六个场景的阻断缺陷为零，且没有新增的无根据主张；逻辑与英文实现的改善要由可指出的句／段具体位置说明，不能用“更流畅”作结论。若候选版只把句子缩短、增加连接词或把段落改成统一模板而未改善对应推理，判不通过。非机器人正文与投稿材料抽检只确认路由没有误触发，不作为机器人写作质量成绩。

**仍无充分证据：** 统一最优句长／段长、主动／被动最佳比例、Nature 发现型结构对所有机器人论文的优越性、固定高频搭配词表。方案故意不为这些设门槛。科学结论和期刊正式规范仍需作者及目标期刊另行核查。

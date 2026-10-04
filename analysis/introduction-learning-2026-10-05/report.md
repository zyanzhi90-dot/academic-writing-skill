# 四篇机器人论文的 Introduction 学习依据与最小改造建议

本轮结论是：应把四篇引言的实际段落组和连续英文补到按需范例层，并修正 Writing 详细引言指南中否定真实技术继承关系的绝对表述。成熟的科学保障、段落组比较、六层学习和按需加载已经存在，可以直接复用；没有依据重建 Writing／Polishing 工作流。四篇论文支持不同的引言组织，不能把其中一种变成固定模板。本轮仅形成分析材料，没有修改 Skill、运行写作测试、安装 Skill 或判定能力通过。

分析依据为工作开始时 `main`／`origin/main` 的 `7d56f349c9a22bf6f98575bf81a1c90a4384ff9a`、作者最新《核心要求.txt》和《我自己的经验和做法.txt》。开始时《核心要求.txt》已有作者未提交的内容更新，本轮没有改写它。最新要求强调既学习真实逻辑，也直接利用适用的成熟英文，并把科学内容及逻辑换成作者自己的；本报告按这一要求分析具体文本。

## 阅读范围、版本和可回查英文

| 本轮来源代号 | 原论文与已有材料对应 | 完整 Introduction 范围 | 原文副本 |
|---|---|---|---|
| P17 | *Robot Learning System Based on Adaptive Neural Control and Dynamic Movement Primitives*；A06／B01；TNNLS 30(3), 2019；DOI `10.1109/TNNLS.2018.2852711` | §I，PDF p.1–2／印刷页777–778 | [P17 完整英文](P17-introduction.md) |
| P05 | *Composite-Learning-Based Adaptive Neural Control for Dual-Arm Robots With Relative Motion*；A07；TNNLS 33(3), 2022；DOI `10.1109/TNNLS.2020.3037795` | §I，PDF p.1–2／印刷页1010–1011 | [P05 完整英文](P05-introduction.md) |
| Fuzzy2023 | *Fixed-Time Fuzzy Control of Uncertain Robots With Guaranteed Transient Performance*；A02；TFS 31(3), 2023；DOI `10.1109/TFUZZ.2022.3194373` | §I，PDF p.1–2／印刷页1041–1042 | [Fuzzy2023 完整英文](Fuzzy2023-introduction.md) |
| ESO2017 | *Extended State Observer-Based Integral Sliding Mode Control for an Underwater Robot With Unknown Disturbances and Uncertain Nonlinearities*；A04；TIE 64(8), 2017；DOI `10.1109/TIE.2017.2694410` | §I，PDF p.1–3／印刷页6785–6787 | [ESO2017 完整英文](ESO2017-introduction.md) |

上表四个副本均包含整节引言，保留论文引用编号、原有科学陈述及语言问题。I01 等是本轮 prose 段落定位号，C01 等是原有贡献条目定位号。跨页／跨栏段落接回原段；图注、脚注、摘要和 §II 不混入。P05 的贡献列表和 roadmap 虽同属一个提取块，按版面分开；ESO 的贡献列表延续到第三页。引言共 P17 九段、P05 九段及三条贡献、Fuzzy2023 四段及三条贡献、ESO2017 九段及三条贡献。所有页面均核对两栏版面，含 ESO 的第三页。

复用 [P17 已有全文提取](../reading/P17.txt)、[P05 已有全文提取](../reading/P05.txt)、[P17 digest](../digests/P17.md)、[P05 digest](../digests/P05.md)、[已有正文证据分析](../../机器人论文正文写作证据分析.md)及候选 Shared 范例。已有两份全文提取与本地 PDF 的重新只读提取在换行规范化后相同，没有覆盖旧文件。Fuzzy2023／ESO2017 使用本轮提取。各 PDF、作者输入及旧提取的哈希见 [source-provenance.json](source-provenance.json)；排版断词操作见 [normalization-log.json](normalization-log.json)。副本仅处理连字、空白、行末断词及首字下沉，不润色或纠正原文。

`root1.pdf` 在仓库、`D:\桌面`、用户 Downloads、Desktop、Documents 位置未检出，最终搜索包含隐藏文件并忽略文件名大小写，当前不能作为作者稿对照。没有用 E04 稿、其他 PDF 或历史版本代替。因此下述迁移是有条件的写作依据，尚不能判定作者引言具体哪段应保留、删改或移动，也不提供冒充作者科学内容的新稿。

## P17／A06：把学习表征和实际执行接成同一任务

### 整节组织与段落展开

| 段落及位置 | 原段内部推进 | 对下一段的作用 |
|---|---|---|
| I01，p.1 左→右，首词 `RECENTLY` | 产品更新需要适应性机器人 → 增强学习 → LfD 由人示教 → motion modeling 是关键 | 开篇从应用变化落到一个明确动作，不在机器人重要性上停留 |
| I02，p.1 右，`The dynamic system` | DS 可生成稳定、可扩展、抗扰的轨迹 → 一个 DS／ELM 工作需要较多数据 → DMP 单示教和弹簧阻尼结构的能力 | 给 DMP 选择提供能力及数据条件依据 |
| I03，p.1 右，`DMPs` | 击打、DMP 序列、风格调节三个用途 → 最优示教难获取 → 作者选择把多次示教整合进一个 DMP | 不是列完文献才突然报方法；此处已有作者设计决定 |
| I04，p.1 右→p.2 左，`Probabilistic approaches` | 概率方法保留示教变异和特征 → GMM／GMR 的学习与生成分工 → SEDS、DS-GMR 已把统计学习与 DS 相接 | 先承认现有组合能力，为作者自己的组合解释理由 |
| I05，p.2 左，`To take advantage` | DMP 非线性函数由 GMM 建模、GMR 获取估计 → 多示教特征综合 → 比较原 DMP 回归方式的示教范围、复杂度及另一方法的效率 | 作者设计后仍有具体比较；并非所有相关工作必须排在方法之前 |
| I06，p.2 左→右，`The imitation performance` | 学习效果还取决于 tracking controller → 准确模型的作用 → 未知载荷阻碍预先精确建模 → 函数近似和 NN → RBFNN 选择理由 | 把表征成功与机器人执行成功区分，并引出第二项设计责任 |
| I07，p.2 右，`In this paper` | joint-space NN 控制、近似对象、Lyapunov 保证 → 两组件 → 第一组件输出 joint-space trajectories → 第二组件跟踪同一输出并补偿不确定动力学 | 不止两个模块名称，给出科学对象的交接 |
| I08，p.2 右，`Here` | 系统同时考虑生成与跟踪 → 与具体前作比较 → 额外控制器处理执行环境影响 → 学得运动在实际机器人上执行 | 收束的是完整任务能力；没有把两个模块写成不相关的贡献 |
| I09，p.2 右，`The remainder` | DMP 模型、学习、控制与稳定性、实验、结论 | 章序与上述问题分工一致；roadmap 自身不是贡献证据 |

该节有两条相接的论证线：示教如何变成可用运动；该运动如何在不确定动力学下实现。I03、I05、I07 已逐步说作者做什么，I08 才综合比较。它不符合“先讲完所有背景、最后才允许出现方法”的硬性顺序；也不需要每一段以一个新的 gap 收尾。I04 在建立可继承的能力，I06 才转换问题轴。

### 连续英文与实际句间关系

I05 全段，p.2 左栏，接 I04 的 DS／概率方法能力，后接 I06 的执行问题：

> To take advantage of the performance of the DS and the probabilistic approach, we integrate DMP and GMM into our proposed system, where the nonlinear function of DMP is modeled with GMM and its estimate is retrieved through GMR. This modification enables the robot to extract more features of the motions from multiple demonstrations and to generate motions that synthesize these features. The original DMP was learned using the locally weighted regression (LWR) [16], and the locally weighted projection regression [17] was employed to optimize the bandwidth of each kernel of LWR. Despite the added complexity of the learning procedure, these methods enable the DMP to learn from only one demonstration. Reservoir computing [18] is another method used to approximate the nonlinear function, but its computing efficiency is less than that of GMR.

第一句把设计落到 `the nonlinear function of DMP`，不是泛称融合两种方法。`is modeled with GMM` 与 `its estimate is retrieved through GMR` 分别承担建模和估计动作；第二句的 `This modification enables ...` 接回这一修改，再交代 `extract ... features` 与 `generate motions that synthesize these features`。后两类比较仍围绕同一非线性函数的学习。可直接利用这组主谓和作用表达，但作者必须有相同的“选用技术—作用对象—输出用途”关系；不能只替换 DMP、GMM 名称却保留不存在的估计／综合机制。

`multiple DMPs`、`multiple demonstrations`、`one DMP model` 在 I03 是三个不同对象，不能通过省词合并。`only one demonstration` 在 I05 说的是这里比较的学习方式；不能写成所有 DMP 技术都只能用一次示教。I05 的效率比较也不能转写成当前方法普遍效率更高。

I07 全段，p.2 右栏，承接 I06 的模型不确定性与控制器选择：

> In this paper, an NN-based controller is designed to guarantee the tracking performance of the manipulator in joint space, where RBFNN is employed to approximate the nonlinear functions of the robot dynamics. The stability of the controller is guaranteed by the Lyapunov stability theory. As shown in Fig. 1, the robot learning system consists of the motion generation component and the trajectory tracking component. The former utilizes the motion model based on DMP to learn and generalize motion skills; these, in turn, are represented as a set of trajectories in joint space. The latter employs the adaptive controller to track the trajectories generated from the former, and RBFNN is incorporated to compensate for the uncertain dynamics.

五句按“控制器责任及近似对象—保证—系统分工—生成输出—跟踪该输出”推进。`trajectories in joint space` 是跨句保持不变的中间对象；`track the trajectories generated ...` 比“两个模块协同提高性能”更能解释系统如何成立。末句 `compensate for the uncertain dynamics` 给补偿动作一个具体对象。作者若有学习／规划与执行链，可以保留这种整段组织和 `consists of`、`is employed to approximate`、`track the trajectories generated`、`compensate for` 的成熟实现，再替换作者自己的输入、输出及不确定项。

这里不继承原段全部表面形式。`The former`／`The latter` 可改成作者明确的组件名；分号改成普通句子。`is guaranteed by the Lyapunov stability theory` 应以作者实际分析对象和结论实现，不是写了 Lyapunov 就可宣称稳定。I08 的 `Here, we present a novel and complete ...` 不符合已有 Here 禁用及证据强度约束；删去 signposting，保留系统责任即可。

### 句式和用词如何选取

| 适用原英文 | 为什么可借用 | 作者内容替换时的边界 |
|---|---|---|
| `The imitation performance of robots also depends on the accuracy of the trajectory tracking controller ...`（I06） | 主语延续完整任务，`also depends on` 引入尚未解释的实现条件 | 作者确有这一依赖时才使用；`also` 需要前文已建立另一条件 |
| `an accurate dynamic model ... cannot be obtained in advance due to ...`（I06） | 先命名所需模型，再说可获得性与物理原因 | 不能把某一部分未知写成整个模型均不可用；`in advance` 不等于永远不能辨识 |
| `we integrate ... into our proposed system, where ...`（I05） | 主动句说设计动作，where 从句落到实现对象 | 作者实际是选择、估计、补偿或组合哪个动作，就用哪个动作；不任意互换 |
| `This modification enables ... to ... and to ...`（I05） | 前句修改接后句作用，两个不定式共享动作主体 | 两个作用必须都由同一修改产生；复杂句负担过大时拆句，保留因果 |
| `consists of ...`；`track the trajectories generated ...`（I07） | 普通明确的组成表达与输出交接 | 不固化两个组件、不固化 joint space，也不预设作者有 NN |

以 A06 为本轮默认表达锚点，应优先学习这些普通主谓、明确对象、理由接作用的具体英文，而非固定它的篇幅、九段结构或每一个修饰词。I06 关于 RBFNN 避免局部最优、收敛较快等强断言只属于该文解释，不能作为任意作者方法的共性。I08 关于前作“只考虑 motion modeling”的比较也必须保持所列前作范围。

## P05／A07：先改变任务条件，再缩小学习条件

### 整节组织与段落展开

| 段落及位置 | 原段内部推进 | 与前后段的接续 |
|---|---|---|
| I01，p.1 左→右，`RECENTLY` | 双臂相对单臂的任务优势 → 应用 → 运动控制／规划更复杂 → 需要控制技术 | 给协调控制问题一个任务来源 |
| I02，p.1 右，`An adaptive` | 三项已有搬运控制及各自作用 → 共同的 firmly held、no relative motion 条件 → 抛光等任务需要沿表面滑动 | 比较的是接触／相对运动条件，不是新旧方法优劣口号 |
| I03，p.1 右，`In this respect` | 相对运动任务命名 → 相对 Jacobian 控制、脑机控制的实际能力 → 动力学已知及接触力稳定性分析缺口 | 承认目标任务已有工作，再把未解决条件说具体 |
| I04，p.1 右→p.2 左，`The dynamic model` | 动力学模型作用 → 抓取物动力学不可预先获得 → 精确模型依赖的困难 → 近似与 NN | 将任务条件与设计所需信息相接 |
| I05，p.2 左，`A fuzzy` | 多项 NN 应用 → tracking-error convergence 与 weight convergence 区别 → 权重学习问题的重要性 | 从“用 NN 处理未知模型”继续到“什么学习结论才需要解释” |
| I06，p.2 左，`In our recent` | 先前 LIP 估计 → NN 权重更难 → PE 的严格性及原因 → PPE 已有局部能力 → recurrence／弱激励限制 | 缩小到适用区域、输入条件和学习速度，没有抹掉 PPE 前作 |
| I07，p.2 左→右，`The work` | 把估计误差信息纳入 adaptation 的已有思路 → 作者复合学习控制 → 当前双臂相对运动及未知动力学范围 → 分别与 [46]、[45] 比较 | 不同前作分别支持不同改进，不能合成“全部前作没有这些能力” |
| I08＋C01–03，p.2 右，`The objective` | 当前任务目标 → 框架适用条件、误差信息进入更新律、激励条件放松三项贡献 | 三项分别接任务条件、学习机制、保证条件 |
| I09，p.2 右，`In the following` | 建模 → 控制及稳定性 → simulation → 结论 | 所述验证为仿真，不可补写机器人实机实验 |

I02–I03 与 I05–I07 是两个连续收窄的段落组。第一个说“目标任务为何不同”；第二个说“未知动力学下的学习为何仍有条件”。只学 `However` 和贡献列表，会漏掉整节的实质。

### 从已有能力到目标任务的整段英文

I02 全段，p.1 右栏，上接双臂复杂性，下接相对运动研究：

> An adaptive decentralized control scheme was proposed to address the object handling problem of a cooperative robot, where an implicit force control scheme was employed to simultaneously regulate the force and position [9]. In [10], a decentralized control structure for multiple mobile manipulators was developed, where the internal forces were constrained by employing an augmented object model for the multiple systems with a virtual linkage. In [11], the loading problem for multiple manipulators was addressed by analyzing the grasp space of the robot. Note that the abovementioned controllers were developed under the assumption that the object is firmly held by the robotic arms such that no relative motion occurred between the arms and the objects. However, in practical applications, such as polishing, grinding, and welding, the robot end-effectors need to operate along the object’s surface, where sliding movements usually happened between the robotic arm and the object [12]–[14].

前三句分别陈述方法的动作及受控对象：force／position、internal forces、loading／grasp space。第四句 `the abovementioned controllers ... under the assumption that ... such that ...` 归纳共同条件；第五句让 `robot end-effectors` 与 `object’s surface` 的真实任务关系改变这一条件。先有能力、再有适用条件、再有当前任务差异，才有下一段 `In this respect`。迁移时应把作者已有工作的能力和条件填实；不能把“作者研究需要某能力”当成“过去工作全部无效”。

`firmly held` 不能替换成宽泛的 contact，`relative motion ... between the arms and the objects` 不能含混成双臂彼此运动。`where` 描述实现或任务情况，`such that` 描述条件导致的运动限制，这两种关系不应仅为变换句式而互换。原文时态有局部不齐，不需要复制过去式 `happened`；关键是比较对象和句间逻辑。

### 保留学习条件的连续英文

I06 全段，p.2 左栏，前段已经区分跟踪误差与 NN 权重：

> In our recent work [39], a filtered operation was presented to control the robotic arm with finite-time convergence under a linear-in-parameter (LIP) robotic dynamic model. Nevertheless, the guaranteed convergence of the NN weights is more difficult. It is well known that the persistent excitation (PE) condition is important to guarantee the estimation convergence [40]. However, in practice, it is very stringent to ensure the PE condition of neural networks due to the sparse characteristics of the NN regressor vector. Recent research of neural networks in [41] presented a partial persistent excitation (PPE) condition instead of the traditional PE condition. It has been proven that, for the radial basis function neural network (RBFNN) defined in a regular lattice, neural nodes could be partially activated for any recurrent NN inputs trajectory remained in this local region [41]. In the subsequent work [42], this idea was employed for the control design of nonlinear strict-feedback systems to guarantee the system stability and accurate NN approximation. However, the NN inputs still need to satisfy the condition of recurrent trajectory, and a small input excitation strength may lead to slow learning speed.

`Nevertheless` 不是泛化批评，而是从 LIP 估计转到 NN 权重估计。`due to the sparse characteristics of the NN regressor vector` 对 PE 难满足给出了技术原因。PPE 的能力落在 `RBFNN defined in a regular lattice`、部分节点激活及局部 recurrent input trajectory；尾句继续保留 recurrence 和 input excitation strength 的限制。整段不等于“PPE 消除了所有激励条件”，也不等于“全部 NN 权重都能无条件到达理想值”。

必要正文复核：§III-C Theorem 1（PDF p.6／1015；[旧全文提取](../reading/P05.txt)首词 `Consider the closed-loop dual-arm robot`）明确要求 PPE，tracking errors 和 weight estimation errors 收敛到包含原点的小邻域，contact-force error 有界。§III-C Remark 6（PDF p.7／1016）解释误差信息如何在 Lyapunov 分析中产生对应项。故学习卡应把引言的“convergence”与正文实际保证连起来，不能照贡献句扩大为精确零误差或无条件全权重收敛。

I07 全段，p.2 左→右，图注已排除：

> The work in [43] indicates that parameter convergence can be improved if certain information of the estimation error can be integrated into the adaptation. In [44], a novel parameter estimation law was proposed for a robotic system with unknown dynamics by using a sliding mode technique and a finite-time estimator. In [45], the estimation error was integrated into the adaptation scheme of a class of nonlinear systems to achieve the convergence of NN weights. Motivated by the abovementioned idea, in this article, we develop a composite learning controller for the dual-arm robot to perform bimanual relative motion tasks. To the best of our knowledge, few studies have investigated the learning control in the frame of the dual-arm robot systems subject to relative motion and unknown dynamics. Moreover, different from the work in [46], a PPE condition is also introduced in the estimation scheme to achieve a relaxation of the requirement of the PE condition. In comparison to the method in [45], the estimation error of the NN weights is properly expressed and employed to enhance the approximation of the neural network.

前三句的共同对象是估计误差信息进入 adaptation，第四句才把它移到作者任务。随后 `few studies` 限定双臂、relative motion、unknown dynamics 的交集；`different from ... [46]` 与 `In comparison to ... [45]` 分别比较 PPE 条件与 NN weight estimation error 的利用。这种连续组织可直接迁移到作者“有成熟机制可继承，但目标条件／信息用法不同”的工作。要保留真实继承关系，不能为显得非增量而把已有思想隐藏。

### 具体用词和迁移条件

| 可选英文 | 应承担的判断／动作 | 不可带入的内容 |
|---|---|---|
| `were developed under the assumption that ...`（I02） | 公平地限定前作适用条件，所列方法须真共享该条件 | 任意扩大到全部方法 |
| `the ... need to operate along ...`（I02） | 任务动作改变先前假设 | 把物理滑动条件替换成抽象“复杂场景” |
| `the convergence of the tracking errors`／`the convergence of NN weights to their ideal values`（I05） | 以重复名词保持不同理论对象 | 把误差有界、权重恒定、权重接近理想值混为一谈 |
| `information of the estimation error ... integrated into the adaptation`（I07） | 明确新增信息进哪个更新动作 | 未知真实参数误差可直接测得的暗示，或照抄当前没有的 NN 机制 |
| `a relaxation of the requirement of the PE condition`（I07） | 保留相对某条件放松的科学含义 | `no excitation is required` 等更强判断 |
| `with no prior knowledge of the dynamics`（C01） | 仅在作者实际控制设计不需要先验动力学时使用 | 把不需要动力学等同于不需要几何、传感或任务模型 |

原文 `NN control synthesizes`、`became invalid`、权重不收敛最终不稳定等表述不作为通用表达／科学规则。保持 A06 的明确普通风格，可以学习 A07 对对象和条件的反复命名，而不继承这些语言错误或未为当前作者证明的强推断。

## Fuzzy2023／A02：把两个性能目标展开，再把假设改进落到证明

### 整节组织与段落展开

| 段落及位置 | 原段推进 | 组织上的实际特点 |
|---|---|---|
| I01，p.1 左→右，`FOR` | 时变参数／扰动造成不确定非线性 → NN／FLS 的近似能力及应用 → 一项前作已同时处理 fixed-time 与 user-defined performance → 计算开销及未来 FLS 优化旁支 → 两项目标少被共同讨论 | 首段很长，含不直接支撑本轮贡献的旁支；不能因是范例便全部模仿 |
| I02，p.1 右，`In practice` | 瞬态差的安全后果 → BLF 处理约束的能力 → 三项相关方案 → 作者 symmetric BLF 的作用 | 先说明为何要约束，再说技术选择；末句已出现作者设计 |
| I03，p.1 右→p.2 左，`In many` | 快收敛需求 → finite-time 前作 → convergence time 与初始条件相关 → fixed-time 前作及其已有约束能力 | 这段建立固定时间选择理由，并非声称作者首创 fixed-time＋BLF |
| I04＋C01–03，p.2 左，`Motivated` | FLS／BLF 的问题范围 → 输出约束及瞬态性能 → adaptive law 证明有界并放松前作假设 → practical fixed-time tracking | 三条贡献有不同责任；没有独立 roadmap，也没有引言末尾实验清单 |

这一节适合学习“两个需要共同满足的指标，各自解释理由，再在设计与分析中合拢”。它不是 P17 的生成／执行输入输出链。C02 的价值在于把原先被假定的有界性改成被证明的有界性，是保证依据的改变。不能把它缩成“提出一个新自适应律”就认为贡献讲清。

### 目标—前作—设计作用的英文

I02 全段，p.1 右栏：

> In practice, the undesirable transient performance may lead to the system instability, even the system safety problems sometimes. Recently, the barrier Lyapunov functions (BLFs) have been widely used to achieve the state and output constraints in the nonlinear control problems [12]–[16]. In [12], with the exponential-type BLF, a practical event-triggered prescribed-time controller has been proposed for a class of space teleoperation systems. In [14], a new command filtered fuzzy controller has been proposed for a class of unknown nonlinear systems to handle full-state constraints and finite-time convergence simultaneously. In [16], an adaptive fuzzy leader-following tracking control scheme has been proposed for heterogeneous nonlinear multiagent systems with finite-time output constraints. In this article, a novel symmetric BLF is designed to guarantee the desired transient performance of the robot system.

句间顺序是后果、可用工具、三个有对象／约束类型的例子、当前工具的作用。末句 `is designed to guarantee the desired transient performance` 可直接利用主动或被动的完整主谓实现；作者真实承担保证的对象、技术及条件必须替换。前几句已经包含 prescribed-time、finite-time、full-state、output constraints 等不同术语，不能当成同一类别。

I03 全段，p.1 右→p.2 左：

> In many industrial systems, the system states are required to achieve fast convergence speed for better control performance. There have been some proposed research works focused on the convergence time of the systems [17]–[19]. In [17], an adaptive observer-based fuzzy controller has been proposed for a class of strict-feedback nonlinear systems to achieve finite-time convergence. In [18], an adaptive finite-time sliding-mode control scheme has been proposed for a class of nonlinear systems with some matched uncertainties. Nevertheless, for the existing finite-time control schemes, the convergence time of the systems is always related to the initial conditions, which are sometimes unavailable. To improve the control performance, the fixed-time control schemes have been proposed and applied in the nonlinear control community [20]–[22]. In [20], a novel fixed-time adaptive fuzzy control scheme combined with the BLF technique has been proposed for uncertain nonstrict-feedback nonlinear systems. In [21], an adaptive event-based fixed-time control scheme has been proposed for the active vehicle suspension systems, and the predefined constraints can be guaranteed.

关键接续是 `Nevertheless ... related to the initial conditions` 接 `fixed-time control schemes ... proposed`，不是为增加转折而加 Nevertheless。段末承认 [20] fixed-time＋BLF 和 [21] fixed-time＋constraints 的已有能力。因此 I01 的 `rarely discussed ... in most ...` 只支持有限覆盖判断，不能变成“尚无方法同时保证瞬态性能和固定时间收敛”，更不能借作作者“首次”贡献。

C02 和相邻 C03，p.2 左栏：

> 2) A novel adaptive law is proposed such that the boundedness of all the closed-loop signals can be proved. Then, the assumption that the weight estimation is bounded in recent fixed-time control research [23]–[25] can be relaxed.

> 3) The tracking performance of the robot system can achieve practical fixed-time convergence regardless of the initial conditions.

`a novel adaptive law` 后的 `such that ... can be proved` 交代了为什么设计该律；`Then, the assumption ... can be relaxed` 指出与具体前作相比改变的是保证依据。可用这两句的连续关系表达作者确有的“新设计使某性质得到证明，从而取消某项先验假定”，不预设作者也有权重估计。

必要正文复核：§II-A（PDF p.2／1042）把目标写成 output errors 进入预定义零邻域；§III Theorem 1（PDF p.4／1044）要求初始误差位于 `−βi(0) < ei(0) < βi(0)`；§III Remark 2（PDF p.6／1046）明确区分 `proved theoretically` 与 `being assumed`。这些定位可由 [全文提取](Fuzzy2023-full-raw.txt) 回查。`regardless of the initial conditions` 不应被学成所有初始误差均可违反约束；时间界不随初始条件变化和初始可行性是不同层次。保留 `practical`，也不能把它写成有限时间精确零误差。

### 语言取舍

`avoid the violation of the output constraints`（C01）、`the boundedness of all the closed-loop signals can be proved`（C02）、`the assumption that ... can be relaxed`（C02）和 `practical fixed-time convergence`（C03）都在明确说明技术对象及保证类型。`boundedness`、`convergence`、`constraint satisfaction` 不能为了统一用词而互换；`assumption` 与 `proof` 不能混写。

首段 `large calculation is always required`、`which is exciting` 和 future FLS topology optimization 不是本轮贡献所需的充分证据。首段 `Combined with adaptive control techniques, ...` 与收束 `Motivated by ...` 是原文分词开头，保留在来源副本，迁移时按已有表达约束用明确科学主语及限定动词。原文 `novel` 不作为必选修饰词，源于作者自己的比较证据才可保留。此篇没有 roadmap 的事实应留作组织变体，不能为了统一四篇学习卡而补造它。

## ESO2017／A04：把扰动物理来源、控制作用和可测信息接到设计

### 整节组织与段落展开

| 段落及位置 | 原段内部推进 | 对设计的实际作用 |
|---|---|---|
| I01，p.1 左→右，`UNDERWATER` | 类型／应用 → 数据质量、tracking 或 station keeping 需要精确控制 | 不止应用广泛，点出误差影响的任务结果 |
| I02，p.1 右，`In practice` | unknown external disturbances 与 model uncertainties → 海流等外部来源、ROV 缆索力 → 水动力系数获取误差和姿态引起变化 | 两类不确定性分别解释来源，避免统称“复杂环境” |
| I03，p.1 右，`Several methods` | adaptive／robust／observer 路线 → 实际 NN／FLS 应用、学习参数数量及验证类型 | 先承认已有能力 |
| I04，p.2 左，`Although` | 近似优势与实际学习参数调节困难 | 单句独立段，与上一段合成一个能力／限制组；不强制每段多句 |
| I05，p.2 左，`As an effective` | SMC 及 ISMC 能力 → integral term 的作用 → chattering 的代价 → 缓解方案 → 无补偿时大界导致抖振 → 需要 disturbance compensator | 控制器选择理由含执行代价及具体补偿责任 |
| I06，p.2 左，`Another approach` | observer 估计 → control design 用估计补偿 → 三类 observer 与实例 → 同时估计状态的能力 → bandwidth 取舍 | 上段补偿需求接本段估计—补偿路径 |
| I07，p.2 右，`In this paper` | 作者装置与可测位置／姿态 → 无直接速度测量 → 直接微分可能损害控制 → 需要 output feedback／state observer → 相关研究及 simulation／experiment 区别 | 当前传感条件在贡献前引出新的必要设计，并再次综述 |
| I08＋C01–03，p.2 右→p.3 左，`In this paper` | MIMO-ESO 估计、未知界自适应、控制律分析 → equivalent／switch controller → 实机实现 → 三条贡献 | 把估计对象、控制作用、保证和验证范围对应起来 |
| I09，p.3 左，`The remainder` | model → ESO → ISMC → experiments → conclusion | 章序对应设计依赖 |

此节确实较长，部分跨领域例子和重复的 `In this paper` 可以不迁移。其有价值的完整逻辑是：不确定性来自哪里，SMC 为何需要补偿，估计结果供谁使用，为什么装置还需要状态估计。I07 从当前装置返回文献的结构，是“在已引入设计后继续交代必要条件”的另一真实变体。

### 物理问题的具体英文

I02 全段，p.1 右栏：

> In practice, there are a number of technical challenges in the control of an underwater robot, such as the unknown external disturbances and model uncertainties. The unknown disturbances in practical oceanic environments include waves, tides, currents, and upward or downward streams. For control design of ROVs, the external force caused by the cable that connects with the depot ship should also be considered. The model uncertainties of an underwater robot are usually caused by the inaccurate hydrodynamic coefficients, which are calculated through the computational fluid dynamics (CFD) methods or towing tank experimental data analysis. During the process of performing a task, different attitude of the robot will also cause the variation of the hydrodynamic coefficient.

第二、三句解释 external disturbances，第四、五句解释 model uncertainties。`caused by`、`calculated through`、`cause the variation of` 的动作分别是物理来源、参数获取方式、任务中的参数变化；不是三个可替换的因果修辞。迁移时可以照这一整段信息组织，先分清作者的误差／不确定项，再给每类真正必要的来源及其对设计的影响。没有缆索的作者系统不能继承 ROV 缆索例子，没有证据的“各类环境复杂性”也不能填进去。

I05 尾部的四个连续句，p.2 左栏，前文已介绍 ISMC／SMC 能力与抖振代价：

> To reduce the chattering, several methods, such as the high-order sliding-mode controller [24], [25], disturbance compensation method [26], [27], and terminal sliding controller [28] have been proposed. In [26], a free chattering SMC is presented via an adaptive term, which continuously compensates for the unknown system dynamics of an ROV. In practice, sometimes, the upper bound of the uncertainties may be large and the SMC without a compensator will cause serious chattering. Therefore, it is necessary to design a compensator for the external disturbance to reduce chattering.

这组句子保留缓解抖振已有方法及其中一项补偿方法，随后用特定大不确定界的情形解释补偿需求。`without a compensator` 限定问题对象，`to reduce chattering` 限定用途。它支持“为什么当前需要一个补偿器”，不支持“全部 SMC 均不能抗扰”，也不支持未经作者证明的“彻底消除抖振”。

I06 开头三个连续句，p.2 左栏：

> Another approach dealing with the unknown disturbance is to design an observer to estimate the unknown external disturbance of a robot, followed by the control design to compensate for the estimated disturbance. Such disturbance observers include sliding mode observer [12], [29], high-gain observer [30], [31], and extended state observer (ESO) [13], [32]. In [12], a sliding mode controller based on a sliding mode observer is proposed for a reusable launch vehicle.

`estimate the unknown external disturbance` 接 `control design to compensate for the estimated disturbance`，估计量进入控制的对象交接清楚。科学上 controller 补偿扰动的作用，使用 disturbance estimate 生成补偿输入；不能因为原文用了 `estimated disturbance` 就把“补偿对象”与“用于补偿的信息”混同。作者实际若估计的是状态、合并不确定项或外力，需要分别保留这些对象类别。`Such disturbance observers` 指回已限定的观察器集合，不是泛称所有 observers。

### 传感条件如何成为设计理由

I07 开头六个连续句，p.2 右栏；后续相关研究与验证分类仍在同一段，完整内容见来源副本：

> In this paper, we design an adaptive sliding mode-based controller for a general type of underwater robots, and experiment is carried on a test bed for underwater object grasping. Onboard sensors, including a depth sensor and an inertial measurement unit (IMU), are equipped to measure the depth and attitude of the robot. The position of the underwater robot is measured by an external vision positioning system (VPS), and some white lightings are equipped on the robot, which can be captured by the VPS to calculate the position of the robot. In such a case, there is no direct measurement of velocity of the robot. Then output feedback is required for our work as the direct differential of the position information may degrade the control performance. In such case, observes are always used to estimate the unmeasured states of the robot [5], [33].

先说装置提供的 depth／attitude／position，再说明 velocity 未直接测量，随后说直接微分的控制后果及 output-feedback 需求。读者能从现实信息条件理解为什么有 observer。可以直接学习 `is measured by`、`there is no direct measurement of`、`output feedback is required ... as ...` 的顺序和用词；作者自己的传感器及信号必须填实。灯光颜色及安装细节未必值得迁移，关键是测得哪些量、缺哪个量、该缺失为何影响设计，而不是实验装置细节越多越好。

`In such a case` 和 `Then` 承担特定条件与设计后果，不是句数填充；合适时改成明确命名科学对象，避免在长段里反复用泛指。原文 `observes`、`white lightings`、`experiment is carried` 等错误或不自然表达不继承。段尾区分仿真和实验，只是验证类型，不能直接推断仿真研究无效或全部实验覆盖当前条件。

### 设计、保证和证据怎样收束

I08 全段，p.2 右栏：

> In this paper, a disturbance compensation approach is utilized to eliminate the chattering based on multiple-input and multiple-output extend-state-observer (MIMO-ESO) with a simple structure. Motivated by the ESO model [32] and the high-gain observer [39], a MIMO-ESO is proposed to estimate the unknown disturbances and the unmeasured states. The bounds of the uncertainties are also estimated using the adaptive control technique. The Lyapunov analysis is involved to design the final control law. The proposed controller in this paper includes two parts, namely the equivalent controller and the switch controller, which guarantees the trajectory tracking error converge to zero theoretically. The proposed controller is successfully implemented on an underwater robot propelled by six thrusters. The main contributions can be summarized as follows.

句组由 disturbance compensation 到 MIMO-ESO 估计对象，再到 bounds、Lyapunov analysis、两个控制部分和实机实现。`is proposed to estimate`、`are also estimated`、`includes two parts`、`is ... implemented on` 明确了不同动作；不能把“估计外扰”“估计不确定项的界”“保证跟踪误差收敛”“实验比较”压成一个宽泛的 robust performance。

必要正文复核：§II（PDF p.3／6787）明确有 nominal matrices 和 bias；`H = Hd + Hun` 区分外扰与模型不确定性，§III 的 extended state 使用 `Hd`。§IV Theorem 1（PDF p.6／6790）依赖 Assumptions 1–2 及参数条件。§V（PDF p.8／6792）列出控制所用 nominal hydrodynamic parameters，并说明比较 PD 的速度由位置微分计算。因此这里不能学成“ESO 使全部模型不再需要”“所有不确定性均由同一估计量精确估出”，也不能把理论渐近性质换成固定／有限时间保证。

原文 C03（PDF p.3／6787）实际写着 `conventional potential difference (PD) control`，这是原论文术语错误，并非提取错误；副本原样保留。§V 的比例／微分增益及位置信息微分与比例微分控制一致，支持把这一展开判为错误；正文此处没有给出一个可直接照搬的完整英文展开。迁移到作者稿时，必须依据作者实际比较控制器确认 PD 或 PD-like 类别，不能由缩写擅自展开，更不能把该错误拿来证明作者自己的科学忠实已通过。

## 四篇不同写法的取舍，以及六层怎样落实

| 维度 | P17／默认锚点 | P05 | Fuzzy2023 | ESO2017 |
|---|---|---|---|---|
| 主要收窄轴 | 示教表征 → 生成输出 → 不确定动力学下执行 | 无相对运动 → 相对运动及未知动力学 → NN 学习条件 | 瞬态约束与收敛时间两个性能目标 | 物理不确定性 → 抖振／补偿 → 传感信息及估计 |
| 方法出现位置 | I03、I05、I07 逐步出现，I08 综合 | 主要在 I07 以后，前文围绕任务及学习条件 | I02 已给 symmetric BLF，I04 综合 | I07 先说作者装置，再补状态估计文献，I08 综合 |
| 贡献实现 | 连续 prose；系统与具体前作比较 | 目标句＋三条列表 | 目标句＋三条列表，无 roadmap | 方法／理论／实机句组＋三条列表＋roadmap |
| 值得保留的局部英文习惯 | 普通主谓、对象输出交接、选择接作用 | 反复命名误差及条件，逐项范围比较 | 保证对象、assumed／proved 区别 | 物理原因、measured／unmeasured 区别、estimate 接 control |
| 不迁移的局部负担 | Here、former/latter 含混风险、若干过强技术概括 | 原文语法问题、把 NN 权重问题泛化为必然不稳定 | 第一段旁支、always／exciting、novel 装饰 | 宽泛跨领域罗列、装置枝节、语言错误与 PD 错误展开 |

成熟写法可在以下六层直接选择、组合、调整，前提都是作者科学含义已经确定。

| 学习层级 | 本轮真实证据 | 在作者内容上的动作与检查 |
|---|---|---|
| Manuscript | P17 的 generation／tracking 与 roadmap，ESO 的 model／observer／control／experiment 接续 | 对照作者全文真正承担的贡献和保证；这里只能识别接口，不能由引言分析宣称六层写作效果通过 |
| Section | 四篇上面的整节段落组及不同方法出现位置 | 先找作者需要解释的任务差异、信息条件或性能目标，再选适用组织；不默认九段、四段、双组件或三贡献 |
| Paragraph | P05 I02 的能力—共享假设—任务差异，ESO I02 的两类来源，Fuzzy I02 的后果—工具—作用 | 直接借成熟整段展开；删去不服务作者贡献的例子，保留使设计必要的前提 |
| Consecutive sentences | P17 I05 的设计—修改作用、I07 的轨迹交接；Fuzzy C02 的证明—假设改变 | 明确后句接前句哪个对象、增加哪个理由／作用／条件；连接词不制造因果 |
| Sentence | `were developed under the assumption that ...`、`is employed to approximate ...`、`can be proved` 等原句 | 保留合适句型与信息顺序，换作者对象／动作／条件；执行已有主语、负荷和标点约束 |
| Phrase／Word | `in advance`、`relative motion`、`tracking errors`、`estimation error`、`practical`、`unmeasured`、`compensate for` | 逐项确认类别、范围和搭配；测量不改写成估计，估计不改写成补偿，有界不改写成收敛 |

这些动作不是六次确认或固定 pipeline。已有清楚的作者句子及科学关系应复用，局部补充可以来自另一篇，但组合后仍要回查主语、技术对象、条件和论证顺序。例如，作者若既有轨迹生成又有执行控制，可以用 P17 的整节联系；如果核心是联合性能指标，则选 Fuzzy2023 的目标分解；若关键是信号可获得性，则选 ESO 的条件—设计链；如果主要差异是接触条件与学习激励，则用 P05。不能为模仿 A06 硬造 learning 模块，也不能把四条路线累加成超长引言。

“直接抄适用的成熟英文”在这里应落实为实际段落展开、连续句逻辑、主谓结构与具体搭配的直接利用。来源的专属科学事实、数据、比较和理论结论都换成作者自己的；作者既有表达约束同时生效。引言学习不需要新增另一套语法检查、泛化 blacklist、词数配额或固定连接词库。

## 对照当前 Skill：已有依据和真正缺口

| 当前文件／位置 | 已有内容与应复用部分 | 本轮证据指出的缺口或冲突 |
|---|---|---|
| [Shared 范例](../../skill-candidate/nature-shared/core/robotics-writing-examples.md)，`Scope and reading order`、`Author meaning`、`Use during drafting`、`Internal expression` | 科学含义先行；读实际英文；主参考／补充协调；六层；逐句上下文检查；按需选择，无另设审批 | 共用机制完整；不应重写，也不应给每篇加相同检查表 |
| 同文件 `Abstract reference selection`、A06／A07／A02／A04 | 四篇已有真实摘要英文，A06 默认摘要锚点；A07 核心对象关系；源文问题已有选择说明 | 摘要不是本轮四篇整节引言；不能把已有 A 卡记成引言学习覆盖 |
| 同文件 B01、任务索引 `引言／文献段落组` | B01 的 P17 双组件全文接口；B02／B03 的其他论文文献段／耦合问题 | 没有这四篇引言的完整组图、连续英文及迁移差异；现有引言索引仍只指 B02／B03 |
| [Shared 正文](../../skill-candidate/nature-shared/core/robotics-main-text.md)，`Introduction and Related Work` | 按实际比较轴组织，段落组共同完成能力／条件／gap／设计后果；允许连续收束或列表，Related Work 可独立 | 与本轮证据一致。无须把每段 gap、固定贡献形态再写成规范 |
| [Writing section/intro](../../skill-candidate/nature-writing/static/fragments/section/intro.md)，`Paragraph jobs`、`Drafting rules` | 四段 arrangement 明说一种可能，方法型 variants 可选，Results 反向动机与条件比较 | 不应把已有灵活 fragment 改成固定四篇模板；只需有合适实文可检索 |
| [Writing 详细指南](../../skill-candidate/nature-writing/references/introduction.md)，`Forward story (write in this order)`、`Important warning`、各 Pipeline Version | backward-first 问题、理由、优势可用；多种开篇与 pipeline 例子保留 | “即使实际增量也不要这样写”否定如实继承；固定写序可能压掉 P17／Fuzzy／ESO 的中途设计；示意句 `Considering that ...` 与共用分词开头禁用冲突 |
| [Polishing section/intro](../../skill-candidate/nature-polishing/static/fragments/section/intro.md)，`Common failure modes` | 已规定段落组比较，贡献列表缺少问题路线才是问题；避免 Results／Conclusion 重述 | 没有把列表本身判错，当前不构成冲突；缺的是四篇可直接用于修复的实际引言实现 |
| [科学英文共用核心](../../skill-candidate/nature-shared/core/scientific-expression.md) | 普通主谓、明确类别／对象、条件与保证、自然搭配、Here／分词开头／标点约束及变体保留 | 足以承担本轮源文语法、术语及迁移检查；没有依据增加第二套通用规则 |
| [Nature 引言指导](../../skill-candidate/nature-shared/core/nature-introduction.md)，`Let the answer emerge late`、`End with a compact research route` | 以问题动机先于作者框架；Nature 稿偏好连贯研究路线 | 当前明确是 Nature 适用范围；不应根据 IEEE 三条列表删除它，也不应将 Nature 偏好扩为所有 robotics 投稿规则 |
| 两端 SKILL.md 的 robotics 条件路由与 Writing [manifest](../../skill-candidate/nature-writing/manifest.yaml) | manuscript／robotics 按需加载共用正文与任务选例，intro 详细指南按适用任务加载 | 无加载失效运行证据；不能声称只是加文件就会实际读到或稳定利用，应沿现有任务索引接入 |

本轮可以确定的是**四篇引言专门实文覆盖不足**及**局部规则文字冲突**。不能确定的是生成器是否会忽略已有规则、现有检查是否可靠、哪项规则实际造成作者稿错误；本轮没有隔离写作输出、没有 root1 对照，也没有测试。因此不把范例缺口直接定性为已证实的效果失败原因。

## 最小必要改造建议：具体问题、动作和预期作用

以下是未来候选改造的建议，本轮未实施。

| 建议及最小文件范围 | 具体问题与原文依据 | 改变哪个判断／执行动作 | 为何预期有效及其限制 |
|---|---|---|---|
| 1. 在 Shared 新增一个按需正文参考 `core/robotics-introduction-examples.md`；只在现有 `robotics-writing-examples.md` 引言任务行及邻近选择说明接入 | A 卡是摘要；B01 是骨架，B02／B03 是其他论文局部。P17 I03–I08、P05 I02–I07、Fuzzy I02–C03、ESO I02–I08 提供四种实际完整推进 | 引言／引言修改选择时，本轮作者偏好以 P17／A06 为默认表达锚点，读对应段落组与英文，再按条件选补充；正文任务不继续误用摘要句作整节依据 | 补齐最接近实际生成的范例层，保留既有按需方式；新参考可自足，无须加载本报告或全文 PDF。是否实际采用与写好仍待后续验证 |
| 2. 同一新增参考放四篇的整节组图、代表性完整段落／相邻句及来源、条件、用词差异；复用 B01 接口，不再复制一套全文结构规则 | 四篇方法出现位置、比较条件及收束形式不同；P17 的轨迹交接、P05 的 PPE、Fuzzy 的 assumed／proved、ESO 的 measured／unmeasured 是词级科学差异 | 从任务所需关系选择英文单位，必要时组合；对不适用的源文事实和错误明确不迁移。保留连续收束、列表及有／无 roadmap 变体 | 提供可直接用的英文和选择边界，减少只读功能标签；收益是依据更具体，不是能力或稳定性通过。不是每次读四篇、不是四种固定填空模板 |
| 3. 局部改 `nature-writing/references/introduction.md` 的 `Important warning`，保留所在技术挑战段及其他 variants | 现文 `Even if the work is actually incremental, do not write it this way` 与 P17 I05／I08、P05 I07、Fuzzy C02、ESO I08 的真实继承和改进相冲突 | 建议替换为：“如实交代前作能力、适用条件和本工作改变的条件或机制。删去无助于理解贡献的开发历史；保留解释为何必须改进及改进如何起作用的比较。”不再为了读者好奇心遮掩增量性质 | 去除明确冲突，并让前作与当前设计的比较可执行；无需全局强化 novelty。尚未证明该警告实际污染过哪次输出 |
| 4. 同一 Writing 详细指南局部调整 `Forward story` 的绝对标题／顺序提示，检查其 Pipeline Version 的句式示意 | P17 I03／I05、Fuzzy I02、ESO I07 均在必要问题说明后给局部设计，并继续解释其他条件；`Considering that ...` 被列为可抄句式但违反共用表达约束 | 将该顺序标为可选组织；允许按作者依赖关系先动机某一组件并介绍设计，再转下一条件。句式示意按已有共用核心改为明确主语的原因句和设计句，保留实质因果 | 与已经灵活的 section fragment 对齐，消除近端示意冲突；不新增路由、新 workflow 或固定句式库。Nature 条件模块继续保留其适用偏好 |

建议1与2属于同一个范例补充，不是两套新规范。最小未来修改集合因此是一个新增 Shared 参考、一个已有 Shared 索引、一个 Writing 详细指南。两端 router、section fragment、`robotics-main-text.md`、`scientific-expression.md`、Nature 专用模块以及摘要卡目前均有理由保留。Polishing 通过现有共用索引使用同一引言证据，不复制一份规则或英文。若将来发现现有按需索引不能使新参考被读到，再根据加载记录调整必要位置；本轮没有这类证据，不能提前扩大范围。

## 本轮完成边界与下一步

已完成四篇完整引言及必要正文边界阅读、两栏和跨页核对、原样科学陈述保存、六层具体英文分析、成熟材料复用及文件级最小建议。未修改候选 Skill，未开展 Drafting、Polishing、组合交付或迁移测试；这些项目本轮均未评价，不补记通过。证据文件和链接的完整性核对只证明本次分析可回查，不能代替自主写作效果。

下一步由负责人独立核对本报告及原文。若后续授权改造，可按上述最小集合落实；作者引言对照仍需要可确认身份的 `root1.pdf`。在取得该稿之前，不用其他稿替代，也不把这些已知范例当作迁移成功案例。后续效果与执行可靠性需要另一次明确授权的独立验证，本轮不启动。

# 四篇主范例 Introduction：整节、段落与真实表达

本轮重新回查 B15–B18 对应的四份本地出版 PDF，完整核对 §I 与 §II 的边界、跨栏／跨页段落和原句，再独立整理以下总结。结论从原文具体科学关系提出；用户给出的观察只作为颗粒度要求。本轮没有修改或安装 Skill，没有效果测试，也没有用 E04 或旧诊断决定引言应该包含什么。

阅读入口如下。每份详析同时提供**完整科学主线、每一段的任务与交接、完整连续原段，以及每句的作用和实际英文实现**；不是只给挑选后的句式。

| 卡片／论文 | 原文范围 | 完整原文与逐句详析 |
|---|---|---|
| B15／P17：*Robot Learning System Based on Adaptive Neural Control and Dynamic Movement Primitives*，TNNLS 30(3), 2019，DOI 10.1109/TNNLS.2018.2852711 | §I，PDF p.1–2／印刷777–778，9个正文段落 | [完整原文](P17-introduction.md)、[逐段逐句](P17-analysis.md) |
| B16／P05：*Composite-Learning-Based Adaptive Neural Control for Dual-Arm Robots With Relative Motion*，TNNLS 33(3), 2022，DOI 10.1109/TNNLS.2020.3037795 | §I，PDF p.1–2／印刷1010–1011，9个正文段落及3条贡献 | [完整原文](P05-introduction.md)、[逐段逐句](P05-analysis.md) |
| B17／Fuzzy2023：*Fixed-Time Fuzzy Control of Uncertain Robots With Guaranteed Transient Performance*，TFS 31(3), 2023，DOI 10.1109/TFUZZ.2022.3194373 | §I，PDF p.1–2／印刷1041–1042，4个正文段落及3条贡献，无 roadmap 段 | [完整原文](Fuzzy2023-introduction.md)、[逐段逐句](Fuzzy2023-analysis.md) |
| B18／ESO2017：*Extended State Observer-Based Integral Sliding Mode Control for an Underwater Robot With Unknown Disturbances and Uncertain Nonlinearities*，TIE 64(8), 2017，DOI 10.1109/TIE.2017.2694410 | §I，PDF p.1–3／印刷6785–6787，9个正文段落及3条贡献 | [完整原文](ESO2017-introduction.md)、[逐段逐句](ESO2017-analysis.md) |

I／C／S 是本轮定位号，分别表示正文段、贡献条目和段内句子，不是论文原有编号。原句仅规范连字、排版断词、空白与首字下沉，不改科学用词、语法或标点。[重新提取记录](source-provenance.json)、[版面文本块](curated-introductions.json)、[断词记录](normalization-log.json)、[完整性核验](evidence-checks.json)供回查。以下英文引文均为注明位置的完整原句或连续句组；省略的上下文在链接的完整段落中保留。

## 一、整节：四条具体科学主线怎样逐段建立

### P17：多示范运动生成之后，为什么还要解释轨迹执行

**科学链。** 产品更新需要适应性机器人 → 人示教经运动建模重现技能 → DS／DMP 提供稳定、可扩展的运动表示 → 最优示范难获得，多示范含有可综合的运动信息 → GMM 建模 DMP 非线性函数，GMR 检索其估计，从多示范生成运动 → 重现效果还取决于所生成轨迹能否准确跟踪 → 未知载荷使动力学难预先获得 → RBFNN 近似动力学非线性，控制器跟踪前一组件生成的关节空间轨迹 → 运动生成与轨迹跟踪共同承担真实执行。[完整段落任务表](P17-analysis.md)

I01 不停在“机器人学习很重要”，而是用人示教的过程落到 motion modeling。I02 先说明 DS 的能力，再以特定 DS 学习的数据需求比较 DMP。I03 的重要转折不是“DMP 不行”，而是从多个 DMP 的不同用途转到**多个示范进入一个 DMP**。I04 承认概率建模与已有 DS＋统计学习的能力，I05 才给当前组合的建模、检索和生成分工。

I06 用 imitation performance 把已解释的生成接到尚未解释的跟踪，从准确模型的好处、未知载荷的困难一直推出 RBFNN。I07 重复关节轨迹这一中间对象，说明生成组件输出什么、跟踪组件接收什么、NN 补偿什么。I08 综合两项责任并作限定前作比较，I09 的 DMP→学习→控制分析→实验安排继续沿这一依赖顺序。

因此这篇不能缩成“有 DMP 和 NN 两个模块”：两个模块分别由多示范表征需求与未知动力学执行需求推出，并通过同一组轨迹相接。本文设计在 I03、I05、I07 分批出现，文献比较也在设计出现后继续进行。[I03–I08 原文及逐句](P17-analysis.md#i03)

### P05：从相对运动条件，一直推进到学习更新需要的信息

**科学链。** 双臂协作有载荷和工作空间优势，但运动控制／规划更复杂 → 紧持物体、手臂与物体无相对运动的前作不对应沿物面滑动的任务 → 相对运动控制已有研究仍依赖已知动力学，并缺接触力稳定性分析 → 抓取物动力学难预知，NN 可补偿未知动力学 → 跟踪误差收敛与 NN 权重估计收敛是不同责任 → NN 稀疏回归使 PE 条件严格，PPE 保留局部重复输入能力但仍有输入及学习速度要求 → 将估计误差信息接入复合学习更新，在双臂相对运动及未知动力学设置下设计控制，以 PPE 放松激励要求 → 分别汇总任务框架、误差信息使用和条件放松，后续给控制分析及仿真。[完整段落任务表](P05-analysis.md)

I01 从双臂优势转到控制复杂性。I02 的前三句分别承认物体操作、内力约束与载荷分析能力，再归纳这几项方法的物理条件；末句的 polishing／grinding／welding 不是装饰性应用，而是解释为什么 end-effector 必须沿物体表面滑动。I03 进入这类任务后，**仍然承认相对运动研究已经存在**，再讨论 dynamics fully available 和接触力分析的条件。[I02–I03](P05-analysis.md#i02)

I04 解释未知动力学来自哪里，才选 NN。I05 把评价对象由 tracking errors 换到 NN weights。I06 进一步解释权重估计需要什么激励，以及 PPE 已解决什么、还需什么。I07 不从抽象“学习不足”直接跳到本文，而是先给估计误差信息进入 adaptation 的已有思想，再给当前控制，并把与 [46] 的条件比较和与 [45] 的信息用法比较分开。[I04–I07](P05-analysis.md#i04)

三条贡献对应三个不同改变：任务及先验范围、权重更新信息、激励条件。它们不是同义的三个“提高性能”。实际跟踪、权重估计、激励和接触力也不是可以互换的科学对象。[I08／C01–C03](P05-analysis.md#i08)

### Fuzzy2023：两个性能目标分别说明，再解释保证依据如何改变

**科学链。** 时变参数与外扰产生未知非线性 → NN／FLS 已用于近似和控制，已有方法也涉及固定时间与用户性能 → 本文关注瞬态约束和收敛时间的共同成立 → 不良瞬态带来稳定／安全风险，BLF 可以处理约束，设计 symmetric BLF → 快收敛另有需要，finite-time 的收敛时间与初值相关，转到 fixed-time 并承认已有 BLF／约束组合 → 在 FLS＋BLF 的不确定机器人跟踪设置中设计约束工具及自适应律 → 输出不越界、闭环信号有界性可证明、practical fixed-time 跟踪不依赖初值 → 某些前作的“权重估计有界”假定被放松。[完整段落任务表](Fuzzy2023-analysis.md)

I01 已在第7句承认 fixed-time convergence 与 user-defined performance 同时成立的前作。因此段末的 rarely／most 不能解释成“此前从未兼顾两者”。其计算量和 WSN 拓扑优化是未来启发支线，未接到后文三项设计；这一旁支不能作为所有成熟引言都应保留的结构。[I01](Fuzzy2023-analysis.md#i01)

I02 独立解释瞬态约束：后果→BLF 能力→三项不同约束／时间设置的工作→当前 symmetric BLF。I03 再解释收敛时间：速度要求→finite-time→初值关系→fixed-time→已存在的约束组合。这里是两个目标的分别论证，不是每段都需要“前作失败”。I02 末句已经给本文设计，I03 末句却仍承认已有能力。[I02–I03](Fuzzy2023-analysis.md#i02)

I04 收成研究范围，贡献进一步回答“保证依赖什么”：自适应律让闭环信号有界性成为可证明的结果，使既有 bounded weight estimation 假定可以放松。第三条保留 **practical** fixed-time，而不是不加条件的精确到零。这篇没有独立 roadmap，也没有引言量化实验结果。[I04／C01–C03](Fuzzy2023-analysis.md#i04)

### ESO2017：补偿需要估计信息，而真实传感条件还要求速度估计

**科学链。** 海洋任务的数据质量与运动精度要求 → 海流等外扰、系缆力、流体参数误差与姿态变化使控制困难 → NN／模糊自适应有近似能力但实际调参困难 → SMC／ISMC 能抑制扰动并改善跟踪，但抖振损失能量和轨迹平滑性 → 扰动补偿需要估计信息，观察器先估计再交给控制补偿 → 本平台深度、姿态与位置可测，速度不可直接测，直接微分可能损害控制表现 → MIMO-ESO 同时估计未知扰动及不可测速度，自适应方法估计未知项的界 → 由分析设计 ESO-based ISMC 的跟踪控制，并在六推进器平台做实机对照。[完整段落任务表](ESO2017-analysis.md)

I01 的高精度要求只有两句，I02 随即逐项解释扰动和模型不确定性的不同来源。I03 承认可用路线，部分文献采用连续多句讲方案、内部机制与验证。I04 是独立的一句桥段，只提出 NN／模糊控制的参数调整困难；它不是把这些方法归为无近似能力。[I01–I04](ESO2017-analysis.md#i01)

I05 的责任是把 ISMC 的能力、抖振代价和补偿器必要性接在一起。I06 给出估计→补偿顺序，承认已有观察器可同时估计模型未知项及不可测状态。I07 已宣布本文控制和试验平台，却继续解释真实传感输出、速度不可测、微分代价和状态估计文献。**当前设计为何需要，依赖实际可测／不可测信息，不能用一个泛泛的“不确定环境”替代。**[I05–I07](ESO2017-analysis.md#i05)

I08 将扰动补偿、MIMO-ESO、界估计、控制分析和平台实现合并；贡献分别承担估计、跟踪保证与实验比较。I07 末句明确承认其他水下控制器已有实验，不能把本文价值说成“此前都只有仿真”。I09 按模型→观察器→ISMC→实验安排后文，与估计输出进入控制的依赖一致。[I08／贡献／I09](ESO2017-analysis.md#i08)

## 二、段落：连续句怎样产生具体推进

四份详析已逐句覆盖所有原段。下面选取七类不同推进，展示不能只靠功能标签说明的句间关系。

### 1. 先承认工具用途，再把真正不同的信息需求交给当前设计

P17 I03 前四句介绍 DMP 灵活性及击打、序列组合、风格调节。最后两句不是突然贬低 DMP，而是换到示范质量与信息整合：

<!-- source P17 I03 5 6 -->
> As mentioned in [10], optimal demonstration is difficult to obtain and multiple demonstrations can encode the ideal trajectory implicitly. Therefore, we consider integrating multiple demonstrations into one DMP model in this paper.

第一句同时给一个现实困难和一个正向信息来源。第二句中的 integrating、multiple demonstrations、one DMP model 对应这一关系，才使 Therefore 成立。随后 I04 的概率方法提取变异、保留特征、通过 GMR 生成运动，承担的是这项信息整合需要，而不是另起文献类别。[I03–I04 完整段落](P17-analysis.md#i03)

### 2. 文献句组成流程，不只“一句一个编号”

ESO I03 对 [1] 连续三句说明方法、机制和证据：

<!-- source ESO2017 I03 2 4 -->
> In [1], a robust adaptive controller considering the velocity constraints is proposed for an ROV. The model parameters are estimated online and a Barrier Lyapunov function is applied in the Lyapunov synthesis. Finally, the results are validated thought simulation.

第一句 controller＋is proposed＋ROV 给方案位置与速度条件；第二句把其内部责任分成在线参数估计和 BLF 使用；第三句才说明验证类型。`The model parameters` 和 `the results` 的承接依赖上一句同一方案。原文 thought 为源文用词错误，不能把它当推荐搭配。这种展开适用于机制或证据需要说明的关键前作，不要求每篇文献都写三句。[完整 I03](ESO2017-analysis.md#i03)

### 3. 前作条件只有在任务改变该条件时，才成为有效比较

P05 I02 前三句分别列 [9] 的力／位置调节、[10] 的内力约束、[11] 的载荷／抓取空间分析。接着是连续两句：

<!-- source P05 I02 4 5 -->
> Note that the abovementioned controllers were developed under the assumption that the object is firmly held by the robotic arms such that no relative motion occurred between the arms and the objects. However, in practical applications, such as polishing, grinding, and welding, the robot end-effectors need to operate along the object’s surface, where sliding movements usually happened between the robotic arm and the object [12]–[14].

`abovementioned controllers` 把限制留在刚列的对象；`firmly held ... such that no relative motion` 说明该条件的物理含义。下一句不是只说实际更复杂，而是 `end-effectors need to operate along ... surface`，让 sliding 改变了条件。I03 因此能研究 relative motion，同时承认 [15]／[16] 已做过这种任务，再限定已知动力学和接触力分析。[I02–I03](P05-analysis.md#i02)

### 4. 先写局部进展，再把尚未满足的信息条件保留下来

P05 I06 前四句把 LIP 前作、NN 权重收敛、PE 与 NN 回归稀疏性相接，随后连续四句：

<!-- source P05 I06 5 8 -->
> Recent research of neural networks in [41] presented a partial persistent excitation (PPE) condition instead of the traditional PE condition. It has been proven that, for the radial basis function neural network (RBFNN) defined in a regular lattice, neural nodes could be partially activated for any recurrent NN inputs trajectory remained in this local region [41]. In the subsequent work [42], this idea was employed for the control design of nonlinear strict-feedback systems to guarantee the system stability and accurate NN approximation. However, the NN inputs still need to satisfy the condition of recurrent trajectory, and a small input excitation strength may lead to slow learning speed.

四句依次是条件进展→局部结果及其条件→同一思想的后续用途→剩余输入条件／速度代价。`regular lattice`、`local region`、`recurrent` 使能力有边界；`still need to satisfy` 保留尚需条件；`may lead to` 给有条件的性能后果。这比“PE 很严格，本文更好”细得多，也没有隐藏 PPE 已有能力。[完整 I06](P05-analysis.md#i06)

### 5. 设计句和作用句必须共享刚刚命名的修改

P17 I05 前两句：

<!-- source P17 I05 1 2 -->
> To take advantage of the performance of the DS and the probabilistic approach, we integrate DMP and GMM into our proposed system, where the nonlinear function of DMP is modeled with GMM and its estimate is retrieved through GMR. This modification enables the robot to extract more features of the motions from multiple demonstrations and to generate motions that synthesize these features.

第一句不是只有 integrate 两个缩写：DMP 的 nonlinear function 是被建模对象，GMM 是建模手段，GMR 是检索估计的手段。第二句 `This modification` 必须指这一改变，`extract ... from multiple demonstrations` 与 `generate ... synthesize these features` 才是连着的作用。不能只借用 `enables`，却不交代作用通过哪个科学对象发生。[完整 I05](P17-analysis.md#i05)

### 6. 一段末尾没有 gap，下一段仍可自然展开另一个责任

P17 I05 末尾仍在比较函数近似的计算效率。I06 不是用“然而本方法存在问题”起段，而是：

<!-- source P17 I06 1 3 -->
> The imitation performance of robots also depends on the accuracy of the trajectory tracking controller that involves the robot dynamics. Generally, a model-based control performs better if the model is accurate enough [19]. However, an accurate dynamic model of a manipulator cannot be obtained in advance due to some uncertainties, e.g., unknown payload.

第一句 `also depends on` 把整体 imitation performance 接到另一责任；第二句给准确模型的作用；第三句才用 unknown payload 解释为什么这项责任不能依赖预知模型。后文 approximation-based controllers→NN→RBFNN 的选择因此有科学来源。段间推进不是“上一段不足—下一段创新”的唯一方式，也可以是“已有一项责任—任务效果还依赖另一项责任”。[I05–I07](P17-analysis.md#i05)

### 7. 传感事实逐句产生输出反馈设计要求

ESO I07 第2–3句已明确深度传感器／IMU 测深度与姿态、VPS 测位置；随后连续三句：

<!-- source ESO2017 I07 4 6 -->
> In such a case, there is no direct measurement of velocity of the robot. Then output feedback is required for our work as the direct differential of the position information may degrade the control performance. In such case, observes are always used to estimate the unmeasured states of the robot [5], [33].

速度缺失→位置直接微分可能损害控制→观察器估计未测状态。`In such a case` 的指代依赖之前真实传感描述，`as` 给 output feedback 的理由；末句的 unmeasured states 交给后面的 velocity observer 文献和当前 MIMO-ESO。原文 observes 与 always 不作统一用词／断言。这里若删掉可测信息，只留下“observer improves performance”，论证就失去设计依据。[完整 I07](ESO2017-analysis.md#i07)

## 三、表达：上述作用在真实英文中具体如何实现

### 1. 段首不是统一背景句，而是命名本段要继续处理的对象

| 真实开句及位置 | 主语—动作—对象／本段承诺 |
|---|---|
| `DMPs have been often employed to solve robot learning problems because of their flexibility.`，[P17 I03](P17-analysis.md#i03) | DMPs＋have been employed＋robot learning problems；先亮已有用途，接其具体变体 |
| `Probabilistic approaches have shown good performance in motion encoding [11]–[13].`，[P17 I04](P17-analysis.md#i04) | approaches＋have shown＋motion encoding performance；是承认可继承能力，后文解释怎样提特征 |
| `An adaptive decentralized control scheme was proposed to address the object handling problem of a cooperative robot, where an implicit force control scheme was employed to simultaneously regulate the force and position [9].`，[P05 I02](P05-analysis.md#i02) | 一个具体方案直接开段；proposed／employed／regulate 把方案、内部方法与力／位置功能分开 |
| `The dynamic model of the robot system is of great importance in the controller design [17]–[22], but it is often unavailable in practice.`，[P05 I04](P05-analysis.md#i04) | dynamic model＋is important／unavailable；直接指出下一段补偿为何需要 |
| `In practice, the undesirable transient performance may lead to the system instability, even the system safety problems sometimes.`，[Fuzzy I02](Fuzzy2023-analysis.md#i02) | transient performance＋may lead to＋后果；由后果论证约束工具需求 |
| `In practice, there are a number of technical challenges in the control of an underwater robot, such as the unknown external disturbances and model uncertainties.`，[ESO I02](ESO2017-analysis.md#i02) | 点出两类未知项；后续逐项说来源，不能只停在 challenges |

共同可借的是**用段首兑现本段科学责任**。开句可以是已知工具、具体前作、模型条件、任务后果；不一定是定义句，也不要求每段第一次出现一个缩写。Fuzzy 的 `FOR the robot dynamic systems ...` 是系统条件直接开篇，而非应用热度开篇；ESO I04 则以 Although 开始一整段的能力—限制关系。源文有目的／分词／介词前置，分析不把这些源文形式固化为作者必须采用的句法。

### 2. 文献句的常用主语，不只有 “In [xx], a method ...”

以下是同一连续段落中的主语变化，不能脱离该段要比较的科学对象：

<!-- source P17 I03 2 4 -->
> In [7], DMPs were modified to model fast movement inherent in hitting motion. Another study used reinforcement learning to combine DMP sequences so that the robot could perform more complex tasks [8]. While both these studies employed multiple DMPs to compose a complete action, another study [9] used multiple DMPs to model style-adaptive trajectory, where the style of the generated motion could be changed by modulating the weight parameters that were coupled with the goals.

| 主语选择 | 源文动作及搭配 | 适合承担的具体关系 |
|---|---|---|
| 技术本身：`DMPs` | `were modified to model ...` | 已有技术怎样被改动、去建模哪一种运动；不是所有文献都只是 proposed |
| 研究主体：`Another study` | `used reinforcement learning to combine DMP sequences so that ...` | 技术手段→处理对象→任务能力，句末放引用也成立 |
| 两项已述研究与另一项研究 | `both these studies employed ... , another study ... used ...` | 明确共同用法再比较不同目的，不机械重复 In |

另一组研究证据、方法和信息主体的连续变化来自 P05 I07：

<!-- source P05 I07 1 3 -->
> The work in [43] indicates that parameter convergence can be improved if certain information of the estimation error can be integrated into the adaptation. In [44], a novel parameter estimation law was proposed for a robotic system with unknown dynamics by using a sliding mode technique and a finite-time estimator. In [45], the estimation error was integrated into the adaptation scheme of a class of nonlinear systems to achieve the convergence of NN weights.

`The work ... indicates that ... if ...` 适合陈述一个有条件的已有结论；`an estimation law was proposed for ... by using ...` 适合方案、对象和实现工具；`the estimation error was integrated into ... to achieve ...` 则让关键信息成为主语，方便下一句继续说信息如何进入当前更新。

常见动词及其责任不能随意互换：`was proposed` 宣布方案，`was developed` 说明开发，`was employed/utilized/applied` 说明使用，`was modified` 说明改变，`was extended` 说明扩展，`indicates/showed` 引出文献结论，`was estimated/approximated` 命名具体内部动作。前作若承担综述介绍，Fuzzy I01 的 `algorithms have been introduced in detail` 才是对应动作；不能硬改为一个新控制器被提出。[Fuzzy I01](Fuzzy2023-analysis.md#i01)

### 3. 条件、比较与限制要写出对象和作用范围

| 真实写法及完整上下文 | 可直接学习的语言选择 | 必须保留的科学关系 |
|---|---|---|
| P05 I02 连续末两句，见上引文 | `were developed under the assumption that ...`，`need to operate along ...` | 已列方法的前提与当前沿表面操作需求相撞，不等于全部前作都不支持接触 |
| [P05 I03 S05](P05-analysis.md#i03)：`In these works, however, the controllers were designed under the assumption that the robot dynamics are fully available, while the stability analysis of the contact force between the robotic arm and the object was not given.` | `In these works` 限定范围，`fully available` 写可得信息，`was not given` 写缺分析 | 已知动力学与未给接触力分析是两项条件；不是泛化为所有研究方法失效 |
| [ESO I04](ESO2017-analysis.md#i04)：`Although the NN and fuzzy-based adaptive controllers have the advantages on the approximation of the uncertainties and disturbances, it is still a challenging task to adjust its learning parameters in real applications.` | `Although ... , it is still ... to ...`，`in real applications` | 先承认近似能力，再说学习参数整定的实际困难 |
| [P17 I02 S05–S07](P17-analysis.md#i02) | `The learned model showed ...`→`this DS-based method required ...`→`In contrast, ... DMP ... requires ...` | 同一实例的能力与数据代价之后才比较 DMP，不靠 However 抹去原有能力 |
| [P17 I05 S04–S05](P17-analysis.md#i05) | `Despite the added complexity ...`，`computing efficiency is less than that of GMR` | 承认单示范能力，再按具体计算效率维度比较另一近似方法 |
| [P05 I06 S08](P05-analysis.md#i06)，见上连续句组 | `still need to satisfy ...`，`may lead to slow learning speed` | 留下输入条件，区分条件要求与可能性能后果 |

`only`、`still`、`some`、`in these works`、`under`、`may` 看似普通，却决定科学范围。比较的限定不只放在一段末尾“本文有局限”，而是在需要处随对象给出。原文里的 stronger／more accurate／less efficient 也都应找回其对象和比较维度，而不是替换成笼统 superior。

### 4. 设计句可以是 we＋动作，也可以让工具／算法直接作主语

P17 I05 的 `we integrate DMP and GMM into ...` 已给组合与内部责任。P05 I07 后两句紧接作者的 composite learning 设计，分别说明两项变化：

<!-- source P05 I07 6 7 -->
> Moreover, different from the work in [46], a PPE condition is also introduced in the estimation scheme to achieve a relaxation of the requirement of the PE condition. In comparison to the method in [45], the estimation error of the NN weights is properly expressed and employed to enhance the approximation of the neural network.

一个以 PPE condition 为主语，动词 introduced，进入 estimation scheme，作用是 relaxation of PE；另一个以 estimation error 为主语，动词 expressed／employed，作用是 enhance approximation。两项不能只压成 `we improve the learning scheme`。

Fuzzy I02 的末句则是设计工具作主语：

<!-- source Fuzzy2023 I02 6 6 -->
> In this article, a novel symmetric BLF is designed to guarantee the desired transient performance of the robot system.

ESO I07 的 `we design an adaptive sliding mode-based controller ...` 是主动方案句，I08 的 `a MIMO-ESO is proposed to estimate the unknown disturbances and the unmeasured states` 是观察器被动方案句。共同要求是命名**实际设计动作、接受该动作的科学对象和它负责的任务**，不是固定主动率或强制 we 开句。`integrate` 是组合，`design/develop` 是建立方案，`introduce` 是把条件／工具引入具体位置，`incorporate` 是把部件放入系统承担责任。[P17 I07](P17-analysis.md#i07)、[ESO I08](ESO2017-analysis.md#i08)

### 5. 作用句用普通动词，沿同一对象把机制交给任务效果

| 科学动作 | 原文实际对象和搭配 | 回查上下文 |
|---|---|---|
| 建模 | `the nonlinear function of DMP is modeled with GMM` | [P17 I05](P17-analysis.md#i05)：与 GMR 检索估计分开 |
| 检索估计 | `its estimate is retrieved through GMR` | 同段下一句接多示范信息综合 |
| 提取／保留 | `extract the features from multiple demonstrations`；`more features ... can be preserved` | [P17 I04](P17-analysis.md#i04)：variability→features→motion |
| 生成 | `generate motions that synthesize these features` | [P17 I05](P17-analysis.md#i05)：输出运动含上游特征 |
| 跟踪 | `track the trajectories generated from the former` | [P17 I07](P17-analysis.md#i07)：复用生成组件同一轨迹 |
| 近似 | `approximate the nonlinear functions of the robot dynamics` | 同段 controller 的跟踪责任与 RBFNN 近似责任不同 |
| 补偿 | `compensate for the uncertain dynamics` | 同段明确被补偿未知项，不只说 robustness |
| 调节／约束 | `simultaneously regulate the force and position`；`internal forces were constrained` | [P05 I02](P05-analysis.md#i02)：各前作处理不同力／位对象 |
| 信息进入更新 | `estimation error was integrated into the adaptation scheme` | [P05 I07](P05-analysis.md#i07)：为 NN 权重学习服务 |
| 估计／减小控制增益 | `estimate the unknown external disturbances and to reduce the control gain` | [ESO I06 S03–S04](ESO2017-analysis.md#i06)：同一 observer 的两个作用 |
| 避免违反约束 | `avoid the violation of the output constraints` | [Fuzzy C01](Fuzzy2023-analysis.md#c01)：随后连接 transient performance |
| 放松条件 | `the assumption ... can be relaxed` | [Fuzzy C02](Fuzzy2023-analysis.md#c02)：来自前句有界性证明 |

这些搭配的可复用部分是动作与对象的自然组合；不能把 estimate 换成 measure、把 approximate 换成 guarantee、把 model 换成 control。`This modification enables ...`、`The designed observer estimates ...`、`The bounds ... are also estimated ...` 让上一设计有清楚的接收点，不要求每句换一个新同义词。[P17 I05](P17-analysis.md#i05)、[ESO I06–I08](ESO2017-analysis.md#i06)

### 6. 过渡词依赖科学关系，而不是自动生成句间逻辑

| 关系 | 原文实现和所在连续段落 | 它实际连接什么 |
|---|---|---|
| 原因 | `due to ... unknown payload`，[P17 I06 S02–S03](P17-analysis.md#i06)；`because of ... approximation ability`，[P17 I06 S04–S06](P17-analysis.md#i06) | 模型不可预知的原因；NN 被选择的能力理由 |
| 执行另一责任 | `also depends on ... trajectory tracking controller`，[P17 I06 S01](P17-analysis.md#i06) | 生成运动仍不足以解释整个 imitation performance |
| 另一条同目标路线 | `Another approach ... is to design an observer ... followed by ... compensate ...`，[ESO I06 S01–S02](ESO2017-analysis.md#i06) | 同一个未知扰动对象下改走估计—补偿路线，不是无关“另一个领域” |
| 条件性结果 | `can be improved if ... integrated into the adaptation`，[P05 I07 S01–S03](P05-analysis.md#i07) | 估计误差信息如何改善参数收敛 |
| 明确用途 | `was employed to optimize the bandwidth of each kernel`，[P17 I05 S03–S04](P17-analysis.md#i05) | LWR 学习之后的核带宽优化，不泛称 improve |
| 设计后的作用 | `This modification enables ...`，[P17 I05 S01–S02](P17-analysis.md#i05) | 已命名组合如何提取和综合示范特征 |
| 限定后的选择 | `Therefore, we consider integrating ...`，[P17 I03 S05–S06](P17-analysis.md#i03) | 最优示范难获得而多示范有信息，因而整合 |
| 尚需条件 | `However ... still need to satisfy ...`，[P05 I06 S05–S08](P05-analysis.md#i06) | PPE 局部能力之后仍需重复输入条件 |
| 后续推论 | `Then, the assumption ... can be relaxed`，[Fuzzy C02](Fuzzy2023-analysis.md#c02) | 先证明闭环信号有界，再改变前作假定 |

因此用 Therefore 前应有够用的原因，用 However 前应有同一评价对象上的差别，用 This modification 前应有可命名的修改。源文还经常直接用 `The learned model`、`The observer`、`The model parameters`、`The designed observer` 接上一方案；不一定靠连接副词。P17 I07 的 former／latter 能工作，是因为上一句已命名两个组件、下一句继续同一组轨迹；借鉴时仍可按作者偏好直接重复组件名。[P17 I07](P17-analysis.md#i07)

### 7. 段末至少有七种不同职责，不固定为 gap

| 段末职责 | 真实句子及上下文 |
|---|---|
| 解释已选模型的性质 | P17 I02：`The inherent property of the spring-damper system enhances the stability and robustness (to perturbations) of the generated motion.` 前文已解释 spring-damper 与待学习函数。[完整段](P17-analysis.md#i02) |
| 汇总可继承能力 | P17 I04：`Both methods exploit the robustness and generalization capability of the DS as well as the excellent learning performance of the probabilistic methods.` 前两项是 SEDS／DS-GMR，后段开始当前组合。[完整段](P17-analysis.md#i04) |
| 当前局部设计选择 | P17 I03：`Therefore, we consider integrating multiple demonstrations into one DMP model in this paper.` 前一句给示范质量及多示范信息理由。[完整段](P17-analysis.md#i03) |
| 明确下一设计责任 | ESO I05：`Therefore, it is necessary to design a compensator for the external disturbance to reduce chattering.` 前两句已给补偿例子及未知界较大时的抖振。[完整段](ESO2017-analysis.md#i05) |
| 给当前工具及作用 | Fuzzy I02：`In this article, a novel symmetric BLF is designed to guarantee the desired transient performance of the robot system.` 下一段展开收敛时间目标。[完整段](Fuzzy2023-analysis.md#i02) |
| 给参数选择折中 | ESO I06：`The bandwidth of the observer is chosen in accordance with two conflicting aspects, the maximal load capability and the dynamic performance of system.` 前文刚讨论 ESO 大扰动能力。[完整段](ESO2017-analysis.md#i06) |
| 归纳证据类型 | ESO I07 最后一句将列出的水下控制器按 simulation／experiment 分组，承认两种既有验证；下一段再给本方案。[完整原句](ESO2017-analysis.md#i07) |

P05 I06 的剩余输入条件是另一种结尾，P17 I08 则以真实运动执行的设计作用收束。都依赖当前段承担的科学责任。把每段结尾统一改成“however, existing methods cannot ...”会丢掉这些真实推进。

### 8. 保证、能力、设计目的与证据用不同动词和限定语

Fuzzy C02 的完整两句尤其清楚：

<!-- source Fuzzy2023 C02 1 2 -->
> 2) A novel adaptive law is proposed such that the boundedness of all the closed-loop signals can be proved. Then, the assumption that the weight estimation is bounded in recent fixed-time control research [23]–[25] can be relaxed.

主语依次是 adaptive law、boundedness、assumption；动作依次是 proposed、proved、relaxed。不是“新算法使性能更好”这一句的三种改写，而是设计→证明→前提变化。其后一条贡献为：

<!-- source Fuzzy2023 C03 1 1 -->
> 3) The tracking performance of the robot system can achieve practical fixed-time convergence regardless of the initial conditions.

`practical` 与 `regardless of the initial conditions` 共同界定保证。ESO I08 同时区分 `theoretically` 与 `successfully implemented`，ESO C03 的 `carried out experimentally ... to demonstrate` 命名实际比较的证据路径。P05 I06 的 `It has been proven that, for ...` 把前作理论能力附在网格／输入条件下。语言模仿时要继承这些对象与限定的写法，科学内容仍换成当前作者实际能支持的结论。

四篇引言没有统一的“必须报一个提升数字”结尾。P17 说明真实执行的设计效果，ESO 说明实机实现与实验比较，其余包括理论保证和后文章节安排。也不能据此得出所有引言都无需研究结果；这里只说明这四篇的收束由其科学主线和文体决定，不存在固定数值配额。

### 9. 时态与普通用词：借鉴作用，而不是给整节统一替换

P17／P05 文献句经常用 `was proposed/developed/presented` 叙述特定工作；Fuzzy 经常用 `has been proposed`，ESO 则多用 `is proposed/presented`。这说明四篇没有一个可固化的文献时态。具体模型已得结果如 P17 I02 的 `The learned model showed ...` 用过去时，常规工具能力 `can approximate ...` 与当前设计 `we integrate/design ...` 又承担不同时间和陈述责任。[P17 I02](P17-analysis.md#i02)、[Fuzzy I01](Fuzzy2023-analysis.md#i01)、[ESO I03](ESO2017-analysis.md#i03)

反复出现的有效词通常很普通：`model`、`learn`、`generate`、`track`、`estimate`、`approximate`、`compensate for`、`regulate`、`constrain`、`integrate ... into`、`combine ... with`、`be based on`、`be used/employed to`、`due to`、`because of`、`under the assumption that`、`in practice`。成熟之处在于每个动词与科学对象稳定配对，必要时重复对象，前后句不改换责任。`novel`、`powerful`、`significant`、`superior`、`exciting` 也见于原文，但这些评价词本身不解释设计，更不能代替具体信息、条件、比较或保证。

## 四、可复用共性、单篇选择与需要修正的概括

这里的“共性”只指四份范例中重复出现、且有明确作用的写法，不声称样本足以代表全部成熟引言。

| 重复出现的可复用关系 | 跨篇依据 | 不应固化的形式 |
|---|---|---|
| 任务要求落到具体技术责任，而不是只讲应用重要 | P17 I01 的 motion modeling；P05 I02 的沿物面相对运动；Fuzzy I02／I03 的约束／时间；ESO I01／I02 的精度／未知项 | 不要求所有开篇都从应用热度开始，Fuzzy 直接从未知非线性开始 |
| 文献承担可命名的动作、对象和当前主题下的能力 | P17 I03／I04；P05 I02／I07；Fuzzy I02／I03；ESO I03／I06 | 不要求每句 In [xx]，也不要求每篇文献只有一句 |
| 承认能力之后，以相关条件／代价继续推进 | P17 I02／I05；P05 I02／I03／I06；Fuzzy I03；ESO I04／I05 | 不强制贬低全体前作或每段都造 gap |
| 设计先命名改变，再说明其作用／保证对象 | P17 I05／I07；P05 I07／C02；Fuzzy I02／C01–C03；ESO I08／贡献 | 不强制统一 we／被动语态，也不固定三个贡献 |
| 相邻段靠同一对象、任务责任或信息需求相接 | P17 运动模型→跟踪同一轨迹；P05 动力学→NN→权重／激励；Fuzzy 瞬态和时间目标；ESO 扰动→补偿→状态估计 | 不只有单向漏斗，也不要求“上一段不足”是唯一接口 |
| 局部设计可以先出现，再继续解释另一条件或文献位置 | P17 I03／I05／I07；P05 I07；Fuzzy I02 后仍有 I03；ESO I07 后仍解释传感和前作 | 不要求全部相关工作写完才第一次宣布方法 |

单篇特有写法应与其任务一起借鉴：P17 是多示范表征接实际跟踪的双责任系统；P05 是任务条件和估计信息／激励要求的逐层推进；Fuzzy 是两目标分别论证及“假设转证明”的贡献；ESO 是真实传感条件推导联合扰动与速度估计。它们提供不同主线，而不是同一个模板的不同缩写。

回查也要求修正几种过强概括。首先，文献句不全是“某方法解决某问题”：还有理论结论、综述介绍、机制续句与验证续句。其次，段首不总是定义术语，段末也不总是缺口。再次，已有工作常已具备本文关心的部分甚至联合能力，贡献需落在实际条件、实现、信息或证明责任的改变上。最后，四篇原文并非处处同样紧凑：Fuzzy I01 的未来拓扑优化、P05 I05 的 flapping-wing 可理解性介绍、ESO I07 的部分跨系统文献，与各自主要问题联系较松。保留这些源文是为了如实分析；它们不能因“出自范例”就成为通用写作步骤。

原文中的分号、Here、目的／分词前置、former／latter、一些数和用词错误均原样留存；分析同时说明其实际关系。适配作者英文时可选择其中符合作者要求的普通主谓与搭配，不为了复制源文而继承错误，也不把全部原句改造成一套防御性限制句。

本轮产出是来源有据的学习总结。完整性检查只证明来源、原句、分段、句子定位、链接和项目未改范围；不证明总结已落实进 Skill 或能够改善生成效果。现有 Skill、效果测试及历史结论保持原样。工作区开始时已有《核心要求.txt》更新与新增《引言写作方法.txt》，本轮读取并原样保留；项目同步会一并保存这两份既有作者输入。提交同步后停止，交负责人验收。

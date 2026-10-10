# Introduction 默认段落推进写法与真实连续句证据

先沿作者研究的科学主线确定本段要完成的任务，再选择适用的范例段落与连续句关系进行参照、组合和调整。P17 是主要风格锚点；P05、Fuzzy2023、ESO2017 补充相应科学关系的推进方式。实际写作中的对象、事实、条件、比较、设计和保证全部来自作者研究。

本稿学习段落内部的科学组织：本句接住什么，增加什么，怎样让下一句自然继续。以下保留九个基于完整出版原段的英文学习示例，覆盖领域价值进入问题、文献能力与条件、设计理由与作用、设计之间的连接及贡献收束。每段的 A1、A2 等按当前示例句序定位，同一句中的紧密分工、条件或作用一起分析，不把分析出的每项责任都拆成独立句。示例按块标为“原文选取”或“基于原文的适配”；页码与 I／C 编号定位来源，A 编号定位当前示例句。首句的承接对象来自前段或已建立的研究语境，末句则完成本段任务或交接下一段。

这些例子按段落的科学任务调用。先参照[整节详略与篇幅分配](robotics-introduction-section.md#detail-allocation)，再对照各段的详略与密度分析及连续英文。所需句数、信息顺序和段末承担的作用，由作者内容及其前后关系决定。

## 1. 领域价值怎样进入具体研究问题

默认从领域的实际价值或重要性确立研究对象，随后说明当前应用为什么需要某项能力，再把能力需要落到本文要处理的研究环节。每次收窄都保留上一步的对象或目的，让具体问题成为实现领域价值所需的一项责任。

<a id="p17-i01"></a>

### 1.1 P17 I01：制造应用 → 适应性 → 学习 → 运动建模

**本段任务与上下文。** 这是 Introduction 首段。它从机器人在制造等领域的应用进入产品更新所带来的适应性需要，再落到示教学习中的运动建模。下一段 I02 接着讨论 DS／DMP 的运动表示能力。

**P17 I01**; PDF p.1 / 刊页 777 左栏 -> PDF p.1 / 刊页 777 右栏.

**示例段首。** `Recently, robots have been widely applied in various fields, especially in manufacturing.`

**英文学习示例（基于原文的适配）。**

> Recently, robots have been widely applied in various fields, especially in manufacturing. Adaptable robots are required due to the increasingly fast updates of the manufactured products. Hence, it is necessary to develop methods for enhancing robot learning. Robot learning from demonstration (LfD) is a valuable technique to simplify the strategy of robot learning [1], [2]. The human tutor shows the way to complete a task and then the robot learns, via motion modeling, to reproduce the skill. Therefore, it is essential to consider how to model motions effectively.

| 句位 | 本句承担的具体任务 | 接住前一句的什么内容 | 新增什么信息 | 与下一句的关系 |
| --- | --- | --- | --- | --- |
| A1 | 建立机器人研究的实际应用背景，突出制造这一应用场景。 | 作为开篇，确立后续问题所属的领域与用途。 | 机器人已广泛进入实际应用，制造是主要讨论入口。 | A2 在制造场景中说明当前为什么需要适应性。 |
| A2 | 把制造应用转为机器人适应性的现实需要。 | 接住 A1 的制造场景。 | 产品更新加快，使适应性成为所需能力。 | A3 继续说明增强学习怎样服务于这项能力需要。 |
| A3 | 确立增强机器人学习的研究必要性。 | 接住 A2 的适应性需求。 | 需要发展增强机器人学习的方法。 | A4 将广义学习需要落到一种相关学习路线。 |
| A4 | 引入 LfD，并说明它简化机器人学习策略的价值。 | 接住 A3 的学习方法需要。 | 示教学习是一条具有相关能力的既有路线。 | A5 继续说明这条路线怎样使机器人获得技能。 |
| A5 | 解释示教技能复现依赖运动建模这一环节。 | 接住 A4 的 LfD 路线。 | 人演示任务，机器人通过运动建模学习并复现技能。 | A6 从技能复现所依赖的环节提出有效建模问题。 |
| A6 | 将本段收束为如何有效建模运动的具体研究问题。 | 接住 A5 的“通过建模复现技能”。 | 有效运动建模成为随后需要讨论的对象。 | 下一段 I02 可以直接研究 DS／DMP 能提供什么运动表示能力。 |

**详略与信息密度。** 应用背景只展开到适应性需要；LfD 用价值与技能复现两步说明其与运动建模的关系，随后立即提出具体问题。每句完成一次收窄，既不省掉依赖关系，也不反复扩写机器人应用或学习价值。

**段首与段末。** 段首亮出机器人应用及制造场景，段末把同一应用需要交给运动建模。中间的适应性、学习与 LfD 连续解释了为什么讨论范围会落到这里。

**适用的借鉴关系。** 当作者需要从领域用途进入某个关键研究环节时，参照“用途 → 当前能力需要 → 相关路线 → 路线所依赖的科学问题”的连续关系。用作者领域的真实价值、当前需要和研究对象替换这些内容。

<a id="eso-i01"></a>

### 1.2 ESO2017 I01：海洋探索价值 → 高精度控制责任

**本段任务与上下文。** 这是 Introduction 首段。它把水下机器人的海洋探索与科研价值直接联系到数据质量、轨迹跟踪和定点保持。下一段 I02 讨论未知扰动与模型不确定性对控制造成的实际挑战。

**ESO2017 I01**; PDF p.1 / 刊页 6785 左栏 -> PDF p.1 / 刊页 6785 右栏.

**示例段首。** `Underwater robots, including autonomous underwater vehicles (AUVs), remotely operated vehicles (ROVs), and underwater gliders, have been increasingly employed to expand human capabilities in marine resource exploration and marine scientific research.`

**英文学习示例（基于原文的适配）。**

> Underwater robots, including autonomous underwater vehicles (AUVs), remotely operated vehicles (ROVs), and underwater gliders, have been increasingly employed to expand human capabilities in marine resource exploration and marine scientific research. To exploit the full potential benefits provided by underwater robots, a high-precision controller for underwater robots is required to guarantee the quality of the collected data and to secure high precision in trajectory tracking or station keeping [1]–[6].

| 句位 | 本句承担的具体任务 | 接住前一句的什么内容 | 新增什么信息 | 与下一句的关系 |
| --- | --- | --- | --- | --- |
| A1 | 说明水下机器人扩展人类海洋探索与科研能力的领域价值。 | 作为开篇，确立研究对象及其服务的实际活动。 | AUV、ROV 与水下滑翔机属于这一对象范围；共同价值是扩展海洋作业能力。 | A2 说明充分发挥这些能力需要什么控制责任。 |
| A2 | 将领域价值落到高精度控制及其服务的目标。 | 接住 A1 的海洋探索与科研收益。 | 高精度控制要支持数据质量、轨迹跟踪与定点保持。 | 下一段 I02 围绕这些控制目标解释扰动与模型不确定性造成的困难。 |

**详略与信息密度。** 领域价值与控制责任直接相关，两个完整句子已容纳对象范围、用途、所需控制及具体目标。对象列举服务于范围，高精度控制的两个目标在同一句并列；无需把每个目标另扩成一句或一段。

**段首与段末。** 段首明确水下机器人的用途；末句完成从用途到高精度控制的连接，并为下一段的控制障碍分析提供对象。

**适用的借鉴关系。** 当领域价值与本文研究环节之间存在直接依赖时，可以紧接价值说明所需技术能力及其具体目标。句数随需要解释的科学关系决定。

## 2. 文献能力怎样连续展开，并由条件产生新的需要

默认先把相关工作放在同一个科学问题下，说明各自用了什么方法、处理了什么对象、具备什么相关能力。相邻文献可以扩充同一能力方向，也可以补充前一工作的机制或输出。随后根据当前研究需要，明确这组能力成立的条件，或综合它们已经能够提供的能力，为后续设计建立理由。

<a id="p05-i02"></a>

### 2.1 P05 I02：协作操作能力 → 共有抓持条件 → 相对运动需要

**本段任务与上下文。** I01 已说明双臂应用优势及其控制复杂性。本段处理已有协作控制能做什么，以及这些控制的任务条件怎样与表面操作需要发生联系。后段 I03 因而进入双臂相对运动／非对称任务。

**P05 I02**; PDF p.1 / 刊页 1010 右栏.

**示例段首。** `In [9], an adaptive decentralized control scheme was proposed to address the object handling problem of a cooperative robot, where an implicit force control scheme was employed to simultaneously regulate the force and position.`

**英文学习示例（基于原文的适配）。**

> In [9], an adaptive decentralized control scheme was proposed to address the object handling problem of a cooperative robot, where an implicit force control scheme was employed to simultaneously regulate the force and position. In [10], a decentralized control structure for multiple mobile manipulators was developed, where the internal forces were constrained by employing an augmented object model for the multiple systems with a virtual linkage. In [11], the loading problem for multiple manipulators was addressed by analyzing the grasp space of the robot. The adaptive decentralized controller in [9], the decentralized control structure in [10], and the grasp-space analysis method in [11] were developed under the assumption that the object is firmly held by the robotic arms such that no relative motion occurs between the arms and the object. However, in practical applications, such as polishing, grinding, and welding, the robot end-effectors need to operate along the object’s surface, where sliding movements usually occur between the robotic arm and the object [12]–[14].

| 句位 | 本句承担的具体任务 | 接住前文的什么内容 | 新增什么信息 | 与后文的关系 |
| --- | --- | --- | --- | --- |
| A1 | 给 [9] 的操作能力及力／位置控制机制。 | 前段双臂协调控制问题。 | 主句给分散控制，where 接隐式力控制的两个受控量。 | A2 扩充内力控制能力。 |
| A2 | 给 [10] 的控制结构与内力约束手段。 | 同一协作控制方向。 | 多移动机械臂结构及含虚拟连杆的增广物体模型。 | A3 补负载处理能力。 |
| A3 | 给 [11] 的抓持空间负载分析。 | 多机械臂操作问题。 | 另一项相关能力。 | A4 综合共有条件。 |
| A4 | 说明牢固抓持与无相对运动假设。 | 三项已有方法的真实能力。 | 臂与物体间无相对运动这一任务条件。 | A5 联系表面操作需要。 |
| A5 | 连接沿表面操作与臂／物体滑动。 | 前句无相对运动条件。 | 抛光、磨削、焊接中的动作及 where 分句的滑动关系。 | I03 接收相对运动研究需要。 |

**详略与信息密度。** 三项文献各给相关能力；[9]、[10] 的机制用 where 分句随方法出现，随后集中说明共有任务条件与当前滑动需要。较多信息用于能力—条件—任务的对应，表面操作与滑动在同一句相连后交给 I03，不重讲三项方法。

**段首与段末。** 段首直接亮出协作操作的一项具体能力；中间的文献扩充同一操作问题下的能力；段末用应用中的滑动需要把下一段的相对运动问题自然推出。

**适用的借鉴关系。** 当已有方法的任务条件与作者所研究任务不同，参照这段先建立真实能力、再综合共有条件、最后说明当前任务具体需要的推进。方法、能力、条件与应用关系按作者证据替换。

<a id="p17-i04"></a>

### 2.2 P17 I04：多示教信息能力 → 文献机制与输出 → 两类方法的综合价值

**本段任务与上下文。** 前段 I03 已说明最优示教难得、多次示教能够隐含理想轨迹，并提出多次示教整合进一个 DMP 的方向。本段说明概率方法能提供什么相关信息能力。紧接的 I05 明确 DMP／GMM／GMR 组合设计。

**P17 I04**; PDF p.1 / 刊页 777 右栏 -> PDF p.2 / 刊页 778 左栏.

**示例段首。** `Probabilistic approaches have shown good performance in motion encoding [11]–[13].`

**英文学习示例（基于原文的适配）。**

> Probabilistic approaches have shown good performance in motion encoding [11]–[13]. The inherent variability of the demonstrations can be extracted, and thus, more features of the demonstrations can be preserved. In [14], an LfD framework using a Gaussian mixture model (GMM) and a Bernoulli mixture model was used to extract the features from multiple demonstrations. A new motion was generated through Gaussian mixture regression (GMR). In contrast with the DS-based and DMP-based motion-learning methods discussed above, GMM combined with GMR can provide additional motion information for robots when learning from multiple demonstrations. In [3], a learning approach named stable estimator of dynamical systems (SEDS) was proposed for motion modeling, where the unknown function was modeled using GMR. DS-GMR is another method that combines the DS with the statistical learning approach [15]. Both SEDS and DS-GMR exploit the robustness and generalization capability of the DS as well as the excellent learning performance of the probabilistic methods.

| 句位 | 本句承担的具体任务 | 接住前文的什么内容 | 新增什么信息 | 与后文的关系 |
| --- | --- | --- | --- | --- |
| A1 | 明确概率方法的运动编码能力。 | 前段多示教信息整合需要。 | 概率编码这一适用方向。 | A2 解释示教信息价值。 |
| A2 | 解释提取变异怎样保留更多特征。 | 概率运动编码能力。 | 变异提取与特征保留的作用关系。 | A3–A4 给具体实现及输出。 |
| A3 | 给出 [14] 的多示教特征提取框架。 | 示教特征保留需要。 | GMM 与 Bernoulli mixture model 的表示职责。 | A4 继续同一工作的生成环节。 |
| A4 | 说明 [14] 通过 GMR 生成新运动。 | 同一多示教表示。 | 表示进入运动输出。 | A5 综合多示教信息价值。 |
| A5 | 将 GMM／GMR 能力接回运动学习。 | 特征提取与生成。 | 相对前文 DS／DMP 方法的额外运动信息。 | A6–A7 给两类方法结合的依据。 |
| A6 | 在同一句给出 SEDS 的任务与 GMR 职责。 | 动态系统与概率学习的结合需要。 | SEDS 用于运动建模，where 分句交代未知函数由 GMR 建模。 | A7 补另一项结合工作。 |
| A7 | 用 DS-GMR 扩充结合依据。 | SEDS 的组合能力。 | 另一种 DS 与统计学习组合。 | A8 综合共同价值。 |
| A8 | 综合 SEDS 与 DS-GMR 的两类能力。 | 两项结合工作。 | DS 的鲁棒／泛化与概率方法的学习性能。 | I05 据此采用组合设计。 |

**详略与信息密度。** 先用两句说明概率编码为何有价值，再以 [14] 的模型与生成输出继续同一文献；SEDS 的建模任务与 GMR 职责放在一句，DS-GMR 补结合依据，最后综合共同能力。这些细节足以支持 I05 的组合；综合完成后无需再加同义总结。

**段首与段末。** 段首亮出概率运动编码能力，段末完成“动态系统能力＋概率学习能力”的综合，为当前组合设计提供直接依据。

**适用的连续句关系。** A3–A4 展示同一文献先说明模型与任务、再说明生成输出的连续推进；A6–A8 则由两个相关工作进入共同能力的综合。后续写作可以根据本段任务选择其中适用关系，再把方法对象和功能换成作者所需的内容。

## 3. 设计理由怎样进入设计，并接续具体作用

默认围绕一项已经明确的研究需要，把适用方法的能力、必要条件及当前设计的职责连续联系起来。设计出现后，继续说明它对前面那个对象产生什么作用。相关比较可以帮助读者看清设计的采用价值；比较的维度始终服务于本段处理的科学需要。

<a id="fuzzy-i02"></a>

### 3.1 Fuzzy2023 I02：瞬态性能的意义 → 约束能力 → 对称 BLF 的职责

**本段任务与上下文。** 前文已把不确定机器人控制的关注点落到瞬态性能与收敛时间。本段处理瞬态性能这一项需要，并为对称 BLF 建立相关方法依据。后段 I03 处理另一项并列需要：收敛时间。

**Fuzzy2023 I02**; PDF p.1 / 刊页 1041 右栏.

**示例段首。** `In practice, undesirable transient performance may lead to system instability and sometimes even safety problems.`

**英文学习示例（基于原文的适配）。**

> In practice, undesirable transient performance may lead to system instability and sometimes even safety problems. Recently, barrier Lyapunov functions (BLFs) have been widely used to enforce state and output constraints in nonlinear control problems [12]–[16]. In [12], with the exponential-type BLF, a practical event-triggered prescribed-time controller has been proposed for a class of space teleoperation systems. In [14], a new command-filtered fuzzy controller has been proposed for a class of unknown nonlinear systems to handle full-state constraints and finite-time convergence simultaneously. In [16], an adaptive fuzzy leader-following tracking control scheme has been proposed for heterogeneous nonlinear multiagent systems with finite-time output constraints. In this article, a novel symmetric BLF is designed to guarantee the desired transient performance of the robot system.

| 句位 | 本句承担的具体任务 | 接住前一句的什么内容 | 新增什么信息 | 与下一句的关系 |
| --- | --- | --- | --- | --- |
| A1 | 说明不良瞬态性能为什么是需要处理的控制问题。 | 接住前文已经提出的瞬态性能关注。 | 瞬态性能可能关联系统不稳定与安全问题。 | A2 引入能处理状态／输出约束的相关方法方向。 |
| A2 | 确立 BLF 的状态与输出约束能力。 | 接住 A1 对瞬态行为的控制需要。 | BLF 已用于非线性控制中的约束问题。 | A3 开始用具体工作展示这项能力怎样与控制目标结合。 |
| A3 | 给出指数型 BLF 在空间遥操作控制中的使用。 | 接住 A2 的 BLF 约束方向。 | [12] 将指数型 BLF 用于实用事件触发指定时间控制器。 | A4 继续补充约束能力与时间性能相结合的另一项工作。 |
| A4 | 给出全状态约束与有限时间收敛同时处理的能力。 | 接住 A3 的约束与时间性能组合方向，以并列工作扩展相关依据。 | 指令滤波模糊控制在未知非线性系统中同时处理这两项目标。 | A5 再扩充到有限时间输出约束的相关控制工作。 |
| A5 | 给出异构非线性多智能体跟踪中的输出约束能力。 | 接住 A4 的约束控制与有限时间目标。 | 自适应模糊领导者跟随控制支持有限时间输出约束。 | A6 将这些相关能力落实为当前机器人设计承担的职责。 |
| A6 | 提出本文对称 BLF，并明确期望瞬态性能保证。 | 接住 A2–A5 建立的约束方法能力及 A1 的瞬态需要。 | 当前设计是对称 BLF，其作用对象是机器人系统的期望瞬态性能。 | 本段完成这项设计的理由与职责；后段 I03 转入另一项性能需要。 |

**详略与信息密度。** 瞬态问题的意义用一句说明，BLF 能力及三项相关工作为选择建立依据；最后一句即交代对称 BLF 的职责。采用理由充分而职责单一时，这一句设计说明已完成任务，后段转入另一项性能需要。

**段首与段末。** 段首明确瞬态问题的实际意义，段末直接给出响应这项需要的设计及保证。本段在设计职责建立后完成任务，下一段继续处理总体目标中的另一项需要。

**适用的借鉴关系。** 当一项性能需要已有相关控制能力作为依据，可以参照“需要的具体意义 → 相关方法能力与实例 → 当前设计及其职责”的推进。能力与实例的数量、设计出现位置按作者研究的论证需要安排。

<a id="fuzzy-i03"></a>

### 3.2 Fuzzy2023 I03：快速收敛需要 → 有限时间能力 → 初始条件 → 固定时间方向

**本段任务与上下文。** 它紧接 I02 的瞬态讨论，处理与之并列的收敛时间要求。后一段 I04 将 FLS、BLF 与固定时间跟踪汇合到不确定机器人的总体控制目标。

**Fuzzy2023 I03**; PDF p.1 / 刊页 1041 右栏 -> PDF p.2 / 刊页 1042 左栏.

**示例段首。** `In many industrial systems, fast convergence of the system states is required for better control performance.`

**英文学习示例（基于原文的适配）。**

> In many industrial systems, fast convergence of the system states is required for better control performance. Previous studies have focused on the convergence time of the systems [17]–[19]. In [17], an adaptive observer-based fuzzy controller has been proposed for a class of strict-feedback nonlinear systems to achieve finite-time convergence. In [18], an adaptive finite-time sliding-mode control scheme has been proposed for a class of nonlinear systems with some matched uncertainties. Nevertheless, for existing finite-time control schemes, the convergence time of the systems is always related to the initial conditions, which are sometimes unavailable. To improve the control performance, the fixed-time control schemes have been proposed and applied in the nonlinear control community [20]–[22]. In [20], a novel fixed-time adaptive fuzzy control scheme combined with the BLF technique has been proposed for uncertain nonstrict-feedback nonlinear systems. In [21], an adaptive event-based fixed-time control scheme has been proposed for active vehicle suspension systems, and the predefined constraints can be guaranteed.

| 句位 | 本句承担的具体任务 | 接住前文的什么内容 | 新增什么信息 | 与后文的关系 |
| --- | --- | --- | --- | --- |
| A1 | 说明快速状态收敛的性能需要。 | 总体目标中的另一项并列责任。 | 工业控制为何关注收敛速度。 | A2 给已有研究方向。 |
| A2 | 确认收敛时间研究基础。 | 快速收敛需要。 | [17]–[19] 定位相关工作。 | A3–A4 给具体能力及系统条件。 |
| A3 | 给观察器模糊控制的有限时间能力。 | 收敛时间研究。 | 严格反馈系统及有限时间收敛。 | A4 补同一能力的另一方法。 |
| A4 | 给有限时间滑模控制及匹配不确定性条件。 | 已有有限时间能力。 | 另一方法与系统范围。 | A5 综合时间依赖条件。 |
| A5 | 在同一句连接初始条件依赖与可得性。 | 已有有限时间方案。 | 收敛时间依赖初始条件，which 保留有时不可得这一条件。 | A6 引入固定时间方向。 |
| A6 | 给用于改善性能的固定时间方向。 | 初始条件依赖。 | 固定时间方案的提出与应用。 | A7 联系约束能力。 |
| A7 | 给固定时间模糊控制与 BLF 结合的能力。 | 固定时间方向及前段约束需要。 | 不确定非严格反馈系统中的结合。 | A8 补联合能力实例。 |
| A8 | 在同一句给悬架控制及预设约束保证。 | 固定时间与约束联合方向。 | [21] 的方法、系统及相应保证。 | 理由已建立，I04 汇合总体目标。 |

**详略与信息密度。** 有限时间能力之后，要保留收敛时间的初始条件依赖及条件有时不可得，不能只说收敛快慢。依赖与可得性在同一句连接；固定时间／BLF 与悬架实例继续支撑联合能力，末句方法和约束保证相连后收束。

**段首与段末。** 段首直接亮出快速收敛这一责任，中间由有限时间能力推进到初始条件，再进入固定时间方向；段末用时间与约束联合能力为总体设计提供依据。

**适用的连续句关系。** A3–A6 可以用于“已有相关能力 → 能力成立或性能依赖的条件 → 适合当前需要的新方向”；A7–A8 可以用于连接两项已经建立的性能要求。瞬态与时间是并列需要，实际写作按作者工作中各项需要的真实关系组合。

<a id="p17-i05"></a>

### 3.3 P17 I05：已有两类能力 → 组合设计 → 多示教作用 → 相关比较

**本段任务与上下文。** I04 已建立 DS 与概率学习的组合价值；本段明确当前 DMP／GMM／GMR 怎样利用这些能力，并以相关 DMP 学习方法继续说明采用价值。后段 I06 转向已生成运动的轨迹执行需要。

**P17 I05**; PDF p.2 / 刊页 778 左栏.

**示例段首。** `To take advantage of the performance of the DS and the probabilistic approach, we integrate DMP and GMM into our robot learning system, where the nonlinear function of DMP is modeled with GMM and its estimate is retrieved through GMR.`

**英文学习示例（基于原文的适配）。**

> To take advantage of the performance of the DS and the probabilistic approach, we integrate DMP and GMM into our robot learning system, where the nonlinear function of DMP is modeled with GMM and its estimate is retrieved through GMR. The DMP motion model integrating GMM and GMR enables the robot to extract more features of the motions from multiple demonstrations and to generate motions that synthesize these features. In [16], the original DMP was learned using locally weighted regression (LWR), and in [17], locally weighted projection regression (LWPR) was employed to optimize the bandwidth of each kernel of LWR. Despite the added complexity of the learning procedure, LWR and LWPR enable the DMP to learn from only one demonstration. Reservoir computing [18] is another method used to approximate the nonlinear function of DMP, but its computing efficiency is less than that of GMR.

| 句位 | 本句承担的具体任务 | 接住前文的什么内容 | 新增什么信息 | 与后文的关系 |
| --- | --- | --- | --- | --- |
| A1 | 由两类能力引出组合，并分清建模与回归职责。 | I04 已建立的 DS 与概率学习价值。 | we integrate 给组合动作；where 中 GMM 建模 DMP 非线性函数，GMR 取得同一函数的估计。 | A2 写组合作用。 |
| A2 | 说明多示教特征提取与运动合成作用。 | 同一 DMP／GMM／GMR 组合。 | 提取的特征进入生成运动。 | A3 给同一函数学习任务的比较对象。 |
| A3 | 在同一句交代 LWR 学习与 LWPR 优化。 | DMP 函数学习对象。 | [16] 对应 LWR；[17] 对应 LWR 核带宽优化，责任各自明确。 | A4 综合代价与示教量。 |
| A4 | 交代学习复杂性与单次示教能力。 | LWR／LWPR 学习途径。 | 复杂性代价及可利用的示教量。 | A5 补计算效率维度。 |
| A5 | 比较 reservoir computing 与 GMR 的效率。 | 同一 DMP 非线性函数逼近。 | 指定方法和指标的差别。 | 本段完成采用价值，I06 转向执行需要。 |

**详略与信息密度。** 主要设计信息集中在前两句：组合理由与两项不同职责在 where 中清楚分配，下一句给特征提取与运动合成作用。后面只在同一函数学习任务下比较示教量与效率；比较完成即转入执行需要，不继续解释 GMM／GMR 算法。

**段首与段末。** 段首把前段的两类能力立即落实为当前组合及分工，下一句接续它的具体作用。后面的比较继续围绕示教信息利用与函数学习，本段因此完成运动生成设计的采用理由。

**适用的连续句关系。** A1–A2 可直接参照为“设计及功能对象 → 对前文需要的具体作用”；A3–A5 补充相关比较，明确这项作用相对所比较方法的价值。按作者证据选择比较对象与维度，保留设计和作用之间的对应。

## 4. 多个设计怎样通过科学责任与输入输出连接

默认围绕同一个研究目的说明各部分的职责：前一部分生成或估计什么，后一部分为什么需要接收它、继续完成什么任务。已有控制或模型保证可以与这些职责联系起来，让读者理解多个设计怎样共同达成目标。

<a id="p17-i07"></a>

### 4.1 P17 I07：跟踪控制职责 → 保证 → 两部分框架 → 生成与执行的接口

**本段任务与上下文。** 前段 I06 已说明模仿性能还依赖准确跟踪，未知负载等使动力学难以预知，并讨论逼近控制与 RBFNN 的适用性。本段给出当前控制职责，再连回前面已经建立的运动生成设计。下一段 I08 收束完整学习框架的贡献。

**P17 I07**; PDF p.2 / 刊页 778 右栏.

**示例段首。** `In this paper, an NN-based controller is designed to guarantee the tracking performance of the manipulator in joint space, where RBFNN is employed to approximate the nonlinear functions of the robot dynamics.`

**英文学习示例（基于原文的适配）。**

> In this paper, an NN-based controller is designed to guarantee the tracking performance of the manipulator in joint space, where RBFNN is employed to approximate the nonlinear functions of the robot dynamics. The stability of the NN-based controller is guaranteed by the Lyapunov stability theory. The robot learning system consists of the motion generation component and the trajectory tracking component (Fig. 1). The motion generation component utilizes the DMP-based motion model to learn and generalize motion skills, which are represented as a set of trajectories in joint space. The trajectory tracking component employs the adaptive controller to track the joint-space trajectories generated by the motion generation component, and RBFNN is incorporated into the controller to compensate for the uncertain robot dynamics.

| 句位 | 本句承担的具体任务 | 接住前文的什么内容 | 新增什么信息 | 与后文的关系 |
| --- | --- | --- | --- | --- |
| A1 | 给出关节空间跟踪职责及动力学逼近手段。 | I06 的未知动力学下准确执行需要。 | 控制器保证跟踪，where 中 RBFNN 逼近动力学非线性函数。 | A2 给稳定性依据。 |
| A2 | 给控制器稳定性依据。 | 同一 NN 控制器。 | Lyapunov 稳定性理论。 | A3 将控制器放回系统。 |
| A3 | 说明系统的两项组成责任。 | 已建立的生成与跟踪设计。 | 运动生成和轨迹跟踪两部分。 | A4 说明第一部分职责及输出。 |
| A4 | 连接运动技能学习／泛化与轨迹表示。 | 运动生成部分。 | DMP 模型学习和泛化技能，which 指这些技能的关节空间轨迹表示。 | A5 让跟踪部分接收同一轨迹。 |
| A5 | 连接轨迹跟踪与动力学补偿。 | 生成部分输出的关节空间轨迹。 | 跟踪部分用自适应控制器接收轨迹；独立具名的 RBFNN 补偿动力学。 | 接口已清楚，I08 收束框架贡献。 |

**详略与信息密度。** 五个连续句子足以说明控制职责、稳定性、系统组成、生成输出及跟踪接收。where 指明逼近职责，which 将已命名技能接到轨迹表示，最后的并列分句保留 RBFNN 的补偿责任；接口清楚后进入贡献，避免重复技能或模块的全称来扩写同一责任。

**段首与段末。** 段首明确本段要给出的跟踪控制及其对象，段末把前文运动模型生成的轨迹交给控制器，并说明补偿怎样服务执行。本段完成控制部分与整个学习框架的连接。

**适用的连续句关系。** A3–A5 可用于“共同目标下的组成 → 第一部分的职责与输出 → 第二部分接收同一输出并完成后续责任”。信息传递对象要明确，各部分的功能与保证按作者系统的真实关系表达。

## 5. 贡献怎样回收前文对象、设计职责与作用

先明确贡献覆盖的研究对象及责任，再说明设计对相应研究需要的作用。当前结尾用贡献引导句和编号列项逐项回收这些关系；P17 I08 提供各项内部的职责、比较与作用承接，整节层 P05／Fuzzy 段落组和表达层 E25／E26 提供引导及列项的真实实现。每个比较对象、条件或补充职责都应接回前文已建立的讨论。

<a id="p17-i08"></a>

### 5.1 P17 I08：完整框架范围 → 相关模型比较 → 执行补偿职责 → 研究目的

**本段任务与上下文。** 前文 I03–I05 已建立多示教运动生成，I06–I07 已建立未知动力学下的轨迹执行。本段把这些设计与责任收束为完整机器人学习框架的贡献；后段 I09 为章节导航。

**P17 I08**; PDF p.2 / 刊页 778 右栏.

**示例段首。** `We present a novel and complete robot learning framework that considers the performance of both motion generation and trajectory tracking.`

**英文学习示例（基于原文的适配）。**

> We present a novel and complete robot learning framework that considers the performance of both motion generation and trajectory tracking. The SEDS presented in [3] is similar to our DMP-based model. However, the constraints that guarantee the stability of SEDS are derived using Lyapunov theory and increase the complexity of learning the SEDS motion model. In contrast to [3] and [25] which considered only motion modeling, our robot learning system is enhanced by an NN-based controller, and the effect of dynamic environments on the robot can be compensated by neural learning. This design enables the robot to perform the learned motions steadily and more robustly in the real world.

| 句位 | 本句承担的具体任务 | 接住前文的什么内容 | 新增什么信息 | 与后文的关系 |
| --- | --- | --- | --- | --- |
| A1 | 确定完整框架的两项责任范围。 | I07 已连接的生成与执行。 | 同时考虑运动生成与轨迹跟踪。 | A2 给相关模型比较对象。 |
| A2 | 明确 SEDS 与当前 DMP 模型的相关性。 | 运动生成责任。 | SEDS 是指定比较对象。 | A3 说明其约束及学习代价。 |
| A3 | 连接 SEDS 稳定性约束依据与学习复杂性。 | 同一 SEDS 模型。 | 约束由 Lyapunov 理论导出，且这些约束增加 SEDS 学习复杂性。 | A4 接回完整框架的执行责任。 |
| A4 | 连接 NN 控制增补与环境影响补偿。 | 框架范围及前文不确定动力学。 | [3]、[25] 的比较范围仍是运动建模；神经学习承担补偿。 | A5 回到学得运动的执行。 |
| A5 | 以稳定、稳健执行收束贡献。 | A4 的控制与补偿及整个框架。 | This design 指已建立的生成／跟踪设计；作用对象仍是学得运动。 | 科学贡献已完成；当前结尾借 P05／Fuzzy 实现编号列项。 |

**详略与信息密度。** 回收框架范围后，只展开与实际差别有关的 SEDS 条件及跟踪补偿；约束依据与学习代价、控制增补与补偿各保持连续。This design 的对象在上下文已清楚，最后一句即可收束可靠执行的作用。当前编号贡献借用这些实质关系，逐项完成职责与作用便结束，不重述整套设计。

**段首与段末。** 段首确定完整框架的两项责任，段末回到机器人执行学得运动这一研究目的。中间的模型条件比较与控制补偿说明，使总体贡献具有来自前文的具体内容。

**适用的连续句关系。** A2–A3 保持比较对象连续，并补充它的相关条件；A4–A5 把本文设计的职责接到最终作用。实际写作使用作者工作的比较对象、职责差别与有证据支持的作用，贡献段由这些关系收束。

## 参照、组合与调整

先明确本段在整节中承担的科学任务，再找能表达同一关系的连续句。例如，文献方法与后续作用可参照 P17 I04 的 A3–A4；能力与任务条件的连接可参照 P05 I02；设计及其作用可参照 P17 I05 的 A1–A2；多个部分的输出与后续职责可参照 P17 I07 的 A3–A5。保留所选关系需要的上下文，把每句内容换成作者研究中对应的对象、事实、条件与结论。

段首清楚亮出本段的对象、问题、方向或责任，后续句持续发展这个对象；段末可以确立下一项需要、综合已有能力、完成当前设计的作用说明，或收束贡献。根据当前论证选择其中适用的完成方式，使相邻段落保持对象与问题的自然交接。

句序随科学依赖关系调整：相关工作的并列扩充、同一工作的机制与作用接续、条件限定、设计与作用以及输入输出联系，各自保留其真实关系。段落推进与适用英文示例共同作为参照，科学含义由作者研究决定。

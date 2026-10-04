# Robotics Introduction examples — B15–B18

Use this reference through `robotics-writing-examples.md` for robotics-centred
Introduction drafting, restructuring, polishing, translation, and feedback.
Keep the requesting skill's workflow, `robotics-main-text.md` section decisions,
and `scientific-expression.md` generation and context checks. The cards supply
actual English realizations, not another workflow or a fixed Introduction form.

## Selection

先确定作者当前部分的科学对象、任务条件、设计理由、作用及可支持的保证。
以 **B15／P17／A06 为默认表达锚点**，选读与当前内容相接的段落组、连续英文
及分析，再按下表选补充。先读整节推进以理解段落任务，使用时回到具体英文，
不能只借“背景—缺口—贡献”等标签。不要求每次读取全部卡片或源 PDF。
保留适合作者内容的整段组织、相邻句逻辑、主谓结构及普通搭配；每句话的科学
对象、条件、因果、比较和结论都换成作者自己的。补充英文与 P17 的明确对象、
普通完整主谓和理由接作用的习惯协调，不强制相同组件、段数或技术。

| 当前要表达的关系 | 选读卡片／英文单位 | 借鉴的实际动作 |
|---|---|---|
| 应用要求落到学习／控制责任，两个环节以同一输出交接 | [B15](#b15)，I01、I03–I08 中适用组 | 先解释表征选择，再把任务效果接到执行条件；命名输出、跟踪对象及补偿对象 |
| 前作任务条件与当前接触／运动条件不同 | [B16](#b16)，I02–I03 | 承认能力，归纳所列前作共同条件，再说明任务为何改变该条件 |
| 参数／权重学习依赖何种信息与激励 | [B16](#b16)，I06–I07 | 区分跟踪和估计对象，保留前作局部能力，逐项说明改进及条件 |
| 两个性能目标共同成立，某性质从假设变为证明 | [B17](#b17)，I02–I03、C02–C03 | 分别动机约束与时间要求，说明设计作用和保证依据改变 |
| 物理不确定项、控制补偿及可测／不可测信息相接 | [B18](#b18)，I02、I05–I08 | 解释来源和控制代价，接估计—补偿路径，再从真实传感条件推出设计 |

来源为四篇出版论文的 §I，不含摘要、脚注、图注或 §II。下面 I 为卡内段落号，
C 为贡献条目号，均为来源定位辅助，并非论文原有段落编号。跨栏／跨页段落
接回原段；引文仅规范连字、行末断词与空白，保留原文错误供选择辨别。
完整段落或明确标注的连续句组保持原有顺序；摘录之间不冒充相邻句。
题名、期刊、DOI、页码和段首足以回查；本地 PDF 链接仅供可选核对。
卡中已有英文、分析和边界可以脱离项目报告及原 PDF 使用。

## B15

### P17／A06 — 默认表达锚点，表征选择接实际执行

**来源。** *Robot Learning System Based on Adaptive Neural Control and Dynamic
Movement Primitives*，TNNLS 30(3), 2019，DOI `10.1109/TNNLS.2018.2852711`。
§I，PDF p.1–2／印刷页777–778；[可选本地 PDF][P17]。
该引言九段。已有 B01 仍负责双组件全文及证据接口；本卡提供引言整节与具体英文。

**整节推进。**

| 段落／页栏／段首 | 真实内部展开及与下一段的联系 |
|---|---|
| I01，p.1 左→右，`RECENTLY` | 产品更新需要适应性机器人 → 学习 → LfD 人示教 → motion modeling，落到一个设计责任 |
| I02，p.1 右，`The dynamic system` | DS 的稳定／扩展／抗扰能力 → 一项 DS 学习需要较多数据 → DMP 的示教需求与弹簧阻尼能力，给选择依据 |
| I03，p.1 右，`DMPs` | 击打、序列、风格调节用途 → 最优示教难获得 → 作者把多示教整合成一个 DMP；设计已开始出现 |
| I04，p.1 右→p.2 左，`Probabilistic approaches` | 概率方法保留变异／特征 → GMM／GMR 分工 → SEDS、DS-GMR 已结合 DS 与统计学习；建立可继承能力 |
| I05，p.2 左，`To take advantage` | 当前非线性函数的建模与估计 → 综合多示教特征 → 所列学习方式的示教范围／复杂度／效率比较 |
| I06，p.2 左→右，`The imitation performance` | 任务效果还取决于跟踪 → 未知载荷妨碍精确动力学 → 函数近似／NN → RBFNN 选择理由 |
| I07，p.2 右，`In this paper` | joint-space 控制与近似对象 → 分析保证 → 两组件 → 生成轨迹 → 跟踪同一轨迹并补偿不确定动力学 |
| I08，p.2 右，`Here` | 同时考虑生成与跟踪 → 与特定前作比较 → 控制器补偿执行环境影响 → 学得运动实际执行 |
| I09，p.2 右，`The remainder` | DMP、学习、控制及稳定性、实验、结论的 roadmap，与设计依赖相接 |

**应用需要如何落到问题，I01 全段，p.1 左→右。**

> RECENTLY, robots have been widely applied in various fields, especially in manufacturing. Adaptable robots are required due to the increasingly fast updates of the manufactured products. Hence, it is necessary to develop methods for enhancing robot learning. Robot learning from demonstration (LfD) is a valuable technique to simplify the strategy of robot learning [1], [2]. The human tutor shows the way to complete a task and then the robot learns, via motion modeling, to reproduce the skill. Therefore, it is essential to consider how to model motions effectively.

`Adaptable robots are required due to ...` 命名应用变化及要求，后续
`shows ... then ... learns` 解释 LfD，`how to model motions effectively`
把引言开篇落到技术责任。作者若有其他任务，需要用其真实需求与过程替换，
不能照搬制造业变化或硬造示教模块。

**多示教选择及可继承的表征能力，I03–I04 两个完整连续段，p.1 右→p.2 左。**

> DMPs have been often employed to solve robot learning problems because of their flexibility. In [7], DMPs were modified to model fast movement inherent in hitting motion. Another study used reinforcement learning to combine DMP sequences so that the robot could perform more complex tasks [8]. While both these studies employed multiple DMPs to compose a complete action, another study [9] used multiple DMPs to model style-adaptive trajectory, where the style of the generated motion could be changed by modulating the weight parameters that were coupled with the goals. As mentioned in [10], optimal demonstration is difficult to obtain and multiple demonstrations can encode the ideal trajectory implicitly. Therefore, we consider integrating multiple demonstrations into one DMP model in this paper.

> Probabilistic approaches have shown good performance in motion encoding [11]–[13]. The inherent variability of the demonstrations can be extracted, and thus, more features of the demonstrations can be preserved. In [14], an LfD framework using a Gaussian mixture model (GMM) and a Bernoulli mixture model was used to extract the features from multiple demonstrations. A new motion was generated through Gaussian mixture regression (GMR). In contrast with the above-mentioned methods, GMM combined with GMR can provide additional motion information for robots when learning from multiple demonstrations. In [3], a learning approach named stable estimator of dynamical systems (SEDS) was proposed for motion modeling, where an unknown function was modeled using GMR. DS-GMR is another method that combines the DS with the statistical learning approach [15]. Both methods exploit the robustness and generalization capability of the DS as well as the excellent learning performance of the probabilistic methods.

I03 先建立 DMP 用途，最后两句才解释“最优示教难获得—多示教编码—当前选择”。
`multiple DMPs`、`multiple demonstrations`、`one DMP model` 是不同对象。
I04 承认现有概率方法及 DS 组合的能力，为 I05 的选择服务；它不需要另造一个
段末缺口。多示教／概率方法事实不能借给没有相同科学关系的作者稿。

**具体设计接修改作用，I05 全段，p.2 左，上接 I04、下接执行问题 I06。**

> To take advantage of the performance of the DS and the probabilistic approach, we integrate DMP and GMM into our proposed system, where the nonlinear function of DMP is modeled with GMM and its estimate is retrieved through GMR. This modification enables the robot to extract more features of the motions from multiple demonstrations and to generate motions that synthesize these features. The original DMP was learned using the locally weighted regression (LWR) [16], and the locally weighted projection regression [17] was employed to optimize the bandwidth of each kernel of LWR. Despite the added complexity of the learning procedure, these methods enable the DMP to learn from only one demonstration. Reservoir computing [18] is another method used to approximate the nonlinear function, but its computing efficiency is less than that of GMR.

`we integrate ... into ...` 说设计动作，`is modeled with GMM` 与
`its estimate is retrieved through GMR` 分别说建模和估计。
后句 `This modification enables ...` 接同一修改，再说特征提取及生成用途。
可以直接用这组句间推进和普通搭配，但动作及其作用对象必须是作者自己的。
此处 `only one demonstration` 限定所比较的学习方式，不是所有 DMP 技术；
复杂度和效率比较也不构成作者方法的普遍优势。

**学习结果到执行条件，I06–I07 两个完整连续段，p.2 左→右。**

> The imitation performance of robots also depends on the accuracy of the trajectory tracking controller that involves the robot dynamics. Generally, a model-based control performs better if the model is accurate enough [19]. However, an accurate dynamic model of a manipulator cannot be obtained in advance due to some uncertainties, e.g., unknown payload. The approximation-based controllers have been designed to overcome such uncertainties. They utilize function approximation tools to learn the nonlinear characteristics of the robot dynamics. NNs have been widely used in controller design because of their approximation ability [20]–[22]. In [23], the backpropagation NN (BPNN) was utilized to approximate the unknown nonlinear function in the model of the vibration suppression device, while in [24], the radial basis function NN (RBFNN) was utilized to approximate the unknown nonlinearity of the telerobot system. Compared to BPNN, the learning procedure of RBFNN is based on local approximation; thus, RBFNN can avoid getting stuck in the local optimum and has a faster convergence rate. Besides, the number of hidden layer units of RBFNN can be adaptively adjusted during the training phase, making NN more flexible and adaptive. Therefore, RBFNN is more appropriate for the design of real-time control.

> In this paper, an NN-based controller is designed to guarantee the tracking performance of the manipulator in joint space, where RBFNN is employed to approximate the nonlinear functions of the robot dynamics. The stability of the controller is guaranteed by the Lyapunov stability theory. As shown in Fig. 1, the robot learning system consists of the motion generation component and the trajectory tracking component. The former utilizes the motion model based on DMP to learn and generalize motion skills; these, in turn, are represented as a set of trajectories in joint space. The latter employs the adaptive controller to track the trajectories generated from the former, and RBFNN is incorporated to compensate for the uncertain dynamics.

I06 的 `also depends on` 把完整任务效果接到此前未解释的跟踪责任。
准确模型的作用、`cannot be obtained in advance due to ...` 的原因、近似方案
和具体技术选择连续相接，不能缩成“系统鲁棒性好”。RBFNN 避免局部最优及
收敛较快是源文的强断言，不自动成为作者方法的选择依据。

I07 按控制器责任及近似对象、保证、组成、输出、使用该输出推进。
`trajectories in joint space` 与 `track the trajectories generated ...`
保持中间科学对象，末句 `compensate for the uncertain dynamics` 给补偿命名。
适用于作者确有的规划／学习到执行链，不固化双组件、joint space 或 NN。
迁移时用明确组件名替代 former／latter，按既有表达要求拆分分号。
`is guaranteed by the Lyapunov stability theory` 需换成作者实际证明对象与
结论；引用分析工具本身不建立保证。

**综合收束，I08 全段，p.2 右。**

> Here, we present a novel and complete robot learning framework that considers the performance of both motion generation and trajectory tracking. The SEDS presented in [3] is similar to our DMP-based model. However, the constraints that guarantee the stability of SEDS are derived by the Lyapunov theory that increases the complexity of the learning. In contrast to [3] and [25] which considered only motion modeling, our system is enhanced by an NN-based controller and the effect caused by the dynamic environments can be compensated by neural learning. This design enables the robot to perform the learned motions steadily and more robustly in the real world.

可以保留“系统责任—具体前作范围—新增设计—任务作用”的整段逻辑。
不用 Here、novel、complete 装饰当前贡献；前作只考虑 motion modeling 的判断
限于所列工作。该节在 I03／I05／I07 逐步出现设计，再在 I08 综合，
不强制所有相关工作排在方法之前。普通主谓、反复命名对象、理由接作用是
默认风格倾向，九段和双组件只是此论文的组织。

## B16

### P05／A07 — 任务条件到信息及学习条件

**来源。** *Composite-Learning-Based Adaptive Neural Control for Dual-Arm Robots
With Relative Motion*，TNNLS 33(3), 2022，DOI `10.1109/TNNLS.2020.3037795`。
§I，PDF p.1–2／印刷页1010–1011；[可选本地 PDF][P05]。
九个 prose 段及三条贡献，与 A07 摘要卡分工不同。

**整节推进。**

| 段落／页栏／段首 | 真实内部展开及段落组的作用 |
|---|---|
| I01，p.1 左→右，`RECENTLY` | 双臂任务优势 → 应用 → 控制／规划复杂性 → 控制技术需求 |
| I02，p.1 右，`An adaptive` | 三项控制能力 → 共同的 firmly held／no relative motion 假设 → 当前沿表面滑动任务改变条件 |
| I03，p.1 右，`In this respect` | 相对运动／asymmetric bimanual task → 已有方法 → 已知动力学假定与接触力分析缺口 |
| I04，p.1 右→p.2 左，`The dynamic model` | 模型作用 → 抓取物动力学难预先获得 → 模型不确定性补偿／NN |
| I05，p.2 左，`A fuzzy` | NN 应用 → 跟踪误差收敛与理想权重收敛区分 → 学习问题 |
| I06，p.2 左，`In our recent` | LIP 估计到 NN 权重 → PE 严格性的技术原因 → PPE 局部能力 → recurrence／弱激励限制 |
| I07，p.2 左→右，`The work` | 误差信息进入更新的已有思想 → 当前任务控制 → 分别比较 PPE 条件与误差信息使用 |
| I08／C01–03，p.2 右，`The objective` | 任务目标及三项贡献：未知动力学任务框架、估计误差信息更新、激励要求放松 |
| I09，p.2 右，`In the following` | 建模、控制及分析、仿真、结论；没有实机验证承诺 |

**前作能力—共同条件—当前任务差异，I02–I03 两个完整连续段，p.1 右。**

> An adaptive decentralized control scheme was proposed to address the object handling problem of a cooperative robot, where an implicit force control scheme was employed to simultaneously regulate the force and position [9]. In [10], a decentralized control structure for multiple mobile manipulators was developed, where the internal forces were constrained by employing an augmented object model for the multiple systems with a virtual linkage. In [11], the loading problem for multiple manipulators was addressed by analyzing the grasp space of the robot. Note that the abovementioned controllers were developed under the assumption that the object is firmly held by the robotic arms such that no relative motion occurred between the arms and the objects. However, in practical applications, such as polishing, grinding, and welding, the robot end-effectors need to operate along the object’s surface, where sliding movements usually happened between the robotic arm and the object [12]–[14].

> In this respect, the coordination control of dual-arm robots with relative motion deserves further investigation. The relative motion is also known as the asymmetric bimanual task. In [15], a relative impedance controller was developed by using a relative Jacobian method such that the dual-arm system can be treated as a single-arm robotic system. In [16], a brain-actuated control architecture was proposed for dual-arm robots to perform the asymmetric bimanual task, where electroencephalogram signals and visual stimulation were employed to send control command through a brain–machine interface. In these works, however, the controllers were designed under the assumption that the robot dynamics are fully available, while the stability analysis of the contact force between the robotic arm and the object was not given.

I02 前三句命名 force／position、internal forces、loading／grasp space 的不同
控制动作；`under the assumption that ... such that ...` 归纳所列工作的共享条件。
任务句的 `need to operate along the object's surface` 改变这一条件，才接 I03。
`firmly held` 不是任意 contact，relative motion 发生在手臂／工具与对象之间，
不能含混成双臂彼此运动。I03 承认已有目标任务研究，随后限定 dynamics fully
available 及 contact-force analysis；不能改写成全部前作均未研究相对运动。
原文时态／数的一些不齐不需复制，保留具体关系与 `were developed under
the assumption that` 等合适句型。

**保留前作局部能力再说改进，I06–I07 两个完整连续段，p.2 左→右。**

> In our recent work [39], a filtered operation was presented to control the robotic arm with finite-time convergence under a linear-in-parameter (LIP) robotic dynamic model. Nevertheless, the guaranteed convergence of the NN weights is more difficult. It is well known that the persistent excitation (PE) condition is important to guarantee the estimation convergence [40]. However, in practice, it is very stringent to ensure the PE condition of neural networks due to the sparse characteristics of the NN regressor vector. Recent research of neural networks in [41] presented a partial persistent excitation (PPE) condition instead of the traditional PE condition. It has been proven that, for the radial basis function neural network (RBFNN) defined in a regular lattice, neural nodes could be partially activated for any recurrent NN inputs trajectory remained in this local region [41]. In the subsequent work [42], this idea was employed for the control design of nonlinear strict-feedback systems to guarantee the system stability and accurate NN approximation. However, the NN inputs still need to satisfy the condition of recurrent trajectory, and a small input excitation strength may lead to slow learning speed.

> The work in [43] indicates that parameter convergence can be improved if certain information of the estimation error can be integrated into the adaptation. In [44], a novel parameter estimation law was proposed for a robotic system with unknown dynamics by using a sliding mode technique and a finite-time estimator. In [45], the estimation error was integrated into the adaptation scheme of a class of nonlinear systems to achieve the convergence of NN weights. Motivated by the abovementioned idea, in this article, we develop a composite learning controller for the dual-arm robot to perform bimanual relative motion tasks. To the best of our knowledge, few studies have investigated the learning control in the frame of the dual-arm robot systems subject to relative motion and unknown dynamics. Moreover, different from the work in [46], a PPE condition is also introduced in the estimation scheme to achieve a relaxation of the requirement of the PE condition. In comparison to the method in [45], the estimation error of the NN weights is properly expressed and employed to enhance the approximation of the neural network.

`Nevertheless` 从 LIP 估计转到 NN 权重，`due to the sparse characteristics
of the NN regressor vector` 解释 PE 难满足的原因。PPE 仍限定 regular lattice、
局部节点及 recurrent trajectory；段末解释剩余输入条件／学习速度。
I07 从估计误差信息进入 adaptation 的已有思路移到作者任务，
`few studies` 限定双臂、relative motion、unknown dynamics 的交集。
与 [46] 的条件比较、与 [45] 的信息使用比较分别成立，不能合成全体前作缺失。
这组适用于作者确有的技术继承及条件／信息用法改变，无须隐藏改进性质。

**贡献列表的三项不同责任，C01–C03，p.2 右。**

> 1) A novel neural control framework is developed for dual-arm robot systems to perform asymmetric bimanual tasks with no prior knowledge of the dynamics.

> 2) A novel composite learning algorithm is designed for NN weights adaptation such that information of the estimate errors could be appropriately integrated into the adaptation law to improve the estimation performance.

> 3) A partial persistent condition is introduced for the adaptation of NN weights such that the requirement of conventional PE condition can be greatly relaxed.

`with no prior knowledge of the dynamics` 只涉及先验动力学需求，不等于不需要
几何、传感或任务模型。`information ... integrated into the adaptation law`
要明确作者实际可用的误差信息及更新对象，不能暗示未知真实权重误差可直接测量。
`relaxation ... PE condition` 不是无激励要求。
必要正文边界：§III-C Theorem 1，PDF p.6／1015，要求 PPE，跟踪误差及权重
估计误差收敛到零邻域，接触力误差有界；Remark 6，p.7／1016，解释误差信息
在分析中的作用。引言 convergence 不可照抄成无条件全权重精确收敛。
I05 的 `NN control synthesizes` 及权重不收敛最终不稳定的概括不作为通用规则。
保留误差、权重及条件的重复命名，协调到 P17 的普通明确英文。

## B17

### Fuzzy2023／A02 — 联合性能目标与保证依据

**来源。** *Fixed-Time Fuzzy Control of Uncertain Robots With Guaranteed Transient
Performance*，TFS 31(3), 2023，DOI `10.1109/TFUZZ.2022.3194373`。
§I，PDF p.1–2／印刷页1041–1042；[可选本地 PDF][Fuzzy2023]。
四个 prose 段及三条贡献，无独立 roadmap。

**整节推进。**

| 段落／页栏／段首 | 真实展开及取舍 |
|---|---|
| I01，p.1 左→右，`FOR` | 时变参数／扰动 → NN／FLS 近似能力及前作 → 已有 fixed-time＋user-defined performance → 计算量与未来拓扑优化旁支 → 联合目标覆盖判断 |
| I02，p.1 右，`In practice` | 瞬态差的安全影响 → BLF 约束能力 → 前作 → 当前 symmetric BLF 的作用；局部设计已出现 |
| I03，p.1 右→p.2 左，`In many` | 快收敛需求 → finite-time → 时间与初始条件相关 → fixed-time 及已有约束能力 |
| I04／C01–03，p.2 左，`Motivated` | FLS／BLF 问题范围 → 瞬态约束、证明有界以放松假设、practical fixed-time tracking 三种贡献责任 |

**约束与收敛时间分别为何必要，I02–I03 两个完整连续段，p.1 右→p.2 左。**

> In practice, the undesirable transient performance may lead to the system instability, even the system safety problems sometimes. Recently, the barrier Lyapunov functions (BLFs) have been widely used to achieve the state and output constraints in the nonlinear control problems [12]–[16]. In [12], with the exponential-type BLF, a practical event-triggered prescribed-time controller has been proposed for a class of space teleoperation systems. In [14], a new command filtered fuzzy controller has been proposed for a class of unknown nonlinear systems to handle full-state constraints and finite-time convergence simultaneously. In [16], an adaptive fuzzy leader-following tracking control scheme has been proposed for heterogeneous nonlinear multiagent systems with finite-time output constraints. In this article, a novel symmetric BLF is designed to guarantee the desired transient performance of the robot system.

> In many industrial systems, the system states are required to achieve fast convergence speed for better control performance. There have been some proposed research works focused on the convergence time of the systems [17]–[19]. In [17], an adaptive observer-based fuzzy controller has been proposed for a class of strict-feedback nonlinear systems to achieve finite-time convergence. In [18], an adaptive finite-time sliding-mode control scheme has been proposed for a class of nonlinear systems with some matched uncertainties. Nevertheless, for the existing finite-time control schemes, the convergence time of the systems is always related to the initial conditions, which are sometimes unavailable. To improve the control performance, the fixed-time control schemes have been proposed and applied in the nonlinear control community [20]–[22]. In [20], a novel fixed-time adaptive fuzzy control scheme combined with the BLF technique has been proposed for uncertain nonstrict-feedback nonlinear systems. In [21], an adaptive event-based fixed-time control scheme has been proposed for the active vehicle suspension systems, and the predefined constraints can be guaranteed.

I02 按后果、可用工具、三个具对象／约束类型的例子、当前工具作用推进。
`is designed to guarantee the desired transient performance` 是设计—作用句，
作者需有实际设计、保证对象及前提。prescribed-time、finite-time、fixed-time，
full-state constraints 和 output constraints 不能互换。
I03 的 `Nevertheless ... related to the initial conditions` 给转向 fixed-time
一个技术理由，段末承认 fixed-time＋BLF 和 fixed-time＋constraints 已有能力。

I01 内另一前作及段尾判断原句如下，**二者之间原文有其他句子，非连续句组**：

> In [8], an adaptive fuzzy control scheme has been proposed for robotic systems to achieve fixed-time convergence and user-defined performance simultaneously.

> Moreover, the desired transient performance and convergence time are rarely discussed simultaneously in most of the existing fuzzy control schemes.

所以 `rarely ... in most ...` 不能成为“没有前作同时处理这两项目标”或作者
“首次”的依据。I01 的未来 FLS topology optimization 与 `which is exciting`
旁支不必迁移；保留最能解释当前贡献的充分证据。

**从设计到证明，再到假设改变，C02–C03，p.2 左。**

> 2) A novel adaptive law is proposed such that the boundedness of all the closed-loop signals can be proved. Then, the assumption that the weight estimation is bounded in recent fixed-time control research [23]–[25] can be relaxed.

> 3) The tracking performance of the robot system can achieve practical fixed-time convergence regardless of the initial conditions.

`such that ... can be proved` 说新律为何需要，`Then, the assumption ... can be
relaxed` 说它改变哪项保证依据。适用于作者确有“原先假定的性质现在可证明”
的贡献，不预设作者也有权重估计。boundedness、constraint satisfaction 与
convergence 是不同性质；保留 `practical`，不改成有限时间精确零误差。
正文 §II-A（p.2／1042）目标为进入预定义零邻域；§III Theorem 1
（p.4／1044）要求 `−βi(0) < ei(0) < βi(0)`；Remark 2（p.6／1046）明确
区分 proved 和 assumed。时间界不依赖初始条件不取消初始可行性。
源文 Combined／Motivated 分词开头及贡献条目分号保留为原文证据，
作者句子按共用表达核心用完整主谓及普通句子实现；novel 取决于真实比较。
列表与无 roadmap 是有效组织变体，不为统一形式而补造内容。

## B18

### ESO2017／A04 — 物理不确定性到补偿与信息条件

**来源。** *Extended State Observer-Based Integral Sliding Mode Control for an
Underwater Robot With Unknown Disturbances and Uncertain Nonlinearities*，
TIE 64(8), 2017，DOI `10.1109/TIE.2017.2694410`。
§I，PDF p.1–3／印刷页6785–6787；[可选本地 PDF][ESO2017]。
九个 prose 段及三条贡献；贡献列表跨至 p.3，排除 Fig.1 图注。

**整节推进。**

| 段落／页栏／段首 | 真实展开及设计依赖 |
|---|---|
| I01，p.1 左→右，`UNDERWATER` | 类型／应用 → 数据质量及 tracking／station keeping 的精确控制需求 |
| I02，p.1 右，`In practice` | 外扰的海况／缆索来源；模型不确定性的参数获取误差／姿态变化，分别解释两类来源 |
| I03，p.1 右，`Several methods` | adaptive、robust、observer 路线 → NN／FLS 应用、学习参数数量及验证类型 |
| I04，p.2 左，`Although` | 单句独立段：近似优势仍有实际调参困难，与 I03 共同完成能力／限制比较 |
| I05，p.2 左，`As an effective` | SMC／ISMC 能力、积分项作用 → 抖振代价 → 已有缓解方案 → 大不确定界且无补偿的问题 → 补偿需求 |
| I06，p.2 左，`Another approach` | observer 估计 → control 用估计补偿 → observer 类型／能力 → bandwidth 取舍 |
| I07，p.2 右，`In this paper` | 当前装置可测信息 → 无直接速度 → 微分后果 → output feedback／状态估计 → 再述前作及验证类型 |
| I08／C01–03，p.2 右→p.3 左，`In this paper` | MIMO-ESO 估计、界自适应、控制分析／两部分 → 实机实现 → 估计、跟踪及实验比较贡献 |
| I09，p.3 左，`The remainder` | model、ESO、ISMC、experiments、conclusion，章序接设计依赖 |

**问题物理来源，I02 全段，p.1 右。**

> In practice, there are a number of technical challenges in the control of an underwater robot, such as the unknown external disturbances and model uncertainties. The unknown disturbances in practical oceanic environments include waves, tides, currents, and upward or downward streams. For control design of ROVs, the external force caused by the cable that connects with the depot ship should also be considered. The model uncertainties of an underwater robot are usually caused by the inaccurate hydrodynamic coefficients, which are calculated through the computational fluid dynamics (CFD) methods or towing tank experimental data analysis. During the process of performing a task, different attitude of the robot will also cause the variation of the hydrodynamic coefficient.

两类对象分别展开，不用“复杂环境”笼统替代。`caused by` 说物理来源，
`calculated through` 说参数获取方式，`cause the variation of` 说任务中的变化。
作者系统若无缆索、无相同参数变化，就不继承这些例子；可以直接选用其
“两类问题各自给出必要来源”的整段组织和动作搭配。

**补偿为何必要，I05 尾部四个连续句，p.2 左；前文已介绍 SMC／ISMC 能力及抖振代价。**

> To reduce the chattering, several methods, such as the high-order sliding-mode controller [24], [25], disturbance compensation method [26], [27], and terminal sliding controller [28] have been proposed. In [26], a free chattering SMC is presented via an adaptive term, which continuously compensates for the unknown system dynamics of an ROV. In practice, sometimes, the upper bound of the uncertainties may be large and the SMC without a compensator will cause serious chattering. Therefore, it is necessary to design a compensator for the external disturbance to reduce chattering.

保留已有缓解方法及补偿前作，再限定 `upper bound ... may be large` 与
`SMC without a compensator` 才得设计后果。`to reduce chattering` 是用途，
不是全部 SMC 失效或当前设计无条件消除抖振的保证。

**估计到控制使用，I06 开头两个连续句，p.2 左，后文列相关 observer 研究与取舍。**

> Another approach dealing with the unknown disturbance is to design an observer to estimate the unknown external disturbance of a robot, followed by the control design to compensate for the estimated disturbance. Such disturbance observers include sliding mode observer [12], [29], high-gain observer [30], [31], and extended state observer (ESO) [13], [32].

`estimate the unknown external disturbance` 接 controller 用估计生成补偿输入。
补偿的物理对象与用于补偿的估计信息要分清；作者若估计状态或合并不确定项，
需按实际对象命名。Such disturbance observers 限定这类 observer，不泛称全部。

**实际可测量信息到设计需求，I07 开头六个连续句，p.2 右；后文继续状态估计研究及仿真／实验分类。**

> In this paper, we design an adaptive sliding mode-based controller for a general type of underwater robots, and experiment is carried on a test bed for underwater object grasping. Onboard sensors, including a depth sensor and an inertial measurement unit (IMU), are equipped to measure the depth and attitude of the robot. The position of the underwater robot is measured by an external vision positioning system (VPS), and some white lightings are equipped on the robot, which can be captured by the VPS to calculate the position of the robot. In such a case, there is no direct measurement of velocity of the robot. Then output feedback is required for our work as the direct differential of the position information may degrade the control performance. In such case, observes are always used to estimate the unmeasured states of the robot [5], [33].

depth／attitude／position 的测量接 velocity 未直接测量，再接微分可能带来的
控制后果及 output-feedback 需求。直接借鉴 `is measured by`、`there is no
direct measurement of`、`is required ... as ...` 的顺序和搭配，让作者的传感
信息解释设计。灯光与装置枝节按贡献需要取舍；`observes`、`white lightings`、
`experiment is carried` 等源文错误或生硬表达不继承。
仿真与实验是验证类型，不据此判定前作无效。

**设计、保证与实现收束，I08 全段，p.2 右。**

> In this paper, a disturbance compensation approach is utilized to eliminate the chattering based on multiple-input and multiple-output extend-state-observer (MIMO-ESO) with a simple structure. Motivated by the ESO model [32] and the high-gain observer [39], a MIMO-ESO is proposed to estimate the unknown disturbances and the unmeasured states. The bounds of the uncertainties are also estimated using the adaptive control technique. The Lyapunov analysis is involved to design the final control law. The proposed controller in this paper includes two parts, namely the equivalent controller and the switch controller, which guarantees the trajectory tracking error converge to zero theoretically. The proposed controller is successfully implemented on an underwater robot propelled by six thrusters. The main contributions can be summarized as follows.

`is proposed to estimate`、`are also estimated`、`includes two parts`、
`is ... implemented on` 分别承担估计、界估计、组成和实机实现，不混成一个
robust performance。源文的 eliminate chattering、converge to zero 不能
直接借给作者；正文 §II（p.3／6787）有 nominal matrices 和 bias，
`H = Hd + Hun` 区分外扰和模型不确定性，§III 的 extended state 使用 Hd。
§IV Theorem 1（p.6／6790）依赖 Assumptions 1–2 及增益条件，§V
（p.8／6792）列出所用 nominal hydrodynamic parameters。因此 ESO 不等于
全部模型免需求，也不能自动把所有不确定项归到同一估计量。

源文 C03（p.3／6787）把 PD 写成 `potential difference`，这是原文术语错误。
§V 的比例／微分增益和位置微分与比例微分控制一致；迁移时仍依据作者实际
控制器确认名称及类别，不由缩写猜展开。Lyapunov、实机比较、误差收敛
分别有自己的对象与范围，不能互相代替证据。
该节把当前装置条件接回前作研究、再收束方法，不需要把全部文献强移到最前。

## Cross-card use

这四张卡在 Section 层保留真实推进；在 Paragraph 层提供完整展开；在相邻句、
Sentence 及 Phrase／Word 层给出可直接利用的英文及科学对象关系。
全文层的接口可与已有 B01 等对照，不由引言卡推断其他章节或证据已成立。
作者若有表征—执行链，用 B15；主要差异为任务／学习条件，用 B16；
联合性能与保证依据，用 B17；关键为物理来源及可测信息，用 B18。
补充可以局部组合，但不累加成一篇超长引言，也不强制相同段末 gap、
三条贡献、roadmap 或验证清单。源文的专属技术、假设、结论和语言问题
不会因是主要参考便成为作者内容。按共用检查回到实际句子和上下文，
保留已经清楚且符合作者表达要求的变体。

[P17]: <../../../文献资料/Robot_Learning_System_Based_on_Adaptive_Neural_Control_and_Dynamic_Movement_Primitives.pdf>
[P05]: <../../../文献资料/Composite-Learning-Based_Adaptive_Neural_Control_for_Dual-Arm_Robots_With_Relative_Motion.pdf>
[Fuzzy2023]: <../../../文献资料/Fixed-Time_Fuzzy_Control_of_Uncertain_Robots_With_Guaranteed_Transient_Performance.pdf>
[ESO2017]: <../../../文献资料/Extended_State_Observer-Based_Integral_Sliding_Mode_Control_for_an_Underwater_Robot_With_Unknown_Disturbances_and_Uncertain_Nonlinearities.pdf>

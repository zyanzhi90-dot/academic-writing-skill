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

整节主线与段落任务由作者研究自主确定；下列真实科学链用于理解范例如何
安排依赖。按当前段落任务选读完整英文及其逐句表，S 号按该段原句顺序计数，
连续句摘录另注明范围。选定的句式须连同上下文读取，再筛选、组合和调整。
Writing 用它形成段落及相邻段递进，Polishing 用同一材料复核作者首稿的
科学关系和具体表达，均沿既有工作流。无需加载项目分析报告或全部逐句表。

| 当前句子要承担的作用 | 回到哪组真实英文及逐句说明 |
|---|---|
| 段首亮出对象、观点或另一责任 | B15 I01 S01–S02、I03 S01、I06 S01；B17 I02 S01／I03 S01；B18 I02 S01 |
| 文献的方法、对象、机制或理论能力 | B15 I03 S02–S04、I04 S03–S08；B16 I02 S01–S03、I06 S05–S07、I07 S01–S03；B18 I06 S03–S07 |
| 比较、条件、限制及其具体后果 | B15 I05 S03–S05、I06 S02–S03；B16 I02 S04–S05、I03 S05、I06 S08／I07 S06–S07；B17 I03 S05–S08 |
| 设计动作紧接机制与作用 | B15 I05 S01–S02、I07 S01；B16 I07 S04／C02；B17 I02 S06／C02；B18 I08 S01–S03 |
| 输出交给下一动作或另一段 | B15 I06 S01→I07、I07 S03–S05；B18 I06 S06–S07→I07 S02–S06 |
| 段末综合、提出需要、保留条件或收束能力 | B15 I01 S06、I03 S05–S06、I04 S08；B16 I06 S08；B17 I03 S07–S08；B18 I06 S09 |

表内不同作用可由同一句承担。选用 `In [..]`、研究／方法主体、信息主体或
`we` 时，看谁实际执行什么动作、作用于什么对象；不是统一套被动文献句。
来源中的 Here、分词／动名词起句、分号及生硬表达仍按共用表达核心筛选，
采用符合作者要求的完整主谓、明确科学对象和普通句子。

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

**科学链。** 产品更新要求机器人适应 → 示教经运动建模重现技能 → DS／DMP
提供可用运动表示 → 最优示教难得，多示教可保留运动信息 → 用 GMM 建模
DMP 非线性函数、GMR 检索估计，综合多示教生成运动 → 重现效果还依赖跟踪，
未知载荷妨碍预知动力学 → RBFNN 近似动力学，控制器跟踪生成的同一关节轨迹
→ 生成与跟踪共同承担真实执行。整节先建立表征责任，再接执行责任。

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

| I01 句 | 主语—动作—对象及连续推进 |
|---|---|
| S01 | `robots have been widely applied in ...` 命名应用对象，范围从 fields 落到 manufacturing。 |
| S02 | `Adaptable robots are required due to ...` 以所需机器人属性为主语，把产品更新接到适应性要求。 |
| S03 | `it is necessary to develop methods for enhancing robot learning` 从要求推出学习方法的责任；Hence 依赖前句理由。 |
| S04 | `Robot learning from demonstration ... is a valuable technique to simplify ...` 命名当前工具及其用途。 |
| S05 | `The human tutor shows ... then the robot learns ... to reproduce the skill` 换主体以交接示教信息；motion modeling 明确中间过程。 |
| S06 | `it is essential to consider how to model motions effectively` 从该过程收束为建模问题，下一段才比较可用表示。 |

**多示教选择及可继承的表征能力，I03–I04 两个完整连续段，p.1 右→p.2 左。**

> DMPs have been often employed to solve robot learning problems because of their flexibility. In [7], DMPs were modified to model fast movement inherent in hitting motion. Another study used reinforcement learning to combine DMP sequences so that the robot could perform more complex tasks [8]. While both these studies employed multiple DMPs to compose a complete action, another study [9] used multiple DMPs to model style-adaptive trajectory, where the style of the generated motion could be changed by modulating the weight parameters that were coupled with the goals. As mentioned in [10], optimal demonstration is difficult to obtain and multiple demonstrations can encode the ideal trajectory implicitly. Therefore, we consider integrating multiple demonstrations into one DMP model in this paper.

> Probabilistic approaches have shown good performance in motion encoding [11]–[13]. The inherent variability of the demonstrations can be extracted, and thus, more features of the demonstrations can be preserved. In [14], an LfD framework using a Gaussian mixture model (GMM) and a Bernoulli mixture model was used to extract the features from multiple demonstrations. A new motion was generated through Gaussian mixture regression (GMR). In contrast with the above-mentioned methods, GMM combined with GMR can provide additional motion information for robots when learning from multiple demonstrations. In [3], a learning approach named stable estimator of dynamical systems (SEDS) was proposed for motion modeling, where an unknown function was modeled using GMR. DS-GMR is another method that combines the DS with the statistical learning approach [15]. Both methods exploit the robustness and generalization capability of the DS as well as the excellent learning performance of the probabilistic methods.

I03 先建立 DMP 用途，最后两句才解释“最优示教难获得—多示教编码—当前选择”。
`multiple DMPs`、`multiple demonstrations`、`one DMP model` 是不同对象。
I04 承认现有概率方法及 DS 组合的能力，为 I05 的选择服务；它不需要另造一个
段末缺口。多示教／概率方法事实不能借给没有相同科学关系的作者稿。

| 原句 | 句内实现与相邻句推进 |
|---|---|
| I03 S01 | `DMPs have been often employed to solve ... because of their flexibility` 用技术主体开段，先给被采用的能力理由。 |
| I03 S02 | `In [7], DMPs were modified to model ...` 动作 modified 及目的 model fast movement 明确，不只说 used。 |
| I03 S03 | `Another study used reinforcement learning to combine DMP sequences so that ...` 研究为主语，组合为机制，复杂任务为用途；与上句换一个有区别的应用。 |
| I03 S04 | `While both these studies employed multiple DMPs ... another study ... used ...` 归纳两项共同表示，再给风格调节例子；where 从句解释权重与 goals 的作用。 |
| I03 S05 | `optimal demonstration is difficult to obtain and multiple demonstrations can encode ...` 从用途转向示教选择，困难与可用信息共同提供理由。 |
| I03 S06 | `we consider integrating multiple demonstrations into one DMP model` 将这些信息交给当前表示设计，下一段需解释如何保留它们。 |
| I04 S01 | `Probabilistic approaches have shown good performance in motion encoding` 接前段待保留的信息，亮出可用方法。 |
| I04 S02 | `variability ... can be extracted ... features ... can be preserved` 同一批示教的变异信息经提取后保留；thus 连接具体信息作用。 |
| I04 S03 | `an LfD framework using ... was used to extract ...` 给多示教特征提取的方法实现。 |
| I04 S04 | `A new motion was generated through ... GMR` 接上句同一框架，继续解释生成，不另开无关文献。 |
| I04 S05 | `GMM combined with GMR can provide additional motion information ... when learning from multiple demonstrations` 按信息能力比较，保留使用条件。 |
| I04 S06 | `a learning approach named ... was proposed for motion modeling, where ... was modeled using GMR` 命名 SEDS，再给内部未知函数建模动作。 |
| I04 S07 | `DS-GMR is another method that combines ...` 引入同类组合，不把组合思想当作本文首次。 |
| I04 S08 | `Both methods exploit ... as well as ...` 综合两类已有能力，交给下一段当前实现；段末可以承认可继承能力。 |

**具体设计接修改作用，I05 全段，p.2 左，上接 I04、下接执行问题 I06。**

> To take advantage of the performance of the DS and the probabilistic approach, we integrate DMP and GMM into our proposed system, where the nonlinear function of DMP is modeled with GMM and its estimate is retrieved through GMR. This modification enables the robot to extract more features of the motions from multiple demonstrations and to generate motions that synthesize these features. The original DMP was learned using the locally weighted regression (LWR) [16], and the locally weighted projection regression [17] was employed to optimize the bandwidth of each kernel of LWR. Despite the added complexity of the learning procedure, these methods enable the DMP to learn from only one demonstration. Reservoir computing [18] is another method used to approximate the nonlinear function, but its computing efficiency is less than that of GMR.

`we integrate ... into ...` 说设计动作，`is modeled with GMM` 与
`its estimate is retrieved through GMR` 分别说建模和估计。
后句 `This modification enables ...` 接同一修改，再说特征提取及生成用途。
可以直接用这组句间推进和普通搭配，但动作及其作用对象必须是作者自己的。
此处 `only one demonstration` 限定所比较的学习方式，不是所有 DMP 技术；
复杂度和效率比较也不构成作者方法的普遍优势。

| I05 句 | 主语、动作与承接 |
|---|---|
| S01 | `we integrate DMP and GMM into ...` 接 I04 两类能力；where 内 `the nonlinear function ... is modeled with ...` 与 `its estimate is retrieved through ...` 分列表示对象和估计信息。 |
| S02 | `This modification enables the robot to extract ... and to generate ...` 主语接同一修改，机器人提取特征再生成综合特征的运动，作用紧跟机制。 |
| S03 | `The original DMP was learned using ...` 与 `... was employed to optimize the bandwidth ...` 回到所比较的原方案，分别给学习与核带宽优化。 |
| S04 | `these methods enable the DMP to learn from only one demonstration` 把所列学习方式共同归纳，Despite 接复杂度代价，only 限定示教数。 |
| S05 | `Reservoir computing ... is another method used to approximate ... but its computing efficiency is less than that of GMR` 保留近似同一函数的能力，只比较计算效率。 |

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

| 原句 | 连续推进及可选表达 |
|---|---|
| I06 S01 | `The imitation performance ... also depends on the accuracy of ...` 重复整体任务效果，用 also depends on 加入执行责任，接回 I05 生成。 |
| I06 S02 | `a model-based control performs better if the model is accurate enough` 先承认准确模型的能力，if 保留其成立条件。 |
| I06 S03 | `an accurate dynamic model ... cannot be obtained in advance due to ... unknown payload` 对同一模型说明不可预知的具体原因，建立替代路线的依据。 |
| I06 S04 | `The approximation-based controllers have been designed to overcome such uncertainties` 提供已有替代路线，尚未直接跳到 RBFNN。 |
| I06 S05 | `They utilize function approximation tools to learn the nonlinear characteristics ...` 续讲这些控制器的机制；作者表达直接命名控制器类别。 |
| I06 S06 | `NNs have been widely used in controller design because of their approximation ability` 从函数近似工具选到 NN，以能力说明选用理由。 |
| I06 S07 | `BPNN was utilized to approximate ... while ... RBFNN was utilized to approximate ...` 两例均保留模型非线性与系统对象，while 在这里并列方法应用。 |
| I06 S08 | `the learning procedure of RBFNN is based on local approximation` 后接源文关于局部最优／收敛的判断；比较建立在指定学习机制上。 |
| I06 S09 | `the number of hidden layer units ... can be adaptively adjusted during ...` 再给结构可调的能力，不把 Besides 当无对象的优点堆叠。 |
| I06 S10 | `RBFNN is more appropriate for the design of real-time control` 汇总本段选择理由，交给 I07 的具体控制责任；此判断需作者证据支持。 |
| I07 S01 | `an NN-based controller is designed to guarantee ... in joint space` 先给控制责任，where 内 `RBFNN is employed to approximate ...` 说明动力学近似。 |
| I07 S02 | `The stability of the controller is guaranteed by ...` 接同一控制器的分析保证，与生成能力分开；按作者真实证明调整。 |
| I07 S03 | `the robot learning system consists of ... and ...` 在两项责任已解释后给组成。 |
| I07 S04 | `The former utilizes the motion model ... to learn and generalize ...` 并接 `are represented as a set of trajectories in joint space`，交出具体轨迹。 |
| I07 S05 | `The latter employs the adaptive controller to track the trajectories generated from the former` 接同一轨迹，`RBFNN is incorporated to compensate for ...` 给近似器的执行作用。 |

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

**科学链。** 双臂协作具有载荷／空间优势，协调控制与路径规划也更复杂
→ 紧持物体的控制条件不对应工具沿物面滑动 → 相对运动控制已有研究仍要求
已知动力学且缺接触力分析 → 抓取物动力学难预知，采用 NN 补偿 → 跟踪误差
收敛与 NN 权重估计收敛是不同责任 → 稀疏回归使 PE 严格，PPE 有局部能力，
仍有重复输入／学习速度要求 → 估计误差信息进入复合学习更新，在未知动力学
相对运动任务中采用 PPE → 分列任务框架、学习信息和激励条件的贡献。

| 段落／页栏／段首 | 真实内部展开及段落组的作用 |
|---|---|
| I01，p.1 左→右，`RECENTLY` | 双臂优势引出应用；协调控制／规划复杂性引出控制研究，两项并列构成任务背景 |
| I02，p.1 右，`An adaptive` | 三项控制能力 → 共同的 firmly held／no relative motion 假设 → 当前沿表面滑动任务改变条件 |
| I03，p.1 右，`In this respect` | 相对运动／asymmetric bimanual task → 已有方法 → 已知动力学假定与接触力分析缺口 |
| I04，p.1 右→p.2 左，`The dynamic model` | 模型作用 → 抓取物动力学难预先获得 → 模型不确定性补偿／NN |
| I05，p.2 左，`A fuzzy` | NN 应用 → 跟踪误差收敛与理想权重收敛区分 → 学习问题 |
| I06，p.2 左，`In our recent` | LIP 估计到 NN 权重 → PE 严格性的技术原因 → PPE 局部能力 → recurrence／弱激励限制 |
| I07，p.2 左→右，`The work` | 误差信息进入更新的已有思想 → 当前任务控制 → 分别比较 PPE 条件与误差信息使用 |
| I08／C01–03，p.2 右，`The objective` | 任务目标及三项贡献：未知动力学任务框架、估计误差信息更新、激励要求放松 |
| I09，p.2 右，`In the following` | 建模、控制及分析、仿真、结论；没有实机验证承诺 |

**优势与控制挑战并列，I01 全段，p.1 左→右。**

> RECENTLY, coordination control of dual-arm robots has received increasing attention due to its superiority compared with traditional single-arm robot systems, including stronger payload capability, larger workspace, and more flexibility. Thus, the dual-arm robots have been involved in many high technology applications, such as intelligent assembly, out-space repairing, and elderly people assistance [1]–[3]. However, controlling the dual-arm robots is challenging due to the increase of complexity in motion control and path planning. Therefore, advanced control technologies have been extensively studied for dual-arm robots in past decades [4]–[11].

S01–S02 用优势解释关注与应用；S03 的 `is challenging due to ... complexity
in motion control and path planning` 另行解释控制困难；S04 从该困难接控制
研究。However 在两项判断间转向，控制复杂性的原因由 S03 自己给出。
源文 controlling 起句按作者要求选成明确科学主语的普通句子。

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

| 原句 | 句内实现与连续推进 |
|---|---|
| I02 S01 | `An adaptive decentralized control scheme was proposed to address the object handling problem ...` 命名方案与任务；where 内 force control `was employed to simultaneously regulate the force and position` 给具体能力。 |
| I02 S02 | `a decentralized control structure ... was developed` 后接 `the internal forces were constrained by employing ...`，换到内力约束，以模型说明机制。 |
| I02 S03 | `the loading problem ... was addressed by analyzing the grasp space ...` 再给载荷问题的分析途径；前三句各有动作与对象。 |
| I02 S04 | `the abovementioned controllers were developed under the assumption that ... such that ...` 归纳这三项的紧持条件及无相对运动关系。 |
| I02 S05 | `the robot end-effectors need to operate along the object's surface` 以末端执行器为主语，应用解释沿表面滑动为何必要，交给 I03。 |
| I03 S01 | `the coordination control ... with relative motion deserves further investigation` 接前段改变的条件，亮出本段对象。 |
| I03 S02 | `The relative motion is also known as the asymmetric bimanual task` 建立文献术语对应。 |
| I03 S03 | `a relative impedance controller was developed by using a relative Jacobian method such that ...` 给方法和降为单臂处理的建模作用。 |
| I03 S04 | `a brain-actuated control architecture was proposed ... to perform ...` 后续 EEG／visual stimulation 通过 interface 送命令，说明另一实现。 |
| I03 S05 | `In these works ... under the assumption that ... fully available, while ... analysis ... was not given` 对这两项分别限定动力学先验和接触力分析，交给下一段模型信息问题。 |

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

| 原句 | 科学推进与具体表达选择 |
|---|---|
| I06 S01 | `a filtered operation was presented to control ... with finite-time convergence under ... LIP ...` 先承认前作在指定模型下的能力。 |
| I06 S02 | `the guaranteed convergence of the NN weights is more difficult` 将对象改为 NN 权重，接 I05 的估计责任。 |
| I06 S03 | `the ... PE condition is important to guarantee the estimation convergence` 给权重估计所需条件。 |
| I06 S04 | `it is very stringent to ensure ... due to the sparse characteristics of the NN regressor vector` 用稀疏回归解释严格性，不止报一个限制标签。 |
| I06 S05 | `Recent research ... presented a ... PPE condition` 先承认已有条件进展。 |
| I06 S06 | `It has been proven that, for ... defined in a regular lattice, neural nodes could be partially activated ...` 给局部结果及 recurrent 输入范围，保留 for 条件。 |
| I06 S07 | `In the subsequent work ... this idea was employed ... to guarantee ...` 同一思想继续用于稳定性及准确近似；idea 的所指是前述 PPE。 |
| I06 S08 | `the NN inputs still need to satisfy ... recurrent trajectory` 后接 `a small input excitation strength may lead to slow learning speed`，将剩余条件与可能代价分开，交给 I07 信息更新路线。 |
| I07 S01 | `The work in [43] indicates that parameter convergence can be improved if ... estimation error ... integrated into ... adaptation` 研究结论作主语，if 给信息使用条件。 |
| I07 S02 | `a ... parameter estimation law was proposed ... by using ...` 给未知动力学系统的估计实现。 |
| I07 S03 | `the estimation error was integrated into the adaptation scheme ... to achieve ... NN weights` 以误差信息为主语，明确进入更新及学习对象。 |
| I07 S04 | `we develop a composite learning controller ... to perform bimanual relative motion tasks` 把前述思想用于作者任务；源文 Motivated 起句按作者要求调整。 |
| I07 S05 | `few studies have investigated ... subject to relative motion and unknown dynamics` 限定当前任务与信息条件交集，不制造普遍空白。 |
| I07 S06 | `a PPE condition is also introduced in the estimation scheme to achieve a relaxation ...` 针对 [46] 改变激励要求，introduced in 命名引入位置。 |
| I07 S07 | `the estimation error of the NN weights is properly expressed and employed to enhance ...` 针对 [45] 改变信息表示及使用，expressed／employed 不是同一动作。 |

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

**科学链。** 参数变化／外扰形成未知非线性 → NN／FLS 可近似，已有工作也已
涉及 fixed-time 与用户性能 → 本文关注瞬态约束和收敛时间两项责任 → 不良瞬态
有安全后果，BLF 可约束，设计 symmetric BLF → 快收敛另有任务需要，finite-time
时间依赖初值，转向 fixed-time 并承认已有约束组合 → 在 FLS／BLF 机器人跟踪
中设计约束工具、自适应律并证明有界性，放松既有假定，给 practical fixed-time
保证。I01 计算量／未来拓扑优化为单篇旁支，按作者主线取舍。

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

| 原句 | 主语、动作与连续推进 |
|---|---|
| I02 S01 | `the undesirable transient performance may lead to ...` 段首亮出不良瞬态的可能安全后果，建立约束责任。 |
| I02 S02 | `the ... BLFs have been widely used to achieve the state and output constraints ...` 引入工具及约束对象。 |
| I02 S03 | `with the exponential-type BLF, a ... controller has been proposed for ...` 给 prescribed-time 方案和空间遥操作对象。 |
| I02 S04 | `a ... fuzzy controller has been proposed ... to handle full-state constraints and finite-time convergence simultaneously` 明确保留前作的联合能力。 |
| I02 S05 | `an adaptive fuzzy ... scheme has been proposed for ... with finite-time output constraints` 再给输出约束与系统类型。 |
| I02 S06 | `a ... symmetric BLF is designed to guarantee the desired transient performance ...` 当前工具为主语，设计紧接作用，下一段解释另一时间责任。 |
| I03 S01 | `the system states are required to achieve fast convergence speed for better control performance` 用状态与速度要求开段，接整体控制目标。 |
| I03 S02 | `research works focused on the convergence time ...` 将该要求交给具体时间研究。 |
| I03 S03 | `an adaptive observer-based fuzzy controller has been proposed ... to achieve finite-time convergence` 给可用 finite-time 方法及 strict-feedback 对象。 |
| I03 S04 | `an adaptive finite-time sliding-mode control scheme has been proposed ... with some matched uncertainties` 补另一方法，保留不确定性类型。 |
| I03 S05 | `the convergence time ... is always related to the initial conditions, which are sometimes unavailable` 明确转向理由；依赖初值与初值信息不可得是两个相接事实。 |
| I03 S06 | `the fixed-time control schemes have been proposed and applied ...` 因此前作引入 fixed-time，尚不是宣布本文独有。 |
| I03 S07 | `a ... fixed-time adaptive fuzzy control scheme combined with the BLF technique has been proposed ...` 承认已有工具组合及 nonstrict-feedback 条件。 |
| I03 S08 | `an ... fixed-time control scheme has been proposed ... and the predefined constraints can be guaranteed` 承认已有约束保证，以能力收尾再转当前方案范围。 |

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

C02 的 S01 是 `A ... adaptive law is proposed such that the boundedness of all
the closed-loop signals can be proved`：律的设计交给有界性证明。S02 的
`Then, the assumption that the weight estimation is bounded ... can be relaxed`
接该证明改变先验假设。C03 换到 `The tracking performance ... can achieve
practical fixed-time convergence regardless of the initial conditions`，主语与
保证对象转为跟踪性能。这组适合证明责任改变，不能仅靠设计句声称放松假设。

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

**科学链。** 海洋任务的数据质量／运动精度需要准确控制 → 海况及缆索外扰、
流体参数误差及姿态变化形成未知项 → NN／FLS 可近似但实际调参困难 →
SMC／ISMC 有抗扰与跟踪能力，抖振有能耗／平滑性代价 → 扰动估计供控制补偿，
已有 observer 也能估计不可测状态 → 当前深度／姿态／位置可测，速度不可直接测，
位置微分有控制代价 → MIMO-ESO 估计扰动和未测速度，自适应方法估计界 →
ESO-based ISMC 由分析设计跟踪控制并在六推进器平台实机验证。I06 的带宽
折中是观察器整定的局部比较；I06→I07 用估计能力与当前测量条件交接。

| 段落／页栏／段首 | 真实展开及设计依赖 |
|---|---|
| I01，p.1 左→右，`UNDERWATER` | 类型／应用 → 数据质量及 tracking／station keeping 的精确控制需求 |
| I02，p.1 右，`In practice` | 外扰的海况／缆索来源；模型不确定性的参数获取误差／姿态变化，分别解释两类来源 |
| I03，p.1 右，`Several methods` | adaptive、robust、observer 路线 → NN／FLS 应用、学习参数数量及验证类型 |
| I04，p.2 左，`Although` | 单句独立段：近似优势仍有实际调参困难，与 I03 共同完成能力／限制比较 |
| I05，p.2 左，`As an effective` | SMC／ISMC 能力、积分项作用 → 抖振代价 → 已有缓解方案 → 大不确定界且无补偿的问题 → 补偿需求 |
| I06，p.2 左，`Another approach` | observer 估计 → control 用估计补偿 → 类型及已有未知项／不可测状态估计能力；末句交代 bandwidth 整定取舍 |
| I07，p.2 右，`In this paper` | 当前装置可测信息 → 无直接速度 → 微分后果 → 用 I06 已有状态估计能力支撑 output feedback → 再述前作及验证类型 |
| I08／C01–03，p.2 右→p.3 左，`In this paper` | MIMO-ESO 估计、界自适应、控制分析／两部分 → 实机实现 → 估计、跟踪及实验比较贡献 |
| I09，p.3 左，`The remainder` | model、ESO、ISMC、experiments、conclusion，章序接设计依赖 |

**问题物理来源，I02 全段，p.1 右。**

> In practice, there are a number of technical challenges in the control of an underwater robot, such as the unknown external disturbances and model uncertainties. The unknown disturbances in practical oceanic environments include waves, tides, currents, and upward or downward streams. For control design of ROVs, the external force caused by the cable that connects with the depot ship should also be considered. The model uncertainties of an underwater robot are usually caused by the inaccurate hydrodynamic coefficients, which are calculated through the computational fluid dynamics (CFD) methods or towing tank experimental data analysis. During the process of performing a task, different attitude of the robot will also cause the variation of the hydrodynamic coefficient.

两类对象分别展开，不用“复杂环境”笼统替代。`caused by` 说物理来源，
`calculated through` 说参数获取方式，`cause the variation of` 说任务中的变化。
作者系统若无缆索、无相同参数变化，就不继承这些例子；可以直接选用其
“两类问题各自给出必要来源”的整段组织和动作搭配。

| I02 句 | 具体实现与句间推进 |
|---|---|
| S01 | `there are ... technical challenges ... such as ... disturbances and model uncertainties` 段首命名两类对象。 |
| S02 | `The unknown disturbances ... include ...` 接第一类对象，以海况具体展开。 |
| S03 | `the external force caused by the cable ... should also be considered` 同属外扰，再给 ROV 系缆来源及应考虑的力。 |
| S04 | `The model uncertainties ... are usually caused by ... coefficients, which are calculated through ...` 换到第二类对象，参数误差及获取方式各有作用。 |
| S05 | `different attitude ... will also cause the variation of the hydrodynamic coefficient` 将静态获取误差接到任务中的参数变化，下一段才比较应对方法。 |

**补偿为何必要，I05 尾部四个连续句，p.2 左；前文已介绍 SMC／ISMC 能力及抖振代价。**

> To reduce the chattering, several methods, such as the high-order sliding-mode controller [24], [25], disturbance compensation method [26], [27], and terminal sliding controller [28] have been proposed. In [26], a free chattering SMC is presented via an adaptive term, which continuously compensates for the unknown system dynamics of an ROV. In practice, sometimes, the upper bound of the uncertainties may be large and the SMC without a compensator will cause serious chattering. Therefore, it is necessary to design a compensator for the external disturbance to reduce chattering.

保留已有缓解方法及补偿前作，再限定 `upper bound ... may be large` 与
`SMC without a compensator` 才得设计后果。`to reduce chattering` 是用途，
不是全部 SMC 失效或当前设计无条件消除抖振的保证。

**估计到控制使用及状态估计能力，I06 全段，p.2 左；下接 I07 当前测量条件。**

> Another approach dealing with the unknown disturbance is to design an observer to estimate the unknown external disturbance of a robot, followed by the control design to compensate for the estimated disturbance. Such disturbance observers include sliding mode observer [12], [29], high-gain observer [30], [31], and extended state observer (ESO) [13], [32]. In [12], a sliding mode controller based on a sliding mode observer is proposed for a reusable launch vehicle. The observer is presented to estimate the unknown external disturbances and to reduce the control gain. In [30], a high-gain observer-based output feedback motion control that considers the unmodeled dynamics, measurement errors, model parameter variations, and unknown external environmental disturbances for observation class ROVs is presented. In [32], a backstepping control based on an ESO is proposed to handle mismatched disturbance of hydraulic systems. The designed observer estimates not only the model uncertainties but also the unmeasured states. In [13], by using an ESO, a backstepping control for a hydraulic system is presented to suppress large unknown external disturbances. The bandwidth of the observer is chosen in accordance with two conflicting aspects, the maximal load capability and the dynamic performance of system.

`estimate the unknown external disturbance` 接 controller 用估计生成补偿输入。
补偿的物理对象与用于补偿的估计信息要分清；作者若估计状态或合并不确定项，
需按实际对象命名。Such disturbance observers 限定这类 observer，不泛称全部。

| I06 句 | 动作、对象及上下文关系 |
|---|---|
| S01 | `design an observer to estimate ... followed by the control design to compensate for the estimated disturbance` 从 I05 补偿需求进入估计—补偿路线；估计信息交给控制。 |
| S02 | `Such disturbance observers include ...` 按该角色列可用类型。 |
| S03 | `a sliding mode controller based on a sliding mode observer is proposed for ...` 给方案与 launch vehicle 对象。 |
| S04 | `The observer is presented to estimate ... and to reduce the control gain` 续讲上句同一观察器，估计与减小增益各有对象。 |
| S05 | `a high-gain observer-based output feedback motion control that considers ... is presented` 换到 ROV，列明所考虑未知项和测量误差，限定方法范围。 |
| S06 | `a backstepping control based on an ESO is proposed to handle mismatched disturbance ...` 给另一个系统及扰动类别。 |
| S07 | `The designed observer estimates not only the model uncertainties but also the unmeasured states` 续讲 S06 观察器，两类估计责任为 I07 的速度估计提供已有能力。 |
| S08 | `by using an ESO, a backstepping control ... is presented to suppress large unknown external disturbances` 另给大扰动处理能力，承认已有结果。 |
| S09 | `The bandwidth ... is chosen in accordance with two conflicting aspects ...` 接这一观察器的整定取舍，比较负载能力与动态性能；下一段的速度估计需要由实际测量条件确定。 |

**实际可测量信息到设计需求，I07 开头六个连续句，p.2 右；后文继续状态估计研究及仿真／实验分类。**

> In this paper, we design an adaptive sliding mode-based controller for a general type of underwater robots, and experiment is carried on a test bed for underwater object grasping. Onboard sensors, including a depth sensor and an inertial measurement unit (IMU), are equipped to measure the depth and attitude of the robot. The position of the underwater robot is measured by an external vision positioning system (VPS), and some white lightings are equipped on the robot, which can be captured by the VPS to calculate the position of the robot. In such a case, there is no direct measurement of velocity of the robot. Then output feedback is required for our work as the direct differential of the position information may degrade the control performance. In such case, observes are always used to estimate the unmeasured states of the robot [5], [33].

depth／attitude／position 的测量接 velocity 未直接测量，再接微分可能带来的
控制后果及 output-feedback 需求。直接借鉴 `is measured by`、`there is no
direct measurement of`、`is required ... as ...` 的顺序和搭配，让作者的传感
信息解释设计。灯光与装置枝节按贡献需要取舍；`observes`、`white lightings`、
`experiment is carried` 等源文错误或生硬表达不继承。
仿真与实验是验证类型，不据此判定前作无效。

| I07 原句范围 | 句内实现与连续推进 |
|---|---|
| S01 | `we design an adaptive sliding mode-based controller for ...` 给当前设计与平台范围，随后仍解释信息条件。 |
| S02 | `Onboard sensors ... are equipped to measure the depth and attitude ...` 列实际传感输出。 |
| S03 | `The position ... is measured by ... VPS` 补位置来源，后续灯光说明该装置如何取得位置。 |
| S04 | `there is no direct measurement of velocity ...` 在前两句可测信息下指出缺失量，In such a case 的所指具体。 |
| S05 | `output feedback is required ... as the direct differential ... may degrade ...` 从位置微分的可能代价说明输出反馈理由。 |
| S06 | `... used to estimate the unmeasured states ...` 将状态缺失交给观察器，接回 I06 S07 的已有能力；后文继续比较 velocity observer 研究。 |

这里的交接是“已有不可测状态估计能力—当前无直接速度测量—选择状态估计”，
并保留位置微分代价。装置描述和当前设计出现后的文献比较是本篇实现方式，
按作者科学主线保留必要信息，不固定为所有引言的句序。

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

| I08 句 | 设计—作用—分析—实现的推进 |
|---|---|
| S01 | `a disturbance compensation approach is utilized to ... based on ... MIMO-ESO` 回应 I05 补偿／减抖责任。 |
| S02 | `a MIMO-ESO is proposed to estimate the unknown disturbances and the unmeasured states` 命名观察器两类输出，承接 I02／I07；源文 Motivated 开头按作者要求调整。 |
| S03 | `The bounds of the uncertainties are also estimated using ...` 界作主语，另给自适应估计责任，also 的关系是增加估计对象。 |
| S04 | `The Lyapunov analysis is involved to design the final control law` 引入控制律设计的分析依据。 |
| S05 | `The proposed controller ... includes two parts ...` 接组成并给源文理论跟踪结论，按作者真实条件及结论调整。 |
| S06 | `The proposed controller is successfully implemented on ...` 继续同一控制器，以平台实现收束，理论结论与实现分别承担证据责任。 |
| S07 | `The main contributions can be summarized as follows` 从已解释的责任转入贡献列表，不再次引出无关方法。 |

源文 C03（p.3／6787）把 PD 写成 `potential difference`，这是原文术语错误。
§V 的比例／微分增益和位置微分与比例微分控制一致；迁移时仍依据作者实际
控制器确认名称及类别，不由缩写猜展开。Lyapunov、实机比较、误差收敛
分别有自己的对象与范围，不能互相代替证据。
该节把当前装置条件接回前作研究、再收束方法，不需要把全部文献强移到最前。

## Cross-card use

稳定共性是以可命名对象开段，文献具体交代动作及能力，以相关条件继续推进，
设计紧接作用，反复命名中间对象以保持交接。P17 的表征—执行双责任、P05 的
学习信息／激励条件、Fuzzy 的联合目标／假设转证明、ESO 的真实传感条件
是各篇主线。分段数量、设计首次出现位置、段末功能与 roadmap 是可选实现。

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

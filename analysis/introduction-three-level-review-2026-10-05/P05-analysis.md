# P05：整节、完整段落及逐句表达分析

Composite-Learning-Based Adaptive Neural Control for Dual-Arm Robots With Relative Motion

[重新核对的完整引言](<P05-introduction.md>)｜[三层综合总结](report.md)

I／C 是定位号；S 是本段句号。英文完整段落按源文顺序保留，表中的句号对应其句子边界。长句中的分号、where／which 从句不另算独立句，表内仍分别解释不同科学动作。分析是本轮中文判断，不是论文原文。

## 完整科学主线

双臂协作具有载荷／空间优势，协调运动控制与路径规划也更复杂 → 紧持物体的前作不对应工具沿物面滑动的相对运动任务 → 该任务已有控制仍依赖已知动力学，且缺接触力分析 → 抓取物动力学难预知，NN 用于补偿 → 跟踪误差收敛与 NN 权重估计收敛不是同一责任 → NN 稀疏回归使 PE 严格，PPE 有局部重复输入能力但仍有输入／学习速度要求 → 将估计误差信息接入复合学习更新，在相对运动及未知动力学条件下设计控制，并以 PPE 放松激励要求 → 分别汇总任务框架、学习信息、条件放松及仿真分析。

## 各段任务与段间交接

| 原段 | 科学任务 | 承接和交出什么 |
|---|---|---|
| [I01](#i01) | 并列交代双臂的任务优势与协调控制／规划复杂性，共同构成应用动机。 | 优势引出应用；协调运动控制／路径规划的复杂性另行引出控制研究。I02 再具体看已有控制怎么处理对象。 |
| [I02](#i02) | 从前作控制能力中提取紧持物体／无相对运动的共同条件，再用真实任务改变该条件。 | I01 的控制问题具体化为物体操作；段末工具沿物面滑动，为 I03 的 relative motion 提供物理含义。 |
| [I03](#i03) | 在相对运动任务内再次承认已有工作，再定位动力学先验和接触力分析。 | 任务条件已从 I02 推出；本段不是说没人研究相对运动，而是明确已有相对运动控制仍有什么假定。I04 接 dynamics fully available。 |
| [I04](#i04) | 用抓取物动力学未知的实际原因解释为何需要 NN 补偿。 | 接 I03 的动力学先验；段末把不确定性补偿落到 NN，I05 才检查已有 NN 控制解决了什么、还需学到什么。 |
| [I05](#i05) | 区别已有跟踪控制能力与 NN 权重学习问题。 | 接已选 NN 路线；以 weights convergence 将下一段从跟踪指标带到参数／激励条件，不能把二者当同一个误差。 |
| [I06](#i06) | 从 NN 权重估计推出激励条件，承认 PPE 局部能力并保留剩余限制。 | 接 I05 的参数学习问题；末句留下 recurrent trajectory 与 excitation strength，I07 再解释额外误差信息及当前估计设计。 |
| [I07](#i07) | 把估计误差信息接入更新的已有思想应用到当前双臂任务，并分别比较条件与信息用法。 | 响应 I06 学习条件问题；末两句的 PPE 和估计误差信息正好交给 C03／C02，不用一个全体前作 gap 替代不同责任。 |
| [I08](#i08) | 把技术铺垫收成双臂相对运动跟踪目标，并引出贡献。 | 不是首次宣布所有方案，而是汇总 I02–I07 已逐步建立的任务和学习条件；三条贡献继续分开列责。 |
| [C01](#c01) | 任务框架贡献：未知动力学下的非对称双臂任务。 | 对应 I02–I04 的物理条件和先验问题。 |
| [C02](#c02) | 学习贡献：估计误差信息进入 NN 权重更新。 | 对应 I05–I07 的参数学习对象与信息使用。 |
| [C03](#c03) | 条件贡献：PPE 放松 PE 要求。 | 对应 I06–I07，三条分别覆盖任务、信息、激励条件。 |
| [I09](#i09) | 按建模、控制分析、仿真安排后文。 | 段落链在建模条件和学习控制上汇总；这里仅承诺 simulation，不补造实机实验。 |

## 完整段落与逐句拆解

<a id="i01"></a>

### I01：并列交代双臂的任务优势与协调控制／规划复杂性，共同构成应用动机。

来源块：p1-b8, p1-b15。

> RECENTLY, coordination control of dual-arm robots has received increasing attention due to its superiority compared with traditional single-arm robot systems, including stronger payload capability, larger workspace, and more flexibility. Thus, the dual-arm robots have been involved in many high technology applications, such as intelligent assembly, out-space repairing, and elderly people assistance [1]–[3]. However, controlling the dual-arm robots is challenging due to the increase of complexity in motion control and path planning. Therefore, advanced control technologies have been extensively studied for dual-arm robots in past decades [4]–[11].

优势引出应用；协调运动控制／路径规划的复杂性另行引出控制研究。I02 再具体看已有控制怎么处理对象。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | 以研究对象及应用优势开篇。`coordination control of dual-arm robots has received increasing attention due to ...` 后列 payload／workspace／flexibility，attention 有技术原因。 |
| S02 | 把上一优势接到应用。`Thus, the dual-arm robots have been involved in ... such as ...` 的应用举例不等于本文验证范围。 |
| S03 | 另行说明控制挑战的原因。`controlling ... is challenging due to ... complexity in motion control and path planning` 将控制困难归于协调运动控制与规划复杂性，与前述载荷／空间优势并列。 |
| S04 | 以已有控制研究接到下一段。`advanced control technologies have been extensively studied for ...` 给文献展开入口，不假设所有前作失效。 |

<a id="i02"></a>

### I02：从前作控制能力中提取紧持物体／无相对运动的共同条件，再用真实任务改变该条件。

来源块：p1-b16。

> An adaptive decentralized control scheme was proposed to address the object handling problem of a cooperative robot, where an implicit force control scheme was employed to simultaneously regulate the force and position [9]. In [10], a decentralized control structure for multiple mobile manipulators was developed, where the internal forces were constrained by employing an augmented object model for the multiple systems with a virtual linkage. In [11], the loading problem for multiple manipulators was addressed by analyzing the grasp space of the robot. Note that the abovementioned controllers were developed under the assumption that the object is firmly held by the robotic arms such that no relative motion occurred between the arms and the objects. However, in practical applications, such as polishing, grinding, and welding, the robot end-effectors need to operate along the object’s surface, where sliding movements usually happened between the robotic arm and the object [12]–[14].

I01 的控制问题具体化为物体操作；段末工具沿物面滑动，为 I03 的 relative motion 提供物理含义。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | 文献首句直接讲方案与功能。`An adaptive decentralized control scheme was proposed to address ... , where ... was employed to simultaneously regulate the force and position` 用 where 解释方案内部的力／位置责任。 |
| S02 | 第二项讲不同控制对象。`a decentralized control structure ... was developed` 接 internal forces 的约束与 augmented object model／virtual linkage 手段。 |
| S03 | 第三项从问题作主语。`the loading problem ... was addressed by analyzing the grasp space`，addressed 的是载荷问题，by 后是分析方式。 |
| S04 | 把前三项放进有证据的共同条件。`controllers were developed under the assumption that ... firmly held ... such that no relative motion occurred ...` 指手臂与对象之间的运动，不是双臂彼此的相对运动。 |
| S05 | 用当前应用真正改变条件。`robot end-effectors need to operate along the object's surface, where sliding movements ...` 将 polishing／grinding／welding 接到沿表面滑动这一要求，下一段才有理由研究 relative motion。 |

<a id="i03"></a>

### I03：在相对运动任务内再次承认已有工作，再定位动力学先验和接触力分析。

来源块：p1-b17。

> In this respect, the coordination control of dual-arm robots with relative motion deserves further investigation. The relative motion is also known as the asymmetric bimanual task. In [15], a relative impedance controller was developed by using a relative Jacobian method such that the dual-arm system can be treated as a single-arm robotic system. In [16], a brain-actuated control architecture was proposed for dual-arm robots to perform the asymmetric bimanual task, where electroencephalogram signals and visual stimulation were employed to send control command through a brain–machine interface. In these works, however, the controllers were designed under the assumption that the robot dynamics are fully available, while the stability analysis of the contact force between the robotic arm and the object was not given.

任务条件已从 I02 推出；本段不是说没人研究相对运动，而是明确已有相对运动控制仍有什么假定。I04 接 dynamics fully available。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | `coordination control ... with relative motion deserves further investigation` 承接已证明的任务差异，不单独声称无人研究。 |
| S02 | `The relative motion is also known as the asymmetric bimanual task` 给当前文献使用的术语对应，避免名称切换丢失对象。 |
| S03 | 第一项已有相对运动控制讲方法与建模作用。`a relative impedance controller was developed by using a relative Jacobian method such that ...`，结果是把双臂系统作为单臂系统处理。 |
| S04 | 另一项讲控制架构及输入。`architecture was proposed ... to perform ... , where ... signals ... were employed to send control command` 将 EEG／视觉刺激接到 brain–machine interface，不说它解决动力学未知。 |
| S05 | 比较严格限于 `In these works`。`controllers were designed under the assumption that ... fully available` 与 `stability analysis ... was not given` 是两个不同限制，不能合成泛泛“性能差”。 |

<a id="i04"></a>

### I04：用抓取物动力学未知的实际原因解释为何需要 NN 补偿。

来源块：p1-b18, p2-b1。

> The dynamic model of the robot system is of great importance in the controller design [17]–[22], but it is often unavailable in practice. For example, in carrying tasks, the dynamics of the grasped object is hard to obtain in advance. Without a precise dynamics model, the model-based control method became invalid and may cause degeneration of the control performance. Hence, advanced control strategies have been presented to compensate for the model uncertainties. Neural network (NN) is well known by its advantages in alleviating modeling difficulties of nonlinear systems due to the powerful approximation ability [23]. Thus, NN control synthesizes have been widely implemented in developing controllers for nonlinear robotic systems [24]–[32].

接 I03 的动力学先验；段末把不确定性补偿落到 NN，I05 才检查已有 NN 控制解决了什么、还需学到什么。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | 段首双面说明建模地位。`The dynamic model ... is of great importance ... , but it is often unavailable in practice` 直接给有用性与可得性差别。 |
| S02 | 以具体任务解释 unavailable。`in carrying tasks, the dynamics of the grasped object is hard to obtain in advance` 的对象是抓取物，而不是机器人所有信息。 |
| S03 | 说精确模型缺失对 model-based control 的后果。`Without a precise dynamics model ... may cause ...` 中 became invalid 是源文较强判断，不能移成所有模型误差必失稳。 |
| S04 | 由后果引出补偿路线。`strategies have been presented to compensate for the model uncertainties` 将 compensate 接到明确不确定项。 |
| S05 | 给 NN 为什么能承担该责任。`Neural network ... alleviating modeling difficulties ... due to ... approximation ability` 是工具能力理由。 |
| S06 | 归纳 NN 已用于控制器开发。`have been widely implemented in developing controllers ...` 承接 I05 的实际例子；原文 `NN control synthesizes` 用词保留作核对，不作推荐搭配。 |

<a id="i05"></a>

### I05：区别已有跟踪控制能力与 NN 权重学习问题。

来源块：p2-b2。

> A fuzzy neural network control approach was presented for pure-feedback stochastic systems by using a semi-Nussbaum function [33]. In [34], an adaptive NN control strategy was proposed for an uncertain robot to ensure the state not to violate the prescribed constraints. Recently, a sensorless admittance controller was designed to solve the unknown environments’ interaction by using the NN technique [35]. Significant works have been done in [36]–[38] to make a complex topic understandable about modeling and control of flapping-wing flying robots to the average reader. While the NN controllers have been successfully developed in the abovementioned work, a major limitation for existing adaptive NN control schemes lies in that only convergence of the tracking errors can be achieved, instead of the convergence of NN weights to their ideal values. Without the convergence of NN weights, the NN compensation can be hardly accomplished, and the system performance may be degraded and, eventually, became unstable. In this respect, developing a novel control scheme with guaranteed NN convergence is of great significance.

接已选 NN 路线；以 weights convergence 将下一段从跟踪指标带到参数／激励条件，不能把二者当同一个误差。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | 先举模糊 NN 的具体适用系统及手段。`approach was presented for ... by using a semi-Nussbaum function` 是方案—系统—工具的文献句。 |
| S02 | 再举不确定机器人中的状态约束。`strategy was proposed ... to ensure the state not to violate ...` 保留 state constraints 对象，而非笼统保证性能。 |
| S03 | 第三例给交互任务和 NN 手段。`a sensorless admittance controller was designed ... by using the NN technique`，sensorless 是方法条件，不等于本文无传感器。 |
| S04 | 这是综述／可理解性贡献的文献句。`Significant works have been done ... to make a complex topic understandable ...` 并非“使用方法解决控制问题”的实例；与权重收敛主线联系较松，不推广为每个文献句范式。 |
| S05 | 先承认开发成功，再换评价对象。`While ... successfully developed ... , a major limitation ... lies in that ...` 对比 tracking errors convergence 与 NN weights convergence，不凭空说没有跟踪能力。 |
| S06 | 说明作者认为权重未收敛会影响补偿与系统表现。`Without ... may be degraded ...` 是源文论述，其失稳概括不能当所有自适应 NN 的数学结论。 |
| S07 | 以 `control scheme with guaranteed NN convergence` 定义下一段要研究的学习问题，而不是再做一般应用宣传。 |

<a id="i06"></a>

### I06：从 NN 权重估计推出激励条件，承认 PPE 局部能力并保留剩余限制。

来源块：p2-b3。

> In our recent work [39], a filtered operation was presented to control the robotic arm with finite-time convergence under a linear-in-parameter (LIP) robotic dynamic model. Nevertheless, the guaranteed convergence of the NN weights is more difficult. It is well known that the persistent excitation (PE) condition is important to guarantee the estimation convergence [40]. However, in practice, it is very stringent to ensure the PE condition of neural networks due to the sparse characteristics of the NN regressor vector. Recent research of neural networks in [41] presented a partial persistent excitation (PPE) condition instead of the traditional PE condition. It has been proven that, for the radial basis function neural network (RBFNN) defined in a regular lattice, neural nodes could be partially activated for any recurrent NN inputs trajectory remained in this local region [41]. In the subsequent work [42], this idea was employed for the control design of nonlinear strict-feedback systems to guarantee the system stability and accurate NN approximation. However, the NN inputs still need to satisfy the condition of recurrent trajectory, and a small input excitation strength may lead to slow learning speed.

接 I05 的参数学习问题；末句留下 recurrent trajectory 与 excitation strength，I07 再解释额外误差信息及当前估计设计。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | 从作者前作继承已完成能力。`a filtered operation was presented ... with finite-time convergence under ... LIP ... model` 将保证附在模型条件下。 |
| S02 | 用 Nevertheless 改换更难的对象。`the guaranteed convergence of the NN weights is more difficult`，不是否认上一句 LIP 情形的能力。 |
| S03 | 引入估计收敛所依赖的信息条件。`the ... PE condition is important to guarantee the estimation convergence` 把 PE 与 estimation 接起来。 |
| S04 | 解释条件为什么严格。`due to the sparse characteristics of the NN regressor vector` 给技术原因，不只说 challenging。 |
| S05 | 介绍有用替代条件。`Recent research ... presented a ... PPE condition instead of ... PE` 把前作的进展说出来，不能藏掉以夸大改进。 |
| S06 | 明确前作局部结果的边界。`for ... RBFNN defined in a regular lattice ... partially activated ... recurrent ... local region` 的网格、局部区域、重复轨迹都是能力条件。 |
| S07 | 继续说明这一思想的后续用途。`In the subsequent work ... this idea was employed ... to guarantee ...` 连接研究序列，稳定性与准确近似各有对象。 |
| S08 | 最后保留尚需的输入条件和速度影响。`inputs still need to satisfy ... recurrent trajectory` 接 `small input excitation strength may lead to slow learning speed`；still／may 各控制判断范围。 |

<a id="i07"></a>

### I07：把估计误差信息接入更新的已有思想应用到当前双臂任务，并分别比较条件与信息用法。

来源块：p2-b4, p2-b6。

> The work in [43] indicates that parameter convergence can be improved if certain information of the estimation error can be integrated into the adaptation. In [44], a novel parameter estimation law was proposed for a robotic system with unknown dynamics by using a sliding mode technique and a finite-time estimator. In [45], the estimation error was integrated into the adaptation scheme of a class of nonlinear systems to achieve the convergence of NN weights. Motivated by the abovementioned idea, in this article, we develop a composite learning controller for the dual-arm robot to perform bimanual relative motion tasks. To the best of our knowledge, few studies have investigated the learning control in the frame of the dual-arm robot systems subject to relative motion and unknown dynamics. Moreover, different from the work in [46], a PPE condition is also introduced in the estimation scheme to achieve a relaxation of the requirement of the PE condition. In comparison to the method in [45], the estimation error of the NN weights is properly expressed and employed to enhance the approximation of the neural network.

响应 I06 学习条件问题；末两句的 PPE 和估计误差信息正好交给 C03／C02，不用一个全体前作 gap 替代不同责任。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | 段首用研究证据句引入改进原则。`The work in [43] indicates that ... can be improved if ...` 中 if 后给估计误差信息进入 adaptation 的条件。 |
| S02 | 参数估计前作给方案与两个实现工具。`a ... estimation law was proposed ... by using ... sliding mode ... finite-time estimator`，对象是 unknown dynamics 的机器人。 |
| S03 | 第三句追踪同一种信息的已有用途。`the estimation error was integrated into the adaptation scheme ... to achieve ... NN weights` 明确 information→update→weights 的链。 |
| S04 | 再做当前任务设计。`we develop a composite learning controller for ... to perform bimanual relative motion tasks`，Motivated by 只是源文过渡，具体设计动作来自 develop。 |
| S05 | 新颖性范围是任务条件交集。`few studies ... dual-arm ... relative motion and unknown dynamics` 不声称全体 NN／双臂／相对运动都无人研究。 |
| S06 | 与 [46] 比较的是激励要求。`PPE condition ... introduced in the estimation scheme to achieve a relaxation ... PE` 仍有条件，不是完全无需激励。 |
| S07 | 与 [45] 比较的是误差信息表达与使用。`estimation error ... is properly expressed and employed to enhance ...` 不把这个信息改进与上一条件改进合成笼统“更优”。 |

<a id="i08"></a>

### I08：把技术铺垫收成双臂相对运动跟踪目标，并引出贡献。

来源块：p2-b7。

> The objective of this article is to develop a control framework for dual-arm robot tracking control under relative motion. The main contributions of this article can be summarized as follows.

不是首次宣布所有方案，而是汇总 I02–I07 已逐步建立的任务和学习条件；三条贡献继续分开列责。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | `The objective ... is to develop a control framework for ... under relative motion` 用目标句汇总任务和明确条件。 |
| S02 | `The main contributions ... can be summarized as follows` 是列点接口，不应替代前段具体设计关系。 |

<a id="c01"></a>

### C01：任务框架贡献：未知动力学下的非对称双臂任务。

来源块：p2-b8。

> 1) A novel neural control framework is developed for dual-arm robot systems to perform asymmetric bimanual tasks with no prior knowledge of the dynamics.

对应 I02–I04 的物理条件和先验问题。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | `framework is developed ... to perform ... with no prior knowledge of the dynamics` 同句给任务与先验边界；不等于没有任何几何、任务或传感信息。 |

<a id="c02"></a>

### C02：学习贡献：估计误差信息进入 NN 权重更新。

来源块：p2-b8。

> 2) A novel composite learning algorithm is designed for NN weights adaptation such that information of the estimate errors could be appropriately integrated into the adaptation law to improve the estimation performance.

对应 I05–I07 的参数学习对象与信息使用。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | `algorithm is designed for NN weights adaptation such that information ... integrated into ... law to improve ...` 逐级交代设计对象、进入的信息、作用位置与估计性能，不暗示未知真实权重直接可测。 |

<a id="c03"></a>

### C03：条件贡献：PPE 放松 PE 要求。

来源块：p2-b8。

> 3) A partial persistent condition is introduced for the adaptation of NN weights such that the requirement of conventional PE condition can be greatly relaxed.

对应 I06–I07，三条分别覆盖任务、信息、激励条件。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | `condition is introduced for ... such that the requirement ... can be ... relaxed` 描述条件替换的作用；relaxed 不等于 removed。 |

<a id="i09"></a>

### I09：按建模、控制分析、仿真安排后文。

来源块：p2-b8。

> In the following sections, the system modeling and control design procedures are detailed. Section II discusses the system modeling of the dual-arm robot in addition to some preliminaries. Section III presents the design of the composite learning control algorithm by utilizing a command filtered backstepping technique with stability analysis. Section IV demonstrates the simulation results. A brief conclusion is given in Section V.

段落链在建模条件和学习控制上汇总；这里仅承诺 simulation，不补造实机实验。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | 先说后文详述 modeling／control procedures。`are detailed` 是组织动词而非性能动词。 |
| S02 | `Section II discusses ... modeling ... preliminaries` 先交代系统与基础条件。 |
| S03 | `Section III presents ... algorithm ... with stability analysis` 将控制实现与分析相接，command filtered backstepping 是本文真实实现。 |
| S04 | `Section IV demonstrates the simulation results` 命名证据类型。 |
| S05 | `A brief conclusion is given in Section V` 结束 roadmap，原引言没有量化结果收束。 |

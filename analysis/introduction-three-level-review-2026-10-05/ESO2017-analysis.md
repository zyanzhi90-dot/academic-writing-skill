# ESO2017：整节、完整段落及逐句表达分析

Extended State Observer-Based Integral Sliding Mode Control for an Underwater Robot With Unknown Disturbances and Uncertain Nonlinearities

[重新核对的完整引言](<ESO2017-introduction.md>)｜[三层综合总结](report.md)

I／C 是定位号；S 是本段句号。英文完整段落按源文顺序保留，表中的句号对应其句子边界。长句中的分号、where／which 从句不另算独立句，表内仍分别解释不同科学动作。分析是本轮中文判断，不是论文原文。

## 完整科学主线

海洋探测的数据质量与轨迹／定点精度要求 → 海流等外扰、系缆力、流体参数误差及姿态变化妨碍控制 → NN／模糊自适应有近似能力但实际调参困难 → SMC／ISMC 能抑制扰动和改善跟踪，抖振造成能耗和平滑性代价 → 扰动补偿需要估计信息，观察器先估计再供控制补偿 → 当前深度／姿态／位置可测而速度不可直接测，直接微分又有代价 → MIMO-ESO 同时估计扰动和未测速度，自适应方法估计未知项的界 → ESO-based ISMC 由分析设计跟踪控制，并在六推进器平台做实机对照。

## 各段任务与段间交接

| 原段 | 科学任务 | 承接和交出什么 |
|---|---|---|
| [I01](#i01) | 海洋应用对精确控制提出轨迹跟踪／定点保持责任。 | 应用只用两句完成；下一段直接解释实现这些控制要求面临哪些真实物理未知项。 |
| [I02](#i02) | 展开未知扰动和模型不确定性的不同物理来源。 | 把 I01 的精度要求分解为需补偿的项；末句补充姿态导致参数变化，I03 可以按这些对象回查控制路线。 |
| [I03](#i03) | 承认已有不确定性／扰动控制，并用多句解释部分方案的机制与验证。 | 按 I02 两种未知项回查方法；I04 对刚列的 NN／模糊路线提出调参问题，而不是否认其近似能力。 |
| [I04](#i04) | 一整段承认近似能力，同时指出实用学习参数调整困难。 | 单句独立桥段：从 I03 的 NN／模糊方案切换到 I05 的扰动抑制路线，不是所有段都要长篇文献。 |
| [I05](#i05) | SMC／ISMC 的跟踪能力、抖振代价及为何需要扰动补偿器。 | 由 I04 的实用限制转向另一可用路线；末句 compensator 接 I06 的估计后补偿，形成具体设计责任。 |
| [I06](#i06) | 先定义估计—补偿信息链，再比较扰动观察器的估计对象与整定折中。 | 接 I05 的补偿器需求；已有观察器同时估计未知项和不可测状态的能力接到 I07 当前速度不可直接测量的条件。段末带宽折中限定观察器整定。 |
| [I07](#i07) | 真实传感条件推出速度状态估计与输出反馈责任，并回查相应前作。 | 先宣布平台和拟采用路线，但随后继续解释设计为何需要；无直接速度测量把 I06 的 observer 能力接到当前任务，I08 才汇总 MIMO-ESO。 |
| [I08](#i08) | 把减抖、扰动／状态估计、自适应界估计、控制分析及平台实现连成当前方案。 | 回应 I02 未知项、I05 减抖、I07 不可测速度；随后贡献把观察器、控制律和实机比较分列。 |
| [C01](#c01) | 观察器责任：未测速度和未知外扰估计。 | 同时回应 I07 的信息缺失和 I02 的物理扰动。 |
| [C02](#c02) | 控制责任：MIMO-ESO-based ISMC 的跟踪误差保证。 | 估计模块继续进入控制设计，而不是与控制器并列不相接。 |
| [C03](#c03) | 证据责任：真实平台上的对照试验。 | 与前两条估计和控制不同，这一条承担实际比较验证。 |
| [I09](#i09) | 按模型、观察器、ISMC 和实机证据安排文章。 | 观察器→控制器的章节次序与 I06／I08 的信息交接一致；没有要求所有贡献都在引言报告数值。 |

## 完整段落与逐句拆解

<a id="i01"></a>

### I01：海洋应用对精确控制提出轨迹跟踪／定点保持责任。

来源块：p1-b10, p1-b17。

> UNDERWATER robots, including autonomous underwater vehicles (AUVs), remote operated vehicles (ROVs), and underwater gliders, have been increasingly employed to expand the abilities of human in marine resources exploration and marine scientific research. To exploit the full potential benefits provided by underwater robots, high-precision controller for underwater robots is required, such that the quality of the collected data can be guaranteed, and high precision in trajectory tracking or station keeping of the robot can be secured [1]–[6].

应用只用两句完成；下一段直接解释实现这些控制要求面临哪些真实物理未知项。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | 以机器人类型及海洋任务界定对象。`robots, including ... , have been increasingly employed to expand ...` 的 including 是系统范围，employed 后给用途。 |
| S02 | 由应用收益推出控制精度要求及其作用。`high-precision controller ... is required, such that ... data ... and ... tracking or station keeping ...` 同时说明数据质量和运动任务，原句 To exploit 是源文目的起句。 |

<a id="i02"></a>

### I02：展开未知扰动和模型不确定性的不同物理来源。

来源块：p1-b18。

> In practice, there are a number of technical challenges in the control of an underwater robot, such as the unknown external disturbances and model uncertainties. The unknown disturbances in practical oceanic environments include waves, tides, currents, and upward or downward streams. For control design of ROVs, the external force caused by the cable that connects with the depot ship should also be considered. The model uncertainties of an underwater robot are usually caused by the inaccurate hydrodynamic coefficients, which are calculated through the computational fluid dynamics (CFD) methods or towing tank experimental data analysis. During the process of performing a task, different attitude of the robot will also cause the variation of the hydrodynamic coefficient.

把 I01 的精度要求分解为需补偿的项；末句补充姿态导致参数变化，I03 可以按这些对象回查控制路线。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | 段首亮出技术对象类别。`technical challenges ... such as ... disturbances and model uncertainties`，后面分别展开，不把二者同义化。 |
| S02 | 明确外界扰动来源。`disturbances ... include waves, tides, currents ...` 是扰动类型列表，不是文献堆砌。 |
| S03 | 给 ROV 特有的系缆外力。`external force caused by the cable ... should also be considered`，also 是向上一扰动集合添加一项带平台条件的力。 |
| S04 | 解释模型不确定性从哪里来。`are usually caused by the inaccurate hydrodynamic coefficients` 后接 CFD／水池数据的估计来源，和外部海流分开。 |
| S05 | 补充运行时参数变化。`different attitude ... cause the variation of the hydrodynamic coefficient` 将姿态变化接到同一系数，为未知动力学建立任务内来源。 |

<a id="i03"></a>

### I03：承认已有不确定性／扰动控制，并用多句解释部分方案的机制与验证。

来源块：p1-b19。

> Several methods, such as adaptive control [1], [7], [8], robust control [9]–[11], and disturbance observer-based control [12], [13], have been introduced to address the technical challenges of model uncertainties and unknown external disturbances. In [1], a robust adaptive controller considering the velocity constraints is proposed for an ROV. The model parameters are estimated online and a Barrier Lyapunov function is applied in the Lyapunov synthesis. Finally, the results are validated thought simulation. Since fuzzy logic systems (FLS) and neural networks (NN) are capable to approximate nonlinearities, the NN and fuzzy approximation-based adaptive controllers have been widely applied to the plants with model uncertainties and unknown disturbances [7], [8], [14]. In [7], an adaptive controller combining NN approximation with dynamics surface control is presented for trajectory tracking of an AUV. The computational load is reduced by introducing an NN learning method using minimal number of learning parameters. In [15], considering the unknown parameters, an adaptive fuzzy sliding mode control (SMC) is presented to steer a low-speed underactuated underwater vehicle and an experiment has justified the method. In [16], the NN-based controller is extended to control the multiple underwater robots and simulation results have been shown.

按 I02 两种未知项回查方法；I04 对刚列的 NN／模糊路线提出调参问题，而不是否认其近似能力。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | 段首按科学困难归类路线。`Several methods, such as ... , have been introduced to address ...` 给 adaptive／robust／observer-based 的共同任务，不替代下文具体实例。 |
| S02 | 先给 ROV 的速度约束控制。`a robust adaptive controller considering the velocity constraints is proposed for ...`，considering 的对象是该文献的条件。 |
| S03 | 紧接上一控制方案内部动作。`model parameters are estimated online` 与 `Barrier Lyapunov function is applied in the Lyapunov synthesis` 不跳到另一篇。 |
| S04 | 第三句交代同一方案验证类型。`results are validated ... simulation`，原文 thought 保留但不推荐；这构成方案→机制→证据连续句组。 |
| S05 | 从函数近似能力推出 NN／FLS 路线。`Since ... approximate nonlinearities ... controllers ... applied ...` 的 Since 有明确能力原因。 |
| S06 | 实例给 AUV 跟踪和组合技术。`controller combining NN approximation with dynamics surface control is presented for trajectory tracking`，不是只说 NN 被用过。 |
| S07 | 继续解释上一例子减少计算的手段。`computational load is reduced by introducing ... minimal number of learning parameters`，结果对象与技术动作相接。 |
| S08 | 另一例子给低速欠驱动系统、未知参数与实验。`SMC is presented to steer ... and an experiment has justified ...`，原词 justified 不等于理论证明。 |
| S09 | 扩展到多水下机器人并交代仿真。`controller is extended to control ... and simulation results ...` 同句明确扩展对象与证据范围。 |

<a id="i04"></a>

### I04：一整段承认近似能力，同时指出实用学习参数调整困难。

来源块：p2-b1。

> Although the NN and fuzzy-based adaptive controllers have the advantages on the approximation of the uncertainties and disturbances, it is still a challenging task to adjust its learning parameters in real applications.

单句独立桥段：从 I03 的 NN／模糊方案切换到 I05 的扰动抑制路线，不是所有段都要长篇文献。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | `Although ... have the advantages ... , it is still a challenging task to adjust ... in real applications` 同时保留能力与实施限制；比较对象是 learning parameters，不是所有不确定性都不可近似。原文其数／代词不齐不需照抄。 |

<a id="i05"></a>

### I05：SMC／ISMC 的跟踪能力、抖振代价及为何需要扰动补偿器。

来源块：p2-b2。

> As an effective tool to suppress disturbances for complex systems, SMC has attracted obvious attentions for the control plant with disturbances [10], [17]–[21]. In [22], a novel ESO-based adaptive control has been proposed for power converters to reject the load connected to the dc-link capacitor and the uncertain parameters. The experiment based on a real power converter prototype validate the control performance. In [9], a sliding mode tracking controller, which uses two sliding surfaces for surge tracking errors and lateral motion tracking errors, is applied to autonomous surface vessels. To address the control technical challenges for the switched stochastic systems, a novel dissipativity-based SMC is proposed in [17]. In [10], integral sliding mode controllers (ISMC) are proposed for trajectory tracking of ROVs. Because of the effect of the additional error-integral term, the ISMC has a more accurate trajectory tracking performance than the conventional SMC. To overcome the time-delay for the AUV control, an ISMC is introduced to overcome the problem that data acquisition rate could not be maintained sufficiently [23]. The major shortcoming of SMC is the chattering problem, which not only causes energy losses but also reduces the trajectory tracking smoothness. To reduce the chattering, several methods, such as the high-order sliding-mode controller [24], [25], disturbance compensation method [26], [27], and terminal sliding controller [28] have been proposed. In [26], a free chattering SMC is presented via an adaptive term, which continuously compensates for the unknown system dynamics of an ROV. In practice, sometimes, the upper bound of the uncertainties may be large and the SMC without a compensator will cause serious chattering. Therefore, it is necessary to design a compensator for the external disturbance to reduce chattering.

由 I04 的实用限制转向另一可用路线；末句 compensator 接 I06 的估计后补偿，形成具体设计责任。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | 段首先给 SMC 的扰动抑制作用。`SMC ... for ... with disturbances` 提供路线理由；As an／obvious attentions 为源文表达，不是共同必选写法。 |
| S02 | 穿插 ESO 自适应控制的跨域例子。`control ... for power converters to reject ...` 是扰动／参数抑制能力的旁证，不是 SMC 分类下纯粹同类实例。 |
| S03 | 下一句继续该 power converter 的真实原型证据。`experiment ... prototype ... control performance`，原文主谓一致错误保留，不从字面推出本文实验结论。 |
| S04 | 给 surface vessel 控制的两种滑模面。`controller, which uses two sliding surfaces for ... , is applied to ...` 分别指 surge 与 lateral 误差。 |
| S05 | 又给 switched stochastic systems 的控制路线。`SMC is proposed ...` 接不同系统的技术挑战，不应把这些系统默认为水下机器人。 |
| S06 | 再缩到 ROV 的 ISMC。`ISMC ... proposed for trajectory tracking of ROVs` 将跟踪目标接到积分滑模。 |
| S07 | 连续解释 ISMC 为什么改善跟踪。`Because of ... additional error-integral term ... more accurate ... than conventional SMC` 明确改动项、性能维度和比较对象。 |
| S08 | 补充 AUV 数据获取不足／时延的 ISMC 用途。`ISMC is introduced to overcome ...` 是另一个任务条件，原句重复 overcome 不推广为成熟共性。 |
| S09 | 明确这条路线的剩余代价。`major shortcoming ... chattering ... not only causes energy losses but also reduces ... smoothness` 抖振后果分为能耗和运动平滑。 |
| S10 | 先承认已有减抖方法。`several methods, such as ... , have been proposed` 回应代价，而不是冒称此前无人减抖。 |
| S11 | 给自适应连续补偿的具体实例。`SMC is presented via an adaptive term, which continuously compensates for ...` 命名补偿项及未知动力学对象。 |
| S12 | 给当前选择补偿器的条件性理由。`upper bound ... may be large` 接 `SMC without a compensator ... serious chattering`，不是任意 SMC 必定严重抖振。 |
| S13 | 将论述收成待设计对象。`Therefore, it is necessary to design a compensator ... to reduce chattering` 交给下一段观察器提供补偿信息。 |

<a id="i06"></a>

### I06：先定义估计—补偿信息链，再比较扰动观察器的估计对象与整定折中。

来源块：p2-b3。

> Another approach dealing with the unknown disturbance is to design an observer to estimate the unknown external disturbance of a robot, followed by the control design to compensate for the estimated disturbance. Such disturbance observers include sliding mode observer [12], [29], high-gain observer [30], [31], and extended state observer (ESO) [13], [32]. In [12], a sliding mode controller based on a sliding mode observer is proposed for a reusable launch vehicle. The observer is presented to estimate the unknown external disturbances and to reduce the control gain. In [30], a high-gain observer-based output feedback motion control that considers the unmodeled dynamics, measurement errors, model parameter variations, and unknown external environmental disturbances for observation class ROVs is presented. In [32], a backstepping control based on an ESO is proposed to handle mismatched disturbance of hydraulic systems. The designed observer estimates not only the model uncertainties but also the unmeasured states. In [13], by using an ESO, a backstepping control for a hydraulic system is presented to suppress large unknown external disturbances. The bandwidth of the observer is chosen in accordance with two conflicting aspects, the maximal load capability and the dynamic performance of system.

接 I05 的补偿器需求；已有观察器同时估计未知项和不可测状态的能力接到 I07 当前速度不可直接测量的条件。段末带宽折中限定观察器整定。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | 段首不是纯报术语，而是给动作顺序。`design an observer to estimate ... , followed by ... compensate for the estimated disturbance` 将估计输出明确交给控制输入。 |
| S02 | `Such disturbance observers include ...` 给上一角色的可用类型，sliding mode／high-gain／ESO 不是无目的目录。 |
| S03 | 文献方案给 launch vehicle 的 observer-based SMC。`controller based on ... observer is proposed for ...` 保留对象所属领域。 |
| S04 | 下一句接同一 observer 的两项作用。`observer ... to estimate ... and to reduce the control gain`，估计扰动与降低控制增益并非同一输出对象。 |
| S05 | 另例给 ROV output feedback 及所考虑未知项。`control that considers ... is presented` 的从句列 unmodeled dynamics／measurement errors 等，用来界定范围。 |
| S06 | 再举 hydraulic systems 的 mismatched disturbance。`backstepping control based on an ESO ... to handle ...` 保留扰动类型，不把 mismatched 丢成一般未知扰动。 |
| S07 | 下一句补充该 observer 的估计责任。`estimates not only ... model uncertainties but also ... unmeasured states` 为本文联合扰动与速度估计提供前作能力。 |
| S08 | 另一个 ESO 例子讲大外扰抑制。`backstepping control ... to suppress large ... disturbances` 不否认先前 ESO 已处理大扰动。 |
| S09 | 段末承认观察器带宽选择的折中。`bandwidth ... chosen in accordance with two conflicting aspects ...`，两个方面是最大负载能力与动态性能，不是为了造段末 gap。 |

<a id="i07"></a>

### I07：真实传感条件推出速度状态估计与输出反馈责任，并回查相应前作。

来源块：p2-b4。

> In this paper, we design an adaptive sliding mode-based controller for a general type of underwater robots, and experiment is carried on a test bed for underwater object grasping. Onboard sensors, including a depth sensor and an inertial measurement unit (IMU), are equipped to measure the depth and attitude of the robot. The position of the underwater robot is measured by an external vision positioning system (VPS), and some white lightings are equipped on the robot, which can be captured by the VPS to calculate the position of the robot. In such a case, there is no direct measurement of velocity of the robot. Then output feedback is required for our work as the direct differential of the position information may degrade the control performance. In such case, observes are always used to estimate the unmeasured states of the robot [5], [33]. A local recurrent NN-based adaptive terminal sliding mode state observer is presented to estimate the unmeasured velocity of an ROV in [5], which considers the uncertain dynamic model, the unmeasured states, and inaccurate thrust model. In [34], an NN-based adaptive observer is presented to address the problem of estimating the unavailable measurements of underwater vehicles’ velocities. In [35], a terminal sliding mode observer of an AUV is introduced to estimate the velocity, and the estimation error is guaranteed to converge to zero in a finite time. In [36], an adaptive backstepping control is introduced for human upper limbs in the presence of disturbances, unmodeled dynamics, and uncertainties. In [37], an output feedback tracking controller is designed to address the problem of steering a quadrotor with unknown disturbances and model uncertainties. The unmeasurable linear and angular velocities are estimated by a series of nonmodel-based filters. In [38], an attitude and speed controller is designed based on an adaptive second-order SMC for an unmanned aerial vehicle (UAV), and an extended observer is applied to estimate the unmeasured states and unknown external disturbances. In [39], a high-gain observer is implemented to estimate the full states of the electro-hydraulic system. It is noted that in the literature mentioned above, controllers designed for underwater robots in [1], [3], [4], [7], [8], [16], [18], [26], and [28] are verified by simulations, and other controllers in [6], [10], [15], [23], and [24] are verified by experiments.

先宣布平台和拟采用路线，但随后继续解释设计为何需要；无直接速度测量把 I06 的 observer 能力接到当前任务，I08 才汇总 MIMO-ESO。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | 先给当前控制路线和抓取试验台。`we design ... controller ... and experiment ... test bed` 是局部作者设计已出现，不代表文献讨论必须结束。 |
| S02 | 命名 onboard sensors 与可测量量。`sensors ... are equipped to measure the depth and attitude` 给深度传感器／IMU 的实际输出。 |
| S03 | 再命名外部 VPS 测位置。`position ... is measured by ...` 后补光源怎样被捕获，形成位置获取条件。 |
| S04 | 明确缺失的可测量量。`there is no direct measurement of velocity` 是由前两句形成的本平台条件，不是整个领域无速度传感。 |
| S05 | 从这个缺失推出 output feedback，并给直接微分的控制代价。`output feedback is required ... as ... differential ... may degrade ...` 的 as 给因果依据。 |
| S06 | 将未测量状态交给 observer。`... used to estimate the unmeasured states` 接回 I06 的信息链；原文 observes／always 保留，不作为统一用词与普遍性断言。 |
| S07 | 第一状态估计文献给 ROV 速度、NN terminal sliding mode 和模型条件。`observer is presented to estimate ... which considers ...`，把不可测量量命名为 velocity。 |
| S08 | 另一项 NN observer 仍针对速度测量缺失。`observer ... to address the problem of estimating ... velocities`，不是改变本文测量事实。 |
| S09 | terminal sliding mode observer 例子分别给估计动作及误差保证。`estimate the velocity` 接 `estimation error ... converge to zero in a finite time`，finite-time 是该文献保证。 |
| S10 | 插入 human upper limbs 的 adaptive backstepping。`control ... in the presence of ...` 展示跨系统不确定性条件，但未像相邻句一样明确状态估计动作，和本段主线联系较弱。 |
| S11 | 给 quadrotor 的 output feedback 跟踪任务。`controller is designed to address ... with ... disturbances ... uncertainties` 保留系统对象。 |
| S12 | 下一句说明同一文献怎样得到未测速度。`unmeasurable linear and angular velocities are estimated by ... filters` 明确 filters 的估计输出。 |
| S13 | UAV 文献同时给 controller 及 observer 两种角色。`controller is designed ... and ... observer is applied to estimate ...`，不可测状态和未知外扰各自保留。 |
| S14 | high-gain observer 例子给电液系统的 full states 估计，为 I08 引用 high-gain 思想提供来源。 |
| S15 | 末句按模拟／实验归纳水下机器人文献证据。`controllers ... are verified by simulations ... other ... by experiments` 承認已有实机研究，不把本文实现写成首个水下控制实验。 |

<a id="i08"></a>

### I08：把减抖、扰动／状态估计、自适应界估计、控制分析及平台实现连成当前方案。

来源块：p2-b5。

> In this paper, a disturbance compensation approach is utilized to eliminate the chattering based on multiple-input and multiple-output extend-state-observer (MIMO-ESO) with a simple structure. Motivated by the ESO model [32] and the high-gain observer [39], a MIMO-ESO is proposed to estimate the unknown disturbances and the unmeasured states. The bounds of the uncertainties are also estimated using the adaptive control technique. The Lyapunov analysis is involved to design the final control law. The proposed controller in this paper includes two parts, namely the equivalent controller and the switch controller, which guarantees the trajectory tracking error converge to zero theoretically. The proposed controller is successfully implemented on an underwater robot propelled by six thrusters. The main contributions can be summarized as follows.

回应 I02 未知项、I05 减抖、I07 不可测速度；随后贡献把观察器、控制律和实机比较分列。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | 段首给补偿作用和实现路线。`disturbance compensation approach is utilized ... based on ... MIMO-ESO`，eliminate chattering 是源文自己的主张强度，不能视为通用保证。 |
| S02 | 说明技术继承并明确估计对象。`a MIMO-ESO is proposed to estimate the unknown disturbances and the unmeasured states` 引用 ESO model／high-gain observer，不虚构完全新来源。 |
| S03 | 用自适应控制补充另一种估计责任。`The bounds of the uncertainties are also estimated` 区分界估计与上一句状态／扰动估计。 |
| S04 | 将 Lyapunov analysis 接到最终控制律设计。`analysis is involved to design ...` 不是只在结尾点名分析工具。 |
| S05 | 分开 equivalent 与 switch controller，再给理论跟踪误差结论。`controller ... includes two parts ... guarantees ... error ... zero theoretically`，保证属于源文研究，不由“有两部分”本身自动成立。 |
| S06 | 把 proposed controller 接到真实六推进器平台。`is successfully implemented on ... propelled by six thrusters` 是实现证据，不是新增第四种控制模块。 |
| S07 | `main contributions ... summarized as follows` 接分工清单，前六句已给具体内容。 |

<a id="c01"></a>

### C01：观察器责任：未测速度和未知外扰估计。

来源块：p2-b6。

> 1) A novel adaptive MIMO-ESO is developed to estimate the unmeasured velocity and the unknown external disturbances of the underwater robot.

同时回应 I07 的信息缺失和 I02 的物理扰动。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | `MIMO-ESO is developed to estimate the unmeasured velocity and the unknown external disturbances` 两个明确估计对象，不把估计改成直接测量。 |

<a id="c02"></a>

### C02：控制责任：MIMO-ESO-based ISMC 的跟踪误差保证。

来源块：p3-b2。

> 2) Based on Lyapunov analysis, an adaptive MIMO-ESO-based ISMC is designed to ensure that the trajectory tracking error converge to zero.

估计模块继续进入控制设计，而不是与控制器并列不相接。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | `ISMC is designed to ensure ... trajectory tracking error ... zero` 同时命名控制技术、依据和保证对象；原语法问题保留，保证条件须按作者实际研究替换。 |

<a id="c03"></a>

### C03：证据责任：真实平台上的对照试验。

来源块：p3-b2。

> 3) Comparative studies with the conventional potential difference (PD) control are carried out experimentally on an underwater robot to demonstrate the superior performance of the proposed control.

与前两条估计和控制不同，这一条承担实际比较验证。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | `Comparative studies with ... are carried out experimentally on ... to demonstrate ...` 将比较对象、实验类型、平台和证明目的写在一起。原词 `potential difference (PD)` 保留，复用前需核对术语，不默改源文。 |

<a id="i09"></a>

### I09：按模型、观察器、ISMC 和实机证据安排文章。

来源块：p3-b2。

> The remainder of this paper is organized as follows: Section II presents the robot model and formulates the problem. In Section III, the adaptive MIMO-ESO is derived to estimate the unknown disturbances and the unmeasured velocities. In Section IV, the ISMC is proposed. Experimental results are shown in Section V, followed by the conclusion of this paper in Section VI.

观察器→控制器的章节次序与 I06／I08 的信息交接一致；没有要求所有贡献都在引言报告数值。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | 组织提示后接 `Section II presents ... model and formulates the problem`，present 与 formulate 各有对象，原文用冒号。 |
| S02 | `MIMO-ESO is derived to estimate ... disturbances ... velocities` 把下一章节的估计输出明确重复，保留接口。 |
| S03 | `ISMC is proposed` 位于观察器之后，符合估计进入控制的依赖。 |
| S04 | `Experimental results are shown ... followed by ... conclusion` 仅为后文安排，不是此处给比较结果数值。 |

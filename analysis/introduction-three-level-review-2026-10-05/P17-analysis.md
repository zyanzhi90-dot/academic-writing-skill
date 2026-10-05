# P17：整节、完整段落及逐句表达分析

Robot Learning System Based on Adaptive Neural Control and Dynamic Movement Primitives

[重新核对的完整引言](<P17-introduction.md>)｜[三层综合总结](report.md)

I／C 是定位号；S 是本段句号。英文完整段落按源文顺序保留，表中的句号对应其句子边界。长句中的分号、where／which 从句不另算独立句，表内仍分别解释不同科学动作。分析是本轮中文判断，不是论文原文。

## 完整科学主线

产品更新要求机器人适应 → 人示教经运动建模重现技能 → DS／DMP 提供稳定、可扩展运动表示 → 最优示范难得，多示范中有可保留的运动信息 → DMP 的非线性函数用 GMM 建模、GMR 检索估计，综合多示范生成运动 → 重现效果还取决于跟踪，未知载荷使动力学难预先获得 → RBFNN 近似动力学，控制器跟踪前一组件生成的关节轨迹 → 生成与跟踪共同承担真实执行。

## 各段任务与段间交接

| 原段 | 科学任务 | 承接和交出什么 |
|---|---|---|
| [I01](#i01) | 制造业变化如何把机器人学习落到运动建模责任。 | 先使 robot learning 有具体任务来源；末句交给 I02 的 motion modeling 工具，而不是泛泛说学习重要。 |
| [I02](#i02) | 选择 DMP 的依据来自 DS 能力与具体示范需求比较。 | 接 I01 的 motion modeling；以 spring-damper 的运动性质收尾，使 I03 能讨论 DMP 的实际用途和进一步多示范需求。 |
| [I03](#i03) | 从 DMP 多种用法中区分“多个 DMP”与“多个示范”，提出一个 DMP 整合多示范。 | 接上段已选择的 DMP；末句提出多示范整合，I04 才引入能保留示范变异的概率方法。 |
| [I04](#i04) | 解释概率方法可继承的多示范信息能力，并建立其与 DS 组合的先例。 | 回应 I03 的多示范整合需求；段末总结已有 DS＋统计学习能力，为 I05 的 DMP＋GMM 组合提供可继承基础，没有额外制造缺口。 |
| [I05](#i05) | DMP＋GMM／GMR 的分工、具体作用与原有学习方法比较。 | 接 I04 可继承的组合能力，先给当前实现，再比较数据需求及计算效率；I06 随后指出运动模型之外还有跟踪责任。 |
| [I06](#i06) | 任务效果还取决于执行跟踪，从未知动力学推出函数近似并选择 RBFNN。 | 不是突然添加控制模块：首句用 imitation performance 接前文运动生成，依次推出动力学、载荷不确定性、NN 和 RBFNN；I07 因而能给出控制与输出接口。 |
| [I07](#i07) | 说明控制责任、保证与生成—跟踪的同一轨迹接口。 | 接 I06 选出的 RBFNN；将前文多示范生成和当前控制组合为系统，为 I08 按整体责任比较前作创造对象。 |
| [I08](#i08) | 把运动生成和轨迹跟踪综合为整体贡献，并作限定前作比较。 | 接 I07 已有完整接口；最后落到学得运动在真实世界的执行，I09 转入文章安排，不再需要段末 gap。 |
| [I09](#i09) | 按方法依赖给出论文安排。 | DMP 基础→学习→RBFNN 控制及稳定性→实验→结论；章节序列呼应生成到执行的主线。 |

## 完整段落与逐句拆解

<a id="i01"></a>

### I01：制造业变化如何把机器人学习落到运动建模责任。

来源块：p1-b8, p1-b16。

> RECENTLY, robots have been widely applied in various fields, especially in manufacturing. Adaptable robots are required due to the increasingly fast updates of the manufactured products. Hence, it is necessary to develop methods for enhancing robot learning. Robot learning from demonstration (LfD) is a valuable technique to simplify the strategy of robot learning [1], [2]. The human tutor shows the way to complete a task and then the robot learns, via motion modeling, to reproduce the skill. Therefore, it is essential to consider how to model motions effectively.

先使 robot learning 有具体任务来源；末句交给 I02 的 motion modeling 工具，而不是泛泛说学习重要。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | 已有应用事实，先定机器人与制造业场景。`robots have been widely applied in ...` 用主体＋现在完成时被动表述使用范围，不先喊新颖性。 |
| S02 | 从产品快速更新推出适应性要求。`Adaptable robots are required due to ...` 将需要的机器人性质置为主语，due to 后给可指认的变化。 |
| S03 | 把适应性要求转成学习方法需求。`Hence, it is necessary to develop methods for enhancing robot learning` 的因果依赖上一句，而非仅靠 Hence。 |
| S04 | 引入可承担学习任务的 LfD。完整术语先作主语，`is a valuable technique to simplify ...` 交代它在当前问题中的用途，引用放句末。 |
| S05 | 解释 LfD 怎么发生。`The human tutor shows ... and then the robot learns, via motion modeling, to reproduce ...` 先人与任务，再机器人、建模手段与重现输出。 |
| S06 | 从刚说明的过程取出本节第一项责任。`Therefore, it is essential to consider how to model motions effectively` 不是全面 gap，而是选择后文要展开的具体对象。 |

<a id="i02"></a>

### I02：选择 DMP 的依据来自 DS 能力与具体示范需求比较。

来源块：p1-b17。

> The dynamic system (DS) is a powerful tool for motion modeling [3]. Compared to the conventional methods, e.g., interpolation techniques, DS offers a flexible solution to model stable and extensible trajectories. In addition, the motion encoded with the DS is robust to perturbations. An approach based on DS was used to learn human motions [4], where the unknown mapping of the DS was approximated using a neural network (NN) called extreme learning machine [5]. The learned model showed adequate stability and generalization. However, this DS-based method required considerable demonstration data for training. In contrast, the dynamic movement primitive (DMP), which is based on a nonlinear DS [6], only requires one demonstration to model motion; here, the DMP models the movement trajectory as a spring-damper system integrated with an unknown function to be learned. The inherent property of the spring-damper system enhances the stability and robustness (to perturbations) of the generated motion.

接 I01 的 motion modeling；以 spring-damper 的运动性质收尾，使 I03 能讨论 DMP 的实际用途和进一步多示范需求。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | 段首直接定义工具位置。`The dynamic system (DS) is a powerful tool for motion modeling` 回答上一段的技术对象，不重开应用背景。 |
| S02 | 比较 DS 与明确举例的传统工具。`DS offers a flexible solution to model ... trajectories` 的对象是轨迹，stable／extensible 是所列能力维度。 |
| S03 | 补充另一个任务相关性质。主语转为 `the motion encoded with the DS`，`is robust to perturbations` 把性质落到生成运动。 |
| S04 | 举出 DS 学习实例及未知映射的实现。`An approach based on DS was used to learn ... , where ... was approximated using ...` 主句讲用途，where 从句讲建模责任与 NN 类型。 |
| S05 | 承认该实例的效果。`The learned model showed adequate stability and generalization` 仍指上一句同一模型，先保留能力再比较。 |
| S06 | 用训练数据代价限定该实例。`this DS-based method required considerable demonstration data` 的 this 限定特定方法，不把所有 DS 说成耗数据。 |
| S07 | 以另一方案回应示范代价，并解释运动模型组成。`the ... DMP ... only requires one demonstration to model motion` 接比较，随后说明 spring-damper 和待学习函数。原句含分号与 here，保留证据，不能固化为作者必选句法。 |
| S08 | 说明 spring-damper 性质如何影响输出。`The inherent property ... enhances the stability and robustness ... of the generated motion` 命名作用来源与被改善对象；此强度属于源文科学主张。 |

<a id="i03"></a>

### I03：从 DMP 多种用法中区分“多个 DMP”与“多个示范”，提出一个 DMP 整合多示范。

来源块：p1-b18。

> DMPs have been often employed to solve robot learning problems because of their flexibility. In [7], DMPs were modified to model fast movement inherent in hitting motion. Another study used reinforcement learning to combine DMP sequences so that the robot could perform more complex tasks [8]. While both these studies employed multiple DMPs to compose a complete action, another study [9] used multiple DMPs to model style-adaptive trajectory, where the style of the generated motion could be changed by modulating the weight parameters that were coupled with the goals. As mentioned in [10], optimal demonstration is difficult to obtain and multiple demonstrations can encode the ideal trajectory implicitly. Therefore, we consider integrating multiple demonstrations into one DMP model in this paper.

接上段已选择的 DMP；末句提出多示范整合，I04 才引入能保留示范变异的概率方法。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | 段首亮出 DMP 用途并给理由。`DMPs have been often employed to solve ... because of their flexibility` 用技术名而非笼统“研究很多”。 |
| S02 | 第一篇文献讲对 DMP 做了什么修改及目标运动。`In [7], DMPs were modified to model fast movement inherent in hitting motion` 中 modified／model 分属修改动作和建模用途。 |
| S03 | 第二篇用主动研究主体变体。`Another study used reinforcement learning to combine DMP sequences so that ...` 把手段、组合对象和复杂任务作用接在一条句链中。 |
| S04 | 归纳前两项共同点后引入第三种用途。`While both these studies employed multiple DMPs ... , another study ...` 先说明可比对象；where 从句将风格调节接到目标耦合权重。并非只换引用编号。 |
| S05 | 从文献用法切换到示范质量这一信息条件。`optimal demonstration is difficult to obtain and multiple demonstrations can encode ... implicitly` 的后一分句给当前选择的正向依据。 |
| S06 | 用 Therefore 收成具体建模决定。`we consider integrating multiple demonstrations into one DMP model` 清楚保留 multiple demonstrations／one DMP，而不是声称多个 DMP 本身失败。 |

<a id="i04"></a>

### I04：解释概率方法可继承的多示范信息能力，并建立其与 DS 组合的先例。

来源块：p1-b19, p2-b2。

> Probabilistic approaches have shown good performance in motion encoding [11]–[13]. The inherent variability of the demonstrations can be extracted, and thus, more features of the demonstrations can be preserved. In [14], an LfD framework using a Gaussian mixture model (GMM) and a Bernoulli mixture model was used to extract the features from multiple demonstrations. A new motion was generated through Gaussian mixture regression (GMR). In contrast with the above-mentioned methods, GMM combined with GMR can provide additional motion information for robots when learning from multiple demonstrations. In [3], a learning approach named stable estimator of dynamical systems (SEDS) was proposed for motion modeling, where an unknown function was modeled using GMR. DS-GMR is another method that combines the DS with the statistical learning approach [15]. Both methods exploit the robustness and generalization capability of the DS as well as the excellent learning performance of the probabilistic methods.

回应 I03 的多示范整合需求；段末总结已有 DS＋统计学习能力，为 I05 的 DMP＋GMM 组合提供可继承基础，没有额外制造缺口。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | 段首先承认研究路线能力。`Probabilistic approaches have shown good performance in motion encoding` 用明确领域限定 performance。 |
| S02 | 解释该能力为何有用。`variability ... can be extracted` 接 `more features ... can be preserved`，从数据差异到信息保留，两个被动对象有因果联系。 |
| S03 | 文献主句交代所用模型及提取对象。`an LfD framework using ... was used to extract the features from multiple demonstrations`，GMM／Bernoulli mixture 是手段，多示范特征是输出。 |
| S04 | 下一句继续同一流程的生成环节。`A new motion was generated through ... GMR` 区分上一句特征提取与此句新运动生成，避免模型名并列。 |
| S05 | 比较组合方式的额外信息能力。`GMM combined with GMR can provide additional motion information ... when ...` 保留比较对象和多示范条件，不笼统宣称最好。 |
| S06 | 再列 DS 与统计模型结合的实例。`a learning approach named ... SEDS was proposed for motion modeling, where ... was modeled using GMR` 名称、用途、未知函数的实现逐层相接。 |
| S07 | 用 `DS-GMR is another method that combines ...` 补足第二个组合实例，another 指已有同类路线。 |
| S08 | 段末归纳前两种方法怎样利用双方能力。`Both methods exploit ... as well as ...` 是选择依据总结，不是 gap 句。 |

<a id="i05"></a>

### I05：DMP＋GMM／GMR 的分工、具体作用与原有学习方法比较。

来源块：p2-b3。

> To take advantage of the performance of the DS and the probabilistic approach, we integrate DMP and GMM into our proposed system, where the nonlinear function of DMP is modeled with GMM and its estimate is retrieved through GMR. This modification enables the robot to extract more features of the motions from multiple demonstrations and to generate motions that synthesize these features. The original DMP was learned using the locally weighted regression (LWR) [16], and the locally weighted projection regression [17] was employed to optimize the bandwidth of each kernel of LWR. Despite the added complexity of the learning procedure, these methods enable the DMP to learn from only one demonstration. Reservoir computing [18] is another method used to approximate the nonlinear function, but its computing efficiency is less than that of GMR.

接 I04 可继承的组合能力，先给当前实现，再比较数据需求及计算效率；I06 随后指出运动模型之外还有跟踪责任。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | 设计首先命名组合，随后分配具体对象。`we integrate DMP and GMM into ...` 接 `the nonlinear function ... is modeled with GMM` 与 `its estimate is retrieved through GMR`，不是只说融合两个优点。 |
| S02 | 马上解释上一修改的任务作用。`This modification enables the robot to extract ... and to generate motions that synthesize ...` 的特征提取和运动生成共享多示范信息来源。 |
| S03 | 回查原 DMP 如何学习，并补充核带宽优化。`was learned using ... LWR` 与 `was employed to optimize the bandwidth of each kernel` 各有对象，不能把 LWR／LWPR 当两个泛化标签。 |
| S04 | 承认比较对象仍有单示范能力。`Despite the added complexity ... these methods enable ...` 不让当前组合抹去前作能力；only one demonstration 限定所述学习方式。 |
| S05 | 以替代近似路线和效率维度收尾。`Reservoir computing ... is another method used to approximate ... , but its computing efficiency is less than that of GMR` 比的是具体函数近似的计算效率。 |

<a id="i06"></a>

### I06：任务效果还取决于执行跟踪，从未知动力学推出函数近似并选择 RBFNN。

来源块：p2-b4, p2-b5。

> The imitation performance of robots also depends on the accuracy of the trajectory tracking controller that involves the robot dynamics. Generally, a model-based control performs better if the model is accurate enough [19]. However, an accurate dynamic model of a manipulator cannot be obtained in advance due to some uncertainties, e.g., unknown payload. The approximation-based controllers have been designed to overcome such uncertainties. They utilize function approximation tools to learn the nonlinear characteristics of the robot dynamics. NNs have been widely used in controller design because of their approximation ability [20]–[22]. In [23], the backpropagation NN (BPNN) was utilized to approximate the unknown nonlinear function in the model of the vibration suppression device, while in [24], the radial basis function NN (RBFNN) was utilized to approximate the unknown nonlinearity of the telerobot system. Compared to BPNN, the learning procedure of RBFNN is based on local approximation; thus, RBFNN can avoid getting stuck in the local optimum and has a faster convergence rate. Besides, the number of hidden layer units of RBFNN can be adaptively adjusted during the training phase, making NN more flexible and adaptive. Therefore, RBFNN is more appropriate for the design of real-time control.

不是突然添加控制模块：首句用 imitation performance 接前文运动生成，依次推出动力学、载荷不确定性、NN 和 RBFNN；I07 因而能给出控制与输出接口。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | 桥接整个系统的另一项责任。`The imitation performance of robots also depends on the accuracy of the trajectory tracking controller`，also 保留生成已解释而执行尚待解释的关系。 |
| S02 | 先说准确模型的正向作用。`a model-based control performs better if the model is accurate enough` 将性能依赖写成 if 条件。 |
| S03 | 再说当前为什么得不到这种模型。`an accurate dynamic model ... cannot be obtained in advance due to ... unknown payload` 的时间条件和载荷例子支撑后面的补偿。 |
| S04 | 由上述未知项引入可用控制路线。`The approximation-based controllers have been designed to overcome such uncertainties`，such 指动力学未知项。 |
| S05 | 补充该路线的实现动作。`utilize function approximation tools to learn the nonlinear characteristics ...` 将 compensate／approximate 前的技术对象讲清。 |
| S06 | 缩到 NN 的选择理由。`NNs have been widely used ... because of their approximation ability` 是具体工具能力，不是只写流行。 |
| S07 | 连续比较 BPNN 与 RBFNN 应用。两半均以具体 NN 为主语，`was utilized to approximate` 接各自系统未知非线性，而不是声称两项工作任务相同。 |
| S08 | 沿局部近似解释源文宣称的优化与收敛优势。`the learning procedure ... is based on local approximation` 接避免局部最优和更快收敛；这些强结论不能变成所有 RBFNN 的通则。 |
| S09 | 增加结构适应能力。`the number of hidden layer units ... can be adaptively adjusted during the training phase` 命名可调整数量与发生阶段，后接源文的灵活性解释。 |
| S10 | 以 `Therefore, RBFNN is more appropriate for the design of real-time control` 完成局部选择，不再泛泛说 NN 有意义。 |

<a id="i07"></a>

### I07：说明控制责任、保证与生成—跟踪的同一轨迹接口。

来源块：p2-b6。

> In this paper, an NN-based controller is designed to guarantee the tracking performance of the manipulator in joint space, where RBFNN is employed to approximate the nonlinear functions of the robot dynamics. The stability of the controller is guaranteed by the Lyapunov stability theory. As shown in Fig. 1, the robot learning system consists of the motion generation component and the trajectory tracking component. The former utilizes the motion model based on DMP to learn and generalize motion skills; these, in turn, are represented as a set of trajectories in joint space. The latter employs the adaptive controller to track the trajectories generated from the former, and RBFNN is incorporated to compensate for the uncertain dynamics.

接 I06 选出的 RBFNN；将前文多示范生成和当前控制组合为系统，为 I08 按整体责任比较前作创造对象。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | 设计句并列控制责任与近似责任。`an NN-based controller is designed to guarantee ... in joint space` 接 RBFNN 所近似的机器人动力学非线性，joint space 不应丢失。 |
| S02 | 将稳定性与作者使用的分析依据联系。`The stability of the controller is guaranteed by ...` 是源文保证陈述；借句式时仍须替换证明对象与实际前提。 |
| S03 | 命名两组件。`the robot learning system consists of ...` 只在系统确有这两个责任时可借用，不作为引言固定双模块。 |
| S04 | 先定义生成组件输出。`utilizes ... to learn and generalize ...` 接 `represented as a set of trajectories in joint space`，形成下句要接收的轨迹。 |
| S05 | 跟踪组件接收上一句相同轨迹。`track the trajectories generated from the former` 后命名 RBFNN 补偿 uncertain dynamics，清楚区分生成输出、跟踪目标与补偿对象。 |

<a id="i08"></a>

### I08：把运动生成和轨迹跟踪综合为整体贡献，并作限定前作比较。

来源块：p2-b7。

> Here, we present a novel and complete robot learning framework that considers the performance of both motion generation and trajectory tracking. The SEDS presented in [3] is similar to our DMP-based model. However, the constraints that guarantee the stability of SEDS are derived by the Lyapunov theory that increases the complexity of the learning. In contrast to [3] and [25] which considered only motion modeling, our system is enhanced by an NN-based controller and the effect caused by the dynamic environments can be compensated by neural learning. This design enables the robot to perform the learned motions steadily and more robustly in the real world.

接 I07 已有完整接口；最后落到学得运动在真实世界的执行，I09 转入文章安排，不再需要段末 gap。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | 合并两种任务责任。`we present ... framework that considers ... both motion generation and trajectory tracking` 的 both 有前文铺垫；Here、novel、complete 是源文选择，不是必抄装饰。 |
| S02 | 先承认相似前作。`The SEDS presented in [3] is similar to our DMP-based model` 保持技术继承关系。 |
| S03 | 沿这一具体前作解释约束与学习复杂度。`the constraints that guarantee ... are derived ...` 不能扩展为所有稳定运动模型都难学习。 |
| S04 | 按责任范围比较所列 [3]／[25]。`our system is enhanced by ...` 后接动态环境影响的补偿；only motion modeling 仅属所列对象。 |
| S05 | 段末以设计接任务效果。`This design enables the robot to perform the learned motions ... in the real world` 将前文 learned motions 交给真实执行，而非另添新目标。 |

<a id="i09"></a>

### I09：按方法依赖给出论文安排。

来源块：p2-b8。

> The remainder of this paper is organized as follows. Section II introduces the DMP and its relevant characteristics. The learning process of the motion model is introduced in Section III. In Section IV, the concept of RBFNN is introduced, and the controller using RBFNN is designed with the proof of stability. The experiments are presented in Section V. Section VI concludes this paper.

DMP 基础→学习→RBFNN 控制及稳定性→实验→结论；章节序列呼应生成到执行的主线。

| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |
|---|---|
| S01 | `The remainder of this paper is organized as follows` 是组织提示，不承载科学创新。 |
| S02 | `Section II introduces the DMP and its relevant characteristics` 先给要使用的运动模型基础。 |
| S03 | `The learning process ... is introduced in Section III` 再给生成模型的学习。 |
| S04 | `In Section IV ... controller ... is designed with the proof of stability` 将控制设计与其分析放在同一责任下。 |
| S05 | `The experiments are presented in Section V` 只承诺实验呈现，没有给出结果数值。 |
| S06 | `Section VI concludes this paper` 完成 roadmap；引言没有强制以实验提升数字结束。 |

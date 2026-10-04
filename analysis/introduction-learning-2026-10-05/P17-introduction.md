# P17 — Introduction 原文核验副本

来源：[Robot_Learning_System_Based_on_Adaptive_Neural_Control_and_Dynamic_Movement_Primitives.pdf](<../../文献资料/Robot_Learning_System_Based_on_Adaptive_Neural_Control_and_Dynamic_Movement_Primitives.pdf>)；§I，PDF p.1–2，印刷页 777–778。

PDF SHA-256：`7273b1391fe1c1878e666f7073beea113a2093a37406c447788ab0e9ec74b2ef`。

本文件完整保留 Introduction，止于 §II 标题之前；摘要、作者脚注、图注和下一节不计入引言。I 为实际 prose 段落，C 为贡献条目；同一段跨栏／跨页时合并。编号是本轮定位号，不是论文原有编号。

仅规范排版：NFKC 连字、行末断词、空白及首字下沉重接；原有词汇、语法、引用编号和句末标点不改。具体断词见 normalization-log.json。页面块与渲染图用于复核段落边界。

这些英文是所提供本地论文的原文证据，不是作者新稿，也不是建议逐字继承的科学断言。

## I01 — p1-b8, p1-b16

> RECENTLY, robots have been widely applied in various fields, especially in manufacturing. Adaptable robots are required due to the increasingly fast updates of the manufactured products. Hence, it is necessary to develop methods for enhancing robot learning. Robot learning from demonstration (LfD) is a valuable technique to simplify the strategy of robot learning [1], [2]. The human tutor shows the way to complete a task and then the robot learns, via motion modeling, to reproduce the skill. Therefore, it is essential to consider how to model motions effectively.

## I02 — p1-b17

> The dynamic system (DS) is a powerful tool for motion modeling [3]. Compared to the conventional methods, e.g., interpolation techniques, DS offers a flexible solution to model stable and extensible trajectories. In addition, the motion encoded with the DS is robust to perturbations. An approach based on DS was used to learn human motions [4], where the unknown mapping of the DS was approximated using a neural network (NN) called extreme learning machine [5]. The learned model showed adequate stability and generalization. However, this DS-based method required considerable demonstration data for training. In contrast, the dynamic movement primitive (DMP), which is based on a nonlinear DS [6], only requires one demonstration to model motion; here, the DMP models the movement trajectory as a spring-damper system integrated with an unknown function to be learned. The inherent property of the spring-damper system enhances the stability and robustness (to perturbations) of the generated motion.

## I03 — p1-b18

> DMPs have been often employed to solve robot learning problems because of their flexibility. In [7], DMPs were modified to model fast movement inherent in hitting motion. Another study used reinforcement learning to combine DMP sequences so that the robot could perform more complex tasks [8]. While both these studies employed multiple DMPs to compose a complete action, another study [9] used multiple DMPs to model style-adaptive trajectory, where the style of the generated motion could be changed by modulating the weight parameters that were coupled with the goals. As mentioned in [10], optimal demonstration is difficult to obtain and multiple demonstrations can encode the ideal trajectory implicitly. Therefore, we consider integrating multiple demonstrations into one DMP model in this paper.

## I04 — p1-b19, p2-b2

> Probabilistic approaches have shown good performance in motion encoding [11]–[13]. The inherent variability of the demonstrations can be extracted, and thus, more features of the demonstrations can be preserved. In [14], an LfD framework using a Gaussian mixture model (GMM) and a Bernoulli mixture model was used to extract the features from multiple demonstrations. A new motion was generated through Gaussian mixture regression (GMR). In contrast with the above-mentioned methods, GMM combined with GMR can provide additional motion information for robots when learning from multiple demonstrations. In [3], a learning approach named stable estimator of dynamical systems (SEDS) was proposed for motion modeling, where an unknown function was modeled using GMR. DS-GMR is another method that combines the DS with the statistical learning approach [15]. Both methods exploit the robustness and generalization capability of the DS as well as the excellent learning performance of the probabilistic methods.

## I05 — p2-b3

> To take advantage of the performance of the DS and the probabilistic approach, we integrate DMP and GMM into our proposed system, where the nonlinear function of DMP is modeled with GMM and its estimate is retrieved through GMR. This modification enables the robot to extract more features of the motions from multiple demonstrations and to generate motions that synthesize these features. The original DMP was learned using the locally weighted regression (LWR) [16], and the locally weighted projection regression [17] was employed to optimize the bandwidth of each kernel of LWR. Despite the added complexity of the learning procedure, these methods enable the DMP to learn from only one demonstration. Reservoir computing [18] is another method used to approximate the nonlinear function, but its computing efficiency is less than that of GMR.

## I06 — p2-b4, p2-b5

> The imitation performance of robots also depends on the accuracy of the trajectory tracking controller that involves the robot dynamics. Generally, a model-based control performs better if the model is accurate enough [19]. However, an accurate dynamic model of a manipulator cannot be obtained in advance due to some uncertainties, e.g., unknown payload. The approximation-based controllers have been designed to overcome such uncertainties. They utilize function approximation tools to learn the nonlinear characteristics of the robot dynamics. NNs have been widely used in controller design because of their approximation ability [20]–[22]. In [23], the backpropagation NN (BPNN) was utilized to approximate the unknown nonlinear function in the model of the vibration suppression device, while in [24], the radial basis function NN (RBFNN) was utilized to approximate the unknown nonlinearity of the telerobot system. Compared to BPNN, the learning procedure of RBFNN is based on local approximation; thus, RBFNN can avoid getting stuck in the local optimum and has a faster convergence rate. Besides, the number of hidden layer units of RBFNN can be adaptively adjusted during the training phase, making NN more flexible and adaptive. Therefore, RBFNN is more appropriate for the design of real-time control.

## I07 — p2-b6

> In this paper, an NN-based controller is designed to guarantee the tracking performance of the manipulator in joint space, where RBFNN is employed to approximate the nonlinear functions of the robot dynamics. The stability of the controller is guaranteed by the Lyapunov stability theory. As shown in Fig. 1, the robot learning system consists of the motion generation component and the trajectory tracking component. The former utilizes the motion model based on DMP to learn and generalize motion skills; these, in turn, are represented as a set of trajectories in joint space. The latter employs the adaptive controller to track the trajectories generated from the former, and RBFNN is incorporated to compensate for the uncertain dynamics.

## I08 — p2-b7

> Here, we present a novel and complete robot learning framework that considers the performance of both motion generation and trajectory tracking. The SEDS presented in [3] is similar to our DMP-based model. However, the constraints that guarantee the stability of SEDS are derived by the Lyapunov theory that increases the complexity of the learning. In contrast to [3] and [25] which considered only motion modeling, our system is enhanced by an NN-based controller and the effect caused by the dynamic environments can be compensated by neural learning. This design enables the robot to perform the learned motions steadily and more robustly in the real world.

## I09 — p2-b8

> The remainder of this paper is organized as follows. Section II introduces the DMP and its relevant characteristics. The learning process of the motion model is introduced in Section III. In Section IV, the concept of RBFNN is introduced, and the controller using RBFNN is designed with the proof of stability. The experiments are presented in Section V. Section VI concludes this paper.

# ESO2017 — Introduction 原文核验副本

来源：[Extended_State_Observer-Based_Integral_Sliding_Mode_Control_for_an_Underwater_Robot_With_Unknown_Disturbances_and_Uncertain_Nonlinearities.pdf](<../../文献资料/Extended_State_Observer-Based_Integral_Sliding_Mode_Control_for_an_Underwater_Robot_With_Unknown_Disturbances_and_Uncertain_Nonlinearities.pdf>)；§I，PDF p.1–3，印刷页 6785–6787。

PDF SHA-256：`cadf07c235cf390626b7c0167e8fbae88e10512001fa76ec0e3960b9d0727dec`。

本文件完整保留 Introduction，止于 §II 标题之前；摘要、作者脚注、图注和下一节不计入引言。I 为实际 prose 段落，C 为贡献条目；同一段跨栏／跨页时合并。编号是本轮定位号，不是论文原有编号。

仅规范排版：NFKC 连字、行末断词、空白及首字下沉重接；原有词汇、语法、引用编号和句末标点不改。具体断词见 normalization-log.json。页面块与渲染图用于复核段落边界。

这些英文是所提供本地论文的原文证据，不是作者新稿，也不是建议逐字继承的科学断言。

## I01 — p1-b10, p1-b17

> UNDERWATER robots, including autonomous underwater vehicles (AUVs), remote operated vehicles (ROVs), and underwater gliders, have been increasingly employed to expand the abilities of human in marine resources exploration and marine scientific research. To exploit the full potential benefits provided by underwater robots, high-precision controller for underwater robots is required, such that the quality of the collected data can be guaranteed, and high precision in trajectory tracking or station keeping of the robot can be secured [1]–[6].

## I02 — p1-b18

> In practice, there are a number of technical challenges in the control of an underwater robot, such as the unknown external disturbances and model uncertainties. The unknown disturbances in practical oceanic environments include waves, tides, currents, and upward or downward streams. For control design of ROVs, the external force caused by the cable that connects with the depot ship should also be considered. The model uncertainties of an underwater robot are usually caused by the inaccurate hydrodynamic coefficients, which are calculated through the computational fluid dynamics (CFD) methods or towing tank experimental data analysis. During the process of performing a task, different attitude of the robot will also cause the variation of the hydrodynamic coefficient.

## I03 — p1-b19

> Several methods, such as adaptive control [1], [7], [8], robust control [9]–[11], and disturbance observer-based control [12], [13], have been introduced to address the technical challenges of model uncertainties and unknown external disturbances. In [1], a robust adaptive controller considering the velocity constraints is proposed for an ROV. The model parameters are estimated online and a Barrier Lyapunov function is applied in the Lyapunov synthesis. Finally, the results are validated thought simulation. Since fuzzy logic systems (FLS) and neural networks (NN) are capable to approximate nonlinearities, the NN and fuzzy approximation-based adaptive controllers have been widely applied to the plants with model uncertainties and unknown disturbances [7], [8], [14]. In [7], an adaptive controller combining NN approximation with dynamics surface control is presented for trajectory tracking of an AUV. The computational load is reduced by introducing an NN learning method using minimal number of learning parameters. In [15], considering the unknown parameters, an adaptive fuzzy sliding mode control (SMC) is presented to steer a low-speed underactuated underwater vehicle and an experiment has justified the method. In [16], the NN-based controller is extended to control the multiple underwater robots and simulation results have been shown.

## I04 — p2-b1

> Although the NN and fuzzy-based adaptive controllers have the advantages on the approximation of the uncertainties and disturbances, it is still a challenging task to adjust its learning parameters in real applications.

## I05 — p2-b2

> As an effective tool to suppress disturbances for complex systems, SMC has attracted obvious attentions for the control plant with disturbances [10], [17]–[21]. In [22], a novel ESO-based adaptive control has been proposed for power converters to reject the load connected to the dc-link capacitor and the uncertain parameters. The experiment based on a real power converter prototype validate the control performance. In [9], a sliding mode tracking controller, which uses two sliding surfaces for surge tracking errors and lateral motion tracking errors, is applied to autonomous surface vessels. To address the control technical challenges for the switched stochastic systems, a novel dissipativity-based SMC is proposed in [17]. In [10], integral sliding mode controllers (ISMC) are proposed for trajectory tracking of ROVs. Because of the effect of the additional error-integral term, the ISMC has a more accurate trajectory tracking performance than the conventional SMC. To overcome the time-delay for the AUV control, an ISMC is introduced to overcome the problem that data acquisition rate could not be maintained sufficiently [23]. The major shortcoming of SMC is the chattering problem, which not only causes energy losses but also reduces the trajectory tracking smoothness. To reduce the chattering, several methods, such as the high-order sliding-mode controller [24], [25], disturbance compensation method [26], [27], and terminal sliding controller [28] have been proposed. In [26], a free chattering SMC is presented via an adaptive term, which continuously compensates for the unknown system dynamics of an ROV. In practice, sometimes, the upper bound of the uncertainties may be large and the SMC without a compensator will cause serious chattering. Therefore, it is necessary to design a compensator for the external disturbance to reduce chattering.

## I06 — p2-b3

> Another approach dealing with the unknown disturbance is to design an observer to estimate the unknown external disturbance of a robot, followed by the control design to compensate for the estimated disturbance. Such disturbance observers include sliding mode observer [12], [29], high-gain observer [30], [31], and extended state observer (ESO) [13], [32]. In [12], a sliding mode controller based on a sliding mode observer is proposed for a reusable launch vehicle. The observer is presented to estimate the unknown external disturbances and to reduce the control gain. In [30], a high-gain observer-based output feedback motion control that considers the unmodeled dynamics, measurement errors, model parameter variations, and unknown external environmental disturbances for observation class ROVs is presented. In [32], a backstepping control based on an ESO is proposed to handle mismatched disturbance of hydraulic systems. The designed observer estimates not only the model uncertainties but also the unmeasured states. In [13], by using an ESO, a backstepping control for a hydraulic system is presented to suppress large unknown external disturbances. The bandwidth of the observer is chosen in accordance with two conflicting aspects, the maximal load capability and the dynamic performance of system.

## I07 — p2-b4

> In this paper, we design an adaptive sliding mode-based controller for a general type of underwater robots, and experiment is carried on a test bed for underwater object grasping. Onboard sensors, including a depth sensor and an inertial measurement unit (IMU), are equipped to measure the depth and attitude of the robot. The position of the underwater robot is measured by an external vision positioning system (VPS), and some white lightings are equipped on the robot, which can be captured by the VPS to calculate the position of the robot. In such a case, there is no direct measurement of velocity of the robot. Then output feedback is required for our work as the direct differential of the position information may degrade the control performance. In such case, observes are always used to estimate the unmeasured states of the robot [5], [33]. A local recurrent NN-based adaptive terminal sliding mode state observer is presented to estimate the unmeasured velocity of an ROV in [5], which considers the uncertain dynamic model, the unmeasured states, and inaccurate thrust model. In [34], an NN-based adaptive observer is presented to address the problem of estimating the unavailable measurements of underwater vehicles’ velocities. In [35], a terminal sliding mode observer of an AUV is introduced to estimate the velocity, and the estimation error is guaranteed to converge to zero in a finite time. In [36], an adaptive backstepping control is introduced for human upper limbs in the presence of disturbances, unmodeled dynamics, and uncertainties. In [37], an output feedback tracking controller is designed to address the problem of steering a quadrotor with unknown disturbances and model uncertainties. The unmeasurable linear and angular velocities are estimated by a series of nonmodel-based filters. In [38], an attitude and speed controller is designed based on an adaptive second-order SMC for an unmanned aerial vehicle (UAV), and an extended observer is applied to estimate the unmeasured states and unknown external disturbances. In [39], a high-gain observer is implemented to estimate the full states of the electro-hydraulic system. It is noted that in the literature mentioned above, controllers designed for underwater robots in [1], [3], [4], [7], [8], [16], [18], [26], and [28] are verified by simulations, and other controllers in [6], [10], [15], [23], and [24] are verified by experiments.

## I08 — p2-b5

> In this paper, a disturbance compensation approach is utilized to eliminate the chattering based on multiple-input and multiple-output extend-state-observer (MIMO-ESO) with a simple structure. Motivated by the ESO model [32] and the high-gain observer [39], a MIMO-ESO is proposed to estimate the unknown disturbances and the unmeasured states. The bounds of the uncertainties are also estimated using the adaptive control technique. The Lyapunov analysis is involved to design the final control law. The proposed controller in this paper includes two parts, namely the equivalent controller and the switch controller, which guarantees the trajectory tracking error converge to zero theoretically. The proposed controller is successfully implemented on an underwater robot propelled by six thrusters. The main contributions can be summarized as follows.

## C01 — p2-b6

> 1) A novel adaptive MIMO-ESO is developed to estimate the unmeasured velocity and the unknown external disturbances of the underwater robot.

## C02 — p3-b2

> 2) Based on Lyapunov analysis, an adaptive MIMO-ESO-based ISMC is designed to ensure that the trajectory tracking error converge to zero.

## C03 — p3-b2

> 3) Comparative studies with the conventional potential difference (PD) control are carried out experimentally on an underwater robot to demonstrate the superior performance of the proposed control.

## I09 — p3-b2

> The remainder of this paper is organized as follows: Section II presents the robot model and formulates the problem. In Section III, the adaptive MIMO-ESO is derived to estimate the unknown disturbances and the unmeasured velocities. In Section IV, the ISMC is proposed. Experimental results are shown in Section V, followed by the conclusion of this paper in Section VI.

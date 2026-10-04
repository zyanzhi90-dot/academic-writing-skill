# Fuzzy2023 — Introduction 原文核验副本

来源：[Fixed-Time_Fuzzy_Control_of_Uncertain_Robots_With_Guaranteed_Transient_Performance.pdf](<../../文献资料/Fixed-Time_Fuzzy_Control_of_Uncertain_Robots_With_Guaranteed_Transient_Performance.pdf>)；§I，PDF p.1–2，印刷页 1041–1042。

PDF SHA-256：`06c3c5357819e6fa301b9afd29e63a05c47175d3288a373bd8f1d0c6fb8babfe`。

本文件完整保留 Introduction，止于 §II 标题之前；摘要、作者脚注、图注和下一节不计入引言。I 为实际 prose 段落，C 为贡献条目；同一段跨栏／跨页时合并。编号是本轮定位号，不是论文原有编号。

仅规范排版：NFKC 连字、行末断词、空白及首字下沉重接；原有词汇、语法、引用编号和句末标点不改。具体断词见 normalization-log.json。页面块与渲染图用于复核段落边界。

这些英文是所提供本地论文的原文证据，不是作者新稿，也不是建议逐字继承的科学断言。

## I01 — p1-b7, p1-b13

> FOR the robot dynamic systems, uncertain nonlinear terms usually exist due to the time-varying model parameters and the external disturbance during operation. Combined with adaptive control techniques, the neural network (NN) [1]–[5] and the fuzzy logic system (FLS) [6]–[8] have been widely applied to handle the tracking control problem for the uncertain robot systems because of their universal approximation capability. In [4], an NN control scheme has been proposed for a robot manipulator to achieve trajectory tracking with output constraints and input saturation. In [5], an admittance adaptation method has been proposed for robot–environment interaction, and the guaranteed trajectory tracking can be achieved by an NN-based controller. In [9], a number of advanced NN control algorithms have been introduced in detail for nonlinear systems, including robots. In [7], an adaptive robust fuzzy control scheme has been proposed for the uncertain two-degree-of-freedom (DOF) lower limb exoskeleton robot system to enhance the rehabilitation training. In [8], an adaptive fuzzy control scheme has been proposed for robotic systems to achieve fixed-time convergence and user-defined performance simultaneously. In [10], a novel adaptive controller based on active inference has been proposed for the robot to handle large model uncertainties and a large number DOFs, which enable to deal with the robot uncertainty, besides the NN and the FLS. It should be noted that large calculation is always required because of the weight iterative process in traditional fuzzy control schemes. In our previous work [11], a topology optimization method has been proposed to reduce the data amount for calculation and storage in wireless sensor networks, which is exciting because it may enlighten optimizing the FLS structure to reduce the computational complexity in our future work. Moreover, the desired transient performance and convergence time are rarely discussed simultaneously in most of the existing fuzzy control schemes.

## I02 — p1-b14

> In practice, the undesirable transient performance may lead to the system instability, even the system safety problems sometimes. Recently, the barrier Lyapunov functions (BLFs) have been widely used to achieve the state and output constraints in the nonlinear control problems [12]–[16]. In [12], with the exponential-type BLF, a practical event-triggered prescribed-time controller has been proposed for a class of space teleoperation systems. In [14], a new command filtered fuzzy controller has been proposed for a class of unknown nonlinear systems to handle full-state constraints and finite-time convergence simultaneously. In [16], an adaptive fuzzy leader-following tracking control scheme has been proposed for heterogeneous nonlinear multiagent systems with finite-time output constraints. In this article, a novel symmetric BLF is designed to guarantee the desired transient performance of the robot system.

## I03 — p1-b15, p2-b1

> In many industrial systems, the system states are required to achieve fast convergence speed for better control performance. There have been some proposed research works focused on the convergence time of the systems [17]–[19]. In [17], an adaptive observer-based fuzzy controller has been proposed for a class of strict-feedback nonlinear systems to achieve finite-time convergence. In [18], an adaptive finite-time sliding-mode control scheme has been proposed for a class of nonlinear systems with some matched uncertainties. Nevertheless, for the existing finite-time control schemes, the convergence time of the systems is always related to the initial conditions, which are sometimes unavailable. To improve the control performance, the fixed-time control schemes have been proposed and applied in the nonlinear control community [20]–[22]. In [20], a novel fixed-time adaptive fuzzy control scheme combined with the BLF technique has been proposed for uncertain nonstrict-feedback nonlinear systems. In [21], an adaptive event-based fixed-time control scheme has been proposed for the active vehicle suspension systems, and the predefined constraints can be guaranteed.

## I04 — p2-b2

> Motivated by the above research works, the problem of fixed-time tracking control is discussed for uncertain robot systems based on the FLS and the BLF technique in this article. The major contributions of our work can be listed as follows.

## C01 — p2-b3

> 1) A novel symmetric BLF is designed to avoid the violation of the output constraints; thus, the desired transient performance of the robot system can be guaranteed.

## C02 — p2-b3

> 2) A novel adaptive law is proposed such that the boundedness of all the closed-loop signals can be proved. Then, the assumption that the weight estimation is bounded in recent fixed-time control research [23]–[25] can be relaxed.

## C03 — p2-b3

> 3) The tracking performance of the robot system can achieve practical fixed-time convergence regardless of the initial conditions.

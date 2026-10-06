# P05 — 完整 Introduction 原文定位

出版 PDF：`文献资料/Composite-Learning-Based_Adaptive_Neural_Control_for_Dual-Arm_Robots_With_Relative_Motion.pdf`。

正文段落以 I 编号，贡献条目以 C 编号；C 是其引导段下的列表条目，不另造正文段落。

仅恢复版面阅读顺序、跨栏/跨页续段、首字母、合字与行末断词；不润色出版原文。原始文本块和页面图像另行保留。

## I01

PDF p.1 / 刊页 1010 左栏 (p1-b8) → PDF p.1 / 刊页 1010 右栏 (p1-b15)

RECENTLY, coordination control of dual-arm robots has received increasing attention due to its superiority compared with traditional single-arm robot systems, including stronger payload capability, larger workspace, and more flexibility. Thus, the dual-arm robots have been involved in many high technology applications, such as intelligent assembly, out-space repairing, and elderly people assistance [1]–[3]. However, controlling the dual-arm robots is challenging due to the increase of complexity in motion control and path planning. Therefore, advanced control technologies have been extensively studied for dual-arm robots in past decades [4]–[11].

## I02

PDF p.1 / 刊页 1010 右栏 (p1-b16)

An adaptive decentralized control scheme was proposed to address the object handling problem of a cooperative robot, where an implicit force control scheme was employed to simultaneously regulate the force and position [9]. In [10], a decentralized control structure for multiple mobile manipulators was developed, where the internal forces were constrained by employing an augmented object model for the multiple systems with a virtual linkage. In [11], the loading problem for multiple manipulators was addressed by analyzing the grasp space of the robot. Note that the abovementioned controllers were developed under the assumption that the object is firmly held by the robotic arms such that no relative motion occurred between the arms and the objects. However, in practical applications, such as polishing, grinding, and welding, the robot end-effectors need to operate along the object’s surface, where sliding movements usually happened between the robotic arm and the object [12]–[14].

## I03

PDF p.1 / 刊页 1010 右栏 (p1-b17)

In this respect, the coordination control of dual-arm robots with relative motion deserves further investigation. The relative motion is also known as the asymmetric bimanual task. In [15], a relative impedance controller was developed by using a relative Jacobian method such that the dual-arm system can be treated as a single-arm robotic system. In [16], a brain-actuated control architecture was proposed for dual-arm robots to perform the asymmetric bimanual task, where electroencephalogram signals and visual stimulation were employed to send control command through a brain–machine interface. In these works, however, the controllers were designed under the assumption that the robot dynamics are fully available, while the stability analysis of the contact force between the robotic arm and the object was not given.

## I04

PDF p.1 / 刊页 1010 右栏 (p1-b18) → PDF p.2 / 刊页 1011 左栏 (p2-b1)

The dynamic model of the robot system is of great importance in the controller design [17]–[22], but it is often unavailable in practice. For example, in carrying tasks, the dynamics of the grasped object is hard to obtain in advance. Without a precise dynamics model, the model-based control method became invalid and may cause degeneration of the control performance. Hence, advanced control strategies have been presented to compensate for the model uncertainties. Neural network (NN) is well known by its advantages in alleviating modeling difficulties of nonlinear systems due to the powerful approximation ability [23]. Thus, NN control synthesizes have been widely implemented in developing controllers for nonlinear robotic systems [24]–[32].

## I05

PDF p.2 / 刊页 1011 左栏 (p2-b2)

A fuzzy neural network control approach was presented for pure-feedback stochastic systems by using a semi-Nussbaum function [33]. In [34], an adaptive NN control strategy was proposed for an uncertain robot to ensure the state not to violate the prescribed constraints. Recently, a sensorless admittance controller was designed to solve the unknown environments’ interaction by using the NN technique [35]. Significant works have been done in [36]–[38] to make a complex topic understandable about modeling and control of flapping-wing flying robots to the average reader. While the NN controllers have been successfully developed in the abovementioned work, a major limitation for existing adaptive NN control schemes lies in that only convergence of the tracking errors can be achieved, instead of the convergence of NN weights to their ideal values. Without the convergence of NN weights, the NN compensation can be hardly accomplished, and the system performance may be degraded and, eventually, became unstable. In this respect, developing a novel control scheme with guaranteed NN convergence is of great significance.

## I06

PDF p.2 / 刊页 1011 左栏 (p2-b3)

In our recent work [39], a filtered operation was presented to control the robotic arm with finite-time convergence under a linear-in-parameter (LIP) robotic dynamic model. Nevertheless, the guaranteed convergence of the NN weights is more difficult. It is well known that the persistent excitation (PE) condition is important to guarantee the estimation convergence [40]. However, in practice, it is very stringent to ensure the PE condition of neural networks due to the sparse characteristics of the NN regressor vector. Recent research of neural networks in [41] presented a partial persistent excitation (PPE) condition instead of the traditional PE condition. It has been proven that, for the radial basis function neural network (RBFNN) defined in a regular lattice, neural nodes could be partially activated for any recurrent NN inputs trajectory remained in this local region [41]. In the subsequent work [42], this idea was employed for the control design of nonlinear strict-feedback systems to guarantee the system stability and accurate NN approximation. However, the NN inputs still need to satisfy the condition of recurrent trajectory, and a small input excitation strength may lead to slow learning speed.

## I07

PDF p.2 / 刊页 1011 左栏 (p2-b4) → PDF p.2 / 刊页 1011 右栏 (p2-b6)

The work in [43] indicates that parameter convergence can be improved if certain information of the estimation error can be integrated into the adaptation. In [44], a novel parameter estimation law was proposed for a robotic system with unknown dynamics by using a sliding mode technique and a finite-time estimator. In [45], the estimation error was integrated into the adaptation scheme of a class of nonlinear systems to achieve the convergence of NN weights. Motivated by the abovementioned idea, in this article, we develop a composite learning controller for the dual-arm robot to perform bimanual relative motion tasks. To the best of our knowledge, few studies have investigated the learning control in the frame of the dual-arm robot systems subject to relative motion and unknown dynamics. Moreover, different from the work in [46], a PPE condition is also introduced in the estimation scheme to achieve a relaxation of the requirement of the PE condition. In comparison to the method in [45], the estimation error of the NN weights is properly expressed and employed to enhance the approximation of the neural network.

## I08

PDF p.2 / 刊页 1011 右栏 (p2-b7)

The objective of this article is to develop a control framework for dual-arm robot tracking control under relative motion. The main contributions of this article can be summarized as follows.

## C1

PDF p.2 / 刊页 1011 右栏 (p2-b8)

1) A novel neural control framework is developed for dual-arm robot systems to perform asymmetric bimanual tasks with no prior knowledge of the dynamics.

## C2

PDF p.2 / 刊页 1011 右栏 (p2-b8)

2) A novel composite learning algorithm is designed for NN weights adaptation such that information of the estimate errors could be appropriately integrated into the adaptation law to improve the estimation performance.

## C3

PDF p.2 / 刊页 1011 右栏 (p2-b8)

3) A partial persistent condition is introduced for the adaptation of NN weights such that the requirement of conventional PE condition can be greatly relaxed.

## I09

PDF p.2 / 刊页 1011 右栏 (p2-b8)

In the following sections, the system modeling and control design procedures are detailed. Section II discusses the system modeling of the dual-arm robot in addition to some preliminaries. Section III presents the design of the composite learning control algorithm by utilizing a command filtered backstepping technique with stability analysis. Section IV demonstrates the simulation results. A brief conclusion is given in Section V.

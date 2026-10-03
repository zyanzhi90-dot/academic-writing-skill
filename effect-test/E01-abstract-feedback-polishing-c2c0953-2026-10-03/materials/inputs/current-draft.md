**English abstract**

This paper proposes a Stable Estimator of Dynamical Systems (SEDS) for learning robot point-to-point motions from demonstrations. A Gaussian mixture model and Gaussian mixture regression are used to learn a nonlinear autonomous dynamical system that maps the current position to velocity. SEDS optimizes the model parameters under stability constraints to reproduce the demonstrated motions while ensuring convergence to the target. The constraints require all local linear dynamical systems to share a common target and the symmetric part of each local system matrix to be negative definite. These sufficient conditions guarantee global asymptotic stability of the learned motion model at the target, with the generated velocity tending to zero. The autonomous model can respond to spatial and temporal perturbations and adjust to target changes without relearning its parameters. Numerical simulations of 20 human handwriting motions are used to evaluate motion reproduction. Experiments with iCub and Katana-T robot arms demonstrate reproduction of the position and velocity characteristics of the demonstrations and motion generation from different initial positions to the target. The Katana-T experiments further show that the generated trajectories adjust to a target moved during execution.

**中文翻译**

本文提出稳定动力系统估计器（SEDS），用于从示范中学习机器人的点到点运动。该方法通过高斯混合模型和高斯混合回归学习一个非线性自治动力系统，将当前位置映射为速度。SEDS 在稳定性约束下优化模型参数，以再现示范运动，同时保证向目标收敛。这些约束要求所有局部线性动力系统具有共同目标，且各局部系统矩阵的对称部分负定。这些充分条件保证学得的运动模型在目标处全局渐近稳定，生成的速度也趋于零。自治模型能够响应空间和时间扰动，并在无需重新学习参数的情况下适应目标变化。研究通过对20种人类手写运动进行数值模拟来评价运动再现能力。iCub 和 Katana-T 机械臂实验展示了对示范中位置及速度特点的再现，以及从不同初始位置生成到达目标的运动。Katana-T 实验进一步表明，当目标在执行过程中被移动时，生成的轨迹会相应调整。

**作者说明**

表达以 A06 为主要语言参考，结合 A02 的约束—保证关系及 A05、A07 的验证写法。全局渐近稳定的保证仅针对所学运动模型；时间扰动响应表述为模型能力，目标移动适应则有具体机器人实验支持。
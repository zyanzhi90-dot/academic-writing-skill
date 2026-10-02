**English abstract**

This paper proposes the Stable Estimator of Dynamical Systems (SEDS) for learning point-to-point robot motions from demonstrations. SEDS fits a nonlinear autonomous dynamical system to the demonstrations under sufficient conditions for global asymptotic stability at the target. These conditions ensure that model trajectories converge to the target from any initial state and that the rate of change tends to zero. A Gaussian mixture model and Gaussian mixture regression are used to represent motion as a combination of local linear dynamical systems with state-dependent weights. The learned model can respond to spatial and temporal perturbations by generating motion from the current state rather than following a prescribed time schedule. Changes in the target position can be accommodated without relearning the model. Simulations of 20 handwriting motions assess reproduction of the demonstrated trajectories. Experiments with the iCub and Katana-T robot arms demonstrate reproduction of position and velocity characteristics and motion generation toward the target from different initial positions. In the Katana-T experiments, the generated trajectories adjust to a target moved during execution.

**中文翻译**

本文提出稳定动力系统估计器（SEDS），用于从示范中学习机器人的点到点运动。SEDS 在保证目标处全局渐近稳定的充分条件下，用非线性自治动力系统拟合示范。这些条件确保模型轨迹从任意初始状态出发均收敛到目标，且状态变化率趋于零。高斯混合模型和高斯混合回归将运动表示为多个局部线性动力系统的组合，其权重随当前状态变化。学习得到的模型根据当前状态生成运动，而不依赖预先安排的时间进度，因此能够响应空间和时间扰动。目标位置发生变化时，无需重新学习模型即可作出调整。通过20种手写运动的模拟，评估模型对示范轨迹的再现能力。iCub 和 Katana-T 机械臂实验展示了对示范运动的位置和速度特点的再现，以及从不同初始位置生成朝向目标的运动。在 Katana-T 实验中，目标在执行期间移动后，生成的轨迹相应调整。

**写作说明**

以 A06 的方法开篇、明确主语和对象交接为主要写法，结合 A02 的设计—保证衔接及 A05 的机制—能力表达，重新组织为“方法与保证—运动表示与调整能力—模拟与实机证据”。删去矩阵判据等支持细节；全局渐近稳定性限定于学习模型，目标移动实验仅承担空间调整的证据作用。
**English abstract**

This paper proposes a stable estimator of dynamical systems (SEDS) for learning robot point-to-point motions from multiple demonstrations. A Gaussian mixture model and Gaussian mixture regression are used to represent motion as a nonlinear autonomous dynamical system. SEDS incorporates stability constraints into model parameter optimization to reproduce the demonstrated motions while ensuring global asymptotic stability of the learned dynamical system at the target. The autonomous motion generator can respond to spatial and temporal perturbations during execution and continue towards the target. Numerical simulations using human handwriting data are carried out to evaluate motion reproduction. Experiments on robot arm tasks demonstrate that the generated motions reproduce demonstrated position and velocity patterns and reach the target from different initial positions. Experiments with the Katana-T arm also show that the generated trajectories adjust to a displaced target during execution without relearning the model.

**中文翻译**

本文提出稳定动力系统估计器（SEDS），用于从多个示范中学习机器人的点到点运动。该方法利用高斯混合模型和高斯混合回归，将运动表示为非线性自治动力系统。SEDS 将稳定性约束纳入模型参数优化，以再现示范运动，同时保证学习得到的动力系统在目标处全局渐近稳定。自治运动生成器能够在执行过程中响应空间扰动和时间扰动，并继续朝目标运动。研究利用人类手写运动数据开展数值模拟，以评价运动再现能力。机械臂任务实验表明，在所测试任务中，生成的运动能够再现示范中的位置及速度特点，并从不同初始位置到达目标。Katana-T 机械臂实验还表明，执行期间目标位置改变后，生成的轨迹会相应调整，无需重新学习模型。

**说明：** 摘要将稳定性保证限定于所学动力系统，未扩展为真实机器人闭环保证。手写模拟仅表述评价目的；时间扰动响应表述为模型能力；移动目标的实机发现明确归于 Katana-T。英文以 A06、A07 为主要表达参考，并采用 A02 的设计—保证关系及 A04 的评价目的表达。
**English abstract**

This paper proposes residual reinforcement learning for robotic manipulation involving contact, friction and movable objects. The control input is the sum of the outputs of a fixed feedback controller and a residual policy learned from robot and object states. The feedback controller guides robot motion towards geometric goals, and the residual policy learns corrections for contact, friction and object dynamics. Reinforcement learning optimizes the residual policy to maximize the expected return for the full task under the combined control. The method is evaluated in simulation and on a seven-degree-of-freedom Sawyer arm by inserting a grasped block between two upright blocks while keeping them upright and in their target positions. The results demonstrate that the residual method requires fewer interaction samples and achieves better final performance than reinforcement learning using the same underlying algorithm without a baseline controller. In real-robot tests with initially misaligned blocks, the residual method achieves 15 successful insertions in 20 trials, compared with 2 in 20 for the hand-designed controller. In a separate simulation-to-real experiment with the two outer blocks fixed, a policy trained in simulation is used as the fixed baseline. The residual policy learns to complete insertion in fewer than 1,000 real-robot interaction steps.

**中文翻译**

本文提出一种残差强化学习方法，用于涉及接触、摩擦和可移动物体的机器人操作。控制输入由固定反馈控制器的输出与根据机器人和物体状态学习的残差策略输出相加得到。反馈控制器引导机器人运动以实现几何目标，残差策略则学习针对接触、摩擦和物体动力学的修正动作。强化学习在组合控制作用下优化残差策略，以最大化完整任务的期望回报。该方法在仿真和七自由度 Sawyer 机械臂上进行评估，任务是在两个竖立块之间插入夹持的第三个块，同时使两侧块保持竖立并处于目标位置。结果表明，与采用相同底层算法但不使用基准控制器的强化学习相比，残差方法所需的交互样本更少，最终表现更好。在竖立块初始方向错位的实机测试中，残差方法在20次试验中成功完成15次插入，人工设计控制器则成功2次。在另一个将两侧块固定的仿真到实机实验中，仿真训练得到的策略被用作固定基准。残差策略在不足1,000个实机交互时间步内学会完成插入。

**摘要外说明**

| 统一术语 | 中文含义与使用范围 |
|---|---|
| residual reinforcement learning | 残差强化学习 |
| fixed baseline | 固定基准；常规设置采用反馈控制器，迁移实验采用仿真训练策略 |
| residual policy | 残差策略；其输出与固定基准的输出相加 |

表达主要参照 A06、A07 的方法开篇、对象交接和验证句式，并借鉴 A05 的控制作用与比较表达。科学结论仅来自作者事实包：样本效率及最终表现对应 F02，错位实机对照对应 F03，固定两侧块的迁移结果对应 F06。
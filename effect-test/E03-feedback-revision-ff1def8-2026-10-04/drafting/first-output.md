**人工反馈修订稿（human-feedback revision）**

**English abstract**

This paper proposes residual reinforcement learning for robotic manipulation involving contact, friction and movable objects. Conventional feedback control can exploit the known structure of robot motion through explicit models, but contact and friction are difficult to model accurately. The control input is the sum of the outputs of a fixed feedback controller and a residual policy learned from robot and object states. The feedback controller guides robot motion towards geometric goals, and the residual policy learns corrections for contact, friction and object dynamics through interaction with the environment. Reinforcement learning optimizes the residual policy to maximize the expected return for the full task under the combined control. The method is evaluated in simulation and on a seven-degree-of-freedom Sawyer arm by inserting a grasped block between two upright blocks while keeping them upright and in their target positions. The results demonstrate that the residual method requires fewer interaction samples and achieves better final performance than reinforcement learning using the same underlying algorithm without a baseline controller. In real-robot tests with initially misaligned blocks, the residual method achieves 15 successful insertions in 20 trials, compared with 2 in 20 for the hand-designed controller.

**中文翻译**

本文提出一种残差强化学习方法，用于涉及接触、摩擦和可移动物体的机器人操作。传统反馈控制能够通过显式模型利用机器人运动的已知结构，但接触和摩擦难以准确建模。控制输入由固定反馈控制器的输出与根据机器人和物体状态学习的残差策略输出相加得到。反馈控制器引导机器人运动以实现几何目标，残差策略则通过与环境交互，学习针对接触、摩擦和物体动力学的修正动作。强化学习在组合控制作用下优化残差策略，以最大化完整任务的期望回报。该方法在仿真和七自由度 Sawyer 机械臂上进行评估，任务是在两个竖立块之间插入夹持的第三个块，同时使两侧块保持竖立并处于目标位置。结果表明，与采用相同底层算法但不使用基准控制器的强化学习相比，残差方法所需的交互样本更少，最终表现更好。在竖立块初始方向错位的实机测试中，残差方法在20次试验中成功完成15次插入，人工设计控制器则成功2次。

**实际修改依据**

- 参照 A08 的连续句逻辑，新增“已知模型结构—接触与摩擦建模难点”的组合理由，并在原分工句中补明残差修正通过环境交互学习获得（F07–F08、F15）。
- 保留 A06 式方法开篇及现稿准确的信号相加、完整任务优化和验证表达；对照 A07 的设计—作用—验证推进检查句间衔接，没有逐句改写。
- 删除固定侧块的仿真到实机分支及千步结果，保留样本效率与最终表现比较、错位实机15/20对2/20的关键证据及其条件（F02–F03）。
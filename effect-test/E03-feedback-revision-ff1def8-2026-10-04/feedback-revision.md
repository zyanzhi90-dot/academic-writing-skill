# E03 人工反馈修订稿

本稿使用 `ff1def8` 的当前 Writing 候选及声明依赖，以 `gpt-6.1-sol / high` 完成一次人工反馈修订，再作两处交付检查中的局部精修。模型原始修订输出另存；不计作自主写作或独立迁移通过，待负责人验收。

**English abstract**

This paper proposes residual reinforcement learning for robotic manipulation involving contact, friction and movable objects. Conventional feedback control can exploit the known structure of robot motion through explicit models, but contact and friction are difficult to model accurately. The control input is the sum of the outputs of a fixed feedback controller and a residual policy based on robot and object states. The feedback controller guides robot motion towards geometric goals, and the residual policy learns corrections for contact, friction and object dynamics through interaction with the environment. Reinforcement learning optimizes the residual policy to maximize the expected return for the full task under the combined control. The method is evaluated in simulation and on a Sawyer arm by inserting a grasped block between two upright blocks while keeping them upright and in their target positions. The results demonstrate that the residual method requires fewer interaction samples and achieves better final performance than reinforcement learning using the same underlying algorithm without a baseline controller. In real-robot tests with initially misaligned blocks, the residual method achieves 15 successful insertions in 20 trials, compared with 2 in 20 for the hand-designed controller.

**中文译文**

本文提出一种残差强化学习方法，用于涉及接触、摩擦和可移动物体的机器人操作。传统反馈控制能够通过显式模型利用机器人运动的已知结构，但接触和摩擦难以准确建模。控制输入由固定反馈控制器的输出与基于机器人和物体状态的残差策略输出相加得到。反馈控制器引导机器人运动以实现几何目标，残差策略则通过与环境交互，学习针对接触、摩擦和物体动力学的修正动作。强化学习在组合控制作用下优化残差策略，以最大化完整任务的期望回报。该方法在仿真和 Sawyer 机械臂上进行评估，任务是在两个竖立块之间插入夹持的第三个块，同时使两侧块保持竖立并处于目标位置。结果表明，与采用相同底层算法但不使用基准控制器的强化学习相比，残差方法所需的交互样本更少，最终表现更好。在竖立块初始方向错位的实机测试中，残差方法在20次试验中成功完成15次插入，人工设计控制器则成功2次。

**实际修改依据**

- 增补模型结构可利用、接触与摩擦难以准确建模的组合理由，并把残差修正接到环境交互学习。借鉴 A08 的能力—难点—互补设计关系，保持方法开篇。
- 保留信号相加与完整任务回报优化；将状态表述为策略输入，交互表述为学习来源，避免混淆两种关系。
- 删除固定侧块的迁移分支及千步结果，保留对纯 RL 的样本与最终表现比较，以及初始错位实机的 15/20 对 2/20。两项分别支持利用既有结构的优势与接触修正的作用，不展开实验清单。
- 保留 Sawyer 和块插入任务，删去自由度数；前者限定实机证据，后者不影响本稿的贡献或结论范围。其余准确成熟的原句保留。

逐句、关键词组及原文依据见 [修改核对](revision-basis.md)；模型未经改动的修订输出见 [原始输出](drafting/first-output.md)。

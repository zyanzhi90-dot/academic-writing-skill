**English abstract**

This paper proposes an impedance learning method for rigid robotic manipulators interacting with unknown, time-varying environments. The method combines an outer impedance learning loop with an inner adaptive position controller. The outer loop adjusts time-varying damping and stiffness to reduce a weighted cost of motion and interaction-force-integral tracking errors over repeated interactions, while the desired inertia remains fixed. Gradient following is combined with iterative improvement based on output errors and their time derivatives, without requiring prior identification of an exact environment model. The learned impedance generates a virtual reference trajectory for the inner controller. The inner controller augments proportional–derivative control with adaptive compensation and does not require a robot dynamics regressor or the virtual reference acceleration. Theoretical analysis establishes asymptotic tracking of the virtual reference trajectory and bounded closed-loop signals under the stated dynamics and reference assumptions and suitable control and adaptation parameters. Numerical simulation results demonstrate interaction-cost improvements for the two tested task-weight settings. Experiments involving repeated contact between a robot wrist and a human hand further show that a higher trajectory-tracking weight increases stiffness and reduces position error, whereas a lower weight decreases stiffness and produces more compliant motion with larger position errors.

**中文翻译**

本文提出一种阻抗学习方法，用于刚性机械臂与未知时变环境之间的物理交互。该方法将外环阻抗学习与内环自适应位置控制相结合。外环在重复交互过程中调整时变阻尼和刚度，以降低由运动跟踪误差和交互力时间积分跟踪误差构成的加权代价，同时保持期望惯性不变。该方法将梯度跟随与基于输出误差及其时间导数的迭代改进相结合，无需预先辨识精确的环境模型。所学阻抗为内环控制器生成虚拟参考轨迹。内环控制器在比例—微分控制中加入自适应补偿，无需机器人动力学回归矩阵或虚拟参考加速度。在所述动力学与参考轨迹假设成立、且控制和自适应参数选择适当的条件下，理论分析证明了对虚拟参考轨迹的渐近跟踪以及闭环信号的有界性。数值仿真结果表明，在所测试的两种任务权重设置下，交互代价得到改善。机器人腕部与人手重复接触的实验进一步表明，较高的轨迹跟踪权重使刚度增大、位置误差减小，而较低的权重使刚度减小，并产生位置误差更大但更柔顺的运动。

**作者说明**

- 组织与表达以 A06 的方法开篇和对象交接为主，结合 A07 的设计—分析—验证推进，以及 A04、A05 的控制分工和机制表达；参考文献中的科学结论未引入本研究。
- “无需精确环境模型”仅指无需预先精确辨识。外环推导仍受线性时变环境模型及相应收敛条件约束；内环保证的对象是虚拟参考轨迹。
- 第二种实机设置的代价曲线尚待复核，因此摘要仅报告两种实机设置均可核对的刚度与位置误差变化。
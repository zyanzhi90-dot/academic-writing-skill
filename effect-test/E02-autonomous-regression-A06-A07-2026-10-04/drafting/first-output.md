**English abstract**

This paper proposes an impedance learning method for rigid robot manipulators interacting with unknown, time-varying environments. An outer learning loop combines gradient following and iterative improvement to adjust the desired damping and stiffness, while the desired inertia remains fixed. The learning is formulated for a linear time-varying mass–damper–spring environment and does not require prior identification of its exact parameters. A weighted interaction-error cost specifies the trade-off between trajectory tracking and tracking the time integral of interaction force. An inner adaptive position controller is designed to track the virtual reference trajectory generated from the learned impedance without requiring a robot dynamics regressor. Theoretical analysis establishes bounded closed-loop signals and asymptotic tracking of the virtual reference trajectory when its velocity and acceleration are bounded and the control and adaptation gains satisfy the required conditions. Numerical simulation results demonstrate task-cost improvement for different trajectory-tracking weights. Experiments with repeated robot wrist–human hand contact further demonstrate that a higher trajectory-tracking weight increases stiffness and reduces position error, whereas a lower weight decreases stiffness and produces more compliant motion.

**中文翻译**

本文提出一种阻抗学习方法，用于刚性机械臂与未知、时变环境之间的交互。外环学习结合梯度跟随与迭代改进，调整期望阻尼和刚度，同时保持期望惯性固定。该学习方法针对线性时变质量—阻尼—弹簧环境建立，无需预先辨识环境参数的精确数值。加权交互误差代价规定了轨迹跟踪与交互力时间积分跟踪之间的折中。内环自适应位置控制器用于跟踪由所学阻抗生成的虚拟参考轨迹，无需机器人动力学回归矩阵。理论分析表明，当虚拟参考轨迹的速度和加速度有界，且控制增益与自适应增益满足相应条件时，闭环信号保持有界，实际位置渐近跟踪虚拟参考轨迹。数值仿真结果表明，不同轨迹跟踪权重下的任务代价均得到改善。机器人腕部与人手反复接触的实验进一步表明，较高的轨迹跟踪权重使刚度增加、位置误差减小，而较低的权重使刚度降低，机器人运动更为柔顺。

**作者说明**

- 以 A06 的方法开篇和对象交接为主要表达依据，结合 A07 的设计—分析—验证推进、A05 的阻抗学习表达及 A04 的理论保证表述，组织为“学习设计—控制实现—理论支持—验证结果”。
- 渐近跟踪保证仅针对内环虚拟参考轨迹；摘要未宣称外环无条件收敛或全局最优，也未将第二种实机设置尚待复核的代价变化写作已证实结果。
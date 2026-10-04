**English abstract**

Fixed impedance parameters may be overly conservative or fail to accommodate changing environment dynamics during physical interaction. This paper proposes an impedance learning method for rigid manipulators interacting with unknown, time-varying environments. An outer learning loop adjusts time-varying damping and stiffness according to a weighted cost of position and integrated interaction-force errors. The outer loop combines gradient following with iterative improvement, which constructs updates from output errors and their rates of change without identifying an exact environment model. The impedance relation generates a virtual reference trajectory for the inner position controller to realize the learned impedance. Adaptive compensation is incorporated into proportional–derivative control to track the virtual reference trajectory without requiring a robot dynamics regressor. Under the assumed robot dynamics, bounded reference velocity and acceleration, and appropriate gain conditions, inner-loop analysis establishes asymptotic tracking of the virtual reference trajectory and bounded closed-loop signals. Numerical simulations and repeated wrist–hand interaction experiments demonstrate improved trajectory tracking at higher stiffness or greater compliance at lower stiffness, depending on the task weights. In the trajectory-focused experiment, position error and task cost decrease over iterations.

**中文翻译**

固定阻抗参数可能过于保守，也可能无法适应物理交互过程中环境动力学的变化。本文提出一种面向刚性机械臂与未知时变环境交互的阻抗学习方法。外环学习根据位置误差和交互力时间积分误差的加权代价，调整随时间变化的阻尼与刚度。外环结合梯度跟随与迭代改进，其中迭代改进利用输出误差及其变化率构造更新，无需辨识精确的环境模型。阻抗关系生成虚拟参考轨迹，供内环位置控制器实现所学阻抗。比例—微分控制中引入自适应补偿，使机械臂跟踪虚拟参考轨迹，无需机器人动力学回归矩阵。在所假定的机器人动力学、参考速度和加速度有界以及适当增益条件下，内环分析证明了对虚拟参考轨迹的渐近跟踪和闭环信号的有界性。数值仿真与重复腕部—人手交互实验表明，根据任务权重的不同，机器人表现为在较高刚度下提高轨迹跟踪精度，或在较低刚度下提高柔顺性。在侧重轨迹跟踪的实验中，位置误差与任务代价随迭代减小。

**作者说明**

- 调整了论述组织，将外环学习与内环实现连成方法主线。主要参照 A06、A07，局部借鉴 A08、A05、A04 的组织和普通英文表达；范例科学内容未作为本研究事实。
- 实际学习的参数仅为阻尼和刚度，期望惯性固定为表观惯性。外环推导限于所述线性时变质量—阻尼—弹簧环境及相应收敛条件，无需精确环境模型不意味着无需先验知识或调参。
- 渐近跟踪保证仅针对虚拟参考轨迹，不等于交互中实际轨迹无偏差地跟踪任务期望轨迹。
- 验证保留任务权重对应的精度—柔顺性取舍，以及侧重轨迹跟踪的实机设置中的代价下降。第二种实机设置的代价下降尚未核实，未纳入结论。
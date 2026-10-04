**英文摘要（nature-writing 阶段稿）**

Fixed impedance parameters can be overly conservative or fail to accommodate changes in an unknown environment. This paper proposes an impedance learning method for rigid robot manipulators to adapt their interaction behaviour through repeated trials. An outer learning loop combines gradient following with iterative improvement to update time-varying damping and stiffness according to a task-dependent interaction error cost, while keeping the desired inertia fixed. The iterative improvement scheme uses output errors and their rates of change to update the impedance without prior identification of an internal environment model. An inner adaptive position controller is designed to track the virtual reference trajectory generated from the target impedance. Adaptive compensation is incorporated into a proportional–derivative control law to account for uncertain robot dynamics without requiring a dynamics regressor or predefined numerical bounds on the dynamics. Theoretical analysis establishes asymptotic tracking of the virtual reference trajectory and bounded closed-loop signals for the considered manipulator dynamics, assuming bounded reference velocity and acceleration and appropriately chosen control and adaptation parameters. Numerical simulations and repeated wrist–hand interaction experiments demonstrate that, under a higher trajectory-tracking weight, stiffness increases and position error decreases over successive trials. Under a lower weight, stiffness decreases and the robot exhibits more compliant motion.

**中文翻译**

固定的阻抗参数可能过于保守，也可能无法适应未知环境中的变化。本文提出一种面向刚性机械臂的阻抗学习方法，通过重复试次调整机器人的交互行为。外环学习结合梯度跟随与迭代改进，根据任务相关的交互误差代价更新随时间变化的阻尼和刚度，同时保持期望惯性固定。迭代改进方案利用输出误差及其变化率更新阻抗，无需事先辨识环境内部模型。内环自适应位置控制器用于跟踪由目标阻抗生成的虚拟参考轨迹。比例—微分控制律中引入自适应补偿，以处理不确定的机器人动力学，无需动力学回归矩阵，也无需预先给定动力学界限的具体数值。对于所考虑的机械臂动力学，在参考速度与加速度有界、控制及自适应参数适当选取的条件下，理论分析确立了对虚拟参考轨迹的渐近跟踪以及闭环信号的有界性。数值仿真与重复腕部—人手交互实验表明，在较高的轨迹跟踪权重下，刚度随试次增加，位置误差减小。在较低权重下，刚度降低，机器人表现出更柔顺的运动。

**作者说明**

- 表达以 A06 为语言锚点，主要借鉴 A07 的设计—作用—分析—验证推进，并结合 A05、A08 的交互任务与方法分工表达。
- 外环分析限于所述线性时变环境模型及迭代收敛条件；摘要未主张任意环境下的无条件收敛或全局最优。
- 验证保留仿真与实机共同支持的刚度、位置误差及柔顺性取舍。第二种实机设置的代价变化尚待复核，未据此宣称全部实验代价均下降。
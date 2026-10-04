**英文摘要**

Fixed impedance parameters can be overly conservative or fail to accommodate changing environment dynamics. This paper proposes a dual-loop impedance learning method for rigid robot manipulators interacting with unknown linear time-varying environments. The outer loop combines gradient following with iterative improvement to update time-varying desired damping and stiffness through repeated trials according to a task-dependent interaction error cost, while keeping the desired inertia fixed at the apparent inertia. The iterative improvement scheme uses output errors and their rates of change to construct the updates without prior identification of an internal environment model. An inner adaptive position controller is designed to track the virtual reference trajectory generated from the target impedance, so that the learned impedance can be realized in robot motion. Adaptive compensation is incorporated into a proportional–derivative-like control law to account for uncertain robot dynamics without requiring a dynamics regressor or predefined numerical bounds on the dynamics. For the considered manipulator dynamics, theoretical analysis establishes asymptotic tracking of the virtual reference trajectory and bounded closed-loop signals, provided that the virtual reference velocity and acceleration are bounded and the control and adaptation parameters are appropriately chosen. Numerical simulation results and repeated wrist–hand interaction experiments demonstrate that the learned impedance improves trajectory tracking when accuracy is prioritized and yields more compliant motion when the tracking weight is reduced.

**中文翻译**

固定的阻抗参数可能过于保守，也可能无法适应环境动力学的变化。本文提出一种双环阻抗学习方法，用于刚性机械臂与未知线性时变环境之间的交互。外环结合梯度跟随与迭代改进，通过重复试次，根据任务相关的交互误差代价更新随时间变化的期望阻尼和刚度，同时将期望惯性固定为表观惯性。迭代改进方案利用输出误差及其变化率构造更新，无需事先辨识环境内部模型。内环自适应位置控制器用于跟踪由目标阻抗生成的虚拟参考轨迹，从而使所学阻抗能够在机器人运动中实现。类比例—微分控制律中引入自适应补偿，以处理不确定的机器人动力学，无需动力学回归矩阵，也无需预先给定动力学界限的具体数值。对于所考虑的机械臂动力学，在虚拟参考速度与加速度有界、控制及自适应参数适当选取的条件下，理论分析确立了对虚拟参考轨迹的渐近跟踪以及闭环信号的有界性。数值仿真结果与重复腕部—人手交互实验表明，当任务优先考虑轨迹精度时，所学阻抗改善轨迹跟踪；当轨迹跟踪权重降低时，所学阻抗使机器人产生更柔顺的运动。

**作者说明**

- 保留问题先行的组织，强化外环学习到内环实现的关系，并将验证压缩为任务权重决定的精度与柔顺性取舍。具体表达以 A06、A07 为主，结合 A08 的方法分工写法。
- 将控制律准确表述为 *proportional–derivative-like*，对应科学事实中的“类比例—微分控制”。
- 内环渐近跟踪的保证对象是虚拟参考轨迹。外环分析以未知参数的线性时变质量—阻尼—弹簧模型及相应迭代条件为前提，不据此主张任意环境下的无条件收敛或全局最优阻抗。
- 第二种实机设置的代价曲线仍待复核，摘要未宣称全部实机设置的代价均随迭代下降。
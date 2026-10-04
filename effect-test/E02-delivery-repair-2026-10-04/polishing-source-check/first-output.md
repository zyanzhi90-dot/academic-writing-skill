**English abstract**

Fixed impedance parameters may be overly conservative or fail to accommodate changing environment dynamics during physical interaction. This paper proposes an impedance learning method for rigid manipulators interacting with unknown, time-varying environments. An outer loop combines gradient following with iterative improvement to learn time-varying damping and stiffness over repeated interactions according to a weighted cost of errors in position and time-integrated interaction force. The iterative improvement constructs updates from output errors and their rates of change without prior parameter identification for the assumed linear time-varying mass–damper–spring environment. The target impedance generates a virtual reference trajectory for an adaptive inner position controller to realize the learned impedance in robot motion. The position controller incorporates adaptive compensation into proportional–derivative-like control without requiring a robot dynamics regressor. Under the assumed manipulator dynamics, bounded virtual reference velocity and acceleration, and appropriate control and adaptation gain conditions, theoretical analysis establishes asymptotic tracking of the virtual reference trajectory and bounded closed-loop signals. Numerical simulations and repeated robot wrist–hand interaction experiments demonstrate adaptation of the balance between trajectory accuracy and compliance according to task weights. The trajectory-focused wrist–hand experiment further shows reductions in position error and task cost over iterations.

**中文翻译**

固定阻抗参数可能过于保守，也可能无法适应物理交互过程中环境动力学的变化。本文提出一种面向刚性机械臂与未知时变环境交互的阻抗学习方法。外环结合梯度跟随与迭代改进，在重复交互中根据位置误差和交互力时间积分误差的加权代价，学习随时间变化的阻尼与刚度。迭代改进利用输出误差及其变化率构造更新，无需预先辨识所假定的线性时变质量—阻尼—弹簧环境的参数。目标阻抗生成虚拟参考轨迹，由自适应内环位置控制器跟踪，使所学阻抗能够在机器人运动中实现。位置控制器将自适应补偿引入类比例—微分控制，无需机器人动力学回归矩阵。在所假定的机械臂动力学、虚拟参考速度和加速度有界，以及适当的控制增益与自适应增益条件下，理论分析证明了对虚拟参考轨迹的渐近跟踪和闭环信号的有界性。数值仿真与重复的机器人腕部—人手交互实验表明，该方法能够根据任务权重调整轨迹精度与柔顺性之间的取舍。侧重轨迹跟踪的腕部—人手交互实验进一步显示，位置误差和任务代价随迭代减小。

**作者说明**

- 论述收束为“固定阻抗的局限—交互反馈驱动的参数学习—所学阻抗的运动实现—理论与验证”，合并了重复的验证表述。
- 主要参照 A06、A07 的真实英文及连续句推进，局部借鉴 A08 的功能分工、A05 的阻抗适应表达和 A04 的理论表述；范例科学内容未作为本研究事实。
- 学习更新仅涉及阻尼和刚度，期望惯性固定为表观惯性。外环推导仍受相应收缩、矩阵非奇异及初始条件约束；内环渐近跟踪的对象是虚拟参考轨迹。
- 第二种实机设置的代价下降尚未核实，未纳入结论。摘要保留已核实的轨迹侧重设置中的代价改进，不主张全局最优或所有环境下均成立。
**English abstract**

Fixed impedance parameters may be overly conservative or fail to accommodate changing environment dynamics during physical interaction. This paper proposes an impedance learning method for rigid manipulators interacting with unknown, time-varying environments. An outer loop combines gradient following with iterative improvement to learn time-varying damping and stiffness according to a weighted cost of position and integrated interaction-force errors. The iterative improvement uses output errors and their rates of change to construct the updates without identifying exact environment parameters. The impedance relation generates a virtual reference trajectory for an inner position controller. Adaptive compensation is added to proportional–derivative control to track the virtual reference trajectory without requiring a robot dynamics regressor. Under the assumed robot dynamics, bounded reference velocity and acceleration, and appropriate gain conditions, theoretical analysis establishes asymptotic tracking of the virtual reference trajectory and bounded closed-loop signals. Numerical simulations and repeated wrist–hand interaction experiments demonstrate adaptation of the accuracy–compliance trade-off to the task weights. In the trajectory-focused experiment, stiffness increases while position error and task cost decrease over iterations. A lower trajectory-tracking weight produces lower stiffness and greater compliance, with larger position errors.

**中文翻译**

固定阻抗参数可能过于保守，也可能无法适应物理交互过程中环境动力学的变化。本文提出一种面向刚性机械臂与未知时变环境交互的阻抗学习方法。外环结合梯度跟随与迭代改进，根据位置误差和交互力时间积分误差的加权代价，学习随时间变化的阻尼与刚度。迭代改进利用输出误差及其变化率构造更新，无需辨识环境参数的精确数值。阻抗关系为内环位置控制器生成虚拟参考轨迹。在比例—微分控制中加入自适应补偿，使机械臂跟踪虚拟参考轨迹，无需机器人动力学回归矩阵。在所假定的机器人动力学、参考速度和加速度有界以及适当增益条件下，理论分析证明了对虚拟参考轨迹的渐近跟踪和闭环信号的有界性。数值仿真与重复腕部—人手交互实验表明，该方法能够根据任务权重调整轨迹精度与柔顺性之间的取舍。在侧重轨迹跟踪的实验中，刚度随迭代增加，位置误差与任务代价减小。较低的轨迹跟踪权重使刚度降低、柔顺性提高，同时位置误差增大。

**摘要外说明**

表达主要参照 A06、A07 的实际英文，并借鉴 A08 的功能分工、A05 的阻抗适应及 A04 的理论与实验表述。参考文献的科学内容未作为本研究事实。

期望惯性固定为表观惯性。外环推导限于所述线性时变质量—阻尼—弹簧环境及相应收敛条件；摘要中的渐近跟踪仅针对虚拟参考轨迹。第二种实机设置的代价下降尚未核实，未纳入结论。
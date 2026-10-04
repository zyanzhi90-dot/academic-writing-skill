**English abstract**

This paper proposes an impedance learning and adaptive position control scheme for rigid manipulators interacting with unknown, time-varying environments. Gradient following and iterative improvement are integrated to adjust the desired damping and stiffness over repeated interactions according to a task-dependent interaction error cost. For an environment represented by a linear time-varying mass–damper–spring system, the iterative improvement scheme uses output errors and their rates of change to update the impedance without identifying an internal model of the environment. An adaptive position controller is designed for the manipulator to track the virtual reference trajectory generated from the learned impedance. In this controller, adaptive compensation is incorporated into proportional–derivative control without requiring a robot dynamics regressor or prior numerical bounds on the robot dynamics. The inner-loop stability analysis establishes asymptotic tracking of the virtual reference trajectory and bounded closed-loop signals for bounded reference velocity and acceleration and suitable control and adaptation parameters. Numerical simulations and wrist–hand interaction experiments on the Nancy robot demonstrate that the impedance learning scheme favors trajectory accuracy or compliance according to the task weights.

**中文译文**

本文提出一种阻抗学习与自适应位置控制方案，用于刚性机械臂与未知时变环境的交互。该方案结合梯度跟随与迭代改进，根据与任务相关的交互误差代价，在重复交互中调整期望阻尼和刚度。对于以线性时变质量—阻尼—弹簧系统表示的环境，迭代改进方案利用输出误差及其变化率更新阻抗，无需辨识环境的内部模型。所设计的自适应位置控制器使机械臂跟踪由所学阻抗生成的虚拟参考轨迹。在该控制器中，自适应补偿被引入比例—微分控制，无需机器人动力学回归矩阵，也无需预先给定机器人动力学界限的具体数值。在参考速度和加速度有界、控制与自适应参数选取适当的条件下，内环稳定性分析证明了对虚拟参考轨迹的渐近跟踪以及闭环信号的有界性。数值仿真和 Nancy 机器人的腕部—人手交互实验表明，阻抗学习方案能够根据任务权重侧重轨迹精度或柔顺性。

**迁移依据**

- **贡献与取舍：** E02 的贡献是通过交互误差信息学习任务所需的阻尼、刚度，并以无需动力学回归矩阵及预知数值界限的自适应位置控制实现所学阻抗。保留环境模型范围、虚拟参考对象和内环保证条件；省略状态展开、更新公式、逐项仿真设置及过冲细节。未主张学习惯性、无条件外环收敛、全局最优或全部实验代价下降。
- **主辅选择：** A06 的实际贡献围绕多示教运动生成与不确定动力学下的轨迹执行，适合借鉴“学习输出交给控制器”的整段组织。A07 的实际贡献围绕相对运动控制、复合学习及 PPE 条件，局部借鉴其“学习信息—作用—理论—验证”的连续推进。
- **句间与措辞：** 英文第1—3句由完整方案进入阻抗学习及其信息来源，第4句将学习输出交给位置控制器，第5句解释控制设计，第6—7句提供理论与实际支持。直接适配 A06 的 `This paper proposes …`、`are integrated to …`、`is designed … to track … generated from …` 和 `In this controller …`；结合 A07 对学习对象的重复命名及 `Numerical simulation results demonstrate …`，将笼统的 `validity` 改为已核实的精度—柔顺性取舍。

本次结果属于“指定范例迁移路线验证”，不计作现有 Skill 的自主或迁移通过证据。
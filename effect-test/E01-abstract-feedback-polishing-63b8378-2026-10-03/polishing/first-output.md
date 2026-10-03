**English abstract**

This paper proposes a stable estimator of dynamical systems (SEDS) for learning robot point-to-point motions from multiple demonstrations. A Gaussian mixture model and Gaussian mixture regression are used to represent motion as a nonlinear autonomous dynamical system. SEDS incorporates stability constraints into model parameter optimization to reproduce the demonstrated motions while ensuring global asymptotic stability of the learned dynamical system at the target. The autonomous motion generator can respond to spatial and temporal perturbations during execution and continue towards the target. Numerical simulations using human handwriting data are carried out to evaluate motion reproduction. Experimental results from the tested robot arm tasks demonstrate that the generated motions reproduce demonstrated position and velocity patterns and reach the target from different initial positions.

**中文翻译**

本文提出稳定动力系统估计器（SEDS），用于从多个示范中学习机器人的点到点运动。该方法利用高斯混合模型和高斯混合回归，将运动表示为非线性自治动力系统。SEDS 将稳定性约束纳入模型参数优化，以再现示范运动，同时保证学习得到的动力系统在目标处全局渐近稳定。自治运动生成器能够在执行过程中响应空间扰动和时间扰动，并继续朝目标运动。研究利用人类手写运动数据开展数值模拟，以评价运动再现能力。所测试机械臂任务的实验结果表明，生成的运动能够再现示范中的位置及速度特点，并从不同初始位置到达目标。

**修改依据**

- 前四句保持原文；末三句收束为模拟评价目的与实机发现，集中支持运动再现和目标到达这一核心贡献，删除独立的 Katana-T 移动目标实验句。
- 对照 A06、A07 完整摘要的贡献与验证组织，采用 A07 的 `results demonstrate …` 结构承载具体实机发现，沿用与 A04 一致的 `are carried out to …` 结构交代模拟目的。
- 保留“所测试机械臂任务”的证据范围；模拟目的未改写为成功结论，时间扰动响应仍属于模型能力，全局渐近稳定保证仍限定于所学动力系统。

按本轮只读要求，未写入文件或同步 GitHub。
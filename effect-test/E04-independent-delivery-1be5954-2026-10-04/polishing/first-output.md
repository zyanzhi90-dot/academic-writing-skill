**English abstract**

Robot manipulation policies learned from demonstrations need to represent multiple valid action modes while generating precise, temporally consistent actions. Stepwise prediction of individual actions can switch between these modes. This paper proposes Diffusion Policy, which learns the score gradient of an observation-conditioned action distribution from demonstrations. The diffusion representation accommodates multimodal, high-dimensional action distributions, allowing temporally correlated actions to be generated jointly by iterative denoising from Gaussian noise. A receding-horizon execution scheme applies a short segment of each predicted sequence before replanning from new observations to balance temporal consistency with responsiveness. The visual policy encodes image observations once per prediction cycle and uses the resulting features to condition all denoising steps, reducing inference computation. Numerical simulation results demonstrate a 46.9% average relative performance improvement across the reported metrics for eight tasks, using the best diffusion architecture and baseline for each metric and each method’s best-performing action space. Real-robot experiments demonstrate 95% success in 20 trials of precise T-shaped object pushing, compared with 20% for a recurrent Gaussian mixture policy and 0% for implicit behavior cloning.

**中文翻译**

从示范中学习的机器人操作策略需要在生成精确且时间一致的动作的同时，表示多个有效动作模式。逐步预测单个动作可能导致预测在这些模式之间跳换。本文提出扩散策略，从示范中学习以观测为条件的动作分布的得分梯度。扩散表示能够容纳多模态、高维动作分布，通过从高斯噪声出发进行迭代去噪，联合生成具有时间关联的动作。滚动时域执行方案先执行每段预测动作序列中的较短一段，再根据新观测重新规划，以平衡时间一致性与响应能力。视觉策略在每轮预测中仅编码一次图像观测，并使用所得特征为所有去噪步骤提供条件，从而减少推理计算量。数值仿真结果表明，在八类任务的所报告指标上，平均相对性能提升为46.9%；比较时，对每项指标选取表现最佳的扩散架构和基线，且各方法均采用其表现最佳的动作空间。真实机器人实验表明，在精细推移T形物体的20次试验中，扩散策略的成功率为95%，循环高斯混合策略和隐式行为克隆的成功率分别为20%和0%。

**Revision notes:**

- 主要参照A06的“This paper proposes …”及对象交接、A07的设计—作用推进与数值验证表达，补明逐步预测的模式跳换问题，并压缩方法步骤。
- 46.9%是所列仿真指标的平均相对提升，排除混合熟练度多示范者结果；比较允许各方法采用表现最佳的动作空间。
- 95%仅对应推T形物体的20次定量试验，实机最佳模型采用CNN；独立扰动演示不计入该成功率。
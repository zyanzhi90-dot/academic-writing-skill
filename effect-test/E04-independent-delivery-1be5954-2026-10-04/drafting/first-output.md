**English abstract — nature-writing draft**

Robot manipulation policies learned from demonstrations need to represent multiple valid action modes while generating precise, temporally consistent actions. This paper proposes Diffusion Policy, which models action generation as an observation-conditioned denoising diffusion process. The policy learns the score gradient of the conditional action distribution from noisy demonstration actions and generates future action sequences by iterative denoising from Gaussian noise. This representation captures multimodal action distributions and jointly predicts temporally correlated actions in high-dimensional action spaces. A receding-horizon execution scheme applies a short segment of each predicted sequence before replanning from new observations, balancing temporal consistency with responsiveness. Image observations are encoded once per prediction cycle, and the resulting visual features condition repeated action denoising to reduce inference computation. Numerical simulation results demonstrate an average relative performance improvement of 46.9% across eight tasks when the best diffusion architecture and baseline are selected for each reported metric. Real-robot experiments further demonstrate 95% success in 20 trials of precise T-shaped object pushing, compared with 20% for a recurrent Gaussian mixture policy and 0% for implicit behavior cloning.

**中文翻译**

从示范中学习的机器人操作策略需要表示多种有效动作模式，同时生成精确且具有时间一致性的动作。本文提出扩散策略，将动作生成建模为观测条件下的去噪扩散过程。该策略从加噪的示范动作中学习条件动作分布的得分梯度，并从高斯噪声出发，通过迭代去噪生成未来动作序列。这种表示能够刻画多模态动作分布，并在高维动作空间中联合预测具有时间关联的动作。滚动时域执行方案只执行每段预测序列中的较短一段，随后依据新观测重新规划，在时间一致性与及时响应之间取得折中。图像观测在每轮预测中只编码一次，所得视觉特征用于多次动作去噪的条件输入，以减少推理计算量。数值仿真结果表明，在八类任务中，对每项报告指标分别选择表现最佳的扩散架构和基线进行比较，平均相对性能提升为46.9%。真实机器人实验进一步表明，精确推移T形物体任务在20次试验中的成功率为95%，而循环网络高斯混合策略和隐式行为克隆分别为20%和0%。

**作者说明**

- 表达主要参照A06的具体对象交接、A07的设计与作用推进，以及A05的实机验证句法。
- 46.9%是仿真所列任务／指标的平均相对提升，排除了混合熟练度多示范者结果；它不是成功率提升46.9个百分点，也不包含实机结果。
- 实机95%来自独立的20次定量试验，不代表扰动条件下的成功率。比较采用各方法表现最佳的动作空间，控制设置并非完全一致。
**Introduction**

Robot manipulation extends robot capabilities to physical tasks that require precise interaction with objects. Learning from demonstrations provides a practical approach to acquiring these skills through supervised policy learning [1,3]. Demonstrated behavior can contain several valid action modes, while successful execution requires precise actions that remain consistent over time. Stepwise prediction of individual actions can switch between these modes. It is therefore essential to consider how to represent multimodal action distributions and generate temporally correlated actions within the same policy.

Explicit policies have been developed to represent multimodal actions while incorporating observation history. In [1], the effects of demonstration quality, data quantity, observations and algorithm choice were systematically studied for robot manipulation. Recurrent Gaussian mixture policies use historical observations and represent multiple action modes through Gaussian components. In [2], a Behavior Transformer was proposed to learn multimodal continuous actions from observation sequences. Continuous actions are clustered into discrete categories, and predicted continuous offsets refine the actions associated with these categories. The numbers of mixture components and action categories must be specified. Moreover, observation history provides temporal context for action prediction, but does not itself provide a joint representation of future actions.

Implicit policies offer another approach to representing multimodal action distributions. In [3], implicit behavioral cloning was proposed to represent an observation-conditioned action distribution through an energy function. Low-energy actions are found by sampling or gradient-based inference. The method supports visual observations and high-dimensional actions and demonstrated millimetre-level precision in real contact tasks. Its contrastive training uses demonstrated actions as positive examples and sampled negative actions to approximate the normalization term of the conditional distribution. The implicit behavioral cloning baseline showed fluctuations during training and evaluation in our comparisons. Direct learning of distribution gradients offers an alternative that avoids this normalization estimate and its associated negative sampling.

Diffusion and score-based generative models provide a basis for learning distribution gradients. In [4], denoising diffusion probabilistic models were developed to generate samples through a learned reverse denoising process. In [5], gradients of the log density were learned at multiple noise scales and used for sample generation. Diffusion models have also been employed for planning and policy learning. In [6], Diffuser was proposed to jointly model states and actions at the trajectory level and generate plans with reward guidance or constraints. In [7], a conditional diffusion model was employed as an action policy for offline reinforcement learning and optimized with a Q-value objective. Concurrent studies investigated goal-conditioned diffusion imitation learning [8] and the imitation of multimodal human behavior with diffusion models [9].

In this paper, we propose Diffusion Policy for learning robot manipulation policies from demonstrations. Robot action generation is modeled as an observation-conditioned denoising diffusion process. The policy learns the score gradient of the conditional action distribution and generates a future action sequence by iterative denoising from Gaussian noise. The diffusion representation accommodates multimodal, high-dimensional distributions, allowing temporally correlated actions to be generated jointly. In our controlled pushing example, Diffusion Policy represents actions passing on either side of an object and maintains one mode during execution. The generated sequence must also support timely responses to new observations. We therefore combine action-sequence prediction with receding-horizon execution. The policy predicts a longer sequence from recent observations, executes a shorter segment and then replans using new observations. The prediction horizon supports temporal consistency, while the shorter execution window allows actions to be updated as the observed situation changes.

The visual policy must incorporate image information while keeping iterative action generation computationally manageable. We therefore use encoded image features to condition action denoising. Image observations are encoded once per prediction cycle, and the resulting features are reused across all denoising steps. This design reduces repeated computation and supports real-time inference. The denoising output consists of actions, so action generation does not require prediction of future visual states. The visual encoder can be trained end to end with the policy to learn features for action prediction.

The denoising network must preserve the temporal variations in actions required by the task. We examine a temporal convolutional network and a time-series diffusion Transformer as alternative architectures. The temporal convolutional network is a practical choice for most of the tested tasks, but its tendency to favor low-frequency signals can excessively smooth changes in the action sequence. The time-series diffusion Transformer is designed to reduce this effect and performs better in some tasks involving rapid action changes or velocity control. Its greater sensitivity to hyperparameters makes architecture choice dependent on the task and training configuration.

We present a demonstration-learning framework that combines diffusion-based action-sequence generation with receding-horizon execution and efficient visual conditioning. The framework is evaluated on eight simulation tasks across four benchmarks and four real-robot tasks. The average relative performance improvement across the reported simulation metrics is 46.9%, using the best diffusion architecture and the best baseline for each metric and excluding mixed-proficiency, multi-demonstrator results. The comparisons use each method’s best-performing action space. Real-robot experiments demonstrate precise manipulation, including 95% success in 20 trials of T-shaped object pushing.

**逐段中文译文**

**第1段**

机器人操作拓展了机器人执行物理任务的能力，这些任务要求机器人与物体进行精确交互。从示范中学习为获取这些技能提供了一种实用途径，即通过监督学习训练策略 [1,3]。示范行为可能包含多个有效动作模式，而成功执行任务需要精确且在时间上保持一致的动作。逐步预测单个动作可能在这些模式之间切换。因此，有必要研究如何在同一策略中表示多模态动作分布并生成具有时间关联的动作。

**第2段**

已有显式策略能够在利用观测历史的同时表示多模态动作。文献 [1] 系统研究了示范质量、数据数量、观测和算法选择对机器人操作学习的影响。循环高斯混合策略利用历史观测，并通过多个高斯分量表示不同的动作模式。文献 [2] 提出了行为 Transformer，用于从观测序列中学习多模态连续动作。连续动作被聚类为离散类别，预测的连续偏移用于修正这些类别所对应的动作。混合分量数量和动作类别数量需要设定。此外，观测历史为动作预测提供了时间上下文，但其本身并不提供未来动作的联合表示。

**第3段**

隐式策略为表示多模态动作分布提供了另一种途径。文献 [3] 提出了隐式行为克隆，通过能量函数表示以观测为条件的动作分布。推理时通过采样或基于梯度的方法寻找低能量动作。该方法支持视觉观测和高维动作，并在真实接触任务中展示了毫米级精度。其对比训练将示范动作作为正例，将采样得到的动作作为负例，以近似条件分布的归一化项。在我们的比较中，隐式行为克隆基线的训练和评价表现出现了波动。直接学习分布梯度提供了一种替代途径，可避免这一归一化估计及其所需的负采样。

**第4段**

扩散模型和基于得分的生成模型为学习分布梯度提供了基础。文献 [4] 提出了去噪扩散概率模型，通过学习反向去噪过程生成样本。文献 [5] 在多个噪声尺度下学习对数密度梯度，并利用这些梯度生成样本。扩散模型也已用于规划和策略学习。文献 [6] 提出了 Diffuser，在轨迹层面联合建模状态与动作，并利用奖励引导或约束生成计划。文献 [7] 将条件扩散模型用作离线强化学习的动作策略，并通过 Q 值目标进行优化。同期研究还探索了目标条件扩散模仿学习 [8]，以及利用扩散模型模仿多模态人类行为 [9]。

**第5段**

本文提出扩散策略，用于从示范中学习机器人操作策略。机器人动作生成被建模为以观测为条件的去噪扩散过程。策略学习条件动作分布的得分梯度，并从高斯噪声出发，通过迭代去噪生成一段未来动作。扩散表示能够容纳多模态、高维分布，从而联合生成具有时间关联的动作。在我们的受控推物示例中，扩散策略能够表示从物体两侧通过的动作，并在执行过程中保持一个模式。生成的动作序列还需要支持对新观测的及时响应。因此，我们将动作序列预测与滚动时域执行相结合。策略依据最近一段观测预测较长的动作序列，执行其中较短的一段，然后利用新观测重新规划。预测时域支持动作的时间一致性，而较短的执行窗口使策略能够随观测到的情况变化更新动作。

**第6段**

视觉策略需要利用图像信息，同时控制迭代动作生成的计算开销。因此，我们将编码后的图像特征用作动作去噪的条件。每轮预测只对图像观测编码一次，并在所有去噪步骤中复用所得特征。这一设计减少了重复计算，并支持实时推理。去噪输出由动作构成，因此生成动作不需要预测未来视觉状态。视觉编码器可以与策略进行端到端训练，以学习用于动作预测的特征。

**第7段**

去噪网络需要保留任务所需的动作时间变化。我们研究了时间卷积网络和时间序列扩散 Transformer 两种替代架构。时间卷积网络在多数已测任务中是一种实用选择，但其偏向低频信号的倾向可能导致动作序列中的变化被过度平滑。时间序列扩散 Transformer 旨在减轻这一影响，并在部分涉及快速动作变化或速度控制的任务中表现更好。它对超参数更敏感，因此架构选择取决于任务和训练配置。

**第8段**

我们提出了一个从示范学习的框架，将基于扩散的动作序列生成、滚动时域执行和高效视觉条件化相结合。该框架在四个基准中的八项仿真任务和四项真实机器人任务上进行了评价。在报告的仿真指标上，平均相对性能提升为 46.9%；计算时对每个指标分别采用表现最好的扩散架构和基线，并排除混合熟练度的多示范者结果。比较采用各方法表现最好的动作空间。真实机器人实验展示了精确操作能力，其中推 T 形物体任务在二十次试验中取得了 95% 的成功率。

**正文实际使用的参考文献**

[1] Mandlekar, A. et al. *What Matters in Learning from Offline Human Demonstrations for Robot Manipulation*. CoRL 2021, PMLR **164**, 1678–1690 (2022).

[2] Shafiullah, N. M. M., Cui, Z. J., Altanzaya, A. & Pinto, L. *Behavior Transformers: Cloning k modes with one stone*. NeurIPS (2022). arXiv:2206.11251.

[3] Florence, P. et al. *Implicit Behavioral Cloning*. CoRL 2021, PMLR **164**, 158–168 (2022).

[4] Ho, J., Jain, A. & Abbeel, P. *Denoising Diffusion Probabilistic Models*. NeurIPS (2020). arXiv:2006.11239.

[5] Song, Y. & Ermon, S. *Generative Modeling by Estimating Gradients of the Data Distribution*. NeurIPS (2019). arXiv:1907.05600.

[6] Janner, M., Du, Y., Tenenbaum, J. & Levine, S. *Planning with Diffusion for Flexible Behavior Synthesis*. ICML, PMLR **162**, 9902–9915 (2022).

[7] Wang, Z., Hunt, J. J. & Zhou, M. *Diffusion Policies as an Expressive Policy Class for Offline Reinforcement Learning*. arXiv:2208.06193, v2 (2022).

[8] Reuss, M., Li, M., Jia, X. & Lioutikov, R. *Goal-Conditioned Imitation Learning using Score-based Diffusion Policies*. RSS (2023). arXiv:2304.02532.

[9] Pearce, T. et al. *Imitating Human Behaviour with Diffusion Models*. ICLR (2023). arXiv:2301.10677.

**作者说明**

- 调整了段落分工：将扩散生成基础与已有应用集中说明，将联合动作生成与滚动执行放在同一段内，明确从预测序列到反馈更新的联系。
- 组织与表达主要参照冻结候选中的 P17 正向学习材料，并结合 P05、Fuzzy2023 和 ESO2017 的适用关系。范例仅用于组织和表达，正文科学事实与引用身份均来自作者材料。
- 46.9% 保留为按指标选择最佳架构和最佳基线后的平均相对性能提升；95% 仅对应二十次推 T 形物体的定量试验。训练波动、模式保持及架构优势均限定于相应比较或任务范围。
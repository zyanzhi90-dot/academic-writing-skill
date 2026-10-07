**Introduction**

Robot manipulation is an important means of automating physical tasks that require precise handling of objects. Learning from demonstrations provides a route to acquiring manipulation skills from human examples. Behavior cloning formulates this learning problem as supervised prediction of actions from observations and has produced effective policies for real-robot manipulation [1]. However, demonstrations may contain several valid ways of performing the same task. A learned policy must represent these action modes while producing temporally consistent actions with sufficient precision for the task. It is therefore necessary to consider how action distributions are represented and how actions are generated over time.

Explicit action distributions provide a useful approach to representing multimodal behavior. In [1], recurrent Gaussian mixture policies were used to learn manipulation skills from offline human demonstrations. These policies use observation history and represent multiple action modes through Gaussian mixture components. In [2], Behavior Transformer was proposed to learn multimodal continuous actions from observation sequences. Continuous actions are clustered into discrete categories, and predicted continuous offsets refine the actions within these categories. Both approaches support multimodal actions and temporal context, although the numbers of mixture components or action categories must be specified. Moreover, the use of observation history does not itself imply joint prediction of future actions. Stepwise prediction can switch between valid modes, motivating a policy that models the temporal relationships within a future action sequence.

Implicit policies offer another approach to multimodal action representation. In [3], implicit behavior cloning was developed to represent a policy through an energy function of observations and actions. Multiple low-energy actions can represent multimodal and multivalued mappings, and actions are obtained through sampling or gradient-based optimization. The method supports visual observations and high-dimensional actions and has demonstrated millimetre-level precision in real-robot contact tasks. Its contrastive training uses demonstration actions as positive samples and sampled actions as negative samples to approximate the normalization term of the conditional action distribution. The difficulty of estimating this term motivates an alternative that directly learns the distribution gradient without the corresponding negative sampling.

Diffusion models provide a generative foundation for this alternative. Denoising diffusion probabilistic models learn a reverse denoising process that generates samples from random noise [4], while score-based generative models learn log-density gradients at different noise scales [5]. Diffusion has also been applied to sequential decision-making. In [6], Diffuser was proposed to jointly model states and actions in trajectories and generate plans through denoising, with reward guidance or constraints determining the desired behavior. In [7], conditional diffusion models were employed as action policies for offline reinforcement learning and improved through a Q-value objective. Concurrent studies investigated goal-conditioned diffusion imitation learning [8] and diffusion models for multimodal human behavior [9]. These studies establish diffusion as a useful representation for planning and policy learning. Our study focuses on supervised learning of observation-conditioned action sequences from demonstrations and their execution in visual robot manipulation.

In this paper, we propose Diffusion Policy, which models action generation as an observation-conditioned denoising diffusion process. The network is trained to predict noise added to demonstration actions, with observations supplied as conditions. This objective learns the score gradient of the conditional action distribution. At inference, the policy generates a future action sequence through iterative denoising from Gaussian noise. The diffusion representation accommodates multimodal, high-dimensional action distributions without specifying a fixed number of action modes. It therefore allows temporally correlated actions to be predicted jointly. Direct score learning also avoids the normalization estimate and negative sampling used in implicit behavior cloning and is associated with more stable training in our comparisons.

The execution of a predicted action sequence must preserve temporal consistency while allowing the policy to respond to new observations. We therefore combine action-sequence prediction with receding-horizon execution. The policy predicts a longer sequence from recent observations, executes a shorter segment, and then predicts again using updated observations. The execution window balances consistency within the predicted sequence with timely responses to changes in the scene. For visual manipulation, the repeated denoising process also makes visual encoding an important part of inference computation. The visual policy encodes image observations once per prediction cycle and uses the resulting features to condition all denoising steps. The denoising output contains the action sequence, while image features provide its observation condition. This design reduces repeated visual computation and supports real-time inference. The visual encoder can be trained jointly with the policy.

The choice of denoising network also affects the action sequences generated by the policy. We consider a temporal convolutional network and a time-series diffusion Transformer as alternative architectures. Temporal convolution can favor low-frequency signals and oversmooth rapid changes in actions. The Transformer is introduced to reduce this tendency and has advantages in some tested tasks involving rapid action changes or velocity control. The convolutional network is easier to use in most tested tasks, whereas the Transformer is more sensitive to hyperparameter choices. The two architectures thus provide different options for action-sequence generation according to the temporal demands of the task.

The proposed policy combines multimodal action-sequence learning, receding-horizon execution, and visual conditioning within a demonstration-learning framework. We evaluate the approach on eight tasks from four simulation benchmarks and four real-robot tasks. Simulation comparisons show a 46.9% average relative performance improvement across the reported metrics, using the best diffusion architecture and best baseline for each metric and each method’s best-performing action space. In real-robot T-shaped object pushing, the convolutional visual policy achieves 95% success in 20 trials, compared with 20% for a recurrent Gaussian mixture policy and 0% for implicit behavior cloning. These evaluations provide evidence for the approach across the tested manipulation tasks.

**逐段中文译文**

**第1段**

机器人操作是实现需要精确处理物体的物理任务自动化的重要手段。从示范学习为机器人通过人类示例获得操作技能提供了一条途径。行为克隆将这一学习问题表述为根据观测监督预测动作，并已在真实机器人操作中获得有效策略[1]。然而，示范可能包含完成同一任务的多种有效方式。学习得到的策略需要表示这些动作模式，同时生成时间上一致、且精度足以满足任务要求的动作。因此，有必要研究如何表示动作分布，以及如何随时间生成动作。

**第2段**

显式动作分布为表示多模态行为提供了一种有效途径。文献[1]使用循环高斯混合策略从离线人类示范中学习操作技能。这些策略利用历史观测，并通过高斯混合分量表示多种动作模式。文献[2]提出了行为 Transformer，根据观测序列学习多模态连续动作。该方法将连续动作聚类为离散类别，再通过预测连续偏移来细化各类别内的动作。这两类方法均支持多模态动作和时间上下文，但需要预先设定混合分量或动作类别的数量。此外，使用历史观测本身并不意味着联合预测未来动作。逐步预测可能在不同有效模式之间切换，因此需要一种能够对未来动作序列内部的时间关系进行建模的策略。

**第3段**

隐式策略为多模态动作表示提供了另一条途径。文献[3]提出了隐式行为克隆，通过观测与动作的能量函数表示策略。多个低能量动作可以表示多模态和多值映射，动作则通过采样或基于梯度的优化获得。该方法支持视觉观测和高维动作，并已在真实机器人接触任务中展示毫米级精度。其对比训练将示范动作作为正样本，将采样动作作为负样本，以近似条件动作分布的归一化项。估计该项的困难促使我们考虑一种替代方式，即直接学习分布梯度，避免相应的负采样。

**第4段**

扩散模型为这一替代方式提供了生成建模基础。去噪扩散概率模型学习反向去噪过程，从随机噪声生成样本[4]；基于得分的生成模型则学习不同噪声尺度下的对数密度梯度[5]。扩散也已应用于序列决策。文献[6]提出了 Diffuser，在轨迹中联合建模状态与动作，通过去噪生成计划，并利用奖励引导或约束确定所需行为。文献[7]将条件扩散模型用作离线强化学习的动作策略，并通过 Q 值目标改善策略。同期研究还探讨了目标条件扩散模仿学习[8]，以及用于多模态人类行为的扩散模型[9]。这些研究确立了扩散作为规划和策略学习表示方式的价值。本研究关注从示范中监督学习观测条件下的动作序列，以及在视觉机器人操作中执行这些序列。

**第5段**

本文提出扩散策略，将动作生成建模为观测条件下的去噪扩散过程。训练时，网络以观测为条件，预测加入示范动作中的噪声。这一目标学习条件动作分布的得分梯度。推理时，策略从高斯噪声出发，通过迭代去噪生成一段未来动作序列。扩散表示能够处理多模态、高维动作分布，无需设定固定的动作模式数量，因此能够联合预测具有时间关联的动作。直接学习得分还避免了隐式行为克隆所使用的归一化估计和负采样，并在本研究的比较中表现出与更稳定训练相联系的结果。

**第6段**

执行预测动作序列时，需要保持时间一致性，同时允许策略响应新观测。因此，我们将动作序列预测与滚动时域执行相结合。策略根据最近的观测预测较长序列，执行其中较短的一段，然后利用更新后的观测再次预测。执行窗口在预测序列内部的一致性与对场景变化的及时响应之间取得折中。对于视觉操作，重复去噪过程也使视觉编码成为推理计算的重要组成部分。视觉策略在每轮预测中只对图像观测编码一次，并用所得特征作为所有去噪步骤的条件。去噪输出包含动作序列，而图像特征提供其观测条件。这一设计减少了重复视觉计算，有助于实时推理。视觉编码器可以与策略联合训练。

**第7段**

去噪网络的选择也会影响策略生成的动作序列。我们将时间卷积网络和时间序列扩散 Transformer 作为两种替代架构进行研究。时间卷积可能偏向低频信号，并过度平滑动作的快速变化。引入 Transformer 是为了减轻这一倾向，它在部分涉及动作快速变化或速度控制的已测任务中具有优势。卷积网络在多数已测任务中更易使用，而 Transformer 对超参数选择更敏感。因此，这两种架构为根据任务的时间变化要求生成动作序列提供了不同选择。

**第8段**

所提出的策略在一个示范学习框架中结合了多模态动作序列学习、滚动时域执行和视觉条件建模。我们在四个仿真基准中的八类任务及四项真实机器人任务上评价该方法。在所报告的仿真指标上，分别采用每项指标中表现最佳的扩散架构和最佳基线，并使用各方法表现最佳的动作空间，比较结果显示平均相对性能提升为46.9%。在真实机器人推 T 形物体任务中，卷积视觉策略在20次试验中取得95%的成功率，循环高斯混合策略和隐式行为克隆的成功率分别为20%和0%。这些评价为该方法在所测操作任务中的表现提供了证据。

**正文实际使用的参考文献**

[1] Mandlekar, A. et al. *What Matters in Learning from Offline Human Demonstrations for Robot Manipulation*. CoRL 2021, PMLR **164**, 1678–1690 (2022).

[2] Shafiullah, N. M. M., Cui, Z. J., Altanzaya, A. & Pinto, L. *Behavior Transformers: Cloning k modes with one stone*. NeurIPS (2022). arXiv:2206.11251.

[3] Florence, P. et al. *Implicit Behavioral Cloning*. CoRL 2021, PMLR **164**, 158–168 (2022).

[4] Ho, J., Jain, A. & Abbeel, P. *Denoising Diffusion Probabilistic Models*. NeurIPS (2020). arXiv:2006.11239.

[5] Song, Y. & Ermon, S. *Generative Modeling by Estimating Gradients of the Data Distribution*. NeurIPS (2019). arXiv:1907.05600.

[6] Janner, M., Du, Y., Tenenbaum, J. & Levine, S. *Planning with Diffusion for Flexible Behavior Synthesis*. ICML, PMLR **162**, 9902–9915 (2022).

[7] Wang, Z., Hunt, J. J. & Zhou, M. *Diffusion Policies as an Expressive Policy Class for Offline Reinforcement Learning*. arXiv:2208.06193 (2022), version 2.

[8] Reuss, M., Li, M., Jia, X. & Lioutikov, R. *Goal-Conditioned Imitation Learning using Score-based Diffusion Policies*. RSS (2023). arXiv:2304.02532.

[9] Pearce, T. et al. *Imitating Human Behaviour with Diffusion Models*. ICLR (2023). arXiv:2301.10677.

**作者说明**

组织与表达以冻结候选中 *Robot Learning System Based on Adaptive Neural Control and Dynamic Movement Primitives* 的正向学习材料为主要锚点，并结合双臂复合学习、固定时间模糊控制及水下机器人 ESO 范例中适用的连续句关系。范例用于组织和表达模仿；本文科学事实及引用依据均来自作者提供的正常材料。结尾保留实验范围与关键比较，用于支撑已建立的方法贡献。
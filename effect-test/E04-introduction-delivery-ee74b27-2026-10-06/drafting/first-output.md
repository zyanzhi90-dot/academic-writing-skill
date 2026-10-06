**Introduction**

Robot learning from demonstrations is a valuable approach to acquiring manipulation skills. Behavior cloning formulates this problem as supervised policy learning and has produced effective policies for real robot manipulation with visual observations [1,3]. Demonstrations can contain several valid ways to complete the same task, and the actions within each execution are temporally correlated. A manipulation policy must therefore represent these alternatives while producing precise, temporally consistent actions. Effective action modeling is essential to reproducing the demonstrated skills.

Explicit action models provide multimodal representations and temporal context. In [1], recurrent policies were evaluated for learning robot manipulation from offline human demonstrations. A recurrent Gaussian mixture policy uses historical observations and represents multiple action modes with Gaussian components. In [2], Behavior Transformer was proposed to learn multimodal continuous actions from observation histories. The model groups actions using k-means clustering and predicts an action category together with a continuous offset that refines the action. The number of Gaussian components or action categories is specified in these representations. Historical observations provide temporal context, but prediction of an individual action does not jointly model the correlations among future actions. Stepwise action prediction can switch between valid modes during execution, motivating the joint generation of future action sequences.

Implicit policies offer another approach to representing multimodal actions. In [3], implicit behavior cloning was proposed to learn an energy function over observations and actions. Multiple low-energy actions represent alternative valid behaviors, and sampling or gradient-based inference is used to select an action. The method supports high-dimensional actions and visual observations and has demonstrated millimetre-level precision in real contact tasks. Its contrastive training objective uses demonstrated actions as positive examples and sampled actions as negative examples to approximate the normalization term of the conditional distribution. An alternative representation that learns the distribution gradient can avoid this normalization estimate and the associated negative sampling.

Diffusion models provide a basis for learning such a representation. In [4], a generative model was trained to reverse progressive noise corruption, while [5] learned log-density gradients at multiple noise scales for iterative sampling. These approaches support multimodal, high-dimensional generation. In [6], Diffuser was developed to generate state–action trajectories for planning, with rewards or constraints guiding the generated plans. In [7], a conditional diffusion action policy was combined with a Q-value objective for offline reinforcement learning. Concurrent imitation-learning studies investigated goal conditioning, multimodal behavior and sampling design [8,9]. These developments establish diffusion as an expressive modeling approach. The present study uses this foundation to learn observation-conditioned action policies directly from demonstrations and to execute them in physical robot manipulation.

This paper proposes Diffusion Policy, which models action generation as an observation-conditioned denoising diffusion process. A network learns the score gradient of the conditional action distribution through noise prediction on corrupted demonstration actions. The resulting learning formulation avoids the negative sampling used for the energy-based normalization estimate and shows more stable training than the evaluated implicit behavior cloning baseline in our tasks. The diffusion representation accommodates multimodal action distributions without prescribing a fixed number of modes. Its ability to handle high-dimensional outputs allows a sequence of temporally correlated actions to be generated jointly by iterative denoising from Gaussian noise. The policy thus models valid action alternatives and their temporal relationships within the same action sequence.

Action-sequence generation also requires a mechanism for incorporating new observations during execution. A longer sequence provides temporal coordination, but executing the entire sequence without updating the prediction delays the response to new observations. We therefore combine joint action prediction with receding-horizon execution. The policy predicts a longer action sequence from recent observations, applies a shorter segment and then predicts again using new observations. The execution window balances temporal consistency with responsiveness, allowing the generated sequence to guide motion while retaining feedback during manipulation.

The visual denoising policy must use image observations efficiently while preserving the action changes needed for precise manipulation. An image encoder supplies features that condition the action denoising network, so action generation requires no prediction of future visual states. The image features are computed once per prediction cycle and reused across the denoising steps, reducing inference computation. The encoder can be trained end to end with the policy. For temporal denoising, we consider a temporal convolutional network and a time-series diffusion Transformer as alternative architectures. Temporal convolutions are convenient for many tasks, but their bias towards low-frequency signals can oversmooth rapid action changes. The Transformer is designed to reduce this smoothing and offers advantages on some tasks involving rapidly changing actions or velocity control. Its greater sensitivity to hyperparameters makes architecture selection dependent on the manipulation task.

Diffusion Policy combines multimodal action learning, joint action-sequence generation and replanning from new observations in a policy learned from demonstrations. We evaluate the approach on eight tasks from four simulation benchmarks and on four real robot tasks. The evaluations cover state and visual observations, different action dimensions, and single-task and multistage manipulation. In precise T-shaped object pushing, Diffusion Policy achieves 95% success over 20 real robot trials, compared with 20% for a recurrent Gaussian mixture policy and 0% for implicit behavior cloning. This comparison uses each method’s best tested variant, including its action-space choice. These results demonstrate the effectiveness of the combined policy representation and execution design on the tested manipulation tasks.

**逐段中文译文**

**第1段**

从示范中学习是机器人获取操作技能的一种有价值的途径。行为克隆将这一问题表述为监督式策略学习，并已在采用视觉观测的真实机器人操作中获得有效策略 [1,3]。示范可能包含完成同一任务的多种有效方式，而每次执行中的动作又具有时间关联。因此，操作策略必须在表示这些不同方式的同时，生成精确且在时间上保持一致的动作。有效的动作建模是复现示范技能的重要环节。

**第2段**

显式动作模型能够提供多模态表示和时间上下文。文献 [1] 评估了利用离线人类示范学习机器人操作的循环策略。循环高斯混合策略使用历史观测，并通过多个高斯分量表示不同的动作模式。文献 [2] 提出了行为 Transformer，用于从观测历史中学习多模态连续动作。该模型利用 k 均值聚类对动作分组，预测动作类别以及用于细化动作的连续偏移量。这些表示需要设定高斯分量或动作类别的数量。历史观测提供了时间上下文，但预测单个动作并不等于联合建模未来动作之间的关联。逐步预测动作可能在执行过程中切换有效模式，这促使我们考虑联合生成未来动作序列。

**第3段**

隐式策略为多模态动作表示提供了另一条途径。文献 [3] 提出了隐式行为克隆，用于学习观测与动作上的能量函数。多个低能量动作表示不同的有效行为，推理时通过采样或基于梯度的方法选择动作。该方法支持高维动作和视觉观测，并已在真实接触任务中展示毫米级精度。其对比训练目标将示范动作作为正例、采样动作作为负例，以近似条件分布的归一化项。学习分布梯度的另一种表示可以绕开这一归一化估计及相应的负采样。

**第4段**

扩散模型为学习这样的表示提供了基础。文献 [4] 训练生成模型来逆转逐步加噪过程，而文献 [5] 学习多个噪声尺度下的对数密度梯度，用于迭代采样。这些方法支持多模态、高维数据生成。文献 [6] 开发了 Diffuser，通过生成状态—动作轨迹进行规划，并利用奖励或约束引导生成的计划。文献 [7] 将条件扩散动作策略与 Q 值目标结合，用于离线强化学习。同期的模仿学习研究还探讨了目标条件、多模态行为和采样设计 [8,9]。这些进展确立了扩散模型作为一种具有丰富表达能力的建模途径。本研究以此为基础，直接从示范中学习观测条件动作策略，并将其用于物理机器人的操作执行。

**第5段**

本文提出扩散策略，将动作生成建模为观测条件下的去噪扩散过程。网络通过预测加噪示范动作中的噪声，学习条件动作分布的得分梯度。这种学习形式绕开了能量模型归一化估计所使用的负采样，并在本研究的任务中表现出比所评估的隐式行为克隆基线更稳定的训练。扩散表示能够容纳多模态动作分布，无需预先指定固定的模式数量。其处理高维输出的能力使一段具有时间关联的动作能够从高斯噪声出发，通过迭代去噪联合生成。因此，策略能够在同一动作序列中建模有效的动作选择及其时间关系。

**第6段**

动作序列生成还需要一种在执行过程中引入新观测的机制。较长的序列能够提供时间上的协调，但如果执行完整序列而不更新预测，对新观测的响应就会延迟。因此，我们将联合动作预测与滚动时域执行结合。策略根据最近的观测预测较长的动作序列，执行其中较短的一段，然后利用新观测再次预测。执行窗口在时间一致性与响应能力之间取得折中，使生成的序列能够指导运动，同时在操作过程中保留反馈。

**第7段**

视觉去噪策略必须高效利用图像观测，同时保留精细操作所需的动作变化。图像编码器提供特征，作为动作去噪网络的条件，因此动作生成无需预测未来视觉状态。每个预测周期仅计算一次图像特征，并在多次去噪中复用，从而减少推理计算量。编码器可以与策略一起进行端到端训练。在时间序列去噪方面，我们考虑时间卷积网络和时间序列扩散 Transformer 两种替代架构。时间卷积在许多任务中便于使用，但其对低频信号的偏向可能使快速动作变化被过度平滑。Transformer 的设计旨在减轻这种平滑，并在涉及快速动作变化或速度控制的部分任务上具有优势。它对超参数更敏感，因此架构选择需要结合具体操作任务。

**第8段**

扩散策略在从示范学得的策略中结合了多模态动作学习、联合动作序列生成以及基于新观测的重新规划。我们在四个仿真基准中的八类任务以及四项真实机器人任务上评估这一方法。评估涵盖状态和视觉观测、不同动作维度，以及单任务和多阶段操作。在精细的 T 形物体推动任务中，扩散策略在二十次真实机器人试验中取得了 95% 的成功率，而循环高斯混合策略和隐式行为克隆分别为 20% 和 0%。这一比较采用各方法已测试的最佳变体，包括各自动作空间的选择。这些结果表明，策略表示与执行设计的结合在所测试的操作任务中有效。

**正文使用的参考文献**

[1] Mandlekar, A., et al. *What Matters in Learning from Offline Human Demonstrations for Robot Manipulation*. CoRL 2021, Proceedings of Machine Learning Research **164**, 1678–1690 (2022).

[2] Shafiullah, N. M. M., Cui, Z. J., Altanzaya, A. & Pinto, L. *Behavior Transformers: Cloning k modes with one stone*. NeurIPS (2022). arXiv:2206.11251.

[3] Florence, P., et al. *Implicit Behavioral Cloning*. CoRL 2021, Proceedings of Machine Learning Research **164**, 158–168 (2022).

[4] Ho, J., Jain, A. & Abbeel, P. *Denoising Diffusion Probabilistic Models*. NeurIPS (2020). arXiv:2006.11239.

[5] Song, Y. & Ermon, S. *Generative Modeling by Estimating Gradients of the Data Distribution*. NeurIPS (2019). arXiv:1907.05600.

[6] Janner, M., Du, Y., Tenenbaum, J. & Levine, S. *Planning with Diffusion for Flexible Behavior Synthesis*. ICML, Proceedings of Machine Learning Research **162**, 9902–9915 (2022).

[7] Wang, Z., Hunt, J. J. & Zhou, M. *Diffusion Policies as an Expressive Policy Class for Offline Reinforcement Learning*. arXiv:2208.06193 (2022).

[8] Reuss, M., Li, M., Jia, X. & Lioutikov, R. *Goal-Conditioned Imitation Learning using Score-based Diffusion Policies*. Robotics: Science and Systems (2023). arXiv:2304.02532.

[9] Pearce, T., et al. *Imitating Human Behaviour with Diffusion Models*. ICLR (2023). arXiv:2301.10677.

**作者说明**

- 整节按“示范学习价值 → 显式表示与时间关系 → 隐式表示与训练目标 → 扩散研究基础 → 本文表示 → 执行反馈 → 视觉计算与网络选择 → 贡献及验证”推进。表达以 B15／P17 为主，结合 B16、B17、B18 中适用的文献续句、设计作用和职责衔接写法；范例科学事实未进入正文。
- 95% 来自二十次定量推物试验，不是扰动条件下的成功率。更稳定的训练和 Transformer 的优势均保留了已测任务范围；正文不将这些结果解释为闭环稳定性保证。
**Introduction**

Behavior cloning treats learning from demonstrations as supervised policy learning and has produced effective policies for real-robot manipulation [1]. A manipulation task can nevertheless admit several valid actions for the same observation. For example, an action sequence may pass to the left or right of an object. The policy must represent these alternatives while generating precise actions that remain consistent over time.

Recurrent Gaussian mixture policies use observation histories and multiple Gaussian components to represent action distributions [1]. Behavior Transformers use historical observations, predict clustered action categories and refine the actions with continuous offsets [2]. These models provide both temporal context and multimodal action prediction, with a prescribed number of components or categories. Conditioning on past observations and jointly predicting future actions are distinct design choices. A policy that predicts individual actions step by step can switch between valid modes during execution, motivating joint prediction of a temporally correlated action sequence.

Implicit behavioral cloning provides an alternative to explicit mixtures and action categories. It represents the policy with an energy function of observations and actions and searches for low-energy actions during inference [3]. Such policies can express multimodal behavior and have been demonstrated with visual observations, high-dimensional actions and precise real-robot manipulation [3]. The contrastive training objective uses demonstration actions as positive samples and sampled actions as negatives to approximate the normalization term of the conditional action distribution. This training procedure motivates learning the distribution gradient directly, without estimating that normalization term.

Denoising diffusion and score-based generative models learn data distributions through noise prediction or score estimation and generate samples by iterative updates from noise [4,5]. Diffuser jointly models state–action trajectories for diffusion-based planning [6], while diffusion policies for offline reinforcement learning combine conditional action generation with a Q-value objective [7]. Contemporaneous imitation-learning work studies goal-conditioned diffusion policies in simulated robot tasks [8] and multimodal human behavior in simulated robot and three-dimensional game environments [9]. These advances establish diffusion as a foundation for policy representation. We investigate how observation-conditioned diffusion can generate precise, temporally consistent action sequences from demonstrations while retaining responsiveness during manipulation.

This paper proposes Diffusion Policy, which models action generation as observation-conditioned denoising diffusion. The policy learns the score gradient of the conditional action distribution from demonstrations. A denoising network is trained to predict the noise added to demonstrated actions using observations as conditions. At inference, the network iteratively denoises Gaussian noise to generate a sequence of future actions. The diffusion representation accommodates multimodal, high-dimensional output, allowing temporally correlated actions to be modeled jointly. The noise-prediction objective avoids the negative sampling used in the energy-based formulation described above.

Diffusion Policy uses observations both to condition action generation and to update its predictions during execution. A receding-horizon execution scheme applies a short segment of each predicted sequence before predicting again from updated observations. The execution window balances temporal consistency with responsiveness, since a longer interval between predictions also delays the use of new observations. For visual policies, image features are used to condition action denoising. The visual encoder runs once per prediction cycle, and the same features are reused across denoising steps to reduce inference computation. The encoder can be trained jointly with the policy. The diffusion process generates actions without requiring the prediction of future visual states.

We evaluate Diffusion Policy on eight simulation tasks across four benchmarks and four real-robot tasks, covering state and visual observations and actions of different dimensions. Simulation comparisons include recurrent Gaussian mixture policies, Behavior Transformers and implicit behavioral cloning. We compare temporal convolutional and Transformer denoising networks and examine how the action execution window affects performance. Real-robot trials examine precise T-shaped object pushing, cup flipping, sauce pouring and periodic sauce spreading. These evaluations assess the benefits and practical trade-offs of action-sequence diffusion in the manipulation tasks studied.

**逐段中文译文**

**第1段。** 行为克隆将从示范中学习视为策略的监督学习，并已在真实机器人操作中获得有效策略 [1]。然而，对于同一观测，一项操作任务可能存在多个有效动作。例如，一段动作序列可以从物体左侧或右侧绕行。策略需要表达这些不同选择，同时生成精确且在时间上保持一致的动作。

**第2段。** 循环高斯混合策略利用观测历史和多个高斯分量表示动作分布 [1]。行为 Transformer 利用历史观测，预测经聚类得到的动作类别，并通过连续偏移修正动作 [2]。这些模型既提供时间上下文，也支持多模态动作预测，其分量数量或类别数量需要预先设定。以过去观测为条件和联合预测未来动作是不同的设计选择。逐步预测单个动作的策略可能在执行过程中切换有效模式，因此有理由联合预测一段具有时间关联的动作序列。

**第3段。** 隐式行为克隆提供了显式混合模型和动作类别之外的一种策略表示方式。它通过观测与动作的能量函数表示策略，并在推理时搜索低能量动作 [3]。这类策略能够表达多模态行为，已有研究已验证其处理视觉观测、高维动作和精密实机操作的能力 [3]。其对比训练目标将示范动作作为正样本，将采样动作作为负样本，以近似条件动作分布的归一化项。这一训练过程促使我们考虑直接学习分布梯度，从而避免估计该归一化项。

**第4段。** 去噪扩散模型和基于得分的生成模型通过噪声预测或得分估计学习数据分布，并从噪声出发，通过迭代更新生成样本 [4,5]。Diffuser 联合建模状态—动作轨迹，以进行基于扩散的规划 [6]；用于离线强化学习的扩散策略则将条件动作生成与 Q 值目标结合 [7]。同期的模仿学习研究分别探讨了仿真机器人任务中的目标条件扩散策略 [8]，以及仿真机器人和三维游戏环境中的多模态人类行为 [9]。这些进展确立了扩散模型作为策略表示基础的可行性。我们研究如何利用观测条件扩散，从示范中生成精确、时间一致的动作序列，同时在操作过程中保持响应能力。

**第5段。** 本文提出扩散策略，将动作生成建模为观测条件下的去噪扩散过程。该策略从示范中学习条件动作分布的得分梯度。去噪网络以观测为条件，训练目标是预测加入示范动作中的噪声。推理时，网络从高斯噪声出发迭代去噪，生成一段未来动作。扩散表示能够容纳多模态、高维输出，因此可以联合建模具有时间关联的动作。噪声预测目标避免了上述能量策略表示所使用的负采样。

**第6段。** 扩散策略既利用观测为动作生成提供条件，也利用观测在执行过程中更新预测。滚动时域执行方案只执行每段预测动作序列中的一个短片段，随后依据更新后的观测再次预测。动作执行窗口在时间一致性与响应能力之间形成折中，因为预测之间的间隔越长，新观测的使用也越迟。对于视觉策略，图像特征作为动作去噪的条件。视觉编码器在每轮预测中只运行一次，同一组特征在各次去噪中重复使用，以减少推理计算量。编码器可以与策略联合训练。扩散过程生成动作，无需预测未来视觉状态。

**第7段。** 我们在四个基准中的八项仿真任务和四项真实机器人任务上评价扩散策略，涵盖状态观测、视觉观测以及不同维度的动作。仿真比较包括循环高斯混合策略、行为 Transformer 和隐式行为克隆。我们比较时间卷积与 Transformer 两种去噪网络，并考察动作执行窗口如何影响性能。实机试验涵盖精确推动 T 形物体、翻杯、浇酱和周期性抹酱。这些评价用于考察动作序列扩散在所研究操作任务中的优势与实际权衡。

**正文使用的参考文献**

1. Mandlekar, A. et al. What Matters in Learning from Offline Human Demonstrations for Robot Manipulation. CoRL 2021, *PMLR* **164**, 1678–1690 (2022).
2. Shafiullah, N. M. M., Cui, Z. J., Altanzaya, A. & Pinto, L. Behavior Transformers: Cloning \(k\) modes with one stone. *NeurIPS* (2022). arXiv:2206.11251.
3. Florence, P. et al. Implicit Behavioral Cloning. CoRL 2021, *PMLR* **164**, 158–168 (2022).
4. Ho, J., Jain, A. & Abbeel, P. Denoising Diffusion Probabilistic Models. *NeurIPS* (2020). arXiv:2006.11239.
5. Song, Y. & Ermon, S. Generative Modeling by Estimating Gradients of the Data Distribution. *NeurIPS* (2019). arXiv:1907.05600.
6. Janner, M., Du, Y., Tenenbaum, J. & Levine, S. Planning with Diffusion for Flexible Behavior Synthesis. *ICML*, *PMLR* **162**, 9902–9915 (2022).
7. Wang, Z., Hunt, J. J. & Zhou, M. Diffusion Policies as an Expressive Policy Class for Offline Reinforcement Learning. arXiv:2208.06193, v2 (2022).
8. Reuss, M., Li, M., Jia, X. & Lioutikov, R. Goal-Conditioned Imitation Learning using Score-based Diffusion Policies. *RSS* (2023). arXiv:2304.02532.
9. Pearce, T. et al. Imitating Human Behaviour with Diffusion Models. *ICLR* (2023). arXiv:2301.10677.

**作者说明**

- 七段依次承担：操作要求、显式策略与时间关联、隐式策略与训练目标、扩散研究基础及本文问题、核心策略表示、观测条件与执行设计、验证路线。采用技术问题展开的组织方式，以方法和验证概述收束，具体性能数字留在摘要与结果部分。
- 组织与表达主要参照冻结卡片 B02、B03，局部衔接参照 B04、B05，分别借鉴比较维度、设计理由、输入—输出交接和方法选择的推进方式。范例中的科学事实未进入本稿；正文文献事实均依据所提供的背景材料与引用材料。
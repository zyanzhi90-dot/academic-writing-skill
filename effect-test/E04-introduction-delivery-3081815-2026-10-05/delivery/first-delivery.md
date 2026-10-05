**English Introduction**

Behavior cloning provides a supervised approach to learning robot manipulation policies from demonstrations and has produced effective policies on physical robots [1,3]. Demonstrations can contain several valid ways to complete a task, requiring the policy to represent a multimodal action distribution. Precise manipulation also requires accurate, temporally consistent actions. A policy that represents multiple valid actions at each step may still switch between incompatible choices during execution. The central challenge is therefore to learn an expressive action distribution while generating a coherent sequence of actions.

Recurrent Gaussian mixture policies use observation history and represent alternative actions with multiple Gaussian components [1]. Behavior Transformers combine action clustering with continuous offsets and predict actions from observation sequences [2]. Both methods incorporate temporal context and can represent multimodal continuous actions, although the number of mixture components or action clusters is set during model design. Conditioning on past observations, however, does not by itself amount to jointly generating future actions. In our controlled pushing example, the explicit policies tested favour one route around an object or switch between valid routes during stepwise prediction. This example motivates joint action-sequence prediction to maintain a coherent choice over time.

Implicit behavior cloning uses an energy function of observations and actions to represent multimodal action distributions [3]. It has supported high-dimensional actions, visual input and precise physical manipulation [3]. Its contrastive training objective uses demonstration actions and negative samples, with the negative samples approximating the conditional normalization term. In our comparisons, the implicit behavior cloning baseline exhibits fluctuations in training and evaluation. We associate these fluctuations with the negative sampling used in energy-based training. This observation motivates learning the distribution gradient directly to avoid this normalization estimate.

We propose Diffusion Policy, an observation-conditioned policy that jointly generates future actions through iterative denoising. The method builds on denoising diffusion models [4] and score-based generative modeling [5]. A network learns the score gradient of the conditional action distribution by predicting noise added to demonstration actions. At inference, iterative denoising transforms Gaussian noise into an action sequence. The diffusion representation accommodates multimodal, high-dimensional outputs and supports joint prediction of temporally correlated actions without specifying a fixed number of action modes. The noise-prediction objective avoids the negative sampling used to approximate the normalization term in contrastive energy-based training.

Diffusion has already been applied to sequential decision-making. Diffuser jointly models states and actions to generate trajectory plans with reward guidance or constraints [6]. Conditional diffusion policies have also been trained with a Q-value objective for offline reinforcement learning [7]. Concurrent work studies goal-conditioned diffusion imitation in simulated robot tasks [8] and multimodal human behavior in simulated robot and game environments [9]. Our study focuses on learning observation-conditioned action sequences through supervised behavior cloning and on the visual conditioning and execution requirements of physical robot manipulation.

Manipulation performance also depends on how the generated actions are executed. We combine action-sequence prediction with receding-horizon execution. The policy predicts a longer sequence from recent observations, executes a shorter segment and then replans from new observations. This design balances temporal consistency with responsiveness.

For visual manipulation, encoded image features condition action denoising. The policy generates actions without jointly denoising images or predicting future visual states. The image encoder can be trained end to end with the policy. Each prediction cycle encodes the images once and reuses the features at every denoising step. This reuse reduces inference computation. Iterative sampling still requires more computation than simpler policies.

We evaluate Diffusion Policy on eight tasks across four simulation benchmarks and on four physical manipulation tasks using UR5 and Franka robots. The simulation comparisons include recurrent Gaussian mixture policies, Behavior Transformers and implicit behavior cloning, using each method’s best-performing action space. We also compare temporal convolutional and diffusion Transformer denoising networks to examine task-dependent performance. The physical tasks comprise T-shaped object pushing, cup flipping, sauce pouring and periodic sauce spreading. Controlled examples, execution-window ablations and training curves examine mode consistency, responsiveness and training behavior, while the physical trials test precise visual manipulation.

**逐段中文译文**

（1）行为克隆通过监督学习从示范中学习机器人操作策略，并已在真实机器人上获得有效策略 [1,3]。示范可能包含完成同一任务的多种有效方式，因此策略需要表示多模态动作分布。精细操作还要求动作准确且在时间上保持一致。即使策略在每一步都能表示多个有效动作，执行过程中仍可能在互不相容的选择之间切换。因此，核心挑战是在学习具有充分表达能力的动作分布的同时，生成连贯的动作序列。

（2）循环高斯混合策略利用观测历史，并通过多个高斯分量表示不同的可选动作 [1]。行为 Transformer 将动作聚类与连续偏移相结合，根据观测序列预测动作 [2]。两类方法都利用时间上下文，并能够表示多模态连续动作，但混合分量或动作类别的数量需要在模型设计时设定。然而，以过去的观测为条件本身并不等同于联合生成未来动作。在我们的受控推物示例中，所测试的显式策略在逐步预测时，表现出偏向绕物体某一侧的路径，或在不同有效路径之间切换的现象。这一示例促使我们采用动作序列的联合预测，以在一段时间内保持连贯的选择。

（3）隐式行为克隆利用观测与动作的能量函数表示多模态动作分布 [3]。该方法已支持高维动作、视觉输入和精密的真实机器人操作 [3]。其对比训练目标使用示范动作和负样本，其中负样本用于近似条件分布的归一化项。在我们的比较中，隐式行为克隆基线的训练和评价表现存在波动。我们将这些波动与能量模型训练所使用的负采样联系起来。这一观察促使我们直接学习分布的梯度，以绕开上述归一化项估计。

（4）我们提出扩散策略，这是一种以观测为条件、通过迭代去噪联合生成未来动作的策略。该方法建立在去噪扩散模型 [4] 和基于得分的生成建模 [5] 之上。网络通过预测加入示范动作的噪声，学习条件动作分布的得分梯度。在推理时，迭代去噪将高斯噪声转化为动作序列。扩散表示能够容纳多模态、高维输出，并支持联合预测具有时间关联的动作，无需预先指定固定的动作模式数量。噪声预测目标绕开了能量模型对比训练中用于近似归一化项的负采样。

（5）扩散方法此前已被用于序贯决策。Diffuser 联合建模状态和动作，并结合奖励引导或约束生成轨迹计划 [6]。已有研究还通过 Q 值目标训练条件扩散策略，用于离线强化学习 [7]。同期工作研究了仿真机器人任务中的目标条件扩散模仿学习 [8]，以及仿真机器人和游戏环境中的多模态人类行为模仿 [9]。本研究关注通过监督行为克隆学习观测条件动作序列，以及真实机器人操作对视觉条件和动作执行的要求。

（6）操作性能还取决于生成的动作如何执行。我们将动作序列预测与滚动时域执行相结合。策略根据最近的观测预测较长的动作序列，执行其中较短的一段，再依据新观测重新规划。这一设计在时间一致性与响应性之间进行折中。

（7）在视觉操作中，编码后的图像特征作为动作去噪的条件。策略生成动作时，不对图像进行联合去噪，也不预测未来视觉状态。图像编码器可以与策略一起进行端到端训练。每个预测周期仅对图像编码一次，并在每一步去噪中复用这些特征。这种复用减少了推理计算量。迭代采样仍比更简单的策略需要更多计算。

（8）我们在四个仿真基准中的八类任务，以及使用 UR5 和 Franka 机器人的四项真实操作任务上评价扩散策略。仿真比较包含循环高斯混合策略、行为 Transformer 和隐式行为克隆，并采用各方法表现最佳的动作空间。我们还比较时间卷积去噪网络与扩散 Transformer 去噪网络，以考察随任务而变化的性能。真实机器人任务包括推 T 形物体、翻杯、浇酱和周期性抹酱。受控示例、执行窗口消融和训练曲线用于考察模式一致性、响应性和训练表现，真实机器人试验则用于检验精细视觉操作能力。

**正文实际使用的参考文献**

[1] Mandlekar, A., et al. What Matters in Learning from Offline Human Demonstrations for Robot Manipulation. *Proceedings of CoRL 2021*, PMLR **164**, 1678–1690 (2022).

[2] Shafiullah, N. M. M., Cui, Z. J., Altanzaya, A. & Pinto, L. Behavior Transformers: Cloning *k* modes with one stone. *NeurIPS* (2022). arXiv:2206.11251.

[3] Florence, P., et al. Implicit Behavioral Cloning. *Proceedings of CoRL 2021*, PMLR **164**, 158–168 (2022).

[4] Ho, J., Jain, A. & Abbeel, P. Denoising Diffusion Probabilistic Models. *NeurIPS* (2020). arXiv:2006.11239.

[5] Song, Y. & Ermon, S. Generative Modeling by Estimating Gradients of the Data Distribution. *NeurIPS* (2019). arXiv:1907.05600.

[6] Janner, M., Du, Y., Tenenbaum, J. & Levine, S. Planning with Diffusion for Flexible Behavior Synthesis. *Proceedings of ICML*, PMLR **162**, 9902–9915 (2022).

[7] Wang, Z., Hunt, J. J. & Zhou, M. Diffusion Policies as an Expressive Policy Class for Offline Reinforcement Learning. arXiv:2208.06193 (2022), version 2, 3 October 2022.

[8] Reuss, M., Li, M., Jia, X. & Lioutikov, R. Goal-Conditioned Imitation Learning using Score-based Diffusion Policies. *RSS* (2023). arXiv:2304.02532.

[9] Pearce, T., et al. Imitating Human Behaviour with Diffusion Models. *ICLR* (2023). arXiv:2301.10677.

**作者说明（Revision notes）**

- 已调整整节逻辑：在训练问题之后直接提出方法，再界定其与已有扩散研究的关系；执行和视觉条件分别成段。
- 表达主要参照冻结卡 B15，辅以 B16 的前作能力与条件比较写法。范例论文只用于组织和表达，其科学内容未进入本稿。
- 模式偏置、切换和训练波动均限定于本研究的示例与基线；结尾交代验证路径，未重复摘要中的定量结果。
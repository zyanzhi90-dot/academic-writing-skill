**Introduction**

Robot manipulation is important for extending automation to tasks that require physical interaction with objects. Adaptable manipulation policies are needed to perform these tasks under the variations encountered during execution. Learning from demonstration provides an effective route to acquiring manipulation skills. Behavior cloning treats policy learning as supervised learning and has produced effective policies for real-robot manipulation [1]. Demonstrations may contain several valid actions for the same observation, and successive actions must remain temporally consistent. Precise manipulation therefore requires a policy that represents multiple valid action modes while preserving the temporal relationships within a motion.

Explicit multimodal policies can represent variability in demonstrations and use past observations to predict actions. In [1], recurrent policies with Gaussian mixture outputs were studied for learning from offline human demonstrations. The recurrent model uses observation history, while multiple Gaussian components represent alternative actions. In [2], Behavior Transformer was proposed to learn multimodal continuous actions from observation sequences. The method clusters actions into discrete categories and predicts continuous offsets to refine the action estimates. Both approaches require the number of mixture components or action categories to be specified. Observation history provides temporal context, but it does not itself ensure joint generation of future actions. Stepwise prediction of individual actions can switch between valid modes. These requirements motivate a policy representation that models alternative action sequences and their temporal dependencies.

Implicit policies offer another way to represent multimodal action distributions. In [3], implicit behavior cloning was proposed to learn an energy function of observations and actions. Actions are obtained through sampling or gradient-based search for low-energy solutions. This representation supports multimodal mappings, high-dimensional actions and visual manipulation, including real contact tasks with millimeter-level precision. Its contrastive training uses demonstration actions as positive samples and negative actions to approximate the normalization term of the conditional distribution. Our comparisons show fluctuations in the training of this implicit baseline, which we relate to the negative sampling used in its energy-based formulation. Diffusion and score-based generative models offer an alternative formulation [4,5]. These models support multimodal, high-dimensional generation through learned denoising processes or gradients of the log density.

Diffusion models have already been employed in planning and policy learning. In [6], Diffuser was developed to jointly generate state–action trajectories for planning, with rewards or constraints used to guide trajectory generation. In [7], a conditional diffusion action policy was trained with a Q-value objective for offline reinforcement learning. Concurrent work has also studied goal-conditioned diffusion imitation learning with sampling-process design [8] and multimodal human-behavior imitation in simulated robot and game environments [9]. These studies establish diffusion as an expressive representation for behavior generation. A visual manipulation policy learned directly from demonstrations must also connect action-sequence generation with timely observation updates and precise execution.

This paper proposes Diffusion Policy, which models action generation as an observation-conditioned denoising diffusion process. The policy learns the score gradient of the conditional action distribution from demonstrations by predicting the noise added to demonstration actions. This training avoids the negative sampling used to estimate the normalization term in implicit behavior cloning, and our comparisons show more stable training in the tested tasks. The diffusion representation does not require a prescribed number of action modes and accommodates high-dimensional outputs. It therefore allows temporally correlated future actions to be generated jointly by iterative denoising from Gaussian noise. Joint prediction supports consistent action choices, but the robot must also respond to changes in its observations. We therefore combine action-sequence prediction with receding-horizon execution. The policy predicts a longer sequence from recent observations, executes a shorter segment and then predicts again from new observations. This execution scheme balances temporal consistency with responsiveness.

Visual action generation also requires efficient use of image observations during iterative denoising. We use an image encoder to extract features from the observations and condition the action denoising network on these features. The image encoder is evaluated once per prediction cycle, and the resulting features are reused throughout the denoising steps. This reduces inference computation and supports real-time operation in the tested configuration. The visual encoder can be trained jointly with the policy. Image observations remain conditioning inputs throughout action generation, so the policy does not need to jointly denoise images and actions or predict future visual states.

The denoising network must also preserve the action changes required for precise manipulation. We study a temporal convolutional network and a time-series diffusion Transformer as alternative architectures. The convolutional network provides a practical choice for most tested tasks, but its bias toward low-frequency signals can oversmooth rapid action changes. The Transformer is designed to reduce this effect and offers advantages on some tasks with rapid action changes or velocity control. These advantages depend on the task, and the Transformer is more sensitive to hyperparameter choices. The two architectures provide alternative choices within the same observation-conditioned action-generation framework.

Diffusion Policy brings multimodal action representation, joint sequence prediction and responsive execution into a policy learned from demonstrations. We evaluate the method on eight simulation tasks across four benchmarks and four real-robot tasks, covering state and visual observations and a range of manipulation behaviors. The simulations show a 46.9% average relative improvement across the reported performance metrics, using the best-performing diffusion architecture and baseline for each metric and each method’s best-performing action space. On real robots, the convolutional policy with end-to-end visual training achieves 95% success in 20 trials of precise T-shaped object pushing, compared with 20% for a recurrent Gaussian mixture policy and 0% for implicit behavior cloning.

**逐段中文译文**

**第1段**

机器人操作对于将自动化扩展到需要与物体进行物理交互的任务具有重要意义。为了在执行过程中遇到的变化下完成这些任务，需要具有适应性的操作策略。从示范学习为获取操作技能提供了一条有效途径。行为克隆将策略学习视为监督学习，并已在真实机器人操作中获得有效策略 [1]。对于相同观测，示范中可能包含多个有效动作，而连续动作之间又必须保持时间一致性。因此，精细操作需要一种能够表示多个有效动作模式、同时保留运动内部时间关系的策略。

**第2段**

显式多模态策略能够表示示范中的变化，并利用过去的观测预测动作。文献 [1] 研究了采用高斯混合输出的循环策略，用于从离线人类示范学习。循环模型利用观测历史，而多个高斯分量表示不同的备选动作。文献 [2] 提出了行为 Transformer，用于根据观测序列学习多模态连续动作。该方法将动作聚类为离散类别，并预测连续偏移来修正动作估计。这两类方法都需要设定混合分量或动作类别的数量。观测历史提供了时间上下文，但其本身并不确保未来动作的联合生成。逐步预测单个动作可能在有效模式之间切换。这些要求促使我们采用能够建模不同动作序列及其时间依赖关系的策略表示。

**第3段**

隐式策略为表示多模态动作分布提供了另一种途径。文献 [3] 提出了隐式行为克隆，用于学习观测与动作的能量函数。动作通过采样或基于梯度的搜索获得，以寻找低能量解。这种表示支持多模态映射、高维动作和视觉操作，包括具有毫米级精度的真实接触任务。其对比训练将示范动作作为正样本，并利用负样本近似条件分布的归一化项。我们的比较显示，该隐式基线的训练存在波动，我们将这种波动与其能量模型所使用的负采样联系起来。扩散生成模型和基于得分的生成模型提供了另一种建模方式 [4,5]。这些模型通过学习去噪过程或对数密度梯度，支持多模态、高维数据的生成。

**第4段**

扩散模型已被用于规划和策略学习。文献 [6] 开发了 Diffuser，通过联合生成状态—动作轨迹进行规划，并利用奖励或约束引导轨迹生成。文献 [7] 使用 Q 值目标训练条件扩散动作策略，用于离线强化学习。同期工作还研究了包含采样过程设计的目标条件扩散模仿学习 [8]，以及在仿真机器人和游戏环境中对多模态人类行为的模仿 [9]。这些研究表明，扩散是一种具有较强表达能力的行为生成表示。直接从示范学习的视觉操作策略还需要将动作序列生成与及时的观测更新和精确执行联系起来。

**第5段**

本文提出扩散策略，将动作生成建模为观测条件下的去噪扩散过程。策略通过预测添加到示范动作中的噪声，从示范学习条件动作分布的得分梯度。这种训练避免了隐式行为克隆中用于估计归一化项的负采样，而且我们的比较显示，它在所测任务中的训练更为稳定。扩散表示不需要预先规定动作模式的数量，并能够处理高维输出。因此，它能够从高斯噪声出发，通过迭代去噪联合生成具有时间关联的未来动作。联合预测有助于保持动作选择的一致性，但机器人还必须响应观测的变化。因此，我们将动作序列预测与滚动时域执行相结合。策略根据最近一段观测预测较长的动作序列，执行其中较短的一段，然后根据新观测再次预测。这种执行方式在时间一致性与响应能力之间取得折中。

**第6段**

视觉动作生成还需要在迭代去噪过程中高效利用图像观测。我们使用图像编码器从观测中提取特征，并以这些特征作为动作去噪网络的条件。每个预测周期只运行一次图像编码器，所得特征在各次去噪中复用。这减少了推理计算量，并支持所测配置下的实时运行。视觉编码器可以与策略联合训练。在整个动作生成过程中，图像观测始终作为条件输入，因此策略不需要对图像与动作进行联合去噪，也不需要预测未来视觉状态。

**第7段**

去噪网络还必须保留精细操作所需的动作变化。我们研究了时间卷积网络和时间序列扩散 Transformer 两种替代架构。卷积网络在多数所测任务中是一种实用选择，但其对低频信号的偏向可能使快速动作变化被过度平滑。Transformer 的设计旨在减轻这一影响，并在涉及快速动作变化或速度控制的部分任务中表现出优势。这些优势取决于任务，而且 Transformer 对超参数选择更加敏感。两种架构为同一观测条件动作生成框架提供了不同选择。

**第8段**

扩散策略将多模态动作表示、联合序列预测和能够及时响应的执行方式整合到从示范学习的策略中。我们在四个基准中的八类仿真任务和四项真实机器人任务上评价该方法，涵盖状态观测、视觉观测及多种操作行为。仿真结果显示，在所报告的性能指标上，平均相对提升为 46.9%；计算时，对每个指标采用表现最佳的扩散架构和基线，并使用各方法表现最佳的动作空间。在真实机器人上，采用端到端视觉训练的卷积策略在精细推 T 形物体任务的二十次试验中达到 95% 的成功率，而循环高斯混合策略和隐式行为克隆的成功率分别为 20% 和 0%。

**正文使用的参考文献**

1. Mandlekar, A. et al. *What Matters in Learning from Offline Human Demonstrations for Robot Manipulation*. CoRL 2021, **PMLR 164**, 1678–1690 (2022).
2. Shafiullah, N. M. M., Cui, Z. J., Altanzaya, A. & Pinto, L. *Behavior Transformers: Cloning k modes with one stone*. NeurIPS (2022). arXiv:2206.11251.
3. Florence, P. et al. *Implicit Behavioral Cloning*. CoRL 2021, **PMLR 164**, 158–168 (2022).
4. Ho, J., Jain, A. & Abbeel, P. *Denoising Diffusion Probabilistic Models*. NeurIPS (2020). arXiv:2006.11239.
5. Song, Y. & Ermon, S. *Generative Modeling by Estimating Gradients of the Data Distribution*. NeurIPS (2019). arXiv:1907.05600.
6. Janner, M., Du, Y., Tenenbaum, J. & Levine, S. *Planning with Diffusion for Flexible Behavior Synthesis*. ICML, **PMLR 162**, 9902–9915 (2022).
7. Wang, Z., Hunt, J. J. & Zhou, M. *Diffusion Policies as an Expressive Policy Class for Offline Reinforcement Learning*. arXiv:2208.06193 (2022), version 2, 3 October 2022.
8. Reuss, M., Li, M., Jia, X. & Lioutikov, R. *Goal-Conditioned Imitation Learning using Score-based Diffusion Policies*. RSS (2023). arXiv:2304.02532.
9. Pearce, T. et al. *Imitating Human Behaviour with Diffusion Models*. ICLR (2023). arXiv:2301.10677.

**必要作者说明**

- 八段依次承担：领域价值与策略要求；显式策略的能力及序列建模需要；隐式策略与训练问题；已有扩散应用；本文表示与执行设计；视觉条件与计算效率；去噪架构选择；总体贡献及代表性验证。表达以冻结候选的 B15/P17 为主，结合 B16/P05、B17/Fuzzy2023 和 B18/ESO2017 的适用正向实例。
- 46.9% 按仿真比较表的任务／指标列分别计算相对提升后求平均，排除混合熟练度多示范者结果；它不是成功率增加 46.9 个百分点。各方法采用表现最佳的动作空间，比较并非全部使用相同控制设置。
- 95% 来自二十次定量推物试验，与独立扰动演示分开；实机最佳模型采用卷积架构。本文科学与引用事实依据作者材料，写作范例只用于组织和表达。
**Introduction**

Robot manipulation extends automation to tasks that require physical interaction with objects. Adaptable policies are required to perform these tasks under variations encountered during execution. Behavior cloning provides a supervised approach to learning such policies from demonstrations and has been effective in real-robot manipulation [1]. Demonstrations may contain several valid actions for the same observation. Precise manipulation also requires accurate predictions and temporally consistent actions. Policy learning must therefore account for both action variability and the temporal structure of motion.

Explicit multimodal policies can represent alternative actions and use observation history to provide temporal context. In [1], recurrent policies with Gaussian mixture outputs were studied for learning from offline human demonstrations. The recurrent model incorporates past observations, while the Gaussian components represent alternative actions. In [2], Behavior Transformer was proposed to learn multimodal continuous actions from observation sequences. Actions are clustered into discrete categories, and continuous offsets are predicted to refine the action estimates. Both representations require the number of Gaussian components or action categories to be specified. Observation history provides temporal context, but policies that predict individual actions can still switch between modes during execution. This motivates joint generation of future actions while preserving multiple valid modes.

Implicit policies offer another way to represent multimodal action distributions. In [3], implicit behavioral cloning was proposed to learn an energy function of observations and actions. Low-energy actions are obtained through sampling or gradient-based search. The energy representation supports multimodal mappings, high-dimensional actions and visual manipulation, including millimeter-level precision in real contact tasks. Its contrastive objective uses demonstration actions as positive samples and negative actions to approximate the normalization term of the conditional distribution. Our comparisons show training fluctuations for this implicit baseline, which we relate to its use of negative sampling.

Diffusion and score-based generative models provide an alternative based on learned denoising processes and gradients of the log density [4,5]. These models support multimodal, high-dimensional generation. In [6], Diffuser was developed to jointly generate state–action trajectories for planning, with rewards or constraints guiding trajectory generation. In [7], a conditional diffusion action policy was trained with a Q-value objective for offline reinforcement learning. Concurrent studies investigated goal-conditioned diffusion imitation learning with sampling-process design [8] and diffusion-based imitation of multimodal human behavior in simulated robot and game environments [9]. These studies establish diffusion as an expressive representation for behavior generation. The present study examines how this representation can be combined with joint action-sequence prediction, feedback during execution and efficient visual conditioning for robot manipulation.

This paper proposes Diffusion Policy, which models robot action generation as an observation-conditioned denoising diffusion process. The policy learns the score gradient of the conditional action distribution from demonstrations, avoiding the negative sampling used to estimate the normalization term in implicit behavioral cloning. Our comparisons show more stable training in the tested tasks. The diffusion representation supports multimodal, high-dimensional outputs without a prescribed number of action modes. We use this representation to jointly predict temporally correlated future actions by iterative denoising from Gaussian noise. The robot must also respond to observations acquired after prediction. We therefore combine action-sequence prediction with receding-horizon execution. The policy predicts a longer action sequence from recent observations, executes a shorter segment and replans from new observations. This balances temporal consistency with responsiveness.

Visual conditioning must provide observation information without repeatedly processing images during action denoising. An image encoder extracts features from the observations, and these features condition the action denoising network. The encoder is evaluated once per prediction cycle, and its features are reused for all denoising steps. This reduces inference computation and supports real-time operation in the tested configuration. The diffusion process generates actions, with image features used only as conditioning inputs. The visual encoder can be trained jointly with the policy.

The denoising network must preserve the rapid action changes required in some manipulation tasks. We study a temporal convolutional network and a time-series diffusion Transformer as alternative architectures. The convolutional network is practical for most tested tasks, but its bias toward low-frequency signals can oversmooth action changes. The Transformer is designed to reduce this effect and has advantages on some tasks with rapid action changes or velocity control, although it is more sensitive to hyperparameter choices.

The resulting policy combines multimodal action representation, joint sequence prediction and receding-horizon execution for learning manipulation skills from demonstrations. We evaluate Diffusion Policy on eight simulation tasks across four benchmarks and four real-robot tasks, covering state and visual observations and different action dimensions. Across the reported simulation metrics, the average relative performance improvement is 46.9%. This comparison uses the best-performing diffusion architecture and baseline for each metric and each method’s best-performing action space. On real robots, the convolutional policy with end-to-end visual training achieves 95% success in 20 trials of precise T-shaped object pushing, compared with 20% for a recurrent Gaussian mixture policy and 0% for implicit behavioral cloning.

**逐段中文译文**

**第1段**

机器人操作将自动化扩展到需要与物体进行物理交互的任务。为了在执行过程中出现的变化下完成这些任务，需要具有适应性的策略。行为克隆提供了一种从示范中学习此类策略的监督学习方法，并已在真实机器人操作中取得有效表现[1]。对于同一观测，示范中可能包含多个有效动作。精细操作还要求准确的预测和时间一致的动作。因此，策略学习必须同时考虑动作的多样性和运动的时间结构。

**第2段**

显式多模态策略能够表示不同的有效动作，并利用观测历史提供时间上下文。文献[1]研究了采用高斯混合输出的循环策略，用于从离线人类示范中学习。循环模型纳入过去的观测，而多个高斯分量表示不同的动作选择。文献[2]提出了行为 Transformer，用于从观测序列中学习多模态连续动作。该方法将动作聚类为离散类别，并预测连续偏移以修正动作估计。这两种表示都需要预先设定高斯分量或动作类别的数量。观测历史提供了时间上下文，但逐个预测动作的策略在执行过程中仍可能在不同模式之间切换。因此，有必要在保留多个有效模式的同时联合生成未来动作。

**第3段**

隐式策略提供了另一种表示多模态动作分布的方式。文献[3]提出了隐式行为克隆，用于学习观测与动作的能量函数。低能量动作通过采样或基于梯度的搜索获得。能量表示支持多模态映射、高维动作和视觉操作，包括在真实接触任务中实现毫米级精度。其对比学习目标使用示范动作作为正样本，并使用负例动作近似条件分布的归一化项。我们的比较显示，这一隐式基线在训练过程中存在波动，我们将其与该方法使用的负采样联系起来。

**第4段**

扩散模型和基于得分的生成模型提供了一种替代路线，其基础是学习去噪过程以及对数密度的梯度[4,5]。这些模型支持多模态、高维数据生成。文献[6]开发了 Diffuser，通过联合生成状态—动作轨迹进行规划，并利用奖励或约束引导轨迹生成。文献[7]使用 Q 值目标训练条件扩散动作策略，用于离线强化学习。同期研究还探讨了结合采样过程设计的目标条件扩散模仿学习[8]，以及在仿真机器人和游戏环境中利用扩散模型模仿多模态人类行为[9]。这些研究确立了扩散作为行为生成表示的表达能力。本研究考察如何将这种表示与联合动作序列预测、执行过程中的反馈以及高效视觉条件处理相结合，用于机器人操作。

**第5段**

本文提出扩散策略，将机器人动作生成建模为观测条件下的去噪扩散过程。该策略从示范中学习条件动作分布的得分梯度，从而避免隐式行为克隆中用于估计归一化项的负采样。我们的比较显示，该策略在所测任务中的训练更为稳定。扩散表示支持多模态、高维输出，无需预先规定动作模式的数量。我们利用这种表示，从高斯噪声出发进行迭代去噪，联合预测具有时间关联的未来动作。机器人还必须响应预测之后获得的观测。因此，我们将动作序列预测与滚动时域执行相结合。策略依据最近一段观测预测较长的动作序列，执行其中较短的一段，再根据新观测重新规划。这在时间一致性与响应能力之间取得折中。

**第6段**

视觉条件处理需要提供观测信息，同时避免在动作去噪过程中重复处理图像。图像编码器从观测中提取特征，这些特征作为动作去噪网络的条件。每个预测周期只运行一次编码器，并在所有去噪步骤中复用其特征。这减少了推理计算量，并在所测配置下支持实时运行。扩散过程生成动作，图像特征仅作为条件输入。视觉编码器可以与策略联合训练。

**第7段**

去噪网络必须保留部分操作任务所需的快速动作变化。我们研究了时间卷积网络和时间序列扩散 Transformer 两种替代架构。卷积网络在多数所测任务中易于使用，但其对低频信号的偏向可能使动作变化过度平滑。Transformer 的设计旨在减轻这一影响，并在部分涉及快速动作变化或速度控制的任务上具有优势，但它对超参数选择更为敏感。

**第8段**

所形成的策略结合了多模态动作表示、联合序列预测和滚动时域执行，用于从示范中学习操作技能。我们在四个基准中的八项仿真任务和四项真实机器人任务上评估扩散策略，涵盖状态观测、视觉观测以及不同的动作维度。在所报告的仿真指标上，平均相对性能提升为46.9%。这一比较对每个指标采用表现最佳的扩散架构和基线，并采用各方法表现最佳的动作空间。在真实机器人上，采用端到端视觉训练的卷积策略在精确推动T形物体的20次试验中达到95%的成功率，循环高斯混合策略和隐式行为克隆的成功率分别为20%和0%。

**正文实际使用的参考文献**

1. Mandlekar, A. et al. *What Matters in Learning from Offline Human Demonstrations for Robot Manipulation*. CoRL 2021, **PMLR 164**, 1678–1690 (2022).
2. Shafiullah, N. M. M., Cui, Z. J., Altanzaya, A. & Pinto, L. *Behavior Transformers: Cloning k modes with one stone*. NeurIPS (2022). arXiv:2206.11251.
3. Florence, P. et al. *Implicit Behavioral Cloning*. CoRL 2021, **PMLR 164**, 158–168 (2022).
4. Ho, J., Jain, A. & Abbeel, P. *Denoising Diffusion Probabilistic Models*. NeurIPS (2020). arXiv:2006.11239.
5. Song, Y. & Ermon, S. *Generative Modeling by Estimating Gradients of the Data Distribution*. NeurIPS (2019). arXiv:1907.05600.
6. Janner, M., Du, Y., Tenenbaum, J. & Levine, S. *Planning with Diffusion for Flexible Behavior Synthesis*. ICML, **PMLR 162**, 9902–9915 (2022).
7. Wang, Z., Hunt, J. J. & Zhou, M. *Diffusion Policies as an Expressive Policy Class for Offline Reinforcement Learning*. arXiv:2208.06193 (2022), version 2, 3 October 2022.
8. Reuss, M., Li, M., Jia, X. & Lioutikov, R. *Goal-Conditioned Imitation Learning using Score-based Diffusion Policies*. RSS (2023). arXiv:2304.02532.
9. Pearce, T. et al. *Imitating Human Behaviour with Diffusion Models*. ICLR (2023). arXiv:2301.10677.

**作者说明**

- 整节调整了文献能力、任务需要与设计作用之间的衔接，压缩重复说明；保留末段实验结果，用于支持方法贡献。
- 组织与表达以冻结候选的 B15/P17 正向范例为主，并结合 B16–B18 的适用写法。范例科学内容未进入本文事实，也未作为新增科学引用。
- 46.9%为所列仿真指标逐列计算后得到的平均相对提升，排除混合熟练度多示范者结果；95%对应20次定量推物试验，与独立扰动演示区分。训练稳定性及实时运行的表述均保留其测试范围。
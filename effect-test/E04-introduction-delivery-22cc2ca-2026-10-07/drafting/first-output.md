**Introduction**

Robot manipulation enables robots to carry out physical tasks through interaction with objects. Fine manipulation requires precise actions, and the actions within a skill must remain temporally consistent. Learning from demonstration is a valuable technique for acquiring such manipulation skills. Behavior cloning formulates policy learning as supervised prediction of demonstrated actions from observations [1]. Demonstrations can contain multiple valid action modes, with temporal relationships between successive actions. It is therefore essential to consider how a learned policy can represent this variability while generating precise, temporally consistent actions.

Explicit probabilistic policies can represent multiple action modes while incorporating observation histories. In [1], a recurrent policy with a Gaussian mixture output was used to learn robot manipulation from offline human demonstrations. The recurrent model supplies temporal context, and the mixture components represent different action modes. In [2], Behavior Transformer was proposed to predict multimodal continuous actions from a sequence of past observations. The model combines action categories obtained by clustering with continuous offsets that refine the corresponding actions. The numbers of mixture components and action categories are specified in these representations. Historical context and joint prediction of future actions, however, serve different purposes. A policy that predicts individual actions step by step can switch between valid modes. The current learning problem therefore calls for a representation that accommodates multimodal, high-dimensional action sequences without fixing the number of modes in advance.

Implicit policies provide an alternative to representing action modes through a finite mixture or a set of action categories. In [3], an energy-based policy was proposed for behavioral cloning. The energy function assigns low energy to actions compatible with an observation, allowing multiple low-energy actions to represent multimodal distributions and multivalued mappings. The method supports high-dimensional actions and visual observations and was demonstrated on real-robot contact tasks with millimeter-level precision. Its contrastive training uses demonstrated actions and sampled negative actions, with the negatives used to approximate the normalization term of the conditional distribution. Directly learning the distribution gradient offers a way to avoid this normalization estimate and the associated negative sampling while retaining an expressive action representation.

Diffusion models offer a generative framework for learning distribution gradients and sampling multimodal, high-dimensional outputs [4], [5]. In [4], a denoising diffusion probabilistic model was developed to generate samples through a learned reverse denoising process. In [5], score estimates at multiple noise scales were used for sample generation. Diffusion has also been applied to decision-making. In [6], Diffuser was proposed to jointly generate states and actions for trajectory planning with rewards or constraints. In [7], conditional diffusion was employed as an offline reinforcement learning policy, with a Q-value objective used to improve the policy. Concurrent work studied goal-conditioned diffusion imitation learning in simulated robot tasks [8] and multimodal human behavior imitation in simulated robot and three-dimensional game environments [9]. These studies establish a basis for diffusion representations of trajectories and policies. A diffusion policy for manipulation learned directly from demonstrations must connect joint action generation with feedback during execution and efficient use of visual observations. To address these requirements, we propose Diffusion Policy, which models action generation as an observation-conditioned denoising diffusion process. The policy learns the score gradient of the conditional action distribution from demonstrations using a noise-prediction objective. Future actions are generated jointly by iterative denoising from Gaussian noise, allowing multimodal actions and their temporal relationships to be represented within the same sequence model.

Joint action generation must retain the temporal structure needed for precise manipulation. Temporal convolutional networks can favor low-frequency signals and smooth changes in the predicted actions. We consider a temporal convolutional network and a time-series diffusion Transformer as alternative denoisers, with the Transformer designed to reduce this smoothing tendency. The execution of a generated sequence presents a separate requirement. Joint prediction represents temporal relationships over the prediction horizon, but executing the entire prediction before observing again would delay the response to new observations. We therefore combine joint prediction with receding-horizon execution. The policy predicts an action sequence from recent observations, executes a shorter segment, and then predicts again using new observations. The longer prediction horizon supports temporally consistent action generation, while execution over a shorter window allows updates from new observations.

Visual conditioning introduces a further computational requirement because iterative action generation repeatedly uses the same observations. The observations remain fixed within each prediction cycle, so the visual computation can be shared across its denoising steps. We therefore encode image observations once per prediction cycle and use the resulting features to condition every denoising step. The image features serve as conditions, while the denoising output consists only of actions. The visual encoder can be trained end to end with the policy. Reusing these features reduces repeated visual computation during action generation and supports timely replanning.

The main contributions of this paper can be summarized as follows.

1\) An observation-conditioned diffusion policy is developed for learning robot manipulation from demonstrations. The policy represents multimodal action distributions through score-gradient learning, avoiding the normalization estimate and negative sampling used in the contrastive energy-based formulation.

2\) Joint action-sequence prediction is combined with receding-horizon execution to address temporal consistency and responsiveness. Temporal convolutional and Transformer networks provide alternative sequence denoisers, with the Transformer included to mitigate excessive smoothing of action changes.

3\) A visual conditioning scheme is developed to reuse encoded image features across all denoising steps. The scheme reduces repeated computation within each action prediction cycle while allowing the visual encoder and policy to be trained end to end.

**逐段中文译文**

（第1段）机器人操作使机器人能够通过与物体交互来完成物理任务。精细操作需要精确的动作，技能中的动作还必须保持时间一致性。从示范学习是获取这类操作技能的一种有价值的技术。行为克隆将策略学习表述为根据观测对示范动作进行监督预测的问题 [1]。示范可以包含多个有效动作模式，连续动作之间也存在时间关联。因此，需要考虑学习得到的策略如何表示这种变化，同时生成精确且在时间上连贯的动作。

（第2段）显式概率策略能够在利用历史观测的同时表示多个动作模式。在文献 [1] 中，具有高斯混合输出的循环策略被用于从离线人类示范中学习机器人操作。循环模型提供时间上下文，而混合分量表示不同的动作模式。在文献 [2] 中，Behavior Transformer 被提出用于根据过去的观测序列预测多模态连续动作。该模型将聚类得到的动作类别与连续偏移结合，利用偏移修正相应的动作。这些表示中的混合分量数量和动作类别数量需要预先设定。然而，历史上下文与未来动作的联合预测承担不同的作用。逐步预测单个动作的策略可能在有效模式之间跳换。因此，当前学习问题需要一种能够表示多模态、高维动作序列，而不预先固定模式数量的表示方法。

（第3段）隐式策略提供了有限混合模型或动作类别集合之外的动作模式表示方式。在文献 [3] 中，能量策略被提出用于行为克隆。能量函数为与观测相符的动作赋予低能量，使多个低能量动作能够表示多模态分布和多值映射。该方法支持高维动作和视觉观测，并已在真实机器人接触任务中展示毫米级精度。其对比训练使用示范动作和采样得到的负例动作，利用负例近似条件分布的归一化项。直接学习分布梯度提供了一条途径，使策略能够在保留丰富动作表示能力的同时，避免这项归一化估计及其相关负采样。

（第4段）扩散模型为学习分布梯度以及采样多模态、高维输出提供了生成建模框架 [4]、[5]。在文献 [4] 中，去噪扩散概率模型被开发用于通过学习得到的反向去噪过程生成样本。在文献 [5] 中，不同噪声尺度下的得分估计被用于样本生成。扩散也已应用于决策问题。在文献 [6] 中，Diffuser 被提出用于联合生成状态和动作，从而进行结合奖励或约束的轨迹规划。在文献 [7] 中，条件扩散被用作离线强化学习策略，并通过 Q 值目标改进策略。同期工作分别在仿真机器人任务中研究了目标条件扩散模仿学习 [8]，以及在仿真机器人和三维游戏环境中研究了多模态人类行为模仿 [9]。这些研究为轨迹和策略的扩散表示奠定了基础。对于直接从示范中学习操作的扩散策略，需要将动作联合生成与执行期间的反馈以及视觉观测的高效利用联系起来。为满足这些要求，本文提出扩散策略，将动作生成建模为观测条件下的去噪扩散过程。该策略采用噪声预测目标，从示范中学习条件动作分布的得分梯度。未来动作通过从高斯噪声开始的迭代去噪联合生成，使多模态动作及其时间关联能够在同一个序列模型中得到表示。

（第5段）动作联合生成需要保留精细操作所需的时间结构。时间卷积网络可能偏向低频信号，并平滑预测动作中的变化。本文采用时间卷积网络和时间序列扩散 Transformer 作为两种替代去噪架构，其中 Transformer 的设计目的是减轻这种平滑倾向。生成序列的执行还涉及另一项要求。联合预测在预测时域内表示动作的时间关联，但如果在再次获取观测前执行完整段预测，就会延迟对新观测的响应。因此，本文将联合预测与滚动时域执行结合。策略根据最近的观测预测一段动作序列，执行其中较短的片段，然后利用新观测再次预测。较长的预测时域支持时间连贯的动作生成，而较短的执行窗口使策略能够利用新观测更新后续动作。

（第6段）视觉条件带来进一步的计算要求，因为迭代动作生成会反复使用同一组观测。每轮预测中的观测保持不变，因此视觉计算可以在该轮的各次去噪之间共享。为此，本文每轮预测只对图像观测编码一次，并使用得到的特征作为每次去噪的条件。图像特征承担条件输入的作用，而去噪输出仅包含动作。视觉编码器可以与策略进行端到端训练。复用这些特征减少了动作生成期间重复的视觉计算，并有助于及时重新规划。

（第7段及贡献项）本文的主要贡献可概括如下。

1\) 提出一种观测条件扩散策略，用于从示范中学习机器人操作。该策略通过得分梯度学习表示多模态动作分布，避免对比式能量建模中的归一化估计与负采样。

2\) 将动作序列联合预测与滚动时域执行结合，以兼顾时间一致性和响应能力。时间卷积网络与 Transformer 提供两种替代序列去噪架构，其中引入 Transformer 的目的是减轻对动作变化的过度平滑。

3\) 提出一种视觉条件方案，在各次去噪中复用编码后的图像特征。该方案减少每轮动作预测中的重复计算，同时允许视觉编码器与策略进行端到端训练。

**正文实际使用的参考文献**

[1] Mandlekar, A. et al. What Matters in Learning from Offline Human Demonstrations for Robot Manipulation. *Proceedings of CoRL 2021*, PMLR **164**, 1678–1690 (2022).

[2] Shafiullah, N. M. M., Cui, Z. J., Altanzaya, A. & Pinto, L. Behavior Transformers: Cloning *k* modes with one stone. *NeurIPS* (2022). arXiv:2206.11251.

[3] Florence, P. et al. Implicit Behavioral Cloning. *Proceedings of CoRL 2021*, PMLR **164**, 158–168 (2022).

[4] Ho, J., Jain, A. & Abbeel, P. Denoising Diffusion Probabilistic Models. *NeurIPS* (2020). arXiv:2006.11239.

[5] Song, Y. & Ermon, S. Generative Modeling by Estimating Gradients of the Data Distribution. *NeurIPS* (2019). arXiv:1907.05600.

[6] Janner, M., Du, Y., Tenenbaum, J. & Levine, S. Planning with Diffusion for Flexible Behavior Synthesis. *ICML*, PMLR **162**, 9902–9915 (2022).

[7] Wang, Z., Hunt, J. J. & Zhou, M. Diffusion Policies as an Expressive Policy Class for Offline Reinforcement Learning. arXiv:2208.06193, v2 (2022).

[8] Reuss, M., Li, M., Jia, X. & Lioutikov, R. Goal-Conditioned Imitation Learning using Score-based Diffusion Policies. *Robotics: Science and Systems* (2023). arXiv:2304.02532.

[9] Pearce, T. et al. Imitating Human Behaviour with Diffusion Models. *ICLR* (2023). arXiv:2301.10677.

**作者说明**

整节依次建立操作学习需要、显式与隐式策略的相关能力、扩散设计的采用理由、序列生成与执行的分工，以及视觉条件的计算作用。组织和表达以冻结候选中的 P17 为主要锚点，结合 P05 的能力—条件推进、Fuzzy 的并列需要与贡献写法，以及 ESO 的计算作用表达；范例科学内容未移入本文。

按最新作者要求，正文及贡献项均未纳入本研究的实验、比较或结果。Transformer 仅按替代架构及减轻平滑的设计目的陈述；减少负采样未被表述为闭环稳定保证。文献 [7] 使用所提供的 2022 年 v2 出版身份。
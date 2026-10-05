## Introduction

Behavior cloning learns robot manipulation policies from demonstrations through supervised learning. Previous studies have shown that this approach can produce effective policies for manipulation with visual observations and precise contact tasks [1,3]. Demonstrations can contain several valid ways to complete the same task, and a policy must preserve these choices while producing accurate actions. The actions must also remain consistent over time and respond to new observations during execution. The central problem is therefore how to represent the demonstrated action distribution and use that representation to generate precise, temporally consistent behavior.

Probabilistic policies provide useful representations of action variability. Recurrent Gaussian mixture policies use observation history and multiple Gaussian components to represent multimodal actions [1]. Behavior Transformers use historical observations to predict an action cluster and a continuous offset, combining discrete action categories with continuous corrections [2]. Both approaches support multimodal actions and temporal context, although the numbers of mixture components or action categories must be specified. Historical observations provide information about past behavior, but their use is distinct from jointly generating future actions. In our controlled pushing example, the compared explicit policies exhibit mode bias or switch between valid routes around an object. This observation motivates a representation that can preserve multiple action modes and generate a temporally correlated action sequence.

Implicit behavioral cloning represents an observation-conditioned action distribution with an energy function and searches for low-energy actions during inference [3]. Multiple low-energy actions support multimodal behavior, and the method has demonstrated visual manipulation, high-dimensional actions and precise real-robot operation. Its contrastive training uses demonstrated actions and negative action samples to approximate the normalization term of the conditional distribution. In our experiments, the implicit behavioral cloning baseline exhibits fluctuations during training and evaluation. The training procedure therefore motivates an alternative that retains an expressive action distribution while avoiding the normalization estimate and negative sampling used by this energy-based policy.

Diffusion models provide a generative representation based on iterative denoising and score learning [4,5]. These methods can represent multimodal distributions and generate high-dimensional samples. Diffusion has already been used to generate joint state–action trajectories for planning [6] and to represent action policies in offline reinforcement learning [7]. Concurrent work also investigates goal-conditioned diffusion imitation learning [8] and diffusion models for multimodal human behavior in simulated robotic and game environments [9]. Our study focuses on learning an observation-conditioned action policy directly from demonstrations for robot manipulation. The question is how to combine expressive action generation with temporal consistency, visual observations and feedback during physical execution.

We propose Diffusion Policy, which models action generation as an observation-conditioned denoising diffusion process. A network is trained to predict the noise added to demonstrated actions, thereby learning the score gradient of the conditional action distribution. During inference, the policy starts from Gaussian noise and iteratively denoises a sequence of future actions. The diffusion representation accommodates multiple action modes without prescribing a fixed number of mixture components or action categories. Its ability to handle high-dimensional outputs allows temporally correlated actions to be generated jointly. Direct score learning also avoids the negative sampling needed to estimate the normalization term in the implicit behavioral cloning baseline, and Diffusion Policy exhibits more stable training in our experiments.

The manipulation performance also depends on how the predicted action sequence is executed. A long execution window delays the use of new observations, whereas a very short window can compromise temporal consistency. We integrate action-sequence prediction with receding-horizon execution to balance these requirements. At each prediction cycle, the policy uses a recent history of observations to generate a longer action sequence and executes only a shorter segment. The policy then acquires new observations and predicts another sequence. This scheme preserves temporal structure within the executed segment while allowing subsequent actions to respond to updated observations.

Visual conditioning introduces an additional computational requirement because action generation involves repeated denoising. We encode image observations once per prediction cycle and use the resulting features to condition every denoising step. Images serve as conditioning inputs, and the denoising output consists of actions. The policy therefore generates actions without inferring future visual states. The visual encoder can be trained jointly with the denoising network. Feature reuse reduces the computation required by repeated denoising and helps support real-time inference.

The denoising network must also represent changes in the action sequence accurately. We consider a temporal convolutional network and a time-series diffusion Transformer as alternative architectures. Temporal convolution can favor low-frequency signals and smooth rapid action changes. The Transformer is designed to mitigate this tendency and offers advantages on some tasks involving rapidly changing actions or velocity control. The convolutional network is easy to use on most evaluated tasks, while the Transformer is more sensitive to hyperparameters. The architecture choice consequently depends on the action characteristics and task requirements.

We evaluate Diffusion Policy on eight simulation tasks from four benchmarks and four real-robot tasks. The simulation study compares recurrent Gaussian mixture policies, Behavior Transformers and implicit behavioral cloning using each method’s best-performing action space. The experiments examine multimodal behavior, training behavior and the effect of the action execution window, alongside manipulation performance. Real-robot experiments test precise T-shaped object pushing, cup flipping, sauce pouring and periodic sauce spreading. Together, these evaluations demonstrate the practical value of observation-conditioned diffusion action sequences and receding-horizon execution for the manipulation tasks studied.

## 逐段中文译文

**第1段**

行为克隆通过监督学习，从示范中学习机器人操作策略。已有研究表明，这种方法能够在使用视觉观测的操作任务和精细接触任务中获得有效策略[1,3]。示范可能包含完成同一任务的多种有效方式，策略需要在生成准确动作的同时保留这些选择。动作还需要在时间上保持一致，并在执行过程中响应新的观测。因此，核心问题是如何表示示范中的动作分布，并利用这种表示生成精确且具有时间一致性的行为。

**第2段**

概率策略为动作的变化性提供了有用的表示。循环高斯混合策略利用观测历史和多个高斯分量表示多模态动作[1]。行为 Transformer 利用历史观测预测动作类别和连续偏移，将离散动作类别与连续修正相结合[2]。这两类方法都支持多模态动作和时间上下文，但混合分量或动作类别的数量需要预先设定。历史观测提供过去行为的信息，但利用历史观测与联合生成未来动作是不同的设计。在我们的受控推物示例中，参与比较的显式策略表现出模式偏置，或在绕过物体的有效路径之间切换。这一观察促使我们采用能够保留多个动作模式并生成时间相关动作序列的表示。

**第3段**

隐式行为克隆使用能量函数表示观测条件下的动作分布，并在推理时寻找低能量动作[3]。多个低能量动作支持多模态行为，该方法也已展示视觉操作、高维动作和精细真实机器人操作能力。其对比训练使用示范动作和负动作样本，近似条件分布的归一化项。在我们的实验中，隐式行为克隆基线的训练和评价表现存在波动。因此，这种训练过程促使我们寻求一种替代方案，在保留动作分布表达能力的同时，绕开该能量策略使用的归一化估计与负采样。

**第4段**

扩散模型提供了一种基于迭代去噪和得分学习的生成表示[4,5]。这些方法能够表示多模态分布并生成高维样本。扩散方法已被用于生成状态与动作的联合轨迹以进行规划[6]，也已被用于表示离线强化学习中的动作策略[7]。同期工作还研究了目标条件扩散模仿学习[8]，以及在仿真机器人和游戏环境中利用扩散模型模仿多模态人类行为[9]。我们的研究关注直接从示范中学习用于机器人操作的观测条件动作策略。研究问题是如何将具有充分表达能力的动作生成与时间一致性、视觉观测及物理执行过程中的反馈相结合。

**第5段**

我们提出扩散策略，将动作生成建模为观测条件下的去噪扩散过程。网络通过预测加入示范动作的噪声进行训练，从而学习条件动作分布的得分梯度。在推理过程中，策略从高斯噪声出发，通过迭代去噪生成一段未来动作。扩散表示能够容纳多个动作模式，无需预先指定固定数量的混合分量或动作类别。其处理高维输出的能力使时间相关的动作能够被联合生成。直接学习得分还绕开了隐式行为克隆基线为估计归一化项所需的负采样，并且扩散策略在我们的实验中表现出更稳定的训练。

**第6段**

操作性能还取决于预测动作序列的执行方式。较长的执行窗口会延迟新观测的使用，而过短的窗口可能损害时间一致性。我们将动作序列预测与滚动时域执行相结合，以平衡这两项要求。在每个预测周期中，策略利用最近一段观测历史生成较长的动作序列，并只执行其中较短的一段。随后，策略获取新的观测并预测下一段序列。这种方式保留了已执行片段内部的时间结构，同时允许后续动作响应更新后的观测。

**第7段**

视觉条件输入带来了额外的计算要求，因为动作生成需要重复去噪。我们在每个预测周期中只对图像观测编码一次，并利用得到的特征为每一步去噪提供条件。图像作为条件输入，去噪输出则由动作构成。因此，策略生成动作时无需推断未来视觉状态。视觉编码器可以与去噪网络联合训练。特征复用减少了重复去噪所需的计算，有助于实现实时推理。

**第8段**

去噪网络还需要准确表示动作序列中的变化。我们考虑时间卷积网络和时间序列扩散 Transformer 两种替代架构。时间卷积可能偏向低频信号，并将快速动作变化过度平滑。Transformer 的设计用于减轻这一倾向，并在涉及快速动作变化或速度控制的部分任务上具有优势。卷积网络在多数已评价任务中易于使用，而 Transformer 对超参数更加敏感。因此，架构选择取决于动作特征和任务要求。

**第9段**

我们在四个基准中的八项仿真任务和四项真实机器人任务上评价扩散策略。仿真研究与循环高斯混合策略、行为 Transformer 和隐式行为克隆进行比较，各方法均采用其表现最佳的动作空间。实验在评价操作性能的同时，考察多模态行为、训练表现及动作执行窗口的影响。真实机器人实验测试精细 T 形物体推动、翻杯、浇酱和周期性抹酱。这些评价共同展示了观测条件扩散动作序列与滚动时域执行在本研究所测操作任务中的实用价值。

## 正文使用的参考文献

[1] Mandlekar, A. et al. **What Matters in Learning from Offline Human Demonstrations for Robot Manipulation.** CoRL 2021, *PMLR* **164**, 1678–1690 (2022).

[2] Shafiullah, N. M. M., Cui, Z. J., Altanzaya, A. & Pinto, L. **Behavior Transformers: Cloning \(k\) modes with one stone.** NeurIPS (2022). arXiv:2206.11251.

[3] Florence, P. et al. **Implicit Behavioral Cloning.** CoRL 2021, *PMLR* **164**, 158–168 (2022).

[4] Ho, J., Jain, A. & Abbeel, P. **Denoising Diffusion Probabilistic Models.** NeurIPS (2020). arXiv:2006.11239.

[5] Song, Y. & Ermon, S. **Generative Modeling by Estimating Gradients of the Data Distribution.** NeurIPS (2019). arXiv:1907.05600.

[6] Janner, M., Du, Y., Tenenbaum, J. & Levine, S. **Planning with Diffusion for Flexible Behavior Synthesis.** ICML, *PMLR* **162**, 9902–9915 (2022).

[7] Wang, Z., Hunt, J. J. & Zhou, M. **Diffusion Policies as an Expressive Policy Class for Offline Reinforcement Learning.** arXiv:2208.06193 (2022).

[8] Reuss, M., Li, M., Jia, X. & Lioutikov, R. **Goal-Conditioned Imitation Learning using Score-based Diffusion Policies.** RSS (2023). arXiv:2304.02532.

[9] Pearce, T. et al. **Imitating Human Behaviour with Diffusion Models.** ICLR (2023). arXiv:2301.10677.

## 作者说明

整节由动作表示推进到训练、序列生成、反馈执行、视觉计算和网络选择，最后交代验证范围。模式偏置和训练波动均限定为本研究中的观察；Transformer 的优势保留任务条件。46.9% 平均相对提升和实机成功率留在已验收摘要及实验章节中展开。

表达主要采用 B15 的“表征选择—执行责任”推进及明确对象的普通主谓句，补充 B16 对前作能力和适用条件的处理。范例科学内容未作为本文事实。

读取公共说明的一次范围过宽，额外返回了 A01–A04 的部分摘要卡；本引言采用的表达范例为 B15 和 B16。
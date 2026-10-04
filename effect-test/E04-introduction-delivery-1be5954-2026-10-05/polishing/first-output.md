**English Introduction**

Robot manipulation policies learned from demonstrations need to generate precise actions while representing multiple valid ways to complete a task. Behavior cloning has produced effective policies for real-robot manipulation through supervised learning from demonstrations [1]. A task may, for example, admit action sequences that pass to either side of an object. The policy must represent these alternatives while maintaining temporal consistency and responding to new observations.

Recurrent Gaussian mixture policies use observation histories and multiple Gaussian components to model action distributions [1]. Behavior Transformers use historical observations to predict clustered action categories and continuous offsets that refine the predicted actions [2]. Both methods support multimodal actions and temporal context, with a prescribed number of components or categories. Observation histories and joint prediction of future actions serve different purposes. Stepwise prediction of individual actions can switch between valid modes during execution, motivating joint generation of a temporally correlated action sequence.

Implicit behavioral cloning represents the policy with an energy function of observations and actions and searches for low-energy actions during inference [3]. This representation supports multimodal behavior and has been demonstrated with visual observations, high-dimensional actions and precise real-robot manipulation [3]. Its contrastive training objective uses demonstration actions as positive samples and sampled actions as negatives to approximate the normalization term of the conditional action distribution. Directly learning the gradient of this distribution offers an alternative to estimating the normalization term.

Denoising diffusion and score-based generative models learn data distributions through noise prediction or score estimation and generate samples iteratively from noise [4,5]. Diffusion has been used to jointly generate state–action trajectories for planning [6] and to represent conditional action policies trained with a Q-value objective for offline reinforcement learning [7]. Contemporaneous work also studies goal-conditioned imitation in simulated robot tasks [8] and multimodal human behavior in simulated robot and three-dimensional game environments [9]. We investigate how observation-conditioned diffusion learned from demonstrations can jointly generate future actions while retaining responsiveness during precise visual manipulation.

This paper proposes Diffusion Policy, which models action generation as observation-conditioned denoising diffusion. The policy learns the score gradient of the conditional action distribution through a noise-prediction objective. A denoising network predicts the noise added to demonstrated actions, using observations as conditions. At inference, iterative denoising transforms Gaussian noise into a sequence of future actions. The diffusion representation accommodates multimodal, high-dimensional action distributions, allowing temporally correlated actions to be generated jointly. The noise-prediction objective avoids the negative sampling used in contrastive energy-based training.

Diffusion Policy combines action-sequence generation with receding-horizon execution to balance temporal consistency with responsiveness. The policy predicts a longer action sequence from recent observations, executes a shorter segment and then predicts again from new observations. The execution window determines how long the robot follows a jointly generated sequence before incorporating new feedback. For visual policies, encoded image features condition action denoising. The visual encoder runs once per prediction cycle, and its features are reused across all denoising steps to reduce inference computation. The encoder can be trained jointly with the policy.

We evaluate Diffusion Policy on eight simulation tasks across four benchmarks and four real-robot tasks, covering state and visual observations and actions of different dimensions. Simulation comparisons include recurrent Gaussian mixture policies, Behavior Transformers and implicit behavioral cloning. We compare temporal convolutional and Transformer denoising networks and examine how the action execution window affects temporal consistency and responsiveness. Real-robot experiments test precise T-shaped object pushing, cup flipping, sauce pouring and periodic sauce spreading. Together, these evaluations examine action-sequence diffusion across the manipulation tasks studied and assess the practical choices involved in its execution.

**逐段中文译文**

**第1段**

从示范中学习的机器人操作策略需要生成精确动作，同时表示完成任务的多种有效方式。行为克隆通过以示范为监督来源的学习，已在真实机器人操作中获得有效策略 [1]。例如，同一任务可以允许从物体任意一侧绕行的动作序列。策略必须表示这些不同选择，同时保持时间一致性并响应新的观测。

**第2段**

循环高斯混合策略利用观测历史和多个高斯分量建模动作分布 [1]。行为 Transformer 利用历史观测预测经聚类得到的动作类别，并预测连续偏移以修正动作 [2]。两类方法都支持多模态动作和时间上下文，其分量或类别数量需要预先设定。观测历史与联合预测未来动作承担不同作用。逐步预测单个动作可能在执行过程中切换有效模式，因此有必要联合生成一段时间相关的动作序列。

**第3段**

隐式行为克隆用观测与动作的能量函数表示策略，并在推理时搜索低能量动作 [3]。这种表示支持多模态行为，且已在视觉观测、高维动作和精密真实机器人操作中得到验证 [3]。其对比训练目标以示范动作为正样本、以采样动作为负样本，近似条件动作分布的归一化项。直接学习该分布的梯度提供了一条替代归一化项估计的途径。

**第4段**

去噪扩散模型和基于得分的生成模型通过噪声预测或得分估计学习数据分布，并从噪声出发迭代生成样本 [4,5]。扩散已被用于联合生成状态—动作轨迹以进行规划 [6]，也被用于表示结合 Q 值目标训练的离线强化学习条件动作策略 [7]。同期研究还探索了仿真机器人任务中的目标条件模仿学习 [8]，以及仿真机器人和三维游戏环境中的多模态人类行为模仿 [9]。我们研究如何利用从示范中学习的观测条件扩散，联合生成未来动作，并在精密视觉操作过程中保持响应能力。

**第5段**

本文提出扩散策略，将动作生成建模为观测条件下的去噪扩散过程。策略通过噪声预测目标学习条件动作分布的得分梯度。去噪网络以观测为条件，预测加入示范动作中的噪声。在推理时，迭代去噪将高斯噪声转化为一段未来动作。扩散表示能够容纳多模态、高维动作分布，使时间相关的动作得以联合生成。噪声预测目标避免了对比式能量模型训练所使用的负采样。

**第6段**

扩散策略将动作序列生成与滚动时域执行相结合，以平衡时间一致性和响应能力。策略根据最近的观测预测较长的动作序列，执行其中较短的一段，再根据新观测重新预测。执行窗口决定了机器人在引入新反馈之前，沿联合生成的序列执行多长时间。对于视觉策略，编码后的图像特征用作动作去噪的条件。视觉编码器在每轮预测中仅运行一次，其特征在所有去噪步骤中复用，以减少推理计算量。编码器可以与策略联合训练。

**第7段**

我们在四个基准中的八类仿真任务和四项真实机器人任务上评估扩散策略，覆盖状态与视觉观测以及不同维度的动作。仿真比较包括循环高斯混合策略、行为 Transformer 和隐式行为克隆。我们比较时间卷积与 Transformer 两种去噪网络，并考察动作执行窗口如何影响时间一致性和响应能力。真实机器人实验测试精密 T 形物体推动、翻杯、浇酱和周期性抹酱。这些评估共同考察动作序列扩散在本研究所测操作任务中的表现，以及执行过程中涉及的实际设计选择。

**正文实际使用的参考文献**

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

- 调整了章节逻辑，使动作表示、时间一致性、训练方式与反馈执行逐步引出本文设计；保留已有方法的多模态、历史观测和精密实机能力。
- 主要表达参照为 B02/B03，B05 补充方法选择的理由展开，B01 补充验证路线组织。范例科学内容未转入本稿事实，写作范例不列入科学参考文献。
- 引言保留验证范围与比较对象，定量结果留在已验收摘要和结果部分；两种去噪网络作为替代架构表述。
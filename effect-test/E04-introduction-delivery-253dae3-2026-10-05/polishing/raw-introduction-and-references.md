Robot manipulation policies learned from demonstrations must generate precise actions while preserving the multiple valid ways in which a task can be completed. Behavior cloning has produced effective policies for visual manipulation and precise contact tasks through supervised learning [1,3]. However, a policy that predicts individual actions step by step can switch between valid action modes during execution. The problem is therefore to represent these modes and generate temporally consistent actions that can respond to new observations.

Probabilistic policies represent the variability of demonstrated actions. Recurrent Gaussian mixture policies use observation history and multiple Gaussian components to model multimodal action distributions [1]. Behavior Transformers predict an action category and a continuous offset from historical observations, combining discrete action clusters with continuous corrections [2]. Both approaches support multimodal actions and temporal context, although the numbers of mixture components or action categories must be specified. Observation history informs the prediction of an action, but does not itself provide joint prediction of future actions. In our controlled pushing example, the compared explicit policies exhibit mode bias or switch between valid routes around an object. This observation motivates joint action-sequence prediction that preserves a mode during execution.

Implicit behavioral cloning provides an alternative representation through an observation–action energy function [3]. The policy searches for low-energy actions during inference and can represent multiple valid actions for the same observation. This approach has demonstrated visual manipulation, high-dimensional actions and precise real-robot operation. Its contrastive training uses demonstrated actions and negative samples to approximate the normalization term of the conditional action distribution. In our experiments, the implicit behavioral cloning baseline exhibits fluctuations during training and evaluation. These observations motivate an expressive action representation that avoids this normalization estimate and the associated negative sampling.

Diffusion models learn to generate samples through iterative denoising and score estimation [4,5]. Their ability to represent multimodal distributions and generate high-dimensional samples provides a basis for modeling action sequences. Diffusion has already been used to generate joint state–action trajectories for planning [6] and to represent action policies in offline reinforcement learning [7]. Concurrent studies also investigate goal-conditioned diffusion imitation learning [8] and the imitation of multimodal human behavior in simulated robotic and game environments [9]. We propose Diffusion Policy to learn an observation-conditioned action distribution directly from demonstrations for robot manipulation. The design combines diffusion action generation with temporal consistency, visual conditioning and feedback during physical execution.

Diffusion Policy is trained to predict the noise added to demonstrated actions, thereby learning the score gradient of the observation-conditioned action distribution. Direct score learning avoids the negative sampling used to estimate the normalization term in the implicit behavioral cloning baseline. During inference, the policy starts from Gaussian noise and iteratively denoises a sequence of future actions. The diffusion representation accommodates multiple action modes without prescribing a fixed number of mixture components or action categories. Its capacity for high-dimensional generation allows temporally correlated actions to be predicted jointly.

Manipulation performance also depends on how the predicted action sequence is executed. A long execution window delays the use of new observations, whereas a very short window can compromise temporal consistency. We integrate action-sequence prediction with receding-horizon execution to balance these requirements. At each prediction cycle, the policy uses a recent history of observations to predict a longer action sequence and executes a shorter segment. The policy then acquires new observations and predicts another sequence. Joint prediction preserves temporal relationships among actions, while repeated prediction allows execution to respond to updated observations.

Repeated denoising introduces a computational requirement for visual conditioning. We encode image observations once per prediction cycle and use the resulting features to condition every denoising step. The denoising network generates actions without jointly generating image observations or inferring future visual states. The visual encoder can be trained jointly with the policy. Feature reuse reduces the computation required by repeated denoising and helps support real-time inference.

The denoising network must also capture changes in the action sequence accurately. We consider a temporal convolutional network and a time-series diffusion Transformer as alternative architectures. Temporal convolution can favor low-frequency signals and smooth rapid action changes. The Transformer is designed to mitigate this tendency, particularly for tasks involving rapidly changing actions or velocity control. The architecture comparison examines this trade-off alongside ease of use and sensitivity to hyperparameters.

We evaluate Diffusion Policy on eight simulation tasks from four benchmarks and four real-robot tasks. The simulation study compares recurrent Gaussian mixture policies, Behavior Transformers and implicit behavioral cloning using each method’s best-performing action space. We examine multimodal behavior, training stability and the effect of the execution window alongside task performance. Real-robot experiments test precise T-shaped object pushing, cup flipping, sauce pouring and periodic sauce spreading to assess the policy across different manipulation requirements.

**正文实际使用的参考文献**

[1] Mandlekar, A. et al. What Matters in Learning from Offline Human Demonstrations for Robot Manipulation. CoRL 2021, *Proceedings of Machine Learning Research* **164**, 1678–1690 (2022).

[2] Shafiullah, N. M. M., Cui, Z. J., Altanzaya, A. & Pinto, L. Behavior Transformers: Cloning \(k\) modes with one stone. *NeurIPS* (2022). arXiv:2206.11251.

[3] Florence, P. et al. Implicit Behavioral Cloning. CoRL 2021, *Proceedings of Machine Learning Research* **164**, 158–168 (2022).

[4] Ho, J., Jain, A. & Abbeel, P. Denoising Diffusion Probabilistic Models. *NeurIPS* (2020). arXiv:2006.11239.

[5] Song, Y. & Ermon, S. Generative Modeling by Estimating Gradients of the Data Distribution. *NeurIPS* (2019). arXiv:1907.05600.

[6] Janner, M., Du, Y., Tenenbaum, J. & Levine, S. Planning with Diffusion for Flexible Behavior Synthesis. *Proceedings of Machine Learning Research* **162**, 9902–9915 (2022).

[7] Wang, Z., Hunt, J. J. & Zhou, M. Diffusion Policies as an Expressive Policy Class for Offline Reinforcement Learning. arXiv:2208.06193 (2022).

[8] Reuss, M., Li, M., Jia, X. & Lioutikov, R. Goal-Conditioned Imitation Learning using Score-based Diffusion Policies. *Robotics: Science and Systems* (2023). arXiv:2304.02532.

[9] Pearce, T. et al. Imitating Human Behaviour with Diffusion Models. *ICLR* (2023). arXiv:2301.10677.

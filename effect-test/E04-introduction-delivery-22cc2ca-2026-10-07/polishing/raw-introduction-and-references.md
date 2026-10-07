Robot manipulation provides a means of automating physical tasks through interaction with objects. Precise and temporally consistent actions are required for fine manipulation. Learning from demonstration is a valuable technique for acquiring such manipulation skills. Behavior cloning formulates policy learning as supervised prediction of demonstrated actions from observations [1]. Demonstrations can contain multiple valid action modes and temporal relationships between successive actions. It is therefore essential to consider how to represent this variability while generating precise, temporally consistent actions.

Explicit probabilistic policies can represent multiple action modes and use observation histories to provide temporal context. In [1], a recurrent policy with a Gaussian mixture output was used to learn robot manipulation from offline human demonstrations. The recurrent model incorporates historical observations, and the mixture components represent different action modes. In [2], Behavior Transformer was proposed to predict multimodal continuous actions from a sequence of past observations. The model combines action categories obtained by clustering with continuous offsets that refine the corresponding actions. The numbers of mixture components and action categories are specified in these representations. Observation history supplies temporal context, but does not by itself provide joint prediction of future actions. Stepwise prediction of individual actions can switch between valid modes. The current learning problem therefore calls for joint prediction of temporally correlated actions with a representation that does not prescribe the number of action modes.

Implicit policies provide an alternative to representing action modes through a finite mixture or a set of action categories. In [3], an energy-based policy was proposed for behavioral cloning. The energy function assigns low energy to actions compatible with an observation, and inference searches for low-energy actions using sampling or gradient-based methods. Multiple low-energy actions can represent multimodal distributions and multivalued mappings. The method supports high-dimensional actions and visual observations and was demonstrated on real-robot contact tasks with millimeter-level precision. Its contrastive training uses demonstrated actions and sampled negative actions to approximate the normalization term of the conditional distribution. Directly learning the distribution gradient offers a way to avoid this normalization estimate and the associated negative sampling.

Diffusion models provide a generative framework for learning distribution gradients and sampling multimodal, high-dimensional outputs [4], [5]. In [4], a denoising diffusion probabilistic model was developed to generate samples through a learned reverse denoising process. In [5], distribution scores at multiple noise scales were learned and used for sample generation. Diffusion has also been applied to planning and policy learning. In [6], Diffuser was proposed to jointly generate state–action trajectories for planning with reward guidance or constraints. In [7], conditional diffusion was employed as an offline reinforcement learning policy, with a Q-value objective used to improve the policy. Concurrent work studied goal-conditioned diffusion imitation learning [8] and diffusion-based imitation of multimodal human behavior [9]. These studies establish a basis for diffusion representations of trajectories and policies.

A manipulation policy learned directly from demonstrations must connect action generation with feedback during execution. Joint prediction can represent temporal relationships over a future action sequence, but executing the entire sequence before observing again would delay the response to new observations. Iterative generation also introduces a computational consideration for visual policies. Repeatedly encoding the same images within one prediction cycle adds computation without incorporating new observations. To address these requirements, we propose Diffusion Policy, which models action generation as an observation-conditioned denoising diffusion process. The policy learns the score gradient of the conditional action distribution by predicting noise added to demonstrated actions. This formulation avoids the normalization estimate and negative sampling used in contrastive energy-based training. Future actions are generated jointly by iterative denoising from Gaussian noise, allowing multimodal, high-dimensional actions and their temporal relationships to be represented within the same sequence model.

The generated action sequence is combined with receding-horizon execution to balance temporal consistency with responsiveness. The policy predicts a sequence from recent observations, executes a shorter segment, and then predicts again using new observations. The longer prediction horizon supports temporally consistent action generation, while the shorter execution window permits updates from new observations. For visual conditioning, image observations are encoded once per prediction cycle, and the resulting features are reused to condition every denoising step. The denoising output consists only of actions, and action generation does not require predicting future visual states. The visual encoder can be trained end to end with the policy. Reusing image features reduces repeated visual computation and supports timely replanning.

The main contributions of this paper can be summarized as follows.

1\) An observation-conditioned diffusion policy is developed for learning robot manipulation from demonstrations. Score-gradient learning provides a representation of multimodal, high-dimensional action distributions without prescribing the number of action modes or using the normalization estimate and negative sampling required by the contrastive energy-based formulation.

2\) Joint action-sequence prediction is combined with receding-horizon execution. Joint prediction represents temporal relationships between future actions, while execution of a shorter segment allows the policy to respond to new observations.

3\) A visual conditioning scheme is developed to reuse encoded image features across all denoising steps within each prediction cycle. The scheme reduces repeated visual computation while allowing the visual encoder and policy to be trained end to end.

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

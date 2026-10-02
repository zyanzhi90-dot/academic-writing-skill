# Drafting | overall argument, abstract, and connected manuscript body

Target: a generic robotics research journal. Using the author facts below,
provide the overall argument and evidence organization for human discussion,
an English abstract, and a connected English manuscript body covering
Introduction, technical method, analysis, experiments, Discussion, and
Conclusion. Use informative section/subsection headings and substantive prose.
Proceed with the requested complete deliverable rather than waiting for outline
approval. Keep any necessary author notes outside the manuscript.

Express the author's own scientific content accurately, concisely, clearly,
plainly, and professionally. Preserve scientific facts and necessary boundaries.
You may state equations supplied here, but do not invent equations, statistics,
citations, or unreported tests. Use the specified Skill and its declared
references, including on-demand examples and original papers, to select and
adapt suitable organization and concrete English realizations.

## Author's writing preferences (provided verbatim)


先把自己真正要表达的科学内容确定下来，再注重写作中的顶刊逻辑与表达。比较好的做法是，通过大量阅读积累丰富的例子，并在具体写作时灵活调用这些积累。

以某几篇论文为主要模仿对象，吸收它们组织内容、推进论述和实现英文表达的方式，逐渐形成自己的主要风格。同时，不断从其他文献中补充经验：遇到某一部分更好的逻辑、句式或用词，就吸收进来，使下次表达相关内容时有更好的写法可以参考。

具体写作时，逐部分写作。每个部分先确定自己真正要表达的科学内容，然后因为脑中已有大量相关文献的相关例子，所以能够根据当前要表达的内容选择、组合和调整合适的写法。**从段落逻辑、句与句的逻辑到句型句式和具体用词，都可以模仿，做到信手拈来。**需要更仔细的推敲时，也可以回查模仿对象原文，直接参照对应的段落和句子。

**最终，每句话都承载自己的科学含义。**借鉴范例的逻辑与表达时，让逻辑关系、事实、条件和结论准确对应自己的工作。

简言之，找到大量好的论文并积累大量例子，然后直接模仿/抄就行了，只是要把其中的内容换成自己想表达的意思，在表达上不要搞创新



## Author scientific material

Research facts (P17, provided as author notes):

- System: a demonstration-based robot learning system with two components. A learned motion model generates reference trajectories; an adaptive neural controller tracks them on a robot manipulator. The manipulator has uncertain dynamics, including unknown payload effects. Experiments used a Baxter robot with two seven-degree-of-freedom arms.
- Prior context: dynamic-system motion models can generate stable, extensible trajectories, but one earlier approach required substantial demonstration data. A conventional dynamic movement primitive (DMP) can model motion from one demonstration. Its original locally weighted regression formulation treats multiple demonstrations as separate models, so it does not combine their features into a single DMP. Probabilistic GMM/GMR methods encode variability across demonstrations. A separate tracking issue remains when the actual robot has uncertain dynamics or payloads. These are distinct modeling and control problems; no blanket failure of prior methods is claimed.
- Motion model scope: point-to-point movement, discussed per one-dimensional joint trajectory; Cartesian trajectories can also be represented as one-dimensional components. The DMP has a spring–damper part, a decaying phase variable, a bounded nonlinear forcing function, a start and goal, and a positive time constant. For each recorded demonstration, positions, velocities, and accelerations yield samples of the nonlinear forcing function. Multiple demonstrations of the same task supply a combined phase–forcing data set. A Gaussian mixture model (GMM) encodes that set and Gaussian mixture regression (GMR) estimates the forcing function for one DMP. Altering start and goal provides spatial generalization; the time constant changes duration. The phase-dependent forcing term decays, so the model tends to the goal under the stated bounded-function condition. An added exponentially converging intermediate state replaces the fixed goal in the spring–damper term to moderate the initial acceleration while retaining goal convergence.
- Controller model: the robot dynamics are `M(θ)θ̈ + C(θ,θ̇)θ̇ + G0(θ) + τp = τ`, where `τp` is payload torque and `τ` is commanded torque. The DMP-generated joint trajectory is the reference `θd`. The joint position controller forms a desired velocity; the joint velocity controller generates torque and uses a radial basis function neural network (RBFNN) to approximate uncertain dynamics. A performance function `δ(t)=(δ0−δ∞)e^(−at)+δ∞`, with positive parameters and `δ∞<δ0`, sets a decaying position-error envelope. A Lyapunov analysis gives semiglobal uniform boundedness of closed-loop signals for bounded `θd` and `θ̇d`; bounded transformed error supports the stated transient bound. Do not call this global, asymptotic, finite-time, or fixed-time convergence.
- Controller experiment: Baxter's left gripper carried a 0.94 kg payload while tracking a circular Cartesian trajectory at fixed orientation, converted to joint references by inverse kinematics. The controller was compared with neural learning disabled and enabled. With learning disabled, joint tracking errors were relatively high. With learning enabled, all tested joint errors fell within `[-0.04, 0.04] rad`; compensation torque increased. No statistical test, numerical effect size between arms, or unseen operating range was supplied.
- Motion-model experiments: five guided demonstrations of a pouring task moved four named joints while other joints remained fixed. The learned DMP reproduced a task motion and, when its goal was changed, guided Baxter to pour into another cup while retaining the motion profile. In a separate drawing task, five irregular human-guided demonstrations were learned in task space; the resulting drawn curve was smoother than the demonstrations. The paper attributes distortion in recorded paths partly to sensor measurement errors. These are demonstrations of those tasks, not a measured population-level generalization rate.
- Boundaries: controller comparison and DMP tests evaluate different components. No reported trial establishes success on arbitrary tasks, arbitrary payloads, or uncontrolled human/environment contact. No reported ablation isolates GMM from GMR, and there is no numerical success rate for the pouring or drawing tasks. Theoretical boundedness is conditional; experimental tracking is observed on the tested setup.

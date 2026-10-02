# Polishing | complete manuscript body

Target: a generic robotics research journal. Polish the complete supplied
English manuscript body using the same author facts below. Return the complete
polished body, covering Introduction, technical method, analysis, experiments,
Discussion, and Conclusion, with any necessary author/revision notes outside
the manuscript. No new abstract is requested for this task.

Treat the author facts as the scientific authority. Preserve the author's
supported scientific meanings and necessary boundaries. Improve organization
and English within this full-body task, retaining accurate natural expressions
and reasonable alternatives. Do not add equations, statistics, citations,
unreported tests, or scientific claims absent from author material. Use the
specified Skill and its declared references, including on-demand examples and
original papers, to select and adapt suitable organization and concrete English
realizations. Express the work accurately, concisely, clearly, plainly, and
professionally.

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


## Supplied manuscript body (verbatim)

### Introduction

Learning a robot movement from demonstration involves two related tasks. A motion model must turn recorded trajectories into a reference that can be reproduced or adapted to a new start, goal, or duration. The robot must then track that reference despite differences between its modeled and actual dynamics. Addressing the first task does not, by itself, resolve the second, particularly when a manipulator carries an uncertain payload.

Dynamic-system motion models provide a way to generate stable, extensible trajectories. A conventional dynamic movement primitive (DMP) can represent a point-to-point motion from one demonstration, but its original locally weighted regression formulation treats multiple demonstrations as separate models rather than combining their features in one DMP. Probabilistic models based on a Gaussian mixture model (GMM) and Gaussian mixture regression (GMR) offer a way to encode variation across demonstrations. Separately, uncertain manipulator dynamics motivate adaptive tracking control. These are distinct problems in reference generation and physical execution.

This study combines a demonstration-based motion model with an adaptive neural controller. Phase–forcing samples from multiple demonstrations are modeled by a GMM, and GMR estimates the forcing function of a single DMP. The resulting joint trajectory is supplied to a controller that uses a radial basis function neural network (RBFNN) to approximate uncertain dynamics while enforcing a prescribed position-error envelope. Analysis addresses conditional boundedness of the closed-loop system. Baxter experiments examine controller tracking with a payload and demonstrate motion reproduction and goal adaptation in pouring and drawing tasks. Each experiment evaluates the component and operating conditions it actually tests.

### Method

#### System architecture and motion scope

The system has two components in sequence. The learned DMP generates a reference trajectory from guided demonstrations; the adaptive neural controller uses that trajectory as the desired manipulator motion. The motion model is described for one-dimensional point-to-point trajectories, such as an individual joint coordinate. Cartesian motion can likewise be represented through one-dimensional components. This representation defines how a movement is generated; it does not specify how accurately a physical robot will track it.

#### Combining demonstrations in one motion model

The DMP contains a spring–damper component directed toward a goal, a decaying phase variable, a bounded nonlinear forcing function, a start and goal, and a positive time constant. For each recorded demonstration, position, velocity, and acceleration provide samples of the nonlinear forcing function at corresponding phase values. Samples from multiple demonstrations of the same task form a combined phase–forcing data set. A GMM encodes this data set, and GMR estimates the phase-dependent forcing function used by one DMP.

The generated movement can be adapted by changing its start and goal, while changing the time constant changes its duration. Under the stated condition that the nonlinear forcing function is bounded, the phase-dependent forcing term decays and the DMP tends toward its goal. To moderate initial acceleration, an exponentially converging intermediate state replaces the fixed goal in the spring–damper component. Because that state converges to the goal, this modification retains the stated goal-convergence behavior.

#### Adaptive neural trajectory tracking

The manipulator dynamics are represented as

\[
M(\theta)\ddot{\theta}+C(\theta,\dot{\theta})\dot{\theta}
+G_0(\theta)+\tau_p=\tau,
\]

where \(\tau_p\) is payload torque and \(\tau\) is commanded torque. The DMP-generated joint trajectory is the reference \(\theta_d\). The position controller forms a desired joint velocity from that reference, and the velocity controller generates torque. An RBFNN in the velocity controller approximates uncertain dynamics, including effects relevant to tracking under an unknown payload.

A time-varying performance function sets a decaying envelope for position error:

\[
\delta(t)=(\delta_0-\delta_\infty)e^{-at}+\delta_\infty,
\]

with positive parameters and \(\delta_\infty<\delta_0\). The controller is designed so that bounded transformed position error supports the prescribed transient bound. This envelope concerns position tracking; it is separate from the DMP’s goal-convergence property.

### Analysis

#### Conditional motion and closed-loop properties

The motion-model argument depends on the decaying phase variable and a bounded nonlinear forcing function. As the phase-dependent forcing contribution diminishes, the spring–damper component directs the generated trajectory toward its goal. The exponentially converging intermediate state changes the initial response while preserving convergence of the goal input. These properties concern the generated reference, not tracking error on the robot.

For the controller, the stated Lyapunov analysis establishes **semiglobal uniform boundedness** of closed-loop signals when \(\theta_d\) and \(\dot{\theta}_d\) are bounded. Boundedness of the transformed error supports the prescribed position-error envelope. The result is conditional on the reference and controller assumptions; it does not establish global, asymptotic, finite-time, or fixed-time convergence. The physical experiments provide a separate observation of tracking on the tested robot.

### Experiments

#### Payload tracking on Baxter

Controller tracking was tested on a Baxter robot, which has two seven-degree-of-freedom arms. For this comparison, the left gripper carried a 0.94 kg payload. A circular Cartesian trajectory at fixed orientation was converted to joint references by inverse kinematics. The controller was evaluated with neural learning disabled and enabled.

With learning disabled, joint tracking errors were relatively high. With learning enabled, all tested joint errors lay within \([-0.04,0.04]\) rad, and the compensation torque increased. This comparison supports improved tracking under the reported payload and trajectory conditions. It does not quantify a statistical effect or establish performance across other payloads or operating ranges.

#### Pouring motion reproduction and goal change

Five guided demonstrations of a pouring task moved four joints while the remaining joints stayed fixed. The combined demonstrations were used to learn a DMP that reproduced the task motion. When the goal was changed, the learned model guided Baxter to pour into another cup while retaining the motion profile. This test illustrates reproduction and goal adaptation for the demonstrated pouring task; no numerical success rate was reported.

#### Drawing from irregular demonstrations

In a separate drawing task, five irregular human-guided demonstrations were learned in task space. The resulting drawn curve was smoother than the demonstrated paths. Sensor measurement errors were identified as one possible contributor to distortion in the recorded paths. The drawing result shows the behavior of the learned motion model in this task, without isolating the cause of the irregularities or measuring generalization across a population of tasks.

### Discussion

The two sets of experiments support complementary, narrower conclusions about the combined system. The pouring and drawing tests show that the learned motion model can produce usable task trajectories from the supplied demonstrations and adapt a pouring movement to a changed goal. The payload comparison shows that neural learning improved observed joint tracking for the tested circular trajectory. Together, they illustrate a route from demonstration to physical execution, while leaving the contributions of the two components experimentally distinct.

Combining phase–forcing data through GMM and GMR addresses the single-model use of multiple demonstrations that the original locally weighted regression formulation does not provide. The reported motion tests demonstrate the behavior of the resulting DMP, but do not isolate the separate effects of GMM and GMR. Likewise, the increased compensation torque is consistent with the controller responding to uncertain dynamics; the comparison does not identify how much of the tracking change is attributable specifically to payload compensation.

The theoretical and empirical claims have different scopes. The boundedness result applies under its stated reference and controller conditions, whereas the error range is an observation from one reported Baxter tracking setup. The pouring and drawing examples establish task-specific behavior, without a measured success rate over arbitrary tasks. Testing additional payloads and trajectories would clarify the controller’s operating range; a component comparison within the motion model would clarify which part of the probabilistic representation accounts for its observed behavior.

### Conclusion

This study connects a DMP learned from multiple demonstrations to adaptive neural tracking on a robot manipulator. Conditional analysis supports bounded closed-loop behavior, while Baxter tests show improved tracking in the reported payload experiment and task-specific motion reproduction and adaptation in pouring and drawing. The evidence supports these demonstrated settings and does not establish performance for arbitrary tasks, payloads, or uncontrolled contact.


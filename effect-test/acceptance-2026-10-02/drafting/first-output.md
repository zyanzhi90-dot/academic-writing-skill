## Overall argument and evidence organization

**Central claim.** A demonstration-based robot system can connect motion generation from multiple examples to tracking under uncertain manipulator dynamics. A Gaussian mixture model (GMM) and Gaussian mixture regression (GMR) estimate the forcing function of one dynamic movement primitive (DMP); an adaptive neural controller then tracks its joint-space reference. The two components have distinct support: a conditional Lyapunov boundedness analysis and a payload tracking comparison address control, while pouring and drawing demonstrations address motion generation.

| Manuscript question | Evidence and scope |
|---|---|
| How are multiple demonstrations represented in one motion model? | Phase–forcing samples from each demonstration are combined, encoded by a GMM, and regressed by GMR to estimate one DMP forcing function. |
| What motion properties follow from the model? | The decaying phase term and bounded forcing function support convergence toward the goal. Changing start and goal changes spatial scale; changing the time constant changes duration. |
| What does the controller establish? | For bounded reference position and velocity, the Lyapunov analysis gives semiglobal uniform boundedness of closed-loop signals. Bounded transformed error supports the stated transient error envelope. |
| What was observed on the robot? | With a 0.94 kg payload, enabling neural learning brought every tested joint tracking error within \([-0.04, 0.04]\) rad. Separate pouring and drawing tests demonstrated reproduction, a changed pouring goal, and a smoother drawn curve. |

**Terminology choices.** The manuscript uses *DMP* for the point-to-point motion model, *GMM/GMR* for its forcing-function estimation, and *radial basis function neural network (RBFNN)* for the controller’s dynamics approximation. “Goal convergence,” “semiglobal uniform boundedness,” and “observed tracking error” name different claims and are kept distinct.

# Draft manuscript

## Abstract

Learning a robot motion from demonstrations requires both a reference trajectory that captures the demonstrated task and a controller that can track it despite uncertain dynamics. We present a system that joins these functions. For point-to-point motion, phase–forcing data from multiple demonstrations are encoded with a Gaussian mixture model, and Gaussian mixture regression estimates the forcing function of a single dynamic movement primitive. The resulting model generates joint references with adjustable start, goal, and duration. An adaptive controller uses a radial basis function neural network to approximate uncertain manipulator dynamics while tracking those references. Under bounded reference position and velocity, Lyapunov analysis gives semiglobal uniform boundedness of the closed-loop signals and supports a prescribed transient position-error bound. On a Baxter robot carrying a 0.94 kg payload, enabling neural learning brought all tested joint tracking errors within \([-0.04, 0.04]\) rad. Separate pouring and drawing demonstrations showed task-motion reproduction, transfer to a changed pouring goal, and a drawn curve smoother than the demonstrations. These results support the combined design within the analyzed conditions and tested tasks.

## 1. Introduction

A robot taught by demonstration must turn recorded movement into a usable reference and then execute that reference on a physical manipulator. These are related but distinct problems. A motion model determines what trajectory the robot should follow; a tracking controller determines how closely the robot follows it when the manipulator dynamics are uncertain.

Dynamic-system motion models provide a way to generate stable, extensible trajectories, although an earlier approach required substantial demonstration data. A dynamic movement primitive (DMP) can model a point-to-point movement from one demonstration. In its original locally weighted regression formulation, however, multiple demonstrations are treated as separate models rather than combined into the forcing function of one DMP. Probabilistic approaches based on Gaussian mixture models and regression offer a way to encode variation across demonstrations. This motivates a motion-model question: how can several demonstrations of the same task inform one DMP while retaining its goal-directed structure?

Execution raises a separate question. A reference trajectory learned from demonstrations does not account for uncertainty in the robot’s actual dynamics, including an unknown payload. Tracking therefore needs a controller that responds to such uncertainty without confusing the properties of the generated reference with guarantees about physical execution.

We address the two questions in one system. First, a GMM encodes phase–forcing samples obtained from multiple demonstrations, and GMR estimates the nonlinear forcing function used by a single DMP. The DMP supplies a joint-space reference whose start, goal, and duration can be changed. Second, an adaptive neural controller tracks that reference and approximates uncertain dynamics with an RBFNN. We analyze the motion model’s goal-directed behavior and the controller’s conditional boundedness, then evaluate the controller and motion model in separate Baxter experiments.

## 2. Motion generation from multiple demonstrations

### 2.1. Point-to-point trajectory representation

We represent a point-to-point movement as one-dimensional trajectories, using one DMP for each joint trajectory. Cartesian motion can likewise be represented through one-dimensional components. The DMP combines a spring–damper system with a nonlinear forcing function. Its phase variable decays over time; its start and goal set the movement endpoints; and a positive time constant controls duration.

The forcing term shapes the movement away from the unforced spring–damper response. Because the term depends on the decaying phase and the nonlinear forcing function is bounded, its influence vanishes as the movement progresses. Under that condition, the model tends toward the goal. Changing the start or goal spatially adapts the generated trajectory, while changing the time constant changes its duration.

A fixed goal in the spring–damper term can produce a large initial acceleration. We therefore replace that fixed target in the spring–damper term with an intermediate state that converges exponentially to the goal. The intermediate state moderates the initial acceleration and still approaches the intended goal. The goal-directed behavior of the modified model depends on both this convergence and the decay of the phase-dependent forcing term.

### 2.2. Estimating one forcing function from several demonstrations

For each recorded demonstration, positions, velocities, and accelerations provide samples of the nonlinear forcing function at corresponding phase values. We combine the phase–forcing samples from demonstrations of the same task into one data set. A GMM encodes this joint data, and GMR estimates the forcing function at each phase value used by the DMP.

This sequence gives the components distinct roles. The demonstrations supply observed motion information; the GMM represents their combined phase–forcing distribution; GMR supplies the forcing-function estimate; and the DMP uses that estimate to generate a reference trajectory. The construction produces one motion model informed by multiple demonstrations. The reported experiments examine trajectories generated by that model, but do not isolate the separate effects of GMM and GMR.

## 3. Adaptive tracking under uncertain dynamics

### 3.1. Manipulator model and controller structure

The DMP-generated joint trajectory, \(\theta_d\), is the reference for a manipulator with dynamics

\[
M(\theta)\ddot{\theta}
+C(\theta,\dot{\theta})\dot{\theta}
+G_0(\theta)+\tau_p=\tau,
\]

where \(\theta\) is joint position, \(\tau_p\) is payload torque, and \(\tau\) is commanded torque. Payload effects and other uncertain dynamics complicate tracking of the generated reference.

The controller has a joint-position stage and a joint-velocity stage. The position stage forms a desired velocity from the reference and position error. The velocity stage generates commanded torque and uses an RBFNN to approximate uncertain dynamics. Thus, the motion model determines the movement to be executed, while the neural controller addresses uncertainty during its execution.

### 3.2. Transient error specification and boundedness analysis

The position controller uses a decaying performance function to specify a transient position-error envelope:

\[
\delta(t)=(\delta_0-\delta_\infty)e^{-at}+\delta_\infty,
\]

with positive parameters and \(\delta_\infty<\delta_0\). The envelope contracts from its initial value toward \(\delta_\infty\). An error transformation relates bounded transformed error to the stated position-error bound.

For bounded reference position \(\theta_d\) and velocity \(\dot{\theta}_d\), the Lyapunov analysis gives **semiglobal uniform boundedness** of the closed-loop signals. Boundedness of the transformed error supports the transient tracking bound specified by the performance function. This is a conditional result about the analyzed controller. It does not assert global, asymptotic, finite-time, or fixed-time convergence, and it does not by itself establish tracking performance for an arbitrary payload.

## 4. Experiments

The experiments examine two different parts of the system. A payload tracking comparison tests the contribution of neural learning in the controller. Pouring and drawing tasks examine motions generated by the learned DMP. Results from one group therefore should not be treated as a direct test of every claim about the other component.

### 4.1. Tracking a circular reference with a payload

The controller was tested on a Baxter robot with two seven-degree-of-freedom arms. The left gripper carried a 0.94 kg payload while the robot tracked a circular Cartesian trajectory at fixed orientation. Inverse kinematics converted the trajectory to joint references. The comparison used the controller with neural learning disabled and enabled.

With neural learning disabled, joint tracking errors were relatively high. With learning enabled, every tested joint tracking error fell within \([-0.04, 0.04]\) rad, while compensation torque increased. The comparison supports improved tracking in this payload and trajectory setting when neural learning is enabled. It does not quantify an effect across different payloads or operating conditions.

### 4.2. Reproducing and redirecting a pouring motion

Five guided demonstrations of a pouring task provided trajectories for joints \(s0\), \(e1\), \(w0\), and \(w1\); the other joints remained fixed. The learned DMP reproduced a pouring motion from those demonstrations. When the goal was changed, the generated joint trajectories approached the new goal while retaining the motion profile, and Baxter poured into another cup.

This task demonstrates reproduction and goal adaptation for the tested pouring setup. It does not provide a numerical success rate or establish how often the model would succeed for other target locations or tasks.

### 4.3. Learning a drawing motion from irregular demonstrations

In a separate task, five irregular human-guided drawing demonstrations were learned in task space. The robot then drew a curve smoother than the demonstrated curves. Distortion in the recorded paths was attributed partly to sensor measurement errors.

The drawing result shows that the learned motion can yield a smoother executed path than these particular demonstrations. It does not identify the separate contribution of each source of demonstration irregularity or measure performance across a broader set of drawing tasks.

## 5. Discussion

The system connects two operations that must both succeed for demonstrated motion to be executed: constructing a reference from demonstrations and tracking that reference on a manipulator with uncertain dynamics. Combining phase–forcing data allows multiple examples of a task to inform one DMP, while the adaptive neural controller addresses uncertainty that the motion model alone does not resolve. The distinction matters when interpreting the evidence. Goal convergence concerns the generated motion under the model’s bounded-forcing condition; semiglobal uniform boundedness concerns the analyzed closed loop under bounded references; the reported tracking errors are observations from one robot experiment.

The pouring test illustrates the practical use of changing a learned goal while retaining a recognizable task motion. The drawing test shows a smoother produced curve than the irregular demonstrations. Neither result, on its own, establishes that the GMM and GMR make separate causal contributions to that behavior: the reported tests evaluate the combined motion-model procedure. Similarly, the payload comparison supports the role of neural learning in the tested controller configuration, but it does not measure the performance of the full system over arbitrary learned tasks and payloads.

The scope of the evidence is therefore specific. The motion demonstrations cover pouring and drawing, and the controller comparison covers a circular reference with a 0.94 kg payload. No reported trial establishes performance under uncontrolled human or environment contact. Further comparisons that separate the mixture model from regression, together with repeated task and payload tests, would clarify which design choices account for the observed behavior and how far the results extend.

## 6. Conclusion

We presented a demonstration-based robot system in which a DMP learned from multiple demonstrations generates reference motion and an adaptive neural controller tracks it under uncertain manipulator dynamics. Conditional analysis establishes goal-directed motion-model behavior and semiglobal uniform boundedness of the analyzed closed loop. Baxter experiments show improved tracking with neural learning in the tested payload setting, as well as pouring-goal adaptation and smoother drawing in separate motion-model tasks. These findings support the system within the stated analysis conditions and experimental settings.

## Author notes

- **Structure and reference choice:** The Introduction uses a two-problem pipeline: multiple-demonstration motion modeling followed by uncertain-dynamics tracking. The source paper’s component handoff and separate experiment groups informed the organization; its scientific claims were limited to the supplied author facts.
- **Evidence still needed for a submission-ready Methods section:** The supplied facts do not give complete DMP, GMM/GMR, controller, or RBFNN implementation settings and update laws. Those details should be checked against the authors’ technical record before submission.
- **References:** Prior-method statements in the Introduction need verified citations in the target journal’s style. None were inserted without an author-approved reference list.
- **Main-text allocation:** The conditional guarantees, payload comparison, and two task outcomes remain in the main text because each supports or bounds a central claim. Detailed parameter settings, trajectory plots, and implementation information belong in Methods, figures, or supporting material as required by the journal. No unreported statistic or component ablation was inferred.
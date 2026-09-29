## Draft

### Introduction

A robot taught by demonstration must both generate a usable motion and execute it despite uncertainty in its dynamics. These are related but distinct problems. A motion model can preserve the structure of a demonstrated task while allowing its start, goal, or duration to change. A tracking controller must then follow the resulting reference on the physical robot, where effects such as an unknown payload can alter the required torque.

Dynamic-system motion models provide a way to generate stable, extensible trajectories, although an earlier approach required substantial demonstration data. A conventional dynamic movement primitive (DMP) can represent motion from a single demonstration. In its original locally weighted regression formulation, however, multiple demonstrations are treated as separate models rather than combined into one DMP. Probabilistic methods based on Gaussian mixture models and Gaussian mixture regression (GMM/GMR) can encode variation across demonstrations. Independently, uncertain manipulator dynamics create a tracking problem even when a reference trajectory is available. [Citations needed for prior-method claims.]

We examine a two-component system that addresses these problems together. A motion model combines phase–forcing samples from several demonstrations through GMM/GMR to estimate the forcing function of one DMP. An adaptive neural controller then tracks the generated joint reference while accounting for uncertain dynamics. We analyze the controller’s conditional boundedness and evaluate the components separately on a Baxter robot: a payload-tracking comparison tests the controller, while pouring and drawing tasks test the motion model. These tests establish behavior in the reported settings; they do not measure success across arbitrary tasks or payloads.

### Motion generation and adaptive tracking

#### Learning a motion from multiple demonstrations

The motion model represents a point-to-point movement as a one-dimensional DMP. Joint trajectories are modeled component by component; Cartesian trajectories can likewise be represented through one-dimensional components. The DMP contains a spring–damper term, a decaying phase variable, a bounded nonlinear forcing function, a start and goal, and a positive time constant.

For each recorded demonstration, its positions, velocities, and accelerations provide samples of the nonlinear forcing function at corresponding phase values. Demonstrations of the same task contribute to a combined phase–forcing data set. A GMM encodes this data set, and GMR estimates the forcing function used by a single DMP. This construction gives the demonstrations a common motion representation rather than assigning a separate DMP to each recording. The start and goal can be changed to generate a motion at a different location, while the time constant changes its duration.

As the phase variable decays, the phase-dependent forcing term also decays. Under the stated bounded-function condition, the DMP consequently tends toward its goal. The model additionally uses an exponentially converging intermediate state in place of the fixed goal within the spring–damper term. This change moderates initial acceleration while retaining convergence toward the goal. The available notes do not specify the full DMP equations or estimation settings, so those implementation details remain to be supplied for reproduction.

#### Controller and robot model

The DMP-generated joint trajectory, \(\theta_d\), supplies the reference for the manipulator controller. The robot dynamics are modeled as

\[
M(\theta)\ddot{\theta}
+C(\theta,\dot{\theta})\dot{\theta}
+G_0(\theta)+\tau_p=\tau,
\]

where \(\tau_p\) is payload torque and \(\tau\) is commanded torque. The controller has two stages. A joint position controller forms a desired velocity from the reference and measured joint position. A joint velocity controller generates the commanded torque. Within the velocity controller, a radial basis function neural network (RBFNN) approximates uncertain dynamics, including effects that are not known precisely from the nominal robot model.

The position-error performance function is

\[
\delta(t)=(\delta_0-\delta_\infty)e^{-at}+\delta_\infty,
\]

with positive parameters and \(\delta_\infty<\delta_0\). It defines a decaying error envelope: the permitted bound begins at \(\delta_0\) and approaches \(\delta_\infty\). The controller analysis uses a transformed error associated with this envelope. Exact controller and adaptation laws, as well as the transformed-error definition, are needed for a reproducible technical specification.

### Conditional closed-loop analysis

For bounded \(\theta_d\) and \(\dot{\theta}_d\), the Lyapunov analysis establishes semiglobal uniform boundedness of the closed-loop signals. Boundedness of the transformed error supports the stated transient position-error bound relative to \(\delta(t)\). This is a conditional result for the analyzed system and reference signals. It does not establish global, asymptotic, finite-time, or fixed-time convergence, and it does not by itself establish tracking performance for every payload or task.

### Experiments

#### Payload tracking on Baxter

The controller was evaluated on Baxter’s left arm while its gripper carried a 0.94 kg payload. The arm tracked a circular Cartesian trajectory at fixed orientation; inverse kinematics converted that trajectory into joint references. The comparison used the controller with neural learning disabled and enabled, allowing the observed effect of the learning component to be examined in this setup.

With learning disabled, joint tracking errors were relatively high. With learning enabled, all tested joint errors fell within \([-0.04, 0.04]\) rad, and compensation torque increased. The comparison supports improved tracking under the reported payload and trajectory conditions. The supplied record gives no numerical between-condition effect size or statistical test, so the magnitude and repeatability of the improvement cannot be quantified further here.

#### Pouring with a changed goal

Five guided demonstrations supplied a pouring motion involving four joints; the other joints remained fixed. The learned DMP reproduced a task motion. After its goal was changed, it guided Baxter to pour into another cup while retaining the motion profile. This test illustrates spatial adaptation of the learned motion in the reported pouring setup. It does not provide a numerical success rate or establish performance for other pouring conditions.

#### Drawing from irregular demonstrations

In a separate drawing task, five irregular human-guided demonstrations were learned in task space. The resulting drawn curve was smoother than the recorded demonstrations. Sensor measurement errors were identified as one possible contributor to distortion in the recorded paths. The observed smoothing is therefore consistent with the motion model producing a regularized task trajectory, but the available test does not isolate GMM from GMR or determine how much of the difference arose from measurement error.

### Discussion

The experiments address the system’s two functions with different evidence. The payload comparison concerns physical tracking under uncertain dynamics. The pouring and drawing tasks concern the motion model’s ability to combine demonstrations and generate task trajectories. Considered together, they support the use of the two components in the tested Baxter system, but the separate evaluations do not isolate every contribution of their integration.

The motion model extends a single-demonstration DMP formulation by estimating one forcing function from multiple demonstrations. Its changed-goal pouring result supports spatial reuse of the learned profile in that task. The smoother drawing result shows a further observed property of the generated trajectory, although the test cannot distinguish the effect of GMM/GMR from all other sources of smoothing. Similarly, the controller comparison supports the role of neural learning in the tested payload-tracking condition without identifying its performance across an unseen operating range.

The theoretical and experimental claims also have different scopes. Semiglobal uniform boundedness follows from the stated analysis conditions, including bounded reference position and velocity. The measured joint-error range describes the reported circular-trajectory experiment. Neither result establishes reliable execution during uncontrolled human or environmental contact, with arbitrary payloads, or on arbitrary tasks. Tests across defined payload and trajectory ranges, along with an ablation that separates GMM from GMR, would clarify which component properties carry beyond the present demonstrations.

### Conclusion

A demonstration-based motion model and an adaptive neural controller were combined to generate and track robot trajectories. GMM/GMR combined multiple demonstrations into the forcing function of one DMP; the controller analysis established conditional semiglobal uniform boundedness; and Baxter experiments showed changed-goal pouring, smoother drawing, and joint errors within \([-0.04, 0.04]\) rad during the reported payload-tracking test with neural learning enabled. These findings support the system’s use in the tested tasks and conditions. Its behavior across broader tasks, payloads, and contact conditions remains unmeasured.

## Section outline

- **Introduction:** distinguish motion learning from uncertain-dynamics tracking and define the system’s scope.
- **Method and analysis:** explain how demonstrations become one DMP, how its reference enters the controller, and what the boundedness result requires.
- **Experiments:** report the controller comparison separately from the pouring and drawing tests.
- **Discussion and Conclusion:** interpret the combined evidence while keeping theoretical, observed, and untested claims distinct.

## Terminology ledger

| Canonical term | First-use definition | Role |
|---|---|---|
| Dynamic movement primitive (DMP) | Point-to-point motion model | Generates the reference trajectory |
| Gaussian mixture model / Gaussian mixture regression (GMM/GMR) | Encoding and regression methods for combined phase–forcing samples | Estimates one DMP forcing function |
| Radial basis function neural network (RBFNN) | Neural approximator in the velocity controller | Approximates uncertain dynamics |
| \(\theta_d\) | DMP-generated joint trajectory | Controller reference |
| \(\tau_p\) | Payload torque | Uncertain term in robot dynamics |
| \(\delta(t)\) | Decaying position-error performance function | Specifies the transient error envelope |

## Assumptions or missing inputs

- Prior-method statements need verified citations before submission.
- Full DMP equations, GMM/GMR settings, controller and adaptation laws, and the transformed-error definition are needed to make the Method reproducible.
- Trial counts, error summaries for learning-disabled tracking, and success criteria for pouring and drawing were not supplied. The draft therefore makes no statistical or population-level claim.

## Claim–evidence map

| Claim | Evidence | Status |
|---|---|---|
| Neural learning improved tracking in the reported payload test | Disabled/enabled comparison; enabled errors within \([-0.04, 0.04]\) rad | Supported within the tested setup |
| The learned motion can be reused with a changed goal for pouring | Five demonstrations and a pour into another cup | Supported for the reported task |
| The drawing output was smoother than its demonstrations | Separate task-space drawing test | Supported as an observation; cause not isolated |
| Closed-loop signals are semiglobally uniformly bounded | Lyapunov analysis under bounded-reference conditions | Conditional theoretical claim |
| Performance generalizes to arbitrary tasks or payloads | No reported test | Needs evidence |

## Main-text discipline audit

The controller comparison, changed-goal pouring, and drawing observation are the core experimental evidence and remain in the main text. The absence of a GMM-versus-GMR ablation and of broader payload or task tests is stated where it bounds interpretation. No statistics, tests, or supplementary results were inferred.
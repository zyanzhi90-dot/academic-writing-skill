# Draft

## Introduction

A robot taught by demonstration must both generate a useful motion and execute it despite uncertainty in its dynamics. These are distinct problems. A motion model can reproduce a demonstrated path while a controller still incurs tracking error when, for example, a payload changes the torque required at the joints.

Dynamic-system motion models provide a way to generate stable, adjustable trajectories. A conventional dynamic movement primitive (DMP) can learn a motion from one demonstration, but its original locally weighted regression formulation treats multiple demonstrations as separate models. Probabilistic models based on Gaussian mixture models (GMMs) and Gaussian mixture regression (GMR) can represent variation across demonstrations. Combining demonstrations into one DMP forcing function addresses the motion-modeling problem; tracking that reference under uncertain robot dynamics requires a separate control mechanism.

Here, we combine a DMP learned from multiple demonstrations with an adaptive neural controller for a robot manipulator. GMM and GMR estimate one phase-dependent forcing function from the demonstrations, while a radial basis function neural network (RBFNN) approximates uncertain dynamics during trajectory tracking. We analyze the resulting motion and control properties and evaluate the components on a Baxter robot with two seven-degree-of-freedom arms. The experiments examine controller tracking with a payload and learned motions for pouring and drawing.

## Method

### System overview

The system first converts demonstrations into a reference trajectory and then tracks that trajectory at the robot joints. The motion model addresses how the desired path is formed and adjusted. The controller addresses the torque needed to follow that path when the manipulator dynamics are uncertain. The two components can therefore be assessed through different tests.

### Learning a motion from multiple demonstrations

We model point-to-point motion using a DMP for each one-dimensional trajectory. A joint trajectory is one such trajectory; Cartesian motion can likewise be represented through one-dimensional components. The DMP contains a spring–damper component, a decaying phase variable, a bounded nonlinear forcing function, a start and goal, and a positive time constant.

For each recorded demonstration, position, velocity, and acceleration yield samples of the nonlinear forcing function. Demonstrations of the same task are pooled into a phase–forcing data set. A GMM represents this combined data set, and GMR estimates the forcing function used by a single DMP. This construction combines information from multiple demonstrations without assigning a separate final DMP to each one.

The generated motion can be adjusted without relearning the forcing function: changing the start and goal changes its spatial endpoints, and changing the time constant changes its duration. We also use an exponentially converging intermediate state in place of the fixed goal in the spring–damper term. This modification moderates initial acceleration while retaining convergence toward the goal.

### Tracking under uncertain dynamics

The manipulator dynamics are represented as

\[
M(\theta)\ddot{\theta}+C(\theta,\dot{\theta})\dot{\theta}
+G_0(\theta)+\tau_p=\tau,
\]

where \(\tau_p\) is payload torque and \(\tau\) is commanded torque. The DMP-generated joint trajectory, \(\theta_d\), supplies the tracking reference. A joint position controller forms a desired velocity. A joint velocity controller then generates torque and uses an RBFNN to approximate uncertain dynamics, including effects associated with an unknown payload.

A decaying performance function specifies the position-error envelope:

\[
\delta(t)=(\delta_0-\delta_\infty)e^{-at}+\delta_\infty,
\qquad a>0,\quad \delta_\infty>0,\quad
\delta_0>\delta_\infty .
\]

It moves from the initial envelope \(\delta_0\) toward \(\delta_\infty\). The controller uses this prescribed envelope in its position-error design.

## Analysis

### Motion-model convergence

The DMP’s phase variable decays over time. Under the stated bounded-forcing-function condition, the phase-dependent forcing term consequently decays, leaving the convergent spring–damper behavior to move the trajectory toward its goal. Replacing the fixed goal in that term with an exponentially converging intermediate state moderates the initial acceleration while preserving goal convergence. These properties concern the generated reference trajectory; they do not by themselves establish tracking accuracy on the robot.

### Closed-loop boundedness

For bounded \(\theta_d\) and \(\dot{\theta}_d\), the Lyapunov analysis gives **semiglobal uniform boundedness** of the closed-loop signals. Bounded transformed position error supports the transient bound specified by the performance function. The result is conditional on the analysis assumptions and the bounded reference signals. It does not establish global, asymptotic, finite-time, or fixed-time convergence.

## Experiments

### Tracking a circular trajectory with a payload

We evaluated the controller on Baxter’s left arm while its gripper carried a 0.94 kg payload. The reference was a circular Cartesian trajectory at fixed orientation, converted into joint references by inverse kinematics. We compared tracking with neural learning disabled and enabled.

With learning disabled, joint tracking errors were relatively high. With learning enabled, the errors for all tested joints fell within \([-0.04,\,0.04]\) rad, and compensation torque increased. This comparison supports improved tracking in the tested payload and trajectory condition. A numerical between-condition effect size and a statistical test were not reported.

### Learning and adjusting a pouring motion

Five human-guided demonstrations of a pouring task moved four selected joints while the other joints remained fixed. The learned DMP reproduced a task motion. Changing its goal guided Baxter to pour into another cup while retaining the motion profile. This test illustrates spatial adjustment of the learned motion in the demonstrated task; it does not measure a success rate across cups or tasks.

### Learning a drawing motion

In a separate task, five irregular human-guided drawing demonstrations were learned in task space. The resulting drawn curve was smoother than the demonstrations. Sensor measurement errors were identified as one possible contributor to distortion in the recorded paths, but the experiment did not isolate their contribution.

## Discussion

The results address two linked requirements of demonstration-based robot learning. The pouring and drawing tests show how multiple demonstrations can inform a single adjustable motion model in the tested tasks. The payload experiment separately shows that neural learning improved joint tracking under the tested trajectory and load. Taken together, these findings support the use of learned references with adaptive tracking on this manipulator, while each experiment evaluates a different component.

The motion model extends the single-demonstration use of a conventional DMP by estimating its forcing function from a combined set of demonstrations. GMM represents the phase–forcing data, and GMR supplies the forcing-function estimate. Because no ablation isolated GMM from GMR, the task outcomes cannot be attributed to either element alone. Likewise, the smoother drawing is consistent with learning a common motion from irregular demonstrations, but the available observations do not establish which part of the modeling process produced the smoothing.

The controller analysis and robot experiment support different levels of inference. The analysis establishes conditional semiglobal uniform boundedness and a transient-error bound under its assumptions. The experiment documents tracking errors within the reported interval when neural learning was enabled for one payload and trajectory condition. Neither result establishes performance under arbitrary payloads, tasks, or uncontrolled human or environmental contact.

A useful next test would vary payloads and reference trajectories while reporting tracking errors under each condition. That comparison would show how far the observed controller behavior extends beyond the present setup. Separate comparisons of motion models would be needed to determine which elements of the GMM/GMR construction account for the pouring and drawing outcomes.

## Conclusion

We presented a demonstration-based system that learns one adjustable DMP from multiple demonstrations and tracks its reference with an adaptive neural controller. Baxter experiments showed learned pouring and drawing motions and improved joint tracking with neural learning enabled in a tested payload condition. The theoretical boundedness result is conditional, and the experiments support conclusions about these tasks and conditions rather than unrestricted generalization.

## Notes

**Section outline:** Introduction frames motion generation and tracking as separate problems; Method describes the DMP and controller; Analysis states their conditional properties; Experiments reports the controller, pouring, and drawing tests; Discussion integrates their implications and boundaries; Conclusion restates the supported contribution.

**Terminology ledger**

| Canonical term | Use |
|---|---|
| Dynamic movement primitive (DMP) | The point-to-point motion model |
| Gaussian mixture model (GMM) | Representation of the combined phase–forcing data |
| Gaussian mixture regression (GMR) | Estimation of the DMP forcing function |
| Radial basis function neural network (RBFNN) | Approximation of uncertain dynamics in the controller |
| \(\theta_d\), \(\tau_p\), \(\delta(t)\) | Joint reference, payload torque, and position-error performance function |

**Assumptions or missing inputs:** The notes do not supply the controller update laws, full Lyapunov assumptions and proof, DMP equations, GMM configuration, identities of the four pouring joints, or enough implementation detail for replication. Prior-work statements need author-verified citations before submission. The reported experiments do not include pouring or drawing success rates, a statistical controller comparison, or an ablation separating GMM from GMR.

**Claim–evidence map**

| Claim | Evidence | Status |
|---|---|---|
| Neural learning improved tracking in the tested payload condition | Disabled/enabled comparison; enabled errors within \([-0.04,0.04]\) rad | Supported within the tested setup |
| The learned DMP could adjust the pouring goal | Pouring demonstration with another cup | Supported for the reported task |
| The learned drawing curve was smoother | Comparison with five irregular demonstrations | Supported as an observation; cause unresolved |
| Closed-loop signals are semiglobally uniformly bounded | Stated Lyapunov result for bounded reference position and velocity | Conditional theoretical claim |

**Main-text discipline audit:** The three reported experiments and the conditional analysis remain in the body because each supports or bounds a central claim. Unreported statistics, ablations, success rates, and operating ranges have not been supplied or inferred. No source manuscript was provided for a before-and-after word count.
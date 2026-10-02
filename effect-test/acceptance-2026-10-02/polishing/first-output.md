## Polished manuscript body

### Introduction

Learning a robot movement from demonstration requires a model that generates a reference trajectory and a controller that tracks it on the physical robot. A reference may be adapted to a new start, goal, or duration, but its successful generation does not ensure accurate tracking when manipulator dynamics are uncertain, particularly with an unknown payload.

Dynamic-system motion models can generate stable, adaptable trajectories. A conventional dynamic movement primitive (DMP) can represent point-to-point motion from one demonstration. In its original locally weighted regression formulation, however, multiple demonstrations are treated as separate models rather than combined within one DMP. Gaussian mixture models (GMMs) and Gaussian mixture regression (GMR) provide a way to represent variation across demonstrations. The separate problem of tracking the generated motion under uncertain dynamics calls for adaptive control.

Here, phase–forcing samples from multiple demonstrations are combined to estimate the forcing function of one DMP. Its generated joint trajectory is passed to an adaptive neural controller that approximates uncertain dynamics and imposes a decaying position-error envelope. We analyse the conditional closed-loop boundedness property and evaluate the components separately on Baxter: a payload experiment examines tracking, while pouring and drawing tasks examine motion reproduction and adaptation.

### Method

#### System architecture and motion scope

The DMP generates reference trajectories from guided demonstrations; the adaptive neural controller tracks those trajectories on the manipulator. We describe point-to-point motion for one-dimensional trajectories, such as individual joint coordinates. Cartesian trajectories can also be represented through one-dimensional components.

#### Learning a DMP from multiple demonstrations

The DMP comprises a spring–damper component, a decaying phase variable, a bounded nonlinear forcing function, a start and goal, and a positive time constant. Recorded positions, velocities, and accelerations from each demonstration provide forcing-function samples at corresponding phase values. Samples from multiple demonstrations of the same task are combined into a phase–forcing dataset. A GMM represents this dataset, and GMR estimates the forcing function used by a single DMP.

Changing the start and goal adapts the generated motion in space; changing the time constant changes its duration. When the nonlinear forcing function is bounded, its phase-dependent contribution decays and the trajectory tends towards the goal. To moderate initial acceleration, an exponentially converging intermediate state replaces the fixed goal in the spring–damper component. Because this state approaches the goal, the modification retains goal convergence under the stated condition.

#### Adaptive neural trajectory tracking

The manipulator dynamics are

\[
M(\theta)\ddot{\theta}+C(\theta,\dot{\theta})\dot{\theta}
+G_0(\theta)+\tau_p=\tau,
\]

where \(\tau_p\) denotes payload torque and \(\tau\) the commanded torque. The DMP-generated joint trajectory, \(\theta_d\), is the tracking reference. The position controller forms a desired joint velocity, and the velocity controller generates torque. A radial basis function neural network (RBFNN) in the velocity controller approximates uncertain dynamics.

The position-error envelope is specified by

\[
\delta(t)=(\delta_0-\delta_\infty)e^{-at}+\delta_\infty,
\]

where the parameters are positive and \(\delta_\infty<\delta_0\). Bounded transformed position error supports the prescribed transient bound. This tracking property is distinct from convergence of the DMP-generated reference towards its goal.

### Analysis

#### Conditional properties of the reference and controller

For a bounded nonlinear forcing function, the decaying phase variable causes the forcing contribution to diminish, and the spring–damper component directs the generated reference towards its goal. The exponentially converging intermediate state moderates the initial response while retaining goal convergence. These are properties of the motion model, rather than guarantees of physical tracking accuracy.

For bounded \(\theta_d\) and \(\dot{\theta}_d\), the stated Lyapunov analysis establishes **semiglobal uniform boundedness** of closed-loop signals. Bounded transformed error supports the prescribed position-error envelope. Both conclusions depend on the stated reference and controller conditions; the physical tracking results are assessed separately in the experiments.

### Experiments

#### Tracking with a payload

Tracking was evaluated on a Baxter robot with two seven-degree-of-freedom arms. In the controller comparison, the left gripper carried a 0.94 kg payload. A circular Cartesian trajectory at fixed orientation was converted to joint references by inverse kinematics, and neural learning was tested in disabled and enabled conditions.

Joint tracking errors were relatively high with learning disabled. With learning enabled, every tested joint error lay within \([-0.04,0.04]\) rad, while compensation torque increased. The comparison shows improved tracking for the reported payload and trajectory; it does not quantify performance over other payloads or operating conditions.

#### Pouring motion and goal adaptation

Five guided pouring demonstrations moved four joints while the others remained fixed. The learned DMP reproduced the task motion. After its goal was changed, the model guided Baxter to pour into another cup while retaining the movement profile. These observations demonstrate reproduction and goal adaptation in the tested pouring task.

#### Drawing from irregular demonstrations

In a separate task, five irregular human-guided drawing demonstrations were learned in task space. The resulting drawn curve was smoother than the demonstrated paths. Sensor measurement error was identified as a possible contributor to distortion in the recorded trajectories. This result describes the learned motion in the tested drawing task; the contribution of each source of irregularity was not isolated.

### Discussion

The motion-model and controller experiments address different parts of the demonstration-to-execution process. The pouring and drawing tasks show what the learned DMP generated from the supplied demonstrations, whereas the payload comparison tests physical tracking of a specified reference. Together, they support the use of the two components in the reported settings without attributing the tracking result to motion-model learning or the task motions to the controller comparison.

Combining phase–forcing samples through GMM and GMR allows multiple demonstrations to inform one DMP, unlike the original locally weighted regression formulation described here. The motion tests show the behaviour of the combined model, but do not isolate the contributions of GMM and GMR. Likewise, greater compensation torque accompanied improved tracking with neural learning enabled; the experiment does not isolate how much of that change arose specifically from payload compensation.

The analysis and experiments support claims at different levels. Semiglobal uniform boundedness depends on the stated conditions, while the reported error range was observed on one Baxter tracking setup. The pouring and drawing results concern the demonstrated tasks, with no measured success rate across other tasks. Comparisons that isolate the motion-model components, and tracking tests across additional payloads and trajectories, would clarify the source and operating range of the observed behaviour.

### Conclusion

A DMP learned from multiple demonstrations was connected to adaptive neural tracking on a robot manipulator. Conditional analysis supports bounded closed-loop behaviour; Baxter experiments show improved tracking in the reported payload comparison and motion reproduction and adaptation in the tested pouring and drawing tasks. These findings establish performance in the reported conditions, rather than across arbitrary tasks, payloads, or uncontrolled contact.

## Revision notes

| Canonical term | Use throughout |
|---|---|
| DMP | Dynamic movement primitive; generates the reference trajectory |
| GMM and GMR | Gaussian mixture model and Gaussian mixture regression; represent samples and estimate the forcing function, respectively |
| RBFNN | Radial basis function neural network; approximates uncertain dynamics in the controller |
| Semiglobal uniform boundedness | The conditional closed-loop result; distinct from DMP goal convergence and observed tracking |

- The section order is unchanged. The Introduction and Discussion now make the handoff between motion generation and physical tracking clearer.
- Claims about convergence, boundedness, and observed tracking remain attached to their respective conditions and evidence.
- The manuscript retains the author’s equations and reported quantities. No tests, statistics, citations, or component effects were added.

**Main-text discipline audit:** The three experimental findings and their qualifications remain in the main text. Repeated scope statements were compressed; nothing was relocated to a caption or supplement. The primary reported tracking quantity remains \([-0.04,0.04]\) rad, with no inferential statistic supplied. The manuscript body is approximately 1,319 words before polishing and 1,170 words after polishing.
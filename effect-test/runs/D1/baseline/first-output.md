## Draft

### Introduction

In human-guided contact tasks such as carving and grinding, an operator directs a robot while its tool interacts with an environment whose properties may be unknown. The robot must remain easy to guide, yet contact with the environment can disturb the intended path. These demands create two coupled objectives: **manipulability**, meaning the ease with which the operator can move the robot, and **contact stability**, concerning the interaction with the environment and the tracking of the intended trajectory.

Robot impedance affects both objectives. Increasing impedance can help the robot resist contact disturbances, but may require the operator to apply more force to guide it. Reducing the operator’s effort can, in turn, compromise performance during contact. A controller for human-guided contact therefore has to account for how a change intended to improve one objective affects the other.

Research on physical human–robot interaction has addressed compliant guidance, estimation of human intent or impedance, and adaptation to human motion or force. Separately, research on robot–environment interaction has addressed contact-force control and disturbance compensation through feedback and learning. These lines of work address different interaction partners. The question considered here is how to use guidance from the human while adapting to disturbances at the tool–environment contact, without treating the two control objectives independently.

This study uses human guidance information to maintain manipulability and adapts robot impedance in response to environmental disturbances to support contact stability. For non-repetitive tasks, it considers adaptive impedance learning under constant environment coefficients and a constant environment equilibrium position. For repetitive tasks with spatially periodic disturbances, it considers an iterative version. Within the stated interaction model, the controllers are designed without prior knowledge of the disturbance or the human reference position. The study examines stability analytically and investigates the approach on an H-MAN robot using virtual disturbances, real carving, and repetitive grinding.

### Related Work

**Human-guided robot control.** Work on physical human–robot interaction has developed ways to make robots compliant during guidance, estimate the human’s intended motion or impedance, and adjust robot behavior using measured human motion or force. These approaches provide ways to interpret and respond to the operator’s input. The material available here does not establish how they address the additional disturbance produced when a human-guided tool simultaneously contacts an unknown environment. That contact is central to the present problem because impedance chosen for easy guidance also affects the robot’s response to the environment.

**Robot contact control.** Work on robot–environment interaction has used feedback and learning to regulate contact force and compensate for disturbances. This work addresses the environmental side of the task, but the approaches described in the supplied material do not explicitly place the guiding human in the same interaction model. The distinction is one of scope, rather than evidence that either research line is ineffective. The present study brings human guidance and environmental contact into a shared control problem, where impedance adaptation must account for their competing effects. Its non-repetitive and repetitive formulations address different disturbance settings.

## Section outline

- Define the human-guided contact task and its two objectives.
- Explain why impedance couples ease of guidance to contact performance.
- Position the human–robot and robot–environment research lines.
- Introduce the two task formulations and the planned analysis and studies.

## Terminology

| Term used in the draft | Intended meaning |
|---|---|
| Manipulability | Ease with which the human operator guides the robot; no formal metric is specified. |
| Contact stability | Behavior during environmental contact, including interaction and trajectory tracking; no formal criterion is specified. |
| Environment equilibrium position | The constant environment position assumed in the non-repetitive formulation. |
| Human reference position | A quantity the stated interaction model does not require to be known in advance. |

## Assumptions or missing inputs

The draft treats the contribution as a control formulation with non-repetitive and iterative variants. The notes do not provide controller equations, stability conditions, comparisons, measurements, or outcomes, so the prose makes no performance or validation claim. Verified citations are needed for both Related Work topics before submission.

## Claim–evidence map

| Claim | Evidence in the supplied notes | Status |
|---|---|---|
| Impedance can create tension between ease of guidance and contact performance. | Author’s description of the two objectives and their trade-off. | Supported as motivation |
| The study considers adaptive and iterative formulations for different task settings. | Author’s stated research decisions. | Supported as study scope |
| The controllers maintain manipulability or contact stability in practice. | Stability analysis and H-MAN studies are named, but their findings are absent. | Needs results |
| Prior approaches leave this combined setting unresolved. | Only the scopes of two research lines are described. | Needs verified literature support |

**结构说明：**引言采用“任务—阻抗权衡—研究问题—本文方案”的顺序。相关工作按人机交互与机器人环境接触两条技术线组织，并将区别限定为现有材料所能支持的研究范围。
**Theorem 1.** Consider the unknown robot manipulator described by (1), with tracking errors \(e_i\) defined in (10). If the initial conditions lie strictly within the output constraints (11) and (12), then, under the neural controller (35) and adaptive law (36), the tracking errors converge in fixed time without violating those constraints. All closed-loop signals are globally uniformly ultimately bounded (GUUB).

**Definition.** Fixed-time convergence means that the convergence-time bound is independent of the initial state.

**Revision notes:** The conditions now sit directly before the guarantees. Fixed-time convergence and GUUB remain separate claims; no time formula or proof has been added. The terminology is fixed as follows:

| Term | Meaning retained |
|---|---|
| Fixed-time convergence | Convergence with a time bound independent of the initial state |
| GUUB | Globally uniformly ultimately bounded |
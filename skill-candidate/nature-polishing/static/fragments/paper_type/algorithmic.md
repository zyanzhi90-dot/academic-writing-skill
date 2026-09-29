# Paper type: algorithmic or device

The argument proposes a procedure, tool, or system and must show that it performs reliably and advantageously.

For a robotics system, compare the task and assumptions, claimed guarantee or
capability, component or proof, tested condition, and boundary before revising
section order. The shared robotics body reference supplies the domain checks;
an ablation is useful where it isolates a component, not obligatory per module.

## What the reader expects

- a clear problem formulation and the precise scope being claimed
- the proposed procedure or device, described to a level a peer could re-implement
- a fair comparison against credible baselines under matched conditions
- ablations or controls when needed to isolate a claimed component or mechanism
- failure modes, runtime/cost characteristics, and applicability boundaries

## Polishing priorities

- Separate "what the system is" from "why it works" from "how well it works"; do not braid them.
- Performance claims must specify the dataset, metric, baseline, and conditions, not stand as bare numbers.
- Avoid marketing verbs (`leverages`, `enables`, `empowers`) unless they carry information.
- The Discussion should name the failure modes the experiments revealed, not only the wins.

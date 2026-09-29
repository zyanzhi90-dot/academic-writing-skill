# Section: Method (writing)

## Default structure

`task formulation -> overview (pipeline / system / approach) -> per-module detail -> implementation notes -> assumptions and boundary`

## The three-element pattern (per module)

Each module should answer:

1. **Motivation** — what problem this module solves, and why the obvious alternative fails
2. **Mechanism** — what the module actually does, to a level a peer could re-implement
3. **Evidence / role** — what downstream claim or test relies on this module;
   an ablation is useful when it can isolate the role, not mandatory per module

If any element is missing, the module reads as a black box. Flag the gap.
For robotics control, state the operating condition before a guarantee and
identify what an introduced quantity becomes in the next step. Use the shared
robotics body reference for the condition-to-guarantee and input-to-output
checks; do not add a motive sentence around every routine equation.

## Pre-writing checklist

Before drafting Method, confirm with the user:

- Task formulation: inputs, outputs, scope.
- Overview figure / pipeline diagram: does one exist? It anchors the section.
- Notation: defined once and consistent.
- Reproducibility scope: code, weights, data — what will be released.

## Forbidden vague phrases

Never leave:

- `under standard conditions`
- `using routine methods`
- `data were analyzed statistically`
- `the method was validated`
- `samples were randomly assigned` (without saying how)

Replace with the actual reproducible information.

## Deeper reference

For module-motivation templates, three-elements examples, and overview-template patterns, open `references/method.md` and `references/examples/method/`.

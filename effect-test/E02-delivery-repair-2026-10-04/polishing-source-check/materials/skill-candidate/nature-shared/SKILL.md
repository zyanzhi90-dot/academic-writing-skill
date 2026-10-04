---
name: nature-shared
description: Internal shared-reference support package for installed Nature Skills, including nature-writing, nature-polishing, nature-response, nature-reader, and nature-paper2ppt. Do not invoke it as a standalone user workflow. Load only the specific core or journal-format file requested by another Nature skill.
---

# Nature Shared References

Use this package only as a dependency of another installed Nature skill.

- Load the exact referenced file; do not preload the whole package.
- Treat `core/` and `journal-formats/` as shared definitions, not standalone workflows.
- Use `core/scientific-expression.md` as nature-writing and nature-polishing's
  common expression core during generation and before delivery; section
  fragments supply purpose-specific guidance and examples remain on demand.
- Use `journal-formats/nature.md` only for the flagship journal Nature and
  `core/research-compliance.md` only when its specialist applicability gate is
  triggered.
- Use `journal-formats/nature-machine-intelligence.md` for exact NMI article
  types, limits, initial-submission files, data/code duties and production
  requirements; do not import flagship Nature or Nature Communications limits.
- Use `core/main-text-discipline.md` for result placement, main-text compression,
  revision accretion, caption/SI allocation, and claim-repetition checks.
- Use `core/nature-results-discussion.md` for corpus-derived Nature-style
  Results claim escalation, evidence-bound local interpretation, and Discussion
  synthesis; do not present it as official journal policy.
- Use `core/discussion-argument-language.md` for journal-general Discussion
  function sequencing, reverse-funnel control, evidence-calibrated modality,
  claim-specific limitations, and uncertainty-driven future work.
- Use `core/nature-introduction.md` for corpus-derived Nature-style problem
  funnels, exact knowledge gaps, literature tension, question-first novelty,
  and Introduction–Results alignment; do not present it as official journal
  policy.
- Use `core/nature-abstract.md` for corpus-derived Nature-style
  discovery-centred abstract compression, claim hierarchy, selective numeric
  support, and field-level payoff; do not present it as official journal policy.
- Load `core/robotics-main-text.md` only when nature-writing or
  nature-polishing requests it for a robotics-centred manuscript body. It
  refines domain decisions without overriding source facts, shared integrity
  safeguards, or target-journal requirements.
- Load `core/robotics-writing-examples.md` for robotics-centred abstracts or
  body work, including overall reasoning, standalone paragraphs, translation,
  and feedback. Read common use/check instructions, task index, and selected
  cards (A for abstracts, B for body); do not preload the full corpus. Exclude
  incidental robotics, title-only, submission administration, and layout.
  Abstract-only tasks do not load the body module. This file is the sole example
  authority; project PDFs and reports are optional source lookups.
- Return to the requesting skill for task logic, output format, and final QA.

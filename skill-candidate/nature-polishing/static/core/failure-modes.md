# Diagnose failure mode before editing

Before rewriting, identify the main problem:

- wrong paper type logic
- missing gap or poor positioning
- claim without evidence
- evidence without a clear claim
- missing boundary or limitation
- Results and Discussion mixed together
- weak title or abstract signal
- inconsistent terminology, abbreviations, units, or notation across sections
- evidence-complete but main-text-bloated Results
- reviewer-driven additions appended without deleting redundant prose
- the same claim or full statistical report repeated across Results and captions
- sentence-level clutter only
- in robotics body prose, a broken condition-to-guarantee link, a changed
  technical object, or a literature comparison that never reaches its design
  significance across the relevant paragraph group

Prioritize fixes in this order:

`paper type -> section job -> evidence placement -> paragraph necessity -> claim/evidence/boundary -> sentence polish`

Do not sentence-polish a draft whose section job is wrong. Surface the structural problem first, then polish.
For a robotics manuscript body, use the conditionally loaded shared robotics
reference to diagnose object handoffs and claim scope before changing voice,
connectives, or sentence length. Check the whole comparison group rather than
requiring every literature paragraph to carry a gap and transition.

For Results or full-main-text work, load
`../../../nature-shared/core/main-text-discipline.md`. Resolve evidence placement,
revision accretion, explanatory recursion, and claim repetition before editing
sentence rhythm.

Terminology consistency is a cross-cutting check that runs at every level: build the Terminology Ledger on first contact (see `../../../nature-shared/core/terminology-ledger.md`) and enforce its canonical forms throughout the polish.

Apply the loaded `scientific-expression.md` when repairing expression and
before delivery, including after feedback. Choose ordinary syntax and explicit
scientific objects, then check meaningful phrases, sentences, and context;
repeated object names are not a reason for automatic pronoun replacement.

For robotics abstracts and body work, follow the conditionally loaded
`robotics-writing-examples.md`: diagnose the failure before selecting relevant
English cards, coordinate main and supplemental references with the current
manuscript style, and adapt only the affected scope. Before delivery run its
internal meaningful-phrase-to-sentence-to-context check, including ordinary
words, grammar, and natural combinations. Distinguish errors, awkwardness that
impairs understanding, and sound variants; do not rewrite the last category
merely to resemble a source. Apply the same check after targeted feedback.

# Nature Communications 2025 — Empirical Drafting Patterns (CS/AI corpus)

Use this file when drafting or restructuring a manuscript and you want
**genre-aware, evidence-backed structure calibration** beyond the generic
section fragments. The patterns below are distilled from a 2025 reading set of
20 open-access *Nature Communications* articles in computer science / AI
(research articles plus Perspective, Comment, Review, and benchmark/framework
papers). Learn suitable syntax, information order, and ordinary collocations
from concrete English, adapting them to author content. Do not import source
facts, distinctive assertions, or passages as the author's own work; retain
necessary attribution. These are observations and options, not required move
orders, sentence counts, signal words, or title forms.

> Companion of `references/article-architecture.md` (generic move orders) and
> `nature-polishing/references/published-article-patterns.md`. This file adds
> the 2025 CS/AI evidence layer, quantified word preferences, and genre splits.

## 0. Decide the genre first — it picks the skeleton

| Genre | Skeleton |
|---|---|
| Research article | Abstract funnel → Intro (hook→gap→`Here we`) → Results (conclusion-first) → Discussion → Methods |
| Benchmark / framework | Same, but the *gap is "the field has no agreed standard"*; tables dominate; stress community / reproducibility / versioning |
| Review | Trend declaration → `This Perspective/Review explores…` → topic/modality chapters synthesising others' work → `Conclusions and outlook` |
| Perspective | History/era hook → numbered argument points → normative `X should…` advice → roadmap close |
| Comment | First-person singular, rhetorical question opening, analogy/history, no IMRaD, no abstract/figures |

State the detected genre before drafting; the rest of this file assumes a
research article unless noted.

## 1. Title

- Four recurring shapes, chosen by intent:
  - Noun phrase, method-led (most common): *AlphaFold prediction of structural ensembles of disordered proteins*
  - Declarative claim (the selling point is a finding): *Dendrites endow artificial neural networks with accurate, robust and parameter-efficient learning*
  - `System name: function` colon form (brands a tool/model): *CodonTransformer: a multispecies codon optimizer…*
  - Gerund/question for benchmark or Perspective: *Benchmarking large language models for…*; *Does provable absence of barren plateaus imply classical simulability?*
- An evaluative adjective often pre-loads the claim: *robust*, *generalizable*, *data-driven*.
- Almost never contains a number or a result; keep digits for the abstract.
- Prepositional chain carries "what + how + where": *…discovery and engineering **with** deep learning **using** CataPro*.

## 2. Abstract — the funnel

A recurring five-move realization in this corpus is one paragraph with 4–11
sentences (research longer, benchmark/active-learning tighter); these counts and
moves describe observations, not quotas for the current abstract:

1. Field value / why-it-matters (present tense, often subject-less assertion)
2. Gap, almost always opened by **However** + a nominalised pain point
3. Hinge sentence: `Here we show/present/introduce X (FULL NAME, abbr.), a … that …`
4. One hard quantified result (a factor, %, or accuracy), past tense
5. Significance + optional resource link (GitHub)

Pattern markers: gap *"However, DE can be inefficient when mutations exhibit … epistatic behavior."*; hinge *"Here, we show that traditional fine-tuning outperforms zero- or few-shot LLMs in most tasks."*; close *"Our findings suggest…"* / *"These results indicate…"*.

## 3. Introduction

- **Hook**, three forms: importance declaration (*"The biological brain is remarkable in its ability to…"*); definition framing (*"Protein engineering is an optimization problem, where…"*); domain-then-obstacle (benchmark default: broad use → *"Despite its promises, progress … is impeded due to the absence of … benchmarks."*).
- **Gap** signal words cluster tightly: **However / remains / Unfortunately / underexplored / the scarcity of … hinder / Without X, Y cannot be …**. High-end move: quantify the scarcity — *"merely 124 (3.0%) have … structures in the PDB."*
- **Contribution**: `Here we…` / `In this work, we…`, usually with a `(Fig. 1)` pointer; multiple contributions as `First… Second… Finally…`.
- Make the **choice of system/problem explicit** — *"We chose this model system because…"* — this satisfies the "科学问题要科学" expectation: the question must be motivated, not assumed.

## 4. Results narrative

- **Subheadings** are either a conclusion sentence or a noun/gerund phrase naming the method — *"CodonTransformer generates DNA sequences with natural-like distributions"*, *"Exploring the biocatalytic synthesis landscape of McbA"*. Avoid neutral *Experiment 1 / Dataset* labels.
- **Conclusion-first**: the paragraph opens with the judgement, evidence and figure call follow — *"Interestingly, wt-McbA displayed a tolerance to multiple 'unprotected' functional groups…"*
- **Figure callouts**, two shapes: figure-led (*"Figure 3 (a) depicts the action distributions…"*) and trailing parenthetical (*"…synthesize 11 pharmaceutical compounds (Fig. 2C)"*).
- **Numbers** come as absolute + relative + direction — *"from 323.4 to 297.3 … representing an improvement of 8.8%"*; closing roll-up *"These findings collectively affirm that…"*.
- Paragraph-advance engine: `With [previous result], we next …` / `To <goal>, we <did> (Fig. X).`

## 5. Transitions (observed frequencies, 5-article subset)

`However` 51 ≫ `Furthermore` 22 · `Therefore` 19 · `Overall`/`Notably` 16 · `In addition` 13 · `In contrast` 6 · `Moreover` 4.
- **However** is the workhorse for turning, gap-opening, and surprise.
- **Furthermore** and **Moreover** are both options for addition; choose by the
  actual relation and manuscript style, not their relative frequency (22 vs 4).
- `Notably / Importantly / Interestingly / Surprisingly` flag the key finding; `Overall / In summary` close a block.

## 6. Syntax & register

- Tense: background/properties = present; what-we-did = past; current meaning/figure description = present.
- Voice: the corpus often uses active **we** for narrative and claims and passive
  for apparatus/method. Choose by attributable action and technical focus; either
  can be appropriate outside those positions.
- Hedges cluster in meaning sentences in this corpus, but uncertainty belongs
  wherever the author's evidence requires it, including results or assumptions.
  Calibrate any intensifier to the supported magnitude or statistical status.

## 7. Genre-difference cheatsheet

| Axis | Research | Review | Perspective | Comment |
|---|---|---|---|---|
| Data | own figures/numbers | synthesis of others' citations | argument, no experiments | none |
| Person | `we` + passive | `we` + survey | `we/our` throughout | first-person `I` |
| Stance | assert findings | weigh + outlook | argue + normative `should` | rhetorical, value-driven |
| Close | Discussion + limits | `Conclusions and outlook` + governance call | roadmap / conditions | call to action |

## 8. 中文迁移要点

- 以上信息链、标题形式和信号词是语料选项；按作者内容与稿件要求选择，不强制摘要数字、标题形式或 gap 连接词。
- 贡献句显式给出选题理由("之所以选该体系,是因为…"),呼应"科学问题要科学"。
- 不确定性放在真实需要限定的位置，不限于意义句。`significantly` 是否适合取决于作者统计与当前句意；缺检验不自动改成其他强化词，可改述具体指标与支持范围。

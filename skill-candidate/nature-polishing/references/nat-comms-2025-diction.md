# Nature Communications 2025 — Diction & Connector Calibration

Use this file during the sentence-level polish pass when you want **empirical,
quantified word-choice calibration** to back up `style-guardrails.md` and
`published-article-patterns.md`. The preferences below are measured from a 2025
reading set of 20 open-access *Nature Communications* computer-science / AI
articles. They are calibration data, not rules to apply blindly — a discipline
or a specific journal house style overrides them. Concrete syntax and ordinary
collocations may be learned and adapted to author content; source facts,
distinctive assertions, and borrowed passages retain their attribution duties.

## 1. Connectors — observed preference order

句首大写连接词词频(5 篇子集合计):
`However` **51** ≫ `Furthermore` 22 · `Therefore` 19 · `Overall`/`Notably` 16 · `In addition` 13 · `In contrast` 6 · `Moreover` 4 · `Importantly` 2.

- **However** carries turns, gap-opening, and surprises — do not scatter weaker
  alternatives where `However` is idiomatic.
- **Furthermore** and **Moreover** are addition options; frequency (22 vs 4)
  does not justify replacing an accurate natural choice. Use **Therefore** only
  for a supported inference; summaries may use **Overall / In summary / In conclusion**.
- Reserve **Notably / Importantly / Interestingly / Surprisingly** for the
  paragraph's key finding, not as routine sentence openers.

## 2. Boosters — magnitude and statistical status

- **`significantly` appears 0 times in the corpus.** When a draft leans on
  "significantly (better/higher/improved)", first check it is a *statistical*
  claim with a test behind it. For descriptive magnitude, check the author's
  metric and scale. If support is insufficient, state the concrete comparison
  or flag missing evidence; do not automatically replace it with another
  intensifier. Corpus absence is not a vocabulary ban.
- This extends the `style-guardrails.md` overclaim list: treat blanket
  intensifiers as a smell, and attach every booster to a number or a test.

## 3. Hedges — concentrated, not sprinkled

- Primary hedges are **may** and **potential**; `might / could / likely` are
  secondary. They cluster in meaning/Discussion sentences, not in Results
  reporting. Pattern marker: *"Encoding these mechanisms **may** help further
  improve the performance."*
- Retain uncertainty where it qualifies the actual result, assumption, or
  interpretation. Do not move a hedge away from the claim it limits merely to
  match this distribution; numbers are useful when scientifically informative.

## 4. Achievement verbs — the house vocabulary

Frequent, defensible when backed by data: **achieve · demonstrate · outperform
· superior · robust · generalizable · comparable**. When the result is *weaker*
than a baseline, state it honestly. Use **comparable** only when the comparison
supports it, optionally with a relevant concession: *"**Despite the smaller scale** of our pre-training data …, the
**comparable** performance highlights the effectiveness."* Do not upgrade
`comparable` to `superior`.

## 5. Tense & voice (polish-pass checks)

- Background / property = present; specific operation = past; figure
  description = present. Flag accidental past-tense for a standing property
  (*"CataPro demonstrates…"* not *"demonstrated"* when stating a capability).
- Active **we** and passive are both available; choose by technical focus and
  attributable action. Flag a construction when it hides a necessary agent,
  not merely because it is passive outside Methods.

## 6. Sentence-skeleton phrases (calibrated to 2025 corpus)

- Abstract hinge: `Here we show/present X (FULL NAME, abbr.), a … that …`
- Gap: `However, … remains a challenge` / `the scarcity of … hinders …` /
  `Without X, Y cannot be quantified`.
- Result close: `These findings collectively affirm/confirm that …`
- Significance (soft promise, not a guarantee): `promises to / offers
  potential / paves the way`.
- Titles in this corpus often omit numbers and results; follow the current
  manuscript's scientific purpose and journal requirements.

These are observed realizations, not fixed templates or mandatory title/word
rules. Choose by the current scientific content and manuscript requirements.

## 7. 中文润色要点

- 连接词:转折/制造空白优先"然而";递进偏"此外/进一步"(对应 Furthermore);
  因果用"因此";收束用"总体而言/综上"。
- “显著”是否适合取决于统计地位与当前句意；无支持时具体报告指标或说明缺项，不自动替换为强化词。
- 不确定性保留在它实际限定的结果、条件或解释处，不强制结果肯定或数字配额。
- 比较措辞须由证据支持；弱于对手如实写弱于，“相当”仅在比较支持时使用，不能凭让步句升级结果。

# E03 修改与交付核对

本轮是人工反馈修订，不是重复自主测试。依据原样 [F01–F15](materials/inputs/scientific-facts.md)、[作者 v2 正文](materials/source-e03/author-v2-full-text.txt)和[来源核对](materials/source-e03/source-check.md)，对照当前卡片中 A06／A07／A08 的完整真实英文与分析。A08 采用本地 ICRA 出版版，完整摘要与作者 v2 经版面规范化后相同，沿用[既有版本核对](../../analysis/RRL2019-example-addition-2026-10-04/source-basis.md)，没有重新提取。

## 实际调整及其作用

| 原稿位置 | 修改 | 判断及依据 |
|---|---|---|
| S1 后 | 增补显式模型结构可利用、接触与摩擦难以准确建模的对照 | 原稿讲了两项职责，却未解释选择这两种方法的依据。F08、F15 和原文 §I、§III.A 支持这一互补关系；A08 S1–S2 从 `by capturing the structure with explicit models` 连到 `contacts and friction, which are difficult to capture …`。新句把同一关系接入方法开篇，不增加制造业泛背景、调参过程或泛称所有反馈控制脆弱。 |
| 原 S3，现 S4 | 增加 `through interaction with the environment` | A08 S4 的 `learning … from interactions with the environment` 给出 RL 如何处理接触问题的依据；F07–F08 支持残差通过交互学习获得。新句仍以两部分为主语，对应几何目标与接触修正，不把两部分变成独立优化。 |
| 原 S8–S9 | 删除固定侧块迁移分支及不足千步结果 | 该结果有独立设置与不同基准，若保留就必须交代这些条件，会开启另一证据分支。当前摘要选择 F02 的样本／最终表现对照和 F03 的错位对照，已分别证明结构复用和接触修正优势；删除整组不移用千步数字，也不否认原论文的迁移结果。 |
| 现 S3，交付检查 | `learned from … states` 改为 `based on … states`，中文相应修改 | 原文式(5)的 πθ(sm, so) 明确把机器人和物体状态作为策略输入；下一句交代环境交互这一学习来源。按 A06／A07 明确对象与关系的语言习惯，把两个关系分别写清；不改变两个输出相加或完整任务优化。 |
| 现 S6，交付检查 | 删除 `seven-degree-of-freedom`，中文相应删除自由度数 | Sawyer 及仿真／实机已标明证据来源，块插入与两侧块状态目标给出贡献所需范围。自由度数不解释所选作用，也不是本方法的适用条件。A06 末句保留 Baxter 而不列关节参数，支持这一取舍。 |

前面三项来自本轮单次模型修订，后面两项是协调端交付检查中的局部精修。[模型原始输出](drafting/first-output.md)原样保留，两处精修记录在 [delivery-edits.json](delivery-edits.json)，没有再次调用模型。交付稿保留原稿 S1、S4、S6、S7 四句原文；原 S2、S3、S5 只作上表说明的局部调整。句数与词数不作为质量门槛。

## 连续句与关键措辞

下表编号指最终交付稿，不是模板。

| 句子 | 必要内容、承接与英文核对 |
|---|---|
| S1 | 原样保留 `This paper proposes … for robotic manipulation involving …`。沿用 A06 方法开篇和 A07 方法—任务范围关系；`contact, friction and movable objects` 指明难点与对象，不添加首创、普适或安全主张。 |
| S2 | 承接 S1 的接触／摩擦，解释常规控制可利用哪些结构、哪些成分难以建模。`can exploit` 是能力，`known structure` 限定可利用部分，`through explicit models` 给出依据；`but` 接同一任务中的建模难点。借鉴 A08 S1–S2 的真实关系，将两句压为一个明确对照，没有搬入泛背景。 |
| S3 | 将刚给出的互补理由落实到 `sum of the outputs`；保留 `outputs` 和 `fixed`，分别明确相加的是控制信号、固定的是基准。`based on robot and object states` 指策略输入，下一句才说明学习来源。A08 S5–S6 的分工—叠加关系在此准确适配，不照搬 A06 的生成后交给跟踪控制器的串联。 |
| S4 | 重复命名 `feedback controller` 与 `residual policy`，按 A06／A07 的对象复现习惯交代两项作用。`guides … towards geometric goals` 对应已有控制结构，`learns corrections for … through interaction with the environment` 回答接触部分为何用 RL。`corrections` 指控制修正，不宣称显式辨识或完全消除接触动力学。 |
| S5 | 原样保留残差策略优化对象、`expected return`、`full task` 和 `under the combined control`。原文 §III.A L259–268 明确状态耦合，式(5)须整体优化；`to maximize` 是优化目的，不是全局最优保证。这句限定前句职责安排的解读。 |
| S6 | 从设计转到仿真及 Sawyer 实机块插入。`by inserting … while keeping …` 提供任务及成功目标，为接下来的比较定范围；`keeping … in their target positions` 是任务要求，没有加入全过程严格零位移。省去自由度数后仍保留足够的证据对象。 |
| S7 | 原样保留 `The results demonstrate that … fewer interaction samples … better final performance than …`。A07 的结果主语—`demonstrate` 接真实发现，替换泛称有效性；F02／§VI.A 支持同底层算法、无基准的比较。`same underlying algorithm` 排除将优势解释成另一个基础 RL 算法；`The results` 回指本任务的仿真／实机，不扩至任意任务。 |
| S8 | 原样保留初始错位、实机、15/20 与人工控制器 2/20。F03／§VI.B 的这组对照直接证明难以手工指定的接触修正作用，承接 S4，不再另启迁移设置。`initially` 与两种控制器的次数承担范围与比较作用；不添加显著性、任意错位成功或统计保证。 |

整段现在是方法提出—互补理由—相加构造—职责与交互学习—完整任务优化—同一装配任务的两类关键对照。A08 提供互补设计的连续关系及 `explicit models`、`contact and friction`、`interaction with the environment` 等具体英文；A06 保持方法开篇、普通句法与对象交接；A07 支持设计—作用—验证推进和结果主语。没有以几个孤立句型代替科学关系，也没有为模仿迁入 DMP、复合学习、PPE 或完整闭环定理。

## 交付判断

组合理由已补足，验证已收束到同一主任务的两个关键比较，科学对象、优化关系与证据条件均与正文一致。中文对应保留这些关系，未增加控制保证。没有需要继续重构主线或再修科学含义的已知问题；两项交付精修已落实，其他准确成熟的原句保留。本稿待负责人独立验收，不能据此给原自主首稿补记通过，也不能外推候选的自主效果。

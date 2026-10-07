# P17 单次示教学习能力：源文含义修正

基线 `3e08054a508349ac951f8e92c31eb0d951dbf017`；开始时本地、origin/main 与最新远端一致。只修正候选正向学习材料的一处已确认含义偏移。

源文定位见 [P17 完整引言](../introduction-section-review-2026-10-06/P17-introduction.md)。

- I02，PDF p.1／刊页777：DMP “only requires one demonstration to model motion”。与前面的 DS 方法需要较多训练示教相对照，这里说明一次示教即可建模。
- I05，PDF p.2／刊页778，左栏：原 DMP 使用 LWR 学习，LWPR 优化 LWR 核带宽；随后原句为 “Despite the added complexity of the learning procedure, these methods enable the DMP to learn from only one demonstration.” 即尽管学习过程更复杂，这些方法仍具有从单次示教学得 DMP 的能力。

| 位置 | 修正前 | 修正后及源文关系 |
| --- | --- | --- |
| robotics-introduction-paragraphs.md，P17 I05-A7，“新增什么信息” | 增加学习复杂性后，这些方法的示教利用仍限于一次示教。 | 尽管增加了学习过程的复杂性，这些方法仍能从单次示教学得 DMP。保留 Despite 的让步关系及 enable 的能力含义。 |
| 同行任务与承接说明 | “上述两种途径”及“LWR／LWPR 学习途径”。 | 明确这些方法的单次示教学习能力，并分别接住 LWR 学习与 LWPR 核带宽优化的职责。 |

整节层 P17 I02／I05 的英文及借鉴说明没有把单次示教能力解释为“只能利用一次示教”；表达层 E14 的 only requires、E20 的 I05-A7／Despite／enable 分析也保留了能力和示教量，未发现相同含义偏移，均不修改。多示教组合设计的作用、相关比较、计算效率及后续轨迹执行责任保持原样。

实际候选修改仅为段落层 I05-A7 一行中的解释；原文、适用英文句式、其他分析、语境判断、路由及历史输出均未改。完成依据是源文含义和三层解释一致，没有运行新测试、生成或润色。按 AGENTS.md 提交同步后停止，交独立验收。

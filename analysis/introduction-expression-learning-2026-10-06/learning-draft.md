# Introduction 默认表达写法与真实连续句证据

先确定作者要表达的科学对象、已有能力、相关条件、设计职责和作用，再调用能表达同一关系的真实英文。P17 为默认表达锚点；P05、Fuzzy2023、ESO2017 提供适用的补充。已验收的[整节学习稿](../introduction-section-learning-draft-2026-10-06/learning-draft.md)与[段落学习稿](../introduction-paragraph-learning-2026-10-06/learning-draft.md)为组织和连续推进提供参照，科学主线及各段任务由作者研究决定；本稿学习适用关系怎样落到英文句子中。

材料按科学关系组织，覆盖领域价值、段首对象、文献能力及续句、条件与比较、设计及作用、设计接口和贡献收束。每组保留真实连续句和必要上下文，逐句拆出主语、谓语、对象，以及实现关系的句式、介词和具体用词。来源标识中的 S 编号对应出版原文句位，分析表中的 A 编号对应当前完整单元的示例句位。英文按块标为“原文选取”或“基于原文的适配”；逐句对应及完整出版原文保留在[来源审计](../introduction-default-learning-cleanup-2026-10-06/audit/adaptation-map.json)中。引文数字沿用各篇论文的文献编号。

“可模仿表达”中的 `〈…〉` 标记分析所得的作者内容位置，不是出版原句。方法、模型、控制器、观察器和量的占位填写准确的科学名称，必要时重复名称；较短指代保留对象的技术身份与作用。使用时按数、时态、条件和证据强度调整，用具有明确主语和限定动词的完整句子连接条件、作用及输入输出。句式是一组可以直接参照的成熟实现，调用顺序与组合方式由当前科学关系决定。来源差异及选取审计另存于 [audit/](audit/preference-repair-record.md)。

## 1. 领域价值怎样写成首句，并接入研究需要

默认先让领域对象作主语，直接写其应用价值或提供的能力。接着让“所需能力”或“实现价值所需的研究环节”进入主语位置，明确为什么需要继续研究。优先参照 P17 的简明领域入口，再按作者内容选择具体价值及需要的表达。

### E01｜应用领域 → 所需能力 → 研究必要性

P17 首段从机器人应用进入制造产品更新，再进入增强机器人学习的必要性；后续句以 LfD 继续收窄到运动建模。

**P17 I01-S1-S3**；原段跨度：PDF p.1 / 刊页 777 / 左栏 -> PDF p.1 / 刊页 777 / 右栏；[来源审计定位](../introduction-section-review-2026-10-06/P17-introduction.md#i01)。

**英文学习示例（基于原文的适配）。**

> Recently, robots have been widely applied in various fields, especially in manufacturing. Adaptable robots are required due to the increasingly fast updates of the manufactured products. Hence, it is necessary to develop methods for enhancing robot learning.

| 示例句位 | 真实主语—动作—对象或补语 | 句式、搭配与用词怎样实现关系 |
| --- | --- | --- |
| I01-A1 | `robots`—`have been widely applied`—`in various fields`，重点为 `manufacturing`。 | 领域对象作主语；现在完成时被动写已建立的应用。`applied in` 接领域，`especially in` 明确与本文相关的主要场景。`widely` 描述应用范围。 |
| I01-A2 | `Adaptable robots`—`are required`—原因是产品更新加快。 | 将前句的机器人加上所需属性 `Adaptable`，直接写能力需求；`due to` 后接原因名词短语，`updates of` 明确被更新的对象。 |
| I01-A3 | 形式主语 `it`—`is necessary`—`to develop methods for enhancing robot learning`。 | `Hence` 承接需求；真正任务放在 `to develop` 中。`methods for + -ing` 写方法服务的环节，`enhancing` 的对象是学习能力。 |

**可模仿表达及作者对应。** `〈领域对象〉 have been widely applied in 〈应用领域〉, especially in 〈本文相关场景〉.`；`〈具备所需能力的对象〉 are required due to 〈实际原因〉.`；`Hence, it is necessary to develop methods for 〈需要增强的研究能力，-ing〉.` 三句中的对象连续：应用对象、该对象的能力需要、增强该能力的研究任务。作者填入自己的大领域价值及真实需求；时间词对应作者讨论的时间背景。

### E02｜用具体能力解释研究价值

P05 开篇把双臂协调控制的研究价值具体化为负载、工作空间和灵活性，再说明相关应用。

**P05 I01-S1-S2**；原段跨度：PDF p.1 / 刊页 1010 / 左栏 -> PDF p.1 / 刊页 1010 / 右栏；[来源审计定位](../introduction-section-review-2026-10-06/P05-introduction.md#i01)。

**英文学习示例（基于原文的适配）。**

> Coordination control of dual-arm robots has received increasing attention due to the advantages of dual-arm robot systems over traditional single-arm robot systems, including stronger payload capability, larger workspace, and more flexibility. Thus, dual-arm robots have been involved in many applications, such as intelligent assembly, repair in space, and assistance for elderly people [1]–[3].

| 示例句位 | 真实主语—动作—对象或补语 | 句式、搭配与用词怎样实现关系 |
| --- | --- | --- |
| I01-A1 | `Coordination control of dual-arm robots`—`has received increasing attention`—由于双臂系统相对单臂系统的负载、工作空间和灵活性优势。 | `due to the advantages of A over B` 明确优势属于哪类系统及其参照；`including` 给具体能力，领域价值与后续应用连续。 |
| I01-A2 | `dual-arm robots`—`have been involved`—智能装配、空间修理及老年人辅助等应用。 | `Thus` 接能力与应用，`such as` 引入真实用途，应用名称直接写 `intelligent assembly`、`repair in space`、`assistance for elderly people`。 |

**可模仿表达及作者对应。** `〈研究领域或对象〉 has received increasing attention due to 〈具体价值〉, including 〈相关能力〉.` 比较存在时可接 `compared with 〈明确参照对象〉`。对应作者内容时，价值由可说明的能力支撑；应用范围可沿用 E01 的 `have been widely applied in ...`，形成 P17 的默认表达风格。

### E03｜领域能力 → 发挥价值所需的技术责任

ESO 首段先说明水下机器人扩展海洋探索和科研能力，再把充分发挥价值联系到高精度控制、数据质量和运动精度。

**ESO2017 I01-S1-S2**；原段跨度：PDF p.1 / 刊页 6785 / 左栏 -> PDF p.1 / 刊页 6785 / 右栏；[来源审计定位](../introduction-section-review-2026-10-06/ESO2017-introduction.md#i01)。

**英文学习示例（基于原文的适配）。**

> Underwater robots, including autonomous underwater vehicles (AUVs), remotely operated vehicles (ROVs), and underwater gliders, have been increasingly employed to expand human capabilities in marine resource exploration and marine scientific research. To exploit the full potential benefits provided by underwater robots, a high-precision controller for underwater robots is required to guarantee the quality of the collected data and to secure high precision in trajectory tracking or station keeping [1]–[6].

| 示例句位 | 真实主语—动作—对象或补语 | 句式、搭配与用词怎样实现关系 |
| --- | --- | --- |
| I01-A1 | `Underwater robots`—`have been increasingly employed`—扩展海洋资源探索与科研能力。 | `including` 列对象类别，`employed to expand` 直接给用途；`human capabilities in` 明确能力及其领域，ROV 使用准确名称 `remotely operated vehicles`。 |
| I01-A2 | `a high-precision controller for underwater robots`—`is required`—保证数据质量及轨迹跟踪／定点保持精度。 | `To exploit ... benefits` 接前句价值，主句给所需控制器；两个平行 `to` 接相应目标，`quality of`、`precision in` 保持各自作用对象。 |

**可模仿表达及作者对应。** `〈领域对象〉 have been increasingly employed to 〈扩展的能力〉 in 〈活动领域〉.`；`To exploit 〈已经说明的收益〉, 〈所需技术，含正确冠词与数〉 is required, such that 〈具体目标〉 can be 〈准确的保证动词〉.` 用作者自己的价值、必要技术和目标建立目的关系。

## 2. 后续段首怎样直接亮出对象、能力或下一项责任

段首让读者立即知道本段讨论什么。P17 常把方法类别或性能对象置于主语位置，用简洁谓语先给能力或依赖关系，再在后续句中具体化。下面的科学对象可按作者内容替换；段首的谓语由本段真正要建立的关系选择。

### E04｜方法对象 → 相关能力 → 另一项能力

P17 I01 已建立运动建模问题，I02 段首直接介绍 DS，并具体说明其表示和抗扰能力。

**P17 I02-S1-S3**；原段跨度：PDF p.1 / 刊页 777 / 右栏；[来源审计定位](../introduction-section-review-2026-10-06/P17-introduction.md#i02)。

**英文学习示例（基于原文的适配）。**

> The dynamic system (DS) is a powerful tool for motion modeling [3]. In comparison to conventional methods, such as interpolation techniques, DS offers a flexible solution to model stable and extensible trajectories. In addition, the motion encoded with the DS is robust to perturbations.

| 示例句位 | 真实主语—动作—对象或补语 | 句式、搭配与用词怎样实现关系 |
| --- | --- | --- |
| I02-A1 | `The dynamic system (DS)`—`is`—`a powerful tool for motion modeling`。 | `is a ... tool for + 名词／-ing` 直接确立本段方法与研究任务。完整术语后给缩写，后续句可以持续使用 DS。 |
| I02-A2 | `DS`—`offers`—`a flexible solution to model stable and extensible trajectories`。 | `In comparison to` 给传统方法这一参照；DS 作主语，`offers a ... solution to` 写表示能力，`stable and extensible` 同时限定轨迹。 |
| I02-A3 | `the motion encoded with the DS`—`is robust`—`to perturbations`。 | `In addition` 增加并列能力；主语从方法切换到它编码的运动。`encoded with` 指定表示手段，`robust to` 指定抗扰对象。 |

**可模仿表达及作者对应。** `〈方法〉 is a 〈有依据的能力修饰〉 tool for 〈本段任务〉.`；`〈方法〉 offers a 〈相关属性〉 solution to 〈具体任务〉.`；`In addition, 〈由该方法产生或表示的对象〉 is robust to 〈扰动或变化〉.` 将“方法有效”落实为作者当前论证需要的能力和对象。

### E17｜整体性能还依赖另一项责任 → 信息条件 → 相应方法

P17 已说明运动生成设计；I06 段首用模仿性能对跟踪精度的依赖进入执行问题，后续句交代准确模型条件、实际不确定性及逼近控制。

**P17 I06-S1-S6**；原段跨度：PDF p.2 / 刊页 778 / 左栏 -> PDF p.2 / 刊页 778 / 右栏；[来源审计定位](../introduction-section-review-2026-10-06/P17-introduction.md#i06)。

**英文学习示例（基于原文的适配）。**

> The imitation performance of robots also depends on the accuracy of the trajectory tracking controller that involves the robot dynamics. Generally, model-based control performs better if the robot dynamic model is accurate enough [19]. However, an accurate dynamic model of a manipulator cannot be obtained in advance due to some uncertainties, e.g., unknown payload. Approximation-based controllers have been designed to overcome uncertainties in the robot dynamics. Approximation-based controllers utilize function approximation tools to learn the nonlinear characteristics of the robot dynamics. NNs have been widely used in controller design because of their approximation ability [20]–[22].

| 示例句位 | 真实主语—动作—对象或补语 | 句式、搭配与用词怎样实现关系 |
| --- | --- | --- |
| I06-A1 | `The imitation performance of robots`—`also depends on`—跟踪控制器的精度。 | `performance of` 明确系统目标；`also depends on` 把下一项责任接回同一目标。`that involves ...` 说明该控制器涉及机器人动力学。 |
| I06-A2 | `model-based control`—`performs better`—在机器人动力学模型足够准确时。 | `Generally` 给概括语境；`if the robot dynamic model is accurate enough` 明确模型身份，保留性能改善所需的精度条件。 |
| I06-A3 | `an accurate dynamic model of a manipulator`—`cannot be obtained`—`in advance`，原因是不确定性。 | `However` 接真实条件差别；`obtained in advance` 写信息可得性，`due to` 接原因，`e.g.` 给未知负载这一具体例子。 |
| I06-A4 | `Approximation-based controllers`—`have been designed`—`to overcome uncertainties in the robot dynamics`。 | 逼近控制器直接接机器人动力学不确定性，`designed to overcome` 使控制职责与前句的信息条件连续。 |
| I06-A5 | `Approximation-based controllers`—`utilize`—函数逼近工具，`to learn` 机器人动力学非线性特征。 | 重复逼近控制器名称；`utilize A to B` 交代工具及职责，`characteristics of the robot dynamics` 保持被学习对象的技术身份。 |
| I06-A6 | `NNs`—`have been widely used`—`in controller design`，因为逼近能力。 | 从方法类进入具体工具；`used in` 接使用环节，`because of` 接选择理由，`approximation ability` 与 A5 的函数逼近对象对应。 |

**可模仿表达及作者对应。** `〈整体性能的准确名称〉 also depends on 〈具体轨迹跟踪控制器及其精度〉.`；`〈模型控制方法的准确名称〉 performs better if the 〈动力学模型的准确名称〉 is accurate enough.`；`The 〈所需动力学模型的准确名称〉 cannot be obtained in advance due to 〈不确定性的具体名称〉.`；`The 〈逼近控制器的准确名称〉 has been designed to overcome 〈同一动力学不确定性的具体名称〉. The 〈同一逼近控制器名称〉 utilizes 〈函数逼近工具的准确名称〉 to learn 〈动力学非线性特征的具体名称〉.` 作者明确性能依赖哪项控制精度、哪个动力学模型在何种条件下可用，以及具体控制器怎样处理同一不确定性。

## 3. 文献句与同一文献续句怎样写出真实能力

优先采用四篇反复出现、作者明确偏好的 `In [xx], ...` 写法：引文定位之后，以具体方法、处理的问题或被利用的信息作主语，写 `was proposed/developed/employed/used/utilized ...`，并接真实任务或作用。P17 的过去时被动是主要参照。具体工作持续影响当前研究时，可以按原文能力关系选择完成时或现在时的成熟实现。

同一文献的续句继续说明刚才的方法、输出、估计对象或计算代价。主语可由“方法”转为“产生的对象”“被估计的信息”或“所改善的指标”，形成实际科学关系。下列各组同时提供这些主语变化及适用的连续句示例。

### E05｜`In [xx]` → `Another study` → 相关工作对比 → 当前研究方向

P17 已说明 DMP 的表示能力，I03 讨论 DMP 的具体学习用途，再由最优示教难得进入多示教整合。

**P17 I03-S1-S6**；原段跨度：PDF p.1 / 刊页 777 / 右栏；[来源审计定位](../introduction-section-review-2026-10-06/P17-introduction.md#i03)。

**英文学习示例（基于原文的适配）。**

> DMPs have often been employed to solve robot learning problems because of their flexibility. In [7], DMPs were modified to model fast movement inherent in hitting motion. Another study used reinforcement learning to combine DMP sequences so that the robot could perform more complex tasks [8]. While the studies in [7] and [8] employed multiple DMPs to compose a complete action, another study [9] used multiple DMPs to model a style-adaptive trajectory. The style of the generated motion could be changed by modulating the weight parameters that were coupled with the goals. The work in [10] indicates that optimal demonstration is difficult to obtain and multiple demonstrations can encode the ideal trajectory implicitly. Therefore, we consider integrating multiple demonstrations into one DMP model in this paper.

| 示例句位 | 真实主语—动作—对象或补语 | 句式、搭配与用词怎样实现关系 |
| --- | --- | --- |
| I03-A1 | `DMPs`—`have often been employed`—`to solve robot learning problems`。 | `employed to solve` 给方法用途；`because of their flexibility` 说明选择理由，`their flexibility` 在同句中保留 DMP 的能力身份。 |
| I03-A2 | `DMPs`—`were modified`—`to model fast movement inherent in hitting motion`。 | `In [7],` 精确定位文献；`modified to model` 区分改动动作与建模目标；`inherent in` 把快速运动限定在击打动作中。 |
| I03-A3 | `Another study`—`used`—`reinforcement learning`，`to combine DMP sequences`。 | 工作作主语的主动变体；`used A to B` 写工具与操作，`so that the robot could perform ...` 紧接具体能力。[8] 位于本句末。 |
| I03-A4–A5 | `the studies in [7] and [8]`—`employed`—多个 DMP；`another study [9]`—`used`—多个 DMP 表示风格可调轨迹；`The style`—`could be changed`—通过目标耦合权值。 | `While` 保持动作组合与轨迹风格的对照。续句让生成运动的风格作主语，用 `by modulating` 和 `coupled with` 写调节手段及权值与目标的联系。 |
| I03-A6 | `The work in [10]`—`indicates`—最优示教难得，多次示教可以隐含编码理想轨迹。 | `The work in [xx] indicates that` 接文献判断；`difficult to obtain` 写可得性，`encode ... implicitly` 写信息能力，二者共同支持下一句的整合方向。 |
| I03-A7 | `we`—`consider integrating`—多次示教进入一个 DMP。 | `Therefore` 根据上句真实信息关系推出方向；`consider + -ing` 接研究选择，`integrate A into B` 明确整合对象和承载模型。 |

**可模仿表达及作者对应。** `In [xx], 〈方法〉 was modified to 〈具体任务〉.`；`Another study used 〈工具〉 to 〈操作〉 so that 〈研究对象〉 could 〈获得的能力〉 [xx].`；`While the studies in [xx] and [yy] employed 〈共同方法的准确名称〉 to 〈任务A〉, another study [zz] used 〈方法的准确名称〉 to 〈任务B〉. The 〈生成运动的风格或属性的准确名称〉 could be changed by 〈调节动作及对象〉.`；`The work in [xx] indicates that 〈已有判断〉. Therefore, we consider 〈由该判断支持的研究选择，-ing〉.` 每个引文对应作者实际读到的那项工作，每个连接词对应这里已建立的共同点、对照点或推论。

### E06｜方法和输入写在文献句中，生成输出由下一句承接

P17 I03 已提出多示教信息整合需要；I04 先给概率编码能力，再用 [14] 的表示和运动生成连续说明这种能力。

**P17 I04-S1-S5**；原段跨度：PDF p.1 / 刊页 777 / 右栏 -> PDF p.2 / 刊页 778 / 左栏；[来源审计定位](../introduction-section-review-2026-10-06/P17-introduction.md#i04)。

**英文学习示例（基于原文的适配）。**

> Probabilistic approaches have shown good performance in motion encoding [11]–[13]. The inherent variability of the demonstrations can be extracted, and thus, more features of the demonstrations can be preserved. In [14], an LfD framework using a Gaussian mixture model (GMM) and a Bernoulli mixture model was used to extract the features from multiple demonstrations. A new motion was generated through Gaussian mixture regression (GMR). In contrast with the DS-based and DMP-based motion-learning methods discussed above, GMM combined with GMR can provide additional motion information for robots when learning from multiple demonstrations.

| 示例句位 | 真实主语—动作—对象或补语 | 句式、搭配与用词怎样实现关系 |
| --- | --- | --- |
| I04-A1 | `Probabilistic approaches`—`have shown`—`good performance in motion encoding`。 | 方法类直接作段首主语；`show performance in` 指定能力领域，引用 [11]–[13] 支撑这一概括。 |
| I04-A2 | `The inherent variability`—`can be extracted`；`more features`—`can be preserved`。 | 从方法名转向被提取的信息；`variability of`、`features of` 指同一示教集合，`and thus` 明确提取与保留之间的作用关系。 |
| I04-A3 | `an LfD framework using ...`—`was used`—`to extract the features from multiple demonstrations`。 | `In [14],` 后用框架作主语，`using` 限定所用模型；`extract A from B` 明确提取对象与信息来源。 |
| I04-A4 | `A new motion`—`was generated`—`through GMR`。 | 同一文献继续以产物为主语，`generated through` 写产生手段；一句就完成表示到运动输出的承接。 |
| I04-A5 | `GMM combined with GMR`—`can provide`—多示教学习中的额外运动信息。 | `In contrast with` 保留前文 DS／DMP 运动学习方法这一比较范围；`combined with` 写组合，`provide A for B` 给信息与使用者，`when learning from multiple demonstrations` 保留情境。 |

**可模仿表达及作者对应。** `In [xx], a 〈框架〉 using 〈模型或工具〉 was used to extract 〈信息〉 from 〈来源〉. 〈输出〉 was generated through 〈生成手段〉.` 续句可参照 `The 〈被利用的信息〉 can be extracted, and thus, 〈需要保留的内容〉 can be preserved.` 作者对应实际信息来源、处理对象与输出；同一文献的两句共用同一个工作范围。

### E07｜命名方法、交代内部职责，再综合共同能力

这一连续组接 E06 的 GMM／GMR 能力，用 SEDS 与 DS-GMR 说明动态系统和概率学习结合的已有依据，后段据此提出当前组合设计。

**P17 I04-S6-S8**；原段跨度：PDF p.1 / 刊页 777 / 右栏 -> PDF p.2 / 刊页 778 / 左栏；[来源审计定位](../introduction-section-review-2026-10-06/P17-introduction.md#i04)。

**英文学习示例（基于原文的适配）。**

> In [3], a learning approach named stable estimator of dynamical systems (SEDS) was proposed for motion modeling. The unknown function in SEDS was modeled using GMR. DS-GMR is another method that combines the DS with the statistical learning approach [15]. Both SEDS and DS-GMR exploit the robustness and generalization capability of the DS as well as the excellent learning performance of the probabilistic methods.

| 示例句位 | 真实主语—动作—对象或补语 | 句式、搭配与用词怎样实现关系 |
| --- | --- | --- |
| I04-A6–A7 | `a learning approach named SEDS`—`was proposed`—`for motion modeling`；`The unknown function in SEDS`—`was modeled`—`using GMR`。 | `In [3], ... named ... was proposed for` 命名方法和任务；续句以 SEDS 中的未知函数作主语，`modeled using` 给 GMR 的建模职责。 |
| I04-A8 | `DS-GMR`—`is another method`—`that combines the DS with the statistical learning approach`。 | `another method that ...` 引入同类工作；`combine A with B` 写组合双方，文献 [15] 紧随该方法能力。 |
| I04-A9 | `Both SEDS and DS-GMR`—`exploit`—DS 的鲁棒／泛化能力及概率方法的学习性能。 | 两个具体方法名称共同作主语；`exploit` 接可利用的能力，`as well as` 连接另一类能力，为组合设计提供依据。 |

**可模仿表达及作者对应。** `In [xx], a 〈方法类别〉 named 〈方法名〉 was proposed for 〈任务〉. The 〈该方法中待建模函数的准确名称〉 was modeled using 〈工具的准确名称〉.`；`〈方法B〉 is another method that combines 〈A〉 with 〈B〉 [xx]. Both 〈方法A的准确名称〉 and 〈方法B的准确名称〉 exploit 〈能力A〉 as well as 〈能力B〉.` 作者的两个相关工作确实共享这些能力时，用这组表达把采用组合设计的依据说具体。

### E08｜以控制结构、被约束的量或被处理的问题作主语

P05 I02 在双臂协调问题下连续给出物体操作、内力控制与负载处理能力。随后才综合牢固抓持条件，见 E15。

**P05 I02-S1-S3**；原段跨度：PDF p.1 / 刊页 1010 / 右栏；[来源审计定位](../introduction-section-review-2026-10-06/P05-introduction.md#i02)。

**英文学习示例（基于原文的适配）。**

> In [9], an adaptive decentralized control scheme was proposed to address the object handling problem of a cooperative robot. An implicit force control scheme was employed to simultaneously regulate the force and position. In [10], a decentralized control structure for multiple mobile manipulators was developed. The internal forces were constrained by employing an augmented object model for the multiple systems with a virtual linkage. In [11], the loading problem for multiple manipulators was addressed by analyzing the grasp space of the robot.

| 示例句位 | 真实主语—动作—对象或补语 | 句式、搭配与用词怎样实现关系 |
| --- | --- | --- |
| I02-A1–A2 | `an adaptive decentralized control scheme`—`was proposed`—处理协作机器人物体操作；`An implicit force control scheme`—`was employed`—同时调节力与位置。 | `In [9], ... was proposed to address` 定位方法与问题。续句 `employed to simultaneously regulate A and B` 补充同一文献的控制机制和两个量。 |
| I02-A3–A4 | `a decentralized control structure`—`was developed`—用于多移动机械臂；`The internal forces`—`were constrained`—通过含虚拟连杆的增广物体模型。 | `In [10]` 后给结构及适用系统。续句让内力作主语，`constrained by employing` 给约束手段，`with a virtual linkage` 保持模型组成。 |
| I02-A5 | `the loading problem for multiple manipulators`—`was addressed`—`by analyzing the grasp space`。 | `In [11],` 后让问题作主语；`was addressed by + -ing` 直接交代解决途径，`grasp space of` 明确分析对象。 |

**可模仿表达及作者对应。** `In [xx], a 〈控制结构的准确名称〉 was developed for 〈系统〉. The 〈同一系统中受控量的准确名称〉 was constrained by employing 〈手段〉.`；`In [xx], the 〈具体问题〉 was addressed by 〈分析或处理动作，-ing〉.`；`In [xx], a 〈方法的准确名称〉 was proposed to address 〈问题〉. A 〈同一工作中控制机制的准确名称〉 was employed to simultaneously regulate 〈量A〉 and 〈量B〉.` 按本段最需要强调的对象选择主语，`proposed`、`developed`、`employed` 分别对应提出、构建和使用。

### E09｜`In [xx], ... has been proposed for ... to ...` 与当前设计职责

Fuzzy I02 围绕瞬态控制需要先给 BLF 约束能力，再用相关文献展示该能力与时间性能的结合，段末给当前对称 BLF 的职责。

**Fuzzy2023 I02-S2-S6**；原段跨度：PDF p.1 / 刊页 1041 / 右栏；[来源审计定位](../introduction-section-review-2026-10-06/Fuzzy2023-introduction.md#i02)。

**英文学习示例（基于原文的适配）。**

> Recently, barrier Lyapunov functions (BLFs) have been widely used to enforce state and output constraints in nonlinear control problems [12]–[16]. In [12], with the exponential-type BLF, a practical event-triggered prescribed-time controller has been proposed for a class of space teleoperation systems. In [14], a new command-filtered fuzzy controller has been proposed for a class of unknown nonlinear systems to handle full-state constraints and finite-time convergence simultaneously. In [16], an adaptive fuzzy leader-following tracking control scheme has been proposed for heterogeneous nonlinear multiagent systems with finite-time output constraints. In this article, a novel symmetric BLF is designed to guarantee the desired transient performance of the robot system.

| 示例句位 | 真实主语—动作—对象或补语 | 句式、搭配与用词怎样实现关系 |
| --- | --- | --- |
| I02-A2 | `barrier Lyapunov functions (BLFs)`—`have been widely used`—约束非线性系统状态与输出。 | `Recently` 给时间背景，`used to enforce` 接状态与输出约束，`in nonlinear control problems` 限定领域。 |
| I02-A3 | `a practical event-triggered prescribed-time controller`—`has been proposed`—`for a class of space teleoperation systems`。 | `In [12], with the exponential-type BLF, ...` 先交代所用工具；方法作主语，`for a class of` 保留适用系统类别。 |
| I02-A4 | `a new command-filtered fuzzy controller`—`has been proposed`—用于未知非线性系统，同时处理全状态约束与有限时间收敛。 | `In [14], ... for ... to handle A and B simultaneously` 写方法、系统范围和联合能力，`command-filtered fuzzy controller` 保留技术身份。 |
| I02-A5 | `an adaptive fuzzy leader-following tracking control scheme`—`has been proposed`—用于异构系统及其有限时间输出约束。 | `In [16], ... for 〈系统〉 with 〈条件或约束〉` 将系统范围与约束放在同一句中。 |
| I02-A6 | `a novel symmetric BLF`—`is designed`—`to guarantee the desired transient performance`。 | `In this article` 明确从已有工作进入当前设计；现在时 `is designed to` 直接写职责，`performance of` 给作用系统。 |

**可模仿表达及作者对应。** `In [xx], with 〈所用工具〉, a 〈方法〉 has been proposed for a class of 〈系统〉.`；`In [xx], a 〈方法〉 has been proposed for 〈系统〉 to handle 〈目标A〉 and 〈目标B〉 simultaneously.`；`In this paper, a 〈作者设计〉 is designed to guarantee 〈有依据的性能〉.` 采用示例的“系统范围＋具体能力”组织，把属性、时态和保证范围换成真实文献与作者设计。

### E10｜同一文献：控制器组合 → 计算负担的改善

ESO I03 已建立 NN 的不确定性逼近能力，这两句继续说明 [7] 的控制组合及其计算作用。

**ESO2017 I03-S6-S7**；原段跨度：PDF p.1 / 刊页 6785 / 右栏；[来源审计定位](../introduction-section-review-2026-10-06/ESO2017-introduction.md#i03)。

**英文学习示例（基于原文的适配）。**

> In [7], an adaptive controller combining NN approximation with dynamic surface control is presented for trajectory tracking of an AUV. The computational load is reduced by introducing an NN learning method using a minimal number of learning parameters.

| 示例句位 | 真实主语—动作—对象或补语 | 句式、搭配与用词怎样实现关系 |
| --- | --- | --- |
| I03-A6 | `an adaptive controller combining NN approximation with dynamic surface control`—`is presented`—用于 AUV 轨迹跟踪。 | `In [7]` 后给控制器，`combining A with B` 限定组合，`presented for` 指任务；`dynamic surface control` 保留该控制技术的准确名称。 |
| I03-A7 | `The computational load`—`is reduced`—通过采用学习参数数目很少的 NN 学习方法。 | 计算指标作主语，`reduced by introducing` 把作用连接手段；`using a minimal number of learning parameters` 给计算作用的具体来源。 |

**可模仿表达及作者对应。** `In [xx], a 〈方法〉 combining 〈A〉 with 〈B〉 is presented for 〈任务〉. The computational load is reduced by introducing 〈承担该作用的设计〉.` 作者替换真实组合、任务及所改善的指标。控制器的功能和计算作用分别落到各自明确的主语上。

### E11｜同一文献：控制方法 → 观察器的两个具体职责

ESO I06 讨论观察器估计未知扰动并支持补偿的能力；这两句说明 [12] 的控制器及其观察器。

**ESO2017 I06-S3-S4**；原段跨度：PDF p.2 / 刊页 6786 / 左栏；[来源审计定位](../introduction-section-review-2026-10-06/ESO2017-introduction.md#i06)。

**英文学习示例（基于原文的适配）。**

> In [12], a sliding mode controller based on a sliding mode observer is proposed for a reusable launch vehicle. The sliding mode observer is presented to estimate the unknown external disturbances and to reduce the control gain.

| 示例句位 | 真实主语—动作—对象或补语 | 句式、搭配与用词怎样实现关系 |
| --- | --- | --- |
| I06-A3 | `a sliding mode controller based on a sliding mode observer`—`is proposed`—`for a reusable launch vehicle`。 | `In [12], ... based on ... is proposed for ...` 给文献、控制器基础与应用系统。 |
| I06-A4 | `The sliding mode observer`—`is presented`—估计未知外扰并降低控制增益。 | 滑模观察器名称接上句同一工具，两个平行 `to` 分别给 `estimate ... disturbances` 和 `reduce ... gain` 的职责。 |

**可模仿表达及作者对应。** `In [xx], a 〈方法〉 based on 〈工具〉 is proposed for 〈系统〉. The 〈同一观察器的准确名称〉 is presented to 〈直接职责〉 and to 〈相应作用〉.` 被估计的量及减小的指标均采用真实工作内容，续句仍属于同一文献。

### E12｜同一文献：方法及问题 → 估计范围的扩充

ESO I06 用 [32] 说明 ESO 的扰动与状态估计能力。这组能力能支持后续未测状态讨论；作者采用时按自己的信息条件连接。

**ESO2017 I06-S6-S7**；原段跨度：PDF p.2 / 刊页 6786 / 左栏；[来源审计定位](../introduction-section-review-2026-10-06/ESO2017-introduction.md#i06)。

**英文学习示例（基于原文的适配）。**

> In [32], backstepping control based on an ESO is proposed to handle mismatched disturbances in hydraulic systems. The ESO estimates not only the model uncertainties but also the unmeasured states.

| 示例句位 | 真实主语—动作—对象或补语 | 句式、搭配与用词怎样实现关系 |
| --- | --- | --- |
| I06-A6 | `backstepping control based on an ESO`—`is proposed`—处理液压系统中的非匹配扰动。 | `In [32]` 定位工作，`based on` 指 ESO 基础，`handle mismatched disturbances in` 保持问题类别与系统范围。 |
| I06-A7 | `The ESO`—`estimates`—模型不确定性和未测状态。 | ESO 名称接同一观察器，主动 `estimates` 给职责；`not only A but also B` 保持两个同层估计对象。 |

**可模仿表达及作者对应。** `In [xx], a 〈方法〉 based on 〈工具〉 is proposed to handle 〈系统问题〉. The 〈同一观察器的准确名称〉 estimates not only 〈对象A〉 but also 〈对象B〉.` 两个对象分别取作者引用工作或当前设计实际估计的量，借此交代估计范围和后续设计所需能力。

### E13｜文献结论 → 信息利用的实现 → 当前设计

P05 已建立权值收敛与激励条件问题，I07 用估计误差信息进入复合学习设计。

**P05 I07-S1-S4**；原段跨度：PDF p.2 / 刊页 1011 / 左栏 -> PDF p.2 / 刊页 1011 / 右栏；[来源审计定位](../introduction-section-review-2026-10-06/P05-introduction.md#i07)。

**英文学习示例（基于原文的适配）。**

> The work in [43] indicates that parameter convergence can be improved if information about the parameter estimation error can be integrated into the parameter adaptation. In [44], a novel parameter estimation law was proposed for a robotic system with unknown dynamics by using a sliding mode technique and a finite-time estimator. In [45], the NN weight estimation error was integrated into the adaptation scheme of a class of nonlinear systems to achieve convergence of the NN weights. We therefore develop a composite learning controller for the dual-arm robot to perform bimanual relative motion tasks.

| 示例句位 | 真实主语—动作—对象或补语 | 句式、搭配与用词怎样实现关系 |
| --- | --- | --- |
| I07-A1 | `The work in [43]`—`indicates`—参数收敛可以在参数估计误差信息进入参数自适应时改善。 | `The work in [xx] indicates that` 给文献判断，`if` 保留改善条件；`information about the parameter estimation error` 和 `integrated into the parameter adaptation` 明确所用信息及其去向。 |
| I07-A2 | `a novel parameter estimation law`—`was proposed`—用于未知动力学机器人，利用滑模及有限时间估计器。 | `In [44], ... was proposed for ... by using A and B` 一句给方法、系统条件及所用技术；`with unknown dynamics` 限定问题范围。 |
| I07-A3 | `the NN weight estimation error`—`was integrated`—进入非线性系统自适应方案以实现 NN 权值收敛。 | `In [45]` 定位工作，被利用的 NN 权值估计误差作主语，`integrated into ... to achieve` 连接信息、去向与权值收敛目标。 |
| I07-A4 | `We`—`therefore develop`—复合学习控制器，供双臂机器人完成相对运动任务。 | `therefore` 接估计误差信息改善学习的依据，`develop A for B to C` 写设计、系统及任务。 |

**可模仿表达及作者对应。** `The work in [xx] indicates that 〈能力或性质〉 can be improved if 〈必要条件〉.`；`In [xx], 〈信息〉 was integrated into 〈设计环节〉 to achieve 〈具体目标〉.`；`We therefore develop 〈复合学习控制器的准确名称〉 for 〈系统〉 to 〈任务〉.` 前句具体的信息利用能力为设计提供理由，作者直接写出相应控制器及任务，保留文献结论、信息类型与设计之间的联系。

## 4. 比较和限制怎样写清能力、条件及设计需要

比较句保持科学对象和维度明确。用条件、信息量、性能依赖、计算指标或任务范围说明相关差别，再把这种差别接回作者的研究需要。下面的 `However`、`In contrast`、`Nevertheless`、`Despite` 各由其后的具体内容实现关系。

### E14｜已有方法 → 作用 → 数据条件 → 另一方法的相应能力

这组接 E04 的 DS 能力，围绕示教量与稳定运动表示比较一个 DS 方法和 DMP。

**P17 I02-S4-S8**；原段跨度：PDF p.1 / 刊页 777 / 右栏；[来源审计定位](../introduction-section-review-2026-10-06/P17-introduction.md#i02)。

**英文学习示例（基于原文的适配）。**

> In [4], an approach based on DS was used to learn human motions. The unknown mapping of the DS was approximated using a neural network (NN) called extreme learning machine [5]. The DS-based motion model learned using extreme learning machine showed adequate stability and generalization. However, the DS-based motion learning approach using extreme learning machine required considerable demonstration data for training. In contrast, the dynamic movement primitive (DMP), which is based on a nonlinear DS [6], only requires one demonstration to model motion. The DMP models the movement trajectory as a spring-damper system integrated with an unknown function to be learned. The inherent property of the spring-damper system enhances the stability and robustness (to perturbations) of the generated motion.

| 示例句位 | 真实主语—动作—对象或补语 | 句式、搭配与用词怎样实现关系 |
| --- | --- | --- |
| I02-A4–A5 | `an approach based on DS`—`was used`—`to learn human motions`；`the unknown mapping of the DS`—`was approximated`—通过 extreme learning machine。 | `In [4],` 后给方法和任务。续句用 DS 的未知映射作主语，`approximated using` 写逼近手段，[5] 定位所用 NN 工具。 |
| I02-A6 | `The DS-based motion model learned using extreme learning machine`—`showed`—`adequate stability and generalization`。 | 主语同时明确运动模型的 DS 身份和学习工具；`showed` 接已有能力，`adequate` 保留该语境下的满足程度。 |
| I02-A7 | `the DS-based motion learning approach using extreme learning machine`—`required`—`considerable demonstration data for training`。 | `However` 从已承认的能力进入训练需求；主语明确同一模型的学习方法，`required A for B` 给数据量和用途。 |
| I02-A8–A9 | `the DMP`—`only requires`—一次示教；`The DMP`—`models`—轨迹为弹簧阻尼系统及待学习未知函数。 | `In contrast` 保持示教量比较；下一句以 DMP 作主语，用 `models A as B integrated with C` 写同一方法的表示组成。 |
| I02-A10 | `The inherent property of the spring-damper system`—`enhances`—所生成运动的稳定性与鲁棒性。 | 主语落到该表示的内在性质；`enhance A of B` 把作用落到生成运动，`robustness (to perturbations)` 明确鲁棒性对象。 |

**可模仿表达及作者对应。** `The 〈已学习运动模型的准确技术名称〉 showed 〈相关能力〉. However, 〈该运动模型学习方法的准确名称〉 required 〈具体资源〉 for 〈用途〉. In contrast, 〈另一运动建模方法的准确名称〉 requires 〈对应资源〉 to 〈同一任务〉.` 解释表示时可参照 `〈运动建模方法的准确名称〉 models 〈运动轨迹的具体名称〉 as 〈动力学表示的准确名称〉 integrated with 〈组成的准确名称〉. The inherent property of the 〈同一动力学表示名称〉 enhances 〈对应运动性能〉.` 用作者引用的真实工作支持能力、资源量与性能关系，分别明确运动模型、学习方法和动力学表示的身份。

### E15｜共同假设 → 实际动作需要 → 下一段研究对象

E08 已写出三项协作控制能力；接续句给牢固抓持条件及表面操作需求，后段据此进入相对运动。

**P05 I02-S4-S5**；原段跨度：PDF p.1 / 刊页 1010 / 右栏；[来源审计定位](../introduction-section-review-2026-10-06/P05-introduction.md#i02)。

**英文学习示例（基于原文的适配）。**

> The adaptive decentralized controller in [9], the decentralized control structure in [10], and the grasp-space analysis method in [11] were developed under the assumption that the object is firmly held by the robotic arms such that no relative motion occurs between the arms and the object. However, in practical applications, such as polishing, grinding, and welding, the robot end-effectors need to operate along the object’s surface. Sliding movements usually occur between the robotic arm and the object in these surface operations [12]–[14].

**P05 I03-S1-S2**；原段跨度：PDF p.1 / 刊页 1010 / 右栏；[来源审计定位](../introduction-section-review-2026-10-06/P05-introduction.md#i03)。

**英文学习示例（原文选取）。**

> In this respect, the coordination control of dual-arm robots with relative motion deserves further investigation. The relative motion is also known as the asymmetric bimanual task.

| 示例句位 | 真实主语—动作—对象或补语 | 句式、搭配与用词怎样实现关系 |
| --- | --- | --- |
| I02-A6 | [9] 自适应分散控制器、[10] 分散结构与 [11] 抓持空间负载方法—`were developed`—在牢固抓持和无相对运动假设下。 | 以具体控制类型及引文共同作主语，`under the assumption that` 保留条件，`such that` 连接牢固抓持与臂／物体之间无相对运动。 |
| I02-A7–A8 | `the robot end-effectors`—`need to operate`—沿物体表面；`Sliding movements`—`usually occur`—在这些表面操作的机械臂与物体之间。 | `However` 对接任务条件，`such as` 给应用。两句分别写末端运动需要和相应滑动，`along`、`between` 保持空间关系，[12]–[14] 定位这组应用。 |
| I03-A1 | `the coordination control of dual-arm robots with relative motion`—`deserves`—`further investigation`。 | `In this respect` 承接刚建立的滑动需要；主语中 `with relative motion` 精确限定研究问题，`deserves further investigation` 直接建立研究需要。 |
| I03-A2 | `The relative motion`—`is also known as`—`the asymmetric bimanual task`。 | 重复上一句对象并给领域命名，`known as` 对应术语身份，使后续文献讨论有明确称谓。 |

**可模仿表达及作者对应。** `〈文献中各控制器的准确名称〉 were developed under the assumption that 〈共同条件〉.`；`However, in practical applications, such as 〈真实任务〉, 〈对象〉 need to 〈实际动作〉, where 〈相关关系〉.`；`In this respect, 〈刚建立的具体问题〉 deserves further investigation.` 作者将所举文献的共同条件与当前任务逐项对应，下一段主语直接接收由此确定的研究对象。

### E16｜时间能力 → 初始条件依赖 → 新方向及其联合能力

Fuzzy I03 已提出快速收敛需要；以下连续句从有限时间方法进入初始条件，再给固定时间及约束相关能力。

**Fuzzy2023 I03-S3-S8**；原段跨度：PDF p.1 / 刊页 1041 / 右栏 -> PDF p.2 / 刊页 1042 / 左栏；[来源审计定位](../introduction-section-review-2026-10-06/Fuzzy2023-introduction.md#i03)。

**英文学习示例（基于原文的适配）。**

> In [17], an adaptive observer-based fuzzy controller has been proposed for a class of strict-feedback nonlinear systems to achieve finite-time convergence. In [18], an adaptive finite-time sliding-mode control scheme has been proposed for a class of nonlinear systems with some matched uncertainties. Nevertheless, for existing finite-time control schemes, the convergence time of the systems is always related to the initial conditions. The initial conditions are sometimes unavailable. To improve the control performance, the fixed-time control schemes have been proposed and applied in the nonlinear control community [20]–[22]. In [20], a novel fixed-time adaptive fuzzy control scheme combined with the BLF technique has been proposed for uncertain nonstrict-feedback nonlinear systems. In [21], an adaptive event-based fixed-time control scheme has been proposed for active vehicle suspension systems. The predefined constraints on the active vehicle suspension systems can be guaranteed.

| 示例句位 | 真实主语—动作—对象或补语 | 句式、搭配与用词怎样实现关系 |
| --- | --- | --- |
| I03-A3 | `an adaptive observer-based fuzzy controller`—`has been proposed`—用于严格反馈系统，实现有限时间收敛。 | `In [17], ... for a class of ... to achieve ...` 给系统类别和能力，`observer-based` 限定方法基础。 |
| I03-A4 | `an adaptive finite-time sliding-mode control scheme`—`has been proposed`—用于含匹配不确定性的非线性系统。 | `In [18], ... for ... with ...` 补同一时间能力的另一方法与系统条件；`matched uncertainties` 是具体技术术语。 |
| I03-A5–A6 | 有限时间方案的 `convergence time`—`is always related to`—初始条件；`The initial conditions`—`are sometimes unavailable`。 | `Nevertheless, for existing finite-time control schemes` 保留方法范围。两句分别写依赖和可得性，重复初始条件名称，限定强度仍是 `always` 与 `sometimes`。 |
| I03-A7 | `the fixed-time control schemes`—`have been proposed and applied`—非线性控制领域。 | `To improve the control performance` 承接所需作用；`proposed and applied` 同时给提出与使用，`in` 限定研究领域。 |
| I03-A8 | `a novel fixed-time adaptive fuzzy control scheme combined with the BLF technique`—`has been proposed`—用于不确定非严格反馈系统。 | `In [20],` 精确定位；`combined with` 修饰方法组合，`for` 保留系统范围，将本段时间需要与前段约束技术相连。 |
| I03-A9–A10 | `an adaptive event-based fixed-time control scheme`—`has been proposed`—用于主动悬架；主动悬架的预设约束—`can be guaranteed`。 | `In [21]` 定位方法，续句以同一系统的约束作主语，`predefined` 保留约束性质，`can be guaranteed` 给相应保证。 |

**可模仿表达及作者对应。** `Nevertheless, for existing 〈方法类〉, 〈具体性能的准确名称〉 is related to 〈条件的准确名称〉. The 〈同一条件名称〉 〈可得性或性质的谓语〉.`；`To improve 〈同一性能目标〉, 〈适用方向〉 have been proposed and applied in 〈领域〉 [xx].` 再用 `In [xx], ... combined with ... has been proposed for ...` 或续句 `The 〈同一系统的具体约束名称〉 can be guaranteed.` 说明所需联合能力。作者给出自己文献范围内的依赖强度、信息条件及保证范围。

### E18｜同一功能的文献对照 → 机制差别 → 采用理由

E17 已从逼近控制进入 NN；这组用两项文献及 RBFNN 的相关能力，说明实时控制工具选择。

**P17 I06-S7-S10**；原段跨度：PDF p.2 / 刊页 778 / 左栏 -> PDF p.2 / 刊页 778 / 右栏；[来源审计定位](../introduction-section-review-2026-10-06/P17-introduction.md#i06)。

**英文学习示例（基于原文的适配）。**

> In [23], the backpropagation NN (BPNN) was utilized to approximate the unknown nonlinear function in the model of the vibration suppression device. In [24], the radial basis function NN (RBFNN) was utilized to approximate the unknown nonlinearity of the telerobot system. In comparison to BPNN, the learning procedure of RBFNN is based on local approximation. Thus, RBFNN can avoid getting stuck in the local optimum and has a faster convergence rate. Besides, the number of hidden layer units of RBFNN can be adaptively adjusted during the training phase. The adaptive adjustment of the number of hidden layer units makes RBFNN more flexible and adaptive. Therefore, RBFNN is more appropriate for the design of real-time control.

| 示例句位 | 真实主语—动作—对象或补语 | 句式、搭配与用词怎样实现关系 |
| --- | --- | --- |
| I06-A7–A8 | `the BPNN` 和 `the RBFNN`—分别 `was utilized`—逼近振动抑制装置与遥操作机器人中的未知非线性。 | 两句分别用 `In [23]` 与 `In [24]` 定位同一功能的文献；`utilized to approximate` 保持方法、系统及各自逼近对象的对应。 |
| I06-A9–A10 | `the learning procedure of RBFNN`—`is based on`—局部逼近；`RBFNN`—`can avoid ... and has ...`—局部最优及收敛速率。 | `In comparison to BPNN` 明确参照。下一句用 `Thus` 和 RBFNN 名称连接局部逼近基础与作用，`local approximation`、`local optimum`、`convergence rate` 保留不同科学身份。 |
| I06-A11–A12 | `the number of hidden layer units of RBFNN`—`can be adaptively adjusted`；该数量的自适应调节—`makes`—RBFNN 更灵活、更具适应性。 | `Besides` 补充能力，`during the training phase` 限定调节阶段。下一句明确以该数量的自适应调节作主语，接相应属性变化。 |
| I06-A13 | `RBFNN`—`is more appropriate`—`for the design of real-time control`。 | `Therefore` 综合刚才的能力；`appropriate for` 写相对当前任务的适用性，把比较收束到工具采用理由。 |

**可模仿表达及作者对应。** `In [xx], 〈工具A〉 was utilized to 〈任务A〉, while in [yy], 〈工具B〉 was utilized to 〈任务B〉.`；`In comparison to 〈参照方法的准确名称〉, the learning procedure of 〈方法的准确名称〉 is based on 〈具体科学基础〉. Thus, 〈同一方法的准确名称〉 〈有依据的作用谓语及对象〉.`；`Besides, the 〈可调量的准确名称〉 in the 〈方法的准确名称〉 can be adaptively adjusted during 〈相关阶段〉. The adaptive adjustment of the 〈同一可调量名称〉 makes the 〈同一方法名称〉 〈对应属性〉.`；`Therefore, 〈方法〉 is more appropriate for 〈当前任务〉.` 作者据自己的证据确定机制、作用和适用条件，保留比较对象及机制与能力、调节与作用的连接。

### E20｜学习途径 → 所能利用的信息 → 效率维度

P17 I05 前两句已给当前多示教组合设计及作用，见 E19；以下用相关学习途径说明采用价值。

**P17 I05-S3-S5**；原段跨度：PDF p.2 / 刊页 778 / 左栏；[来源审计定位](../introduction-section-review-2026-10-06/P17-introduction.md#i05)。

**英文学习示例（基于原文的适配）。**

> In [16], the original DMP was learned using locally weighted regression (LWR). In [17], locally weighted projection regression (LWPR) was employed to optimize the bandwidth of each kernel of LWR. Despite the added complexity of the learning procedure, LWR and LWPR enable the DMP to learn from only one demonstration. Reservoir computing [18] is another method used to approximate the nonlinear function of DMP, but its computing efficiency is less than that of GMR.

| 示例句位 | 真实主语—动作—对象或补语 | 句式、搭配与用词怎样实现关系 |
| --- | --- | --- |
| I05-A5–A6 | `the original DMP`—`was learned`—使用 LWR；`LWPR`—`was employed`—优化 LWR 的核带宽。 | `In [16]` 和 `In [17]` 分别定位学习与带宽优化工作；`learned using`、`employed to optimize` 区分两个工具的责任，`bandwidth of each kernel` 明确被优化量。 |
| I05-A7 | `LWR and LWPR`—`enable`—DMP 从一次示教学得。 | `Despite` 保留学习复杂性这一代价；两个学习工具具名作主语，`enable ... to learn from only one demonstration` 保留能力范围及示教量。 |
| I05-A8 | `Reservoir computing`—`is another method used to approximate`—DMP 的非线性函数；`its computing efficiency`—`is less than`—GMR 的计算效率。 | 函数名称接住同一 DMP 学习对象；`but` 引入效率比较，`its computing efficiency` 与 `that of GMR` 保持明确的技术指标及比较双方。 |

**可模仿表达及作者对应。** `In [xx], the 〈模型的准确名称〉 was learned using 〈工具的准确名称〉. In [yy], 〈另一工具的准确名称〉 was employed to optimize 〈前一工具中被优化量的准确名称〉.`；`Despite 〈已付出的代价〉, 〈学习方法A的准确名称〉 and 〈学习方法B的准确名称〉 enable 〈运动模型的准确名称〉 to 〈能力范围〉.`；`〈方法〉 is another method used to 〈同一任务〉, but its 〈具体指标名称〉 is less than that of 〈参照方法〉.` 作者的比较维度由研究需要与实际文献共同确定。

## 5. 设计怎样出现，并紧接具体作用

理由已经建立后，用 `we integrate/develop/present ...` 或设计作主语的 `is designed/proposed/employed ...` 明确作者采取了什么。紧接它处理的对象、发挥的作用或保证的性质。组合设计沿用 P17 的作者动作与作用关系，作用句以整合后的具体运动模型名称作主语，明确哪项设计使什么成为可能。

### E19｜理由 → 作者动作与组成职责 → 具体作用

前段 E06–E07 已说明概率信息能力与 DS 的鲁棒／泛化能力，这两句将其落实到 DMP、GMM、GMR 组合。

**P17 I05-S1-S2**；原段跨度：PDF p.2 / 刊页 778 / 左栏；[来源审计定位](../introduction-section-review-2026-10-06/P17-introduction.md#i05)。

**英文学习示例（基于原文的适配）。**

> To take advantage of the performance of the DS and the probabilistic approach, we integrate DMP and GMM into our robot learning system. The nonlinear function of DMP is modeled with GMM. The estimate of the nonlinear function of DMP is retrieved through GMR. The DMP motion model integrating GMM and GMR enables the robot to extract more features of the motions from multiple demonstrations and to generate motions that synthesize these features.

| 示例句位 | 真实主语—动作—对象或补语 | 句式、搭配与用词怎样实现关系 |
| --- | --- | --- |
| I05-A1–A3 | `we`—`integrate`—DMP 与 GMM 进入机器人学习系统；`The nonlinear function of DMP`—`is modeled`—用 GMM；同一函数的估计—`is retrieved`—通过 GMR。 | `To take advantage of` 接前文能力，`integrate A and B into C` 写组合。两句接续命名 DMP 非线性函数及其估计，`modeled with` 和 `retrieved through` 分别给建模与回归职责。 |
| I05-A4 | `The DMP motion model integrating GMM and GMR`—`enables`—多示教特征提取与合成运动生成。 | 组合后的具体运动模型作主语，`enables A to B and to C` 写两项相接作用。`extract ... from` 给输入来源，`motions that synthesize these features` 保持输出与同一特征的关系。 |

**可模仿表达及作者对应。** `To take advantage of 〈前文已说明的能力〉, we integrate 〈方法A的准确名称〉 and 〈方法B的准确名称〉 into 〈作者系统的准确名称〉. The 〈待建模非线性函数的准确名称〉 is modeled with 〈建模工具的准确名称〉. The estimate of the 〈同一非线性函数名称〉 is retrieved through 〈回归工具的准确名称〉. The 〈整合后的运动模型的准确名称〉 enables 〈研究对象〉 to 〈作用A〉 and to 〈接续作用B〉.` 作者对应“为什么组合、各自处理什么、组合使什么成为可能”，持续说明同一函数及其估计、输入信息和生成产物。

### E21｜新增设计 → 放宽条件；所用信息 → 改善能力

E13 已用误差信息建立复合学习设计；P05 I07 末两句说明 PPE 与误差信息各承担什么作用。

**P05 I07-S6-S7**；原段跨度：PDF p.2 / 刊页 1011 / 左栏 -> PDF p.2 / 刊页 1011 / 右栏；[来源审计定位](../introduction-section-review-2026-10-06/P05-introduction.md#i07)。

**英文学习示例（基于原文的适配）。**

> Moreover, in contrast to the work in [46], a PPE condition is also introduced in the NN weight estimation scheme to relax the requirement of the PE condition. In comparison to the method in [45], the estimation error of the NN weights is properly expressed and employed to enhance the approximation of the neural network.

| 示例句位 | 真实主语—动作—对象或补语 | 句式、搭配与用词怎样实现关系 |
| --- | --- | --- |
| I07-A5 | `a PPE condition`—`is also introduced`—进入 NN 权值估计方案以放宽 PE 要求。 | `Moreover` 增加设计职责，`in contrast to the work in [46]` 保留比较对象；`introduced in ... to relax` 明确加入位置和条件作用。 |
| I07-A6 | `the estimation error of the NN weights`—`is ... expressed and employed`—增强 NN 逼近能力。 | `In comparison to the method in [45]` 指定参照；误差信息作主语，`expressed and employed to enhance` 把表达、利用和作用相连，`approximation of` 给作用对象。 |

**可模仿表达及作者对应。** `Moreover, 〈新增条件或设计〉 is introduced in 〈环节〉 to achieve a relaxation of 〈已有要求〉.`；`In comparison to the method in [xx], 〈具体信息〉 is expressed and employed to enhance 〈能力〉.` 作者把条件改进与信息利用分清，各句所述作用回到前文已有的需要。

### E22｜设计基础与目的 → 估计对象 → 补充估计职责

ESO 的前文已建立扰动补偿和未测状态估计需要；I08 开头给 MIMO-ESO 设计及其职责。

**ESO2017 I08-S1-S3**；原段跨度：PDF p.2 / 刊页 6786 / 右栏；[来源审计定位](../introduction-section-review-2026-10-06/ESO2017-introduction.md#i08)。

**英文学习示例（基于原文的适配）。**

> In this paper, a disturbance compensation approach based on a multiple-input multiple-output extended state observer (MIMO-ESO) with a simple structure is utilized to eliminate chattering. The ESO model [32] and the high-gain observer [39] motivate the design of the MIMO-ESO. The MIMO-ESO is proposed to estimate the unknown disturbances and the unmeasured states. The bounds of the uncertainties are also estimated using the adaptive control technique.

| 示例句位 | 真实主语—动作—对象或补语 | 句式、搭配与用词怎样实现关系 |
| --- | --- | --- |
| I08-A1 | `a disturbance compensation approach based on ... MIMO-ESO`—`is utilized`—消除抖振。 | `In this paper` 进入当前工作，`based on` 将补偿方法与简单结构的 MIMO-ESO 直接连接，`utilized to eliminate` 给设计目的。 |
| I08-A2–A3 | `The ESO model [32] and the high-gain observer [39]`—`motivate`—MIMO-ESO 设计；`The MIMO-ESO`—`is proposed`—估计未知扰动与未测状态。 | 两个已有方法具名作主语，`motivate the design of` 保留启发关系。续句重复当前观察器名称，`proposed to estimate A and B` 保持估计范围。 |
| I08-A4 | `The bounds of the uncertainties`—`are also estimated`—`using the adaptive control technique`。 | 从观察器切换到补充估计量；`bounds of` 保留估计的是界，`also` 加另一职责，`using` 给采用的手段。 |

**可模仿表达及作者对应。** `In this paper, a 〈设计的准确名称〉 based on 〈基础工具的准确名称〉 is utilized to 〈有依据的目的〉.`；`The 〈已有方法A的准确名称〉 [xx] and the 〈已有方法B的准确名称〉 [yy] motivate the design of the 〈作者观察器的准确名称〉. The 〈同一观察器名称〉 is proposed to estimate 〈对象A〉 and 〈对象B〉. The 〈补充量〉 are also estimated using 〈相应技术〉.` 作者按自己真正需要估计的状态、扰动或界填写，明确已有方法的启发关系及当前观察器的估计职责，并使目的动词与实际证据强度一致。

### 设计句与作用句的直接调用

E13 的 `we develop ... for ... to ...` 对应已建立的信息利用理由；E09 的 `is designed to guarantee ...` 将设计与单项性能职责写在一句；E19 以整合后的运动模型名称接 `enables ...`，紧接组合设计的作用；E22 以具体观察器及被估计的量作后续主语继续说明职责。选择这些实现时，先明确作者的动作、功能对象与作用，再按需要组合“设计句＋作用句”或单句中的设计与作用。

## 6. 多个设计怎样通过主语和输入输出连接

让组成、职责、产物和接收者在英文中明确对应。先给跟踪设计与稳定性，再用 `consists of` 明确系统组成。后续句直接写运动生成模块、运动模型、关节空间轨迹、轨迹跟踪模块及自适应控制器的具体名称，使跟踪控制接收运动生成产生的同一轨迹。

### E23｜控制职责 → 保证 → 系统组成 → 前一部分输出 → 后一部分接收

E17–E18 已建立轨迹执行与 NN 选择理由；I07 给当前控制器，再将其连接到已有运动生成设计。

**P17 I07-S1-S5**；原段跨度：PDF p.2 / 刊页 778 / 右栏；[来源审计定位](../introduction-section-review-2026-10-06/P17-introduction.md#i07)。

**英文学习示例（基于原文的适配）。**

> In this paper, an NN-based controller is designed to guarantee the tracking performance of the manipulator in joint space. RBFNN is employed in the NN-based controller to approximate the nonlinear functions of the robot dynamics. The stability of the NN-based controller is guaranteed by the Lyapunov stability theory. The robot learning system consists of the motion generation component and the trajectory tracking component (Fig. 1). The motion generation component utilizes the DMP-based motion model to learn and generalize motion skills. The motion skills learned and generalized using the DMP-based motion model are represented as a set of trajectories in joint space. The trajectory tracking component employs the adaptive controller to track the joint-space trajectories generated by the motion generation component. RBFNN is incorporated into the adaptive controller to compensate for the uncertain robot dynamics.

| 示例句位 | 真实主语—动作—对象或补语 | 句式、搭配与用词怎样实现关系 |
| --- | --- | --- |
| I07-A1–A2 | `an NN-based controller`—`is designed`—保证机械臂关节空间跟踪性能；`RBFNN`—`is employed`—逼近机器人动力学非线性函数。 | `In this paper` 进入当前设计，`designed to guarantee` 写职责，`in joint space` 给范围。续句明确 RBFNN 在同一控制器中的函数逼近职责。 |
| I07-A3 | `The stability of the NN-based controller`—`is guaranteed`—`by the Lyapunov stability theory`。 | 性质主语保留 NN 控制器身份，`stability of` 接同一设计，`guaranteed by` 给理论依据。 |
| I07-A4 | `The robot learning system`—`consists of`—运动生成与轨迹跟踪模块。 | 系统名称直接作主语，`consists of A and B` 写组成；框架图定位附在句末，后文继续用具体模块名称连接职责。 |
| I07-A5–A6 | `The motion generation component`—`utilizes`—DMP 模型以学习和泛化技能；同一 DMP 模型学得并泛化的运动技能—`are represented`—为关节空间轨迹。 | 两句分别命名模块与运动技能，`utilizes ... to learn and generalize` 给职责，`represented as` 接技能表示和轨迹输出。 |
| I07-A7–A8 | `The trajectory tracking component`—`employs`—自适应控制器以跟踪生成模块产生的关节空间轨迹；`RBFNN`—`is incorporated`—进入同一控制器以补偿不确定动力学。 | 跟踪模块接同一关节空间轨迹，`generated by` 命名来源。续句 `incorporated into ... to compensate for` 保持工具、控制器及补偿对象的连接。 |

**可模仿表达及作者对应。** `〈系统〉 consists of 〈运动生成模块的准确名称〉 and 〈轨迹跟踪模块的准确名称〉. The 〈同一运动生成模块名称〉 utilizes the 〈运动模型的准确名称〉 to learn and generalize 〈运动技能的具体名称〉. The 〈同一运动技能名称〉 are represented as 〈关节空间轨迹的具体名称〉. The 〈轨迹跟踪模块的同一名称〉 employs the 〈自适应控制器的准确名称〉 to track the 〈同一关节空间轨迹名称〉 generated by the 〈运动生成模块的同一名称〉. The 〈逼近工具的准确名称〉 is incorporated into the 〈同一自适应控制器名称〉 to compensate for 〈不确定动力学的具体名称〉.` 理论性质可接 `The 〈性质〉 of the 〈设计的准确名称〉 is guaranteed by 〈依据〉.` 作者保持模块、模型、技能、轨迹与控制器的身份明确，逐句连接学习、表示、生成、跟踪及补偿。

## 7. 过渡和贡献怎样用具体对象收束

过渡表达承接已经明确的科学信息：E05 先用 `The work in [xx] indicates that ...` 写信息依据，再用 `Therefore` 接研究选择；E15 的 `In this respect` 接相对运动问题，E17 的 `also depends on` 接执行责任，E19 的 `To take advantage of` 接两类能力，E23 用具体运动技能和关节空间轨迹名称连接技能与表示。贡献段继续用这些已建立的对象与职责说清总体作用。

### E24｜总体框架 → 指定模型比较 → 增补职责 → 实际作用

P17 前文已把多示教运动生成和未知动力学下的执行连接起来；I08 回收这两项责任。

**P17 I08-S1-S5**；原段跨度：PDF p.2 / 刊页 778 / 右栏；[来源审计定位](../introduction-section-review-2026-10-06/P17-introduction.md#i08)。

**英文学习示例（基于原文的适配）。**

> We present a novel and complete robot learning framework that considers the performance of both motion generation and trajectory tracking. The SEDS presented in [3] is similar to our DMP-based model. However, the constraints that guarantee the stability of SEDS are derived by the Lyapunov theory. The Lyapunov-derived stability constraints of SEDS increase the complexity of learning the SEDS motion model. In contrast to [3] and [25] which considered only motion modeling, our robot learning system is enhanced by an NN-based controller. The effect of dynamic environments on the robot can be compensated by neural learning. The robot learning framework integrating motion generation and NN-based trajectory tracking enables the robot to perform the learned motions steadily and more robustly in the real world.

| 示例句位 | 真实主语—动作—对象或补语 | 句式、搭配与用词怎样实现关系 |
| --- | --- | --- |
| I08-A1 | `We`—`present`—同时考虑运动生成和跟踪性能的完整机器人学习框架。 | `We present` 直接给总体工作，`framework that considers the performance of both A and B` 明确两项责任范围。贡献强度按作者证据选择。 |
| I08-A2 | `The SEDS presented in [3]`—`is similar`—`to our DMP-based model`。 | `presented in [xx]` 定位方法；`similar to` 明确所比对象，使后续条件讨论围绕同一模型。 |
| I08-A3–A4 | SEDS 稳定性约束—`are derived`—通过 Lyapunov 理论；同一约束—`increase`—SEDS 运动模型的学习复杂性。 | `However` 进入 SEDS 条件，两句分别交代约束依据及学习代价。约束与运动模型均保留 SEDS 身份，使理论条件与作用对象连续。 |
| I08-A5–A6 | `our robot learning system`—`is enhanced`—由 NN 控制器增补；动态环境对机器人的影响—`can be compensated`—通过神经学习。 | `In contrast to [3] and [25]` 保留仅考虑运动建模的指定范围。两句分别用 `enhanced by` 写控制增补、`compensated by` 写相应环境影响的补偿来源。 |
| I08-A7 | 整合运动生成与 NN 轨迹跟踪的机器人学习框架—`enables`—机器人稳定、稳健地执行学得运动。 | 完整框架名称接 `enables ... to perform`，`steadily`、`more robustly` 修饰运动执行，`in the real world` 给作用场景，回收生成与跟踪两项责任。 |

**可模仿表达及作者对应。** `We present a 〈框架的准确名称〉 that considers the performance of both 〈责任A〉 and 〈责任B〉.`；`In contrast to [xx] and [yy] which considered 〈真实比较范围〉, the 〈系统的准确名称〉 is enhanced by the 〈增补控制器的准确名称〉. The 〈相应环境影响的具体名称〉 can be compensated by 〈学习或控制机制的准确名称〉. The 〈同一学习框架名称〉 enables 〈对象〉 to perform 〈原研究任务〉 〈有依据的执行方式〉.` 作者的贡献通过覆盖范围、设计职责和最终作用回收前文，保留指定工作的比较范围及补偿与运动执行之间的联系。

### E25｜研究目标 → 贡献引导 → 各项设计及作用

P05 已建立相对运动任务、未知动力学、权值学习信息与激励条件需要，结尾逐项回收。

**P05 I08-S1-S2**；原段跨度：PDF p.2 / 刊页 1011 / 右栏；[来源审计定位](../introduction-section-review-2026-10-06/P05-introduction.md#i08)。

**英文学习示例（原文选取）。**

> The objective of this article is to develop a control framework for dual-arm robot tracking control under relative motion. The main contributions of this article can be summarized as follows.

**P05 C1-S1**；原段跨度：PDF p.2 / 刊页 1011 / 右栏；[来源审计定位](../introduction-section-review-2026-10-06/P05-introduction.md#c1)。

**英文学习示例（原文选取）。**

> 1) A novel neural control framework is developed for dual-arm robot systems to perform asymmetric bimanual tasks with no prior knowledge of the dynamics.

**P05 C2-S1**；原段跨度：PDF p.2 / 刊页 1011 / 右栏；[来源审计定位](../introduction-section-review-2026-10-06/P05-introduction.md#c2)。

**英文学习示例（基于原文的适配）。**

> 2) A novel composite learning algorithm is designed for NN weight adaptation. The composite learning algorithm allows information about the NN weight estimation errors to be appropriately integrated into the NN weight adaptation law to improve estimation performance.

**P05 C3-S1**；原段跨度：PDF p.2 / 刊页 1011 / 右栏；[来源审计定位](../introduction-section-review-2026-10-06/P05-introduction.md#c3)。

**英文学习示例（基于原文的适配）。**

> 3) A partial persistent excitation condition is introduced for NN weight adaptation such that the requirement of the conventional PE condition can be greatly relaxed.

| 示例句位 | 真实主语—动作—对象或补语 | 句式、搭配与用词怎样实现关系 |
| --- | --- | --- |
| I08-A1 | `The objective of this article`—`is to develop`—双臂相对运动跟踪控制框架。 | `objective ... is to + 动词` 清楚给研究目标；`framework for` 指服务任务，`under relative motion` 保留任务条件。 |
| I08-A2 | `The main contributions of this article`—`can be summarized`—`as follows`。 | 直接从目标进入贡献列项；`summarized as follows` 引导随后真实贡献。 |
| C1-A1 | `A novel neural control framework`—`is developed`—用于双臂系统，完成非对称任务。 | `developed for ... to perform ... with ...` 依次说明系统、任务与信息条件；`no prior knowledge of the dynamics` 对应前文未知动力学需要。 |
| C2-A1–A2 | `A novel composite learning algorithm`—`is designed`—用于 NN 权值自适应；同一算法—`allows`—估计误差信息进入权值自适应律以改善估计。 | 设计句给用途，续句重复复合学习算法名称，`allows ... to be integrated into ... to improve` 保留信息、去向和估计作用。 |
| C3-A1 | `A partial persistent excitation condition`—`is introduced`—用于 NN 权值自适应；传统 PE 要求—`can be greatly relaxed`。 | `introduced for` 给作用环节，`such that` 接条件改善；`partial persistent excitation` 使用与前文 PPE 一致的完整技术名称。 |

**可模仿表达及作者对应。** `The objective of this paper is to develop 〈设计〉 for 〈研究任务〉 under 〈相关条件〉. The main contributions of this paper can be summarized as follows.` 贡献句可直接参照 `A 〈设计〉 is developed for 〈系统〉 to perform 〈任务〉 with 〈信息条件〉.`；`A 〈算法〉 is designed for 〈环节〉 such that 〈信息〉 can be integrated into 〈信息去向〉 to improve 〈对应性能〉.`；`A 〈条件〉 is introduced for 〈环节〉 such that the requirement of 〈已有条件〉 can be relaxed.` 内容、修饰强度及列项数量来自作者实际贡献。

### E26｜设计 → 可保证的性质 → 假设改善；最后保留性质范围

Fuzzy 的前文已经建立瞬态约束和收敛时间两项需要，这组贡献分别说明 BLF、自适应律与实用固定时间性质。

**Fuzzy2023 C1-S1**；原段跨度：PDF p.2 / 刊页 1042 / 左栏；[来源审计定位](../introduction-section-review-2026-10-06/Fuzzy2023-introduction.md#c1)。

**英文学习示例（基于原文的适配）。**

> 1) A novel symmetric BLF is designed to avoid violation of the output constraints. Thus, the desired transient performance of the robot system can be guaranteed.

**Fuzzy2023 C2-S1-S2**；原段跨度：PDF p.2 / 刊页 1042 / 左栏；[来源审计定位](../introduction-section-review-2026-10-06/Fuzzy2023-introduction.md#c2)。

**英文学习示例（基于原文的适配）。**

> 2) A novel adaptive law for fuzzy weight estimation is proposed such that the boundedness of all the closed-loop signals can be proved. Then, the assumption that fuzzy weight estimates are bounded in recent fixed-time control research [23]–[25] can be relaxed.

**Fuzzy2023 C3-S1**；原段跨度：PDF p.2 / 刊页 1042 / 左栏；[来源审计定位](../introduction-section-review-2026-10-06/Fuzzy2023-introduction.md#c3)。

**英文学习示例（基于原文的适配）。**

> 3) Robot tracking can achieve practical fixed-time convergence regardless of the initial conditions.

| 示例句位 | 真实主语—动作—对象或补语 | 句式、搭配与用词怎样实现关系 |
| --- | --- | --- |
| C1-A1–A2 | `A novel symmetric BLF`—`is designed`—避免输出约束被违反；期望瞬态性能—`can be guaranteed`。 | `designed to avoid violation of` 写职责，后续完整句以 `Thus` 连接相应性能保证，系统范围保持为同一机器人。 |
| C2-A1 | `A novel adaptive law for fuzzy weight estimation`—`is proposed`；全部闭环信号的有界性—`can be proved`。 | 自适应律名称明确模糊权值估计职责；`proposed such that` 接闭环信号有界性，`all` 保留证明对象的范围。 |
| C2-A2 | `the assumption that fuzzy weight estimates are bounded`—`can be relaxed`。 | `Then` 将闭环有界性接到假设改善，具体命名模糊权值估计量，`in ... research [23]–[25]` 保留指定文献范围。 |
| C3-A1 | `Robot tracking`—`can achieve`—实用固定时间收敛，不依赖初始条件。 | 跟踪任务作主语，`practical fixed-time convergence` 保留完整性质范围，`regardless of the initial conditions` 回收时间性能需要。 |

**可模仿表达及作者对应。** `A 〈设计的准确名称〉 is designed to 〈直接职责及对象〉. Thus, the 〈对应性能的准确名称〉 of the 〈系统的准确名称〉 can be guaranteed.`；`A 〈自适应律的准确名称〉 is proposed such that the boundedness of 〈精确的信号范围〉 can be proved. Then, the assumption that 〈被证明所支持的假设〉 in 〈指定工作〉 can be relaxed.` 收敛作用句保留作者真实的性质名称、限定词与条件关系，表达设计与理论贡献的连续联系。

## 按作者科学内容选择、组合和调整

先从作者已经确定的科学主线和段落任务明确当前句要完成什么，再选择同一关系的英文实现。领域价值参照 E01–E03；后续段首参照 E04、E06、E17；具体文献优先参照 E05–E09、E13、E18 的 `In [xx], ...`；同一文献续句参照 E06、E10–E12、E14；条件与比较参照 E14–E16、E18、E20；设计紧接作用参照 E13、E19、E22；组成和接口参照 E23；贡献收束参照 E24–E26。每组按需要读取其连续示例和分析。

主语选择跟随当前科学重点：方法作主语写采用与能力，信息或问题作主语写处理对象，输出作主语写生成结果，性能作主语写作用或保证，`we` 作主语写作者设计动作。动作与对象一起选择，例如 `extract features from demonstrations`、`approximate nonlinear functions`、`compensate for uncertain dynamics`、`relax a requirement` 都在相应连续句中给出了具体搭配与适用关系。

承接句优先重复准确的科学名称：同一观察器名称接其估计职责，两个具体方法名称接共同能力，整合后的运动模型名称接其作用，运动生成模块与轨迹跟踪模块名称接各自职责和同一轨迹。较短表达在保留技术身份与作用清晰时使用，例如同句中的 `its computing efficiency` 与 `that of GMR` 已明确比较的是计算效率。作者填入自己的科学内容后，继续保持对象、方法、信息、条件、输入输出和作用之间的准确对应，使成熟英文直接承载作者的研究。

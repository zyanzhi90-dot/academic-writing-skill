# 独立审查的识别、漏检与误报评价

本文件在审查完整首次输出保存之后形成。审查端未获得此评价、上轮 coordinator 评价、上轮 Polishing 输出或已知 failure。原样报告见 [first-output.md](../review/first-output.md)，逐句跨阶段证据见 [comparison-evidence.json](comparison-evidence.json)。这里不修改首稿、审查报告或历史结论。

**一次独立审查执行完成。审查具有局部真实问题识别能力，但未达到按完整作者要求准确识别首稿问题的目标：两项已经确认的表达冲突仍漏检。** 本次不是自主生成或润色，不计为自主写作通过。

## 首次报告实际完成了什么

审查报告开篇判断科学主线基本成立，提出两个局部问题：第3段末句的梯度量名精度，以及第5段“训练目标学习”的动作承担者。它给出原句、段落／文件行号、事实编号和技术解释；随后逐组解释整节推进、已有能力、训练比较范围、执行／视觉合段、架构条件、验证数字和引用身份。没有给出替换句、修改稿或要求作者填补虚构事实，也没有要求固定段数、每段 gap 或禁止实验内容。

位置对应原样 current-draft.md 的8个英文正文段落，第3段在第5行，第5段在第9行。审查报告中的临时目录链接保持原样；可长期核验的同字节副本为 [review/materials/inputs/current-draft.md](../review/materials/inputs/current-draft.md)。没有修补首次报告的链接或文字。

## 报告问题是否成立

### 学习动作承担者：明确的真实问题，正确识别

Writing P05-S02–S03：

> The network is trained to predict noise added to demonstration actions, with observations supplied as conditions. This objective learns the score gradient of the conditional action distribution.

前句由网络接受训练、预测噪声，后句把学习动作赋给 objective。F02 区分加噪、网络预测和策略学习；目标规定训练任务，不能在这里替代学习主体。审查准确指出的是连续句中的科学职责错位，而没有声称扩散训练机制本身错误。

P17 I05（PDF p.2／刊页778）先说明 DMP 的非线性函数由 GMM 建模、其估计通过 GMR 获得，再给组合的运动作用。当前 E19 的正向适配用具名函数、估计和组合运动模型承担各自动作，E23 同样分别命名生成模块、输出轨迹和接收模块。该适配已标明基于原文，不冒充出版原句。本次审查援引 E19/E23 的对象—职责关系有依据。

上轮 Polishing P05-S02 已将该句写为 “The action-denoising network learns the score gradient of the conditional action distribution by predicting noise added to demonstration actions.” 这份后续稿没有进入本次审查；它与独立审查结果相互支持局部学习职责问题，但不能证明旧润色会话如何在内部发现或修改。

### distribution gradient：有依据的精度提示，不能升级为错误科学机制

Writing P03-S06：

> The difficulty of estimating this term motivates an alternative that directly learns the distribution gradient without the corresponding negative sampling.

F02 写得分梯度，B06 明确对数密度梯度；P04-S02 也写 “log-density gradients”。对概率密度与其对数密度取梯度不是同一数学量，归一化常数能否消去与这一对象有关，因此审查要求辨明量名有技术依据。报告还明确表示后文可恢复意图，没有据此判定作者实际学习错误梯度，这个限制合理。

但 B05 自身也采用“直接学习分布梯度”的简写，作者输入没有把每次使用这个短称规定为错误。原稿的上下文支持得分学习。因此该项记录为**合理的量名精度提示**，不据单个短语判定明确的科学错误，也不把它当作新增强制作者规则。若把此提示升级为“作者算法错误”或“所有类似短称必改”，会超出证据；首次报告没有作这样的升级。

上轮 Polishing P03-S06 仍用 distribution gradient，说明这个提示不局限于首稿；上轮评价没有单独记录这一提示。本次作为补充观察保存，不改写原测试评价。

## 确定漏检

### 学习路线开句：作者风格要求未用于实际判定

Writing P01-S01–S03：

> Robot manipulation is an important means of automating physical tasks that require precise handling of objects. Learning from demonstrations provides a route to acquiring manipulation skills from human examples. Behavior cloning formulates this learning problem as supervised prediction of actions from observations and has produced effective policies for real-robot manipulation [1].

第一句已经实现领域价值入口，不应再误报“从学习路线开篇”。问题在第二句的 Learning 动名词开句，不是科学事实或普通语法错误。当前已返回的 scientific-expression 明确要求普通科学主体与有限动词，并排除动名词开句；作者要求具体表达按成熟主语、动作、对象来实现。

P17 I01 的出版句为 “Robot learning from demonstration (LfD) is a valuable technique to simplify the strategy of robot learning [1], [2].”（PDF p.1／刊页777）。它命名学习技术再说明价值，并不是以 Learning 行为开句。当前 P17 I01 完整段落、E01–E03 和对象分析均已实际返回。本次报告却只肯定首段组织，没有把科学主线正确与具体表达符合作者偏好分开判定，也没有报告该句。

上轮 Polishing P01-S02 仅把 provides 换成 offers，保留同一开句。单独审查仍漏检这个类别，是新增的可观察诊断证据，不是从旧会话隐藏检查推导出来的结论。

### 联合生成作用主体：有先行词不等于技术身份保留

Writing P05-S05–S06：

> The diffusion representation accommodates multimodal, high-dimensional action distributions without specifying a fixed number of action modes. It therefore allows temporally correlated actions to be predicted jointly.

前句明确扩散表示及分布表达能力；后句给未来动作联合生成作用，但 It 不保留表示／模型的技术类别和该作用责任。scientific-expression 要求短称自身保留技术身份与作用，不能仅凭存在先行词认为达标。科学含义在上下文中能被读者恢复，不能代替作者所要求的英文实现。

P17 I05／E19 的当前正向适配连续句包括：

> The nonlinear function of DMP is modeled with GMM. The estimate of the nonlinear function of DMP is retrieved through GMR. The DMP motion model integrating GMM and GMR enables the robot to extract more features of the motions from multiple demonstrations and to generate motions that synthesize these features.

这组句子保留函数、估计、组合模型及其动作责任；E23 用具名模块接同一轨迹。同一源段的科学内容不能成为作者事实，适用的是持续命名作用主体的表达关系。审查能够发现 objective 学习职责错位，说明它并非完全不能判断科学主体；但未把相同作者要求落实到这个意义可恢复却身份缺失的作用句。

上轮 Polishing 将 predicted 换成 generated，仍保留 It。本次审查再次没有报告这个构造。报告援引 E19/E23 解释其他问题，不能当作这一连续句也已有效复核。

上述两项都是原稿中的遗漏。本次没有提供上轮 Polishing 新增的 “Directly learning…” 开句，故其未被报告**不算本次漏检**。上轮 “This design reduces…” 当前含设计类别和紧接的视觉计算职责，也不机械追加为漏检。

## 合理变体与误报核对

审查对完整稿件作出的下列正向判断有实际依据：

| 范围 | 原稿及作者依据 | 协调端判断 |
| --- | --- | --- |
| P01–P05 整节推进 | 价值→动作表示与时间需要；显式和隐式两条能力／条件分别建立设计理由；扩散研究位置后汇合本文设计。 | 科学任务成立，不固定段数或要求所有需要在下一段立刻解决；不能由此宣称这些段落每句表达都符合偏好。 |
| P02 文献能力及续句 | RNN-GMM 使用历史、混合分量表示多模态；Behavior Transformer 类别加偏移，均承认时间上下文；逐步切换用 can。B01–B04 支持这些关系。 | 没有虚构“不支持多模态／历史”的缺陷。对应 P17 I04（pp.1–2／777–778）的同文献续句和 P05 I02（p.1／1010）的能力→条件组织。 |
| P03–P05 能力与比较 | IBC 的视觉／高维／毫米级真实接触能力仍在；扩散规划、离线强化学习与同期模仿不是本文首创；训练稳定性限定为本研究比较。 | 科学范围合理，不补造闭环稳定定理。Fuzzy I02–I03（pp.1–2／1041–1042）可供不同目标分别建立需要的组织借鉴，不引入其 BLF/固定时间事实。 |
| P06 执行和视觉合段 | 长预测／短执行／新观测、一次编码与复用共同解释连续执行和计算条件，F04–F05 支持。 | 合段不是确定结构错误；ESO I03（p.1／6785）的计算负担→设计作用可作关系补充。实时支持作用不等于无条件延迟保证。 |
| P07 架构条件 | 替代架构、部分快速变化／速度任务、CNN易用、Transformer调参敏感，F06/C03支持。 | 条件保留，无普遍优越或串联组件误报。 |
| P08 贡献与验证 | 46.9%为仿真所列指标相对改善及逐指标最佳变体条件，实机95%为CNN的20次试验，未混入扰动演示。 | 最新调整允许正常科学论证选材，不恢复旧实验排除规则；“任务／数字出现”不算错误。 |
| 引用与短称 | [1]–[9]对应 citation-facts；k排版差别无科学影响。形式主语 It is necessary 与作用主语 It 不同；Direct score learning 是技术名词短语。 | 不按机械禁词表误报。允许保留技术身份和作用明确的短称。 |

首次报告提出的两个事项未发现确定误报；梯度提示的证据等级需保持上述限定。报告“目前没有必须由作者澄清的科学冲突”是对输入可判断性的陈述，并不等于作者表达已符合。不能因为漏检存在就否定它全部正向判断，也不能用正向判断覆盖漏检。

## 实际返回、公开判断及失效位置

本次实际返回比上轮两阶段更加完整：hub、整节六项、段落九项、表达26项的全部非空上下文、英文和分析表都返回。科学表达核心 item_9 全文返回；段落读取在 item_19/23/24，表达读取在 item_20/25–28，hub 在 item_16。没有读取总卡片文件，没有带入其他 section 出版英文或冲突 generic 指令，也没有额外读取出版源文件。详见 [loading-summary.json](../loading-summary.json)、[context-evidence.json](../context-evidence.json) 和完整 events。

“返回全部”证明材料进入上下文，不能证明逐项应用或正确判定。公开 item_22 重点说明设计理由、相邻因果和数字范围；item_40 明确将两个局部科学对象问题作为报告重点；item_41 首次完整交付只报告这两项。能确认的失效位于**单独审查的适用判定、问题识别或最终报告**，不是这次生成替换文本的阶段，因为本次根本没有改稿。没有隐藏推理记录可以继续区分“没有注意”“判断为合理变体”或“注意后没有写入报告”。

## 下一步修改证据支持到哪里

证据支持把下一步定位重点放在现有机器人 Introduction 复核中的**作者表达要求适用判断与原句保留判断**，最贴近的既有接点是共享 `robotics-introduction-examples.md` 的 Use during Polishing 及它与角色 intro fragment／scientific-expression 的实际复核衔接。它们已要求对保留句核对科学主体、有限动作和作用关系；本次需要解决的是语义可恢复、普通语法成立的句子如何仍按有效作者偏好判为表达问题，而不是新增同义禁令或更长范例库。

当前证据不支持继续改三层正向材料、总索引读取路由、generic 隔离、实验信息规则或其他 section。也不支持只优化润色替换后检查：未发生替换的独立审查已漏检，说明识别／保留判断本身也需要关注。objective 问题可识别且上轮可修，保留它所体现的有效主体—职责判断很重要，不能扩展成禁止所有短称的补丁。

这是下一步的修改**位置与目标依据**，不是本轮实施方案；本轮没有改候选。仍无法确定：哪一种最小改动能让自主决策稳定生效；问题究竟未被识别还是未被报告；独立审查与内嵌润色复核有多大机制差异；单次完整返回是否带来注意负担；这种表现是否能迁移到其他研究。一个 review 调用不能验证这些原因，也不能证明旧会话隐藏检查完全未做。

本轮终态：局部识别成功，作者偏好下两项真实表达问题漏检，完整审查目标未通过；无明确误报、无改稿、无反馈重跑。保留全部首次记录并提交同步后停止，不覆盖原 E04，不记自主写作、迁移或稳定性通过。

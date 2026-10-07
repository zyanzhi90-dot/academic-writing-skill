# E04 首次全文评价：Writing 与 Polishing

本评价在两阶段完整首次输出保存之后进行，仅判断本次原样全文。候选冻结于 `447c0c4165afb7fdc08a0458d534042a8704dc94`；没有反馈重跑、挑选结果或协调端修稿。句位沿用 [output-index.json](output-index.json)，完整原文分别见 [Writing](../drafting/first-output.md) 和 [Polishing](../polishing/first-output.md)。索引是只读定位，词形计数不作为质量判据。

## 分阶段判断

| 项目 | Writing 首次输出 | Polishing 首次输出 |
| --- | --- | --- |
| 科学忠实与文献身份 | 本次全文核对对齐；未确认科学事实、职责、条件或引文身份错误。 | 本次全文核对对齐；新增训练波动及数值证据均有作者材料支持，未确认新增科学错误。 |
| 整节、段落与连续句推进 | 领域价值→学习需要→显式表示能力与条件→隐式策略及梯度路线→已有扩散工作与本文→序列／执行→视觉计算→架构选择→贡献，八段连贯。 | 将生成基础集中到 P04、本文生成与执行集中到 P05，八段仍沿相同需要推进；保留并加强能力、条件及作用联系。 |
| 成熟具体英文 | 真实文献句及续句、条件与设计、设计与作用、输入输出承接均有适用正向范例对应。 | 保留已有适用实现，调整主语、对象名称和连续职责；未确认新增作者偏好冲突。 |
| 中文与实际参考文献 | 八段译文保留英语事实与范围，九条正文引用对应 R1–R9。 | 八段译文保留包括 46.9% 口径及 95% 试验范围在内的英语含义，九条引用身份不变。 |

协调端对本次已核对全文的判断是两阶段均对齐，未确认需要修稿的阻塞 failure。这是本例首次输出的判断，仍交负责人独立验收，不是规则或加载检查推导的效果结论。

## 全文科学任务与推进依据

| 位置与实际英文 | 作者科学依据及连续关系 | 适用范例关系与具体实现 |
| --- | --- | --- |
| Writing P01-S01 “Robot manipulation is essential for extending robot capabilities to physical tasks that require accurate interaction with objects.”；Polishing P01-S01 “Robot manipulation extends robot capabilities to physical tasks that require precise interaction with objects.”；两稿随后进入示范监督学习、多种有效动作及时间一致性。 | F01、B01、B03 支持操作、示范学习与精度／时序需要。首句主体是研究领域 robot manipulation，作用是扩大机器人完成物理任务的能力，随后才引入学习路线及具体表示问题。Polishing 新增 stepwise prediction 的模式切换可能性来自 F01，不是将所有显式方法判为必然失败。 | P17 I01／E01 从领域应用及能力需要进入学习与建模；ESO I01／E03 用扩展能力的价值进入技术责任。两稿采用领域对象—具体作用—学习路线—研究需要的连续实现，没有移入制造更新或海洋研究事实。 |
| 两稿 P02-S02–S05：“In [1], the effects of demonstration quality, data quantity, observations and algorithm choice were systematically studied for robot manipulation. Recurrent Gaussian mixture policies use historical observations and represent multiple action modes through Gaussian components. In [2], a Behavior Transformer was proposed to learn multimodal continuous actions from observation sequences.” 后句接动作类别与偏移；Polishing 明确 “predicted continuous offsets refine the actions associated with these categories”。 | B01–B02：R1 的系统研究及循环混合策略能力，R2 的历史上下文、多模态连续动作、聚类和连续偏移。接着说明类别／分量数量需设定、历史观测不等于未来序列联合表示。Writing P02-S08 的模式偏置／切换限于当前受控推物比较，符合 B04；Polishing 删除该句后，F01 的切换可能性及历史／未来区别仍建立设计需要。 | P17 I04／E06 的具体文献→所用模型／输入→产物续句，E05 的 `In [xx]` 成熟定位及主动／被动变体。P05 I02／E15 提供能力先行、再接当前任务条件的关系。原句实际使用 studied／use／represent／was proposed to learn／refine，动作对应真实文献和模型职责。 |
| Writing P03-S02–S06 与 Polishing P03-S02–S07：IBC 通过能量函数表示策略，采样或梯度推理寻找低能量动作，支持视觉高维和毫米级实机精度；“Its contrastive training uses demonstrated actions as positive samples…” 接归一化项；随后 “Direct learning of distribution gradients offers an alternative…” 。 | B03、B05、F07：先承认 IBC 已有真实能力，再由其负采样／归一化训练条件引出梯度路线。Polishing P03-S06 增加 “The implicit behavioral cloning baseline showed fluctuations during training and evaluation in our comparisons.”，限定当前基线及比较，没有否定 R3 全部方法或宣称闭环不稳定。 | P05 I02 的能力与适用条件、P17 I05／E20 的同一任务比较，以及 ESO E11–E12 的同一文献职责续接。这里方法、低能量动作、训练过程依次作主语，关系由表示→推理→能力→训练条件推进；代词仍接同一 IBC 方法。 |
| Writing P03-S07–S09、P04-S01–S08；Polishing P04 全段及 P05-S01–S03：DDPM 的反向去噪、不同噪声尺度的 log-density gradient、Diffuser 联合状态动作与奖励／约束、离线 RL 的 Q 值目标、同期模仿研究，接 “In this paper, we propose Diffusion Policy…” 及 observation-conditioned action generation。 | B06–B09、F02：已有生成基础、规划／RL／模仿能力保持真实，未声称首次扩散策略或其他工作不支持长时域／多模态。自己的监督示范、观测条件动作生成与前述状态动作规划／Q 目标不同。Writing 明说噪声预测训练；Polishing 保留得分学习与动作去噪的概念职责，省略训练细节不改变方法身份。 | P17 I04→I05 从相关能力进入适用设计；E05–E07 的文献方法和能力、E19 的直接设计及组成职责。不是机械要求每段末尾设置 gap：Polishing P04 完成相关能力与设置，P05 接作者设计，设计需要还由 P01–P03 延续。 |
| Writing P05-S05–S08：“Temporal consistency must also be balanced with responsiveness to new observations. We therefore combine action-sequence prediction with receding-horizon execution. The policy predicts a longer sequence from recent observations, executes a shorter segment and then predicts again using new observations.”；Polishing P05-S06–S09 保留同一关系，以 “replans” 明确更新。 | F03–F04：序列表示多模态、联合时间相关动作；只执行较短窗口并使用新观测预测。两稿明确长预测与短执行的不同职责，没有开环执行全部或每步重新推理的错写，也没有普遍模式恢复保证。 | P17 I07／E23 从前一部分输出接后一部分职责，I06／E17 提出整体性能的另一项需要；Fuzzy I03 说明相关能力仍需面对具体条件的组织关系。`we combine`、`predicts…executes…predicts/replans`、两个 horizon/window 的主语和作用对应作者接口。 |
| Writing P06-S02–S05：图像→特征条件、编码一次→多步复用→“This design reduces the computation associated with iterative action generation and supports real-time inference.”；Polishing P06-S02–S05：“We therefore use encoded image features to condition action denoising. Image observations are encoded once per prediction cycle, and the resulting features are reused across all denoising steps. This design reduces repeated computation and supports real-time inference.” 后句说明输出是动作。 | F05、B10：视觉编码职责与去噪输出明确，复用减少重复编码计算，supports 不构成任意硬件实时保证。P06 由视觉推理计算需要引出特征条件和复用，没有把视觉状态与动作共同去噪或未来图像生成写成当前方法。 | P17 I05／E19 的设计及作用，I07／E23 的输入输出交接；ESO E11／E22 的设计后继续具体职责。`encoded features`—`condition action denoising`、`features`—`are reused`、`design`—`reduces/supports` 构成明确作用链。 |
| 两稿 P07-S01–S05：“The denoising network must preserve…” 接 “We examine…as alternative architectures”，卷积低频倾向可能平滑动作，Transformer 在部分快速变化／速度控制任务有优势，最后以超参数敏感性限定选择。 | F06、C03：网络是替代架构，未写成串联；部分任务优势和调参代价保持，未把真实机器人最佳模型归给 Transformer。架构段接前面的动作生成责任，具体讨论动作变化的时间特征。 | P17 I06／E17–E18 由性能责任进入相关工具、能力与选择条件；E14／E20 的同一任务比较及条件。这里 `tendency to favor`、`can…smooth`、`is designed to reduce`、`some tasks`、`sensitivity to hyperparameters` 连续限定而非无条件优越性。 |
| Writing P08-S01–S05 将 multimodal representation／joint sequence／responsive execution 与视觉计算、替代架构收束为框架和所测任务证据；Polishing P08-S01 “We present a demonstration-learning framework that combines diffusion-based action-sequence generation with receding-horizon execution and efficient visual conditioning.” 后接验证范围与具体结果。 | S01–S03、S05、C01–C03：八项仿真／四项实机，46.9% 只归仿真报告指标、逐指标取最佳扩散架构和基线、排除混合熟练度多示范者结果、使用各方法最佳动作空间；95% 仅归 20 次推 T 定量试验。没有百分点误写、归到每个单一架构或扰动成功率，也没有理论稳定／普遍成功结论。 | P17 I08／E24 的总体框架及相关职责回收，整节层 contributions 的需要→职责→贡献。两种结尾均围绕前文设计与支持证据。实验信息依正常论证判断，不因其出现在引言中认定失败，也不将本次选材固定为默认结构。 |

## 英文实现、保留与修改的语境判断

两个版本均有七处 `In [n]` 单引文实现，但数量不证明对齐。上表逐项核对了其真实科学主语、动作、对象和续句：R1 是 studied 的研究对象，R2 是 was proposed 的模型及聚类／偏移能力，R3 是能量策略及推理／训练，R4–R7 各有生成或优化动作。设计使用 `we propose`、`we combine`、`we use`，后续句承接所处理对象、条件与作用；重复名称和短称按连续语境选择。

- 两稿 P01-S02 的 “Learning from demonstrations provides…” 接已经明确的领域价值，再给监督学习路线和动作表示问题。P17 I01 也以示范学习的价值进入运动建模；此处不因动名词形式判 failure。Polishing 将 “by treating policy learning as supervised learning” 收为 “through supervised policy learning”，科学含义保留。
- 两稿 P01-S05 的 “It is therefore necessary/essential to consider…” 是引出具体研究需要的非人称构造，后接 multimodal action distribution／temporally correlated actions。可对应 P17 I01 的 “Therefore, it is essential to consider how to model motions effectively.”，不是对象身份缺失。
- Writing P05-S02 的 `Its capacity` 接 diffusion representation；P06-S04 的 `This design` 接编码一次、多步复用；P07-S05 的 `Its greater sensitivity` 接 Transformer，作用及最近指代均清楚。Polishing 保留 P06 的 `This design` 和 P07 的短称，与 E19 原文 `This modification` 在同一组合设计后接作用的关系相容。
- Writing P05-S04 的 “this representation captures…maintains one mode” 在该段动作序列生成及受控示例中可恢复其政策实现含义，未找到它宣称纯表示在所有任务独立保证模式保持的证据。Polishing P05-S05 直接写 “Diffusion Policy represents…maintains one mode”，使实际执行者更明确。记录为科学身份更清楚的改进，不仅凭 representation／短称补造职责 failure。
- Polishing 将 Writing 的扩散基础集中到 P04，将本文设计与执行集中到 P05；为 IBC 训练条件加入当前比较波动；将 “image observations are encoded once” 与特征复用直接相连。均由原材料支持，没有删掉必须保留的接口或改变条件。`distribution gradients` 在邻句 log-density gradients 和本文 score gradient 中明确，不能据该短称单独判科学量错误。

已确认的必须修复 failure：本次未发现。Polishing 的变化包括组织与表达改进以及有依据的选材，不据此推断它曾执行完整隐藏检查或已证明能修复任何尚未出现的真实错误。没有把未采用的事实算作可靠漏检，也没有给合理变体提出强制替换稿。

## 实际读取、体现与结论边界

实际可用的资源、返回的英文／分析和输出体现分别记录。参照 [loading-summary.json](../loading-summary.json) 与 [context-evidence.json](../context-evidence.json)：两端专用片段、索引、核心完整返回；整节六组英文完整返回；Writing 的八组段落与十五组表达、Polishing 的六组段落与十五组表达的英文块及分析表完整返回。部分外围说明仅部分返回，不能记为全文全载。原始 events 给出实际内容与命令 ID，部分返回不被扩写为完整阅读。

上述全文句段与范例关系和真实英文的对应支持本次对齐判断；并非因为返回了范例才判通过。Writing 的公开主线及段落分工见 agent message `item_29`、`item_39`，Polishing 的选择与组织见 `item_22`、`item_30`、`item_31`；这些记录只说明公开决策，不推断隐藏推理。没有 generic 冲突指导、无关卡集或额外出版原文显式返回，没有历史评价或目标原文输入。

本例结果不证明迁移、稳定性、完整遗漏检测或未来自主修复能力。两稿、各阶段运行及来源证据保持原样；候选及既有记录未修改。提交同步后停止，交负责人独立验收。

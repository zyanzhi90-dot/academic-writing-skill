# Introduction 采用理由衔接与润色科学分工审计

本轮只完成两处候选修改及静态核对，没有新写作输出、效果测试、安装或历史稿修订。三个问题在被审计成稿中仍然存在；本轮实施不能记作它们已经通过自主交付验收。

## 当前依据与边界

本地及更新后的 `origin/main` 为 `025528f5c5621e14631f9abd61fa9b5021624b72`，候选内容沿用 `22cc2ca`；后者之后的提交记录了该候选的首次效果输出。本地代理端口不可用导致初次 fetch 失败，随后用单次 `git -c http.proxy= -c https.proxy= fetch origin` 成功，不修改持久配置。

读取当前 [AGENTS.md](../../AGENTS.md)，以根目录四份有效作者要求为当前依据。新鲜字节副本及 SHA-256 见 [inputs](inputs) 和 [evidence.json](evidence.json)；根目录 `current-author-adjustment.txt` 同时复制到本记录根目录及 `inputs/`。本记录是开发审计，不是新写作会话。历史冻结作者文件仅用于解释历史执行，未作为本轮当前要求。预先存在的未跟踪文件 `11当前进展.txt` 保留原样，不纳入本轮改造。

审计对象为 [E04 两阶段首次记录](../../effect-test/E04-introduction-delivery-22cc2ca-2026-10-07/)。直接读取两端首次英文、完整首次输出、原始 `events.jsonl`、执行请求、身份核对和实际加载文件；没有运行其历史检查脚本或执行器。来源采用本地四篇出版 PDF 与已有完整引言原文阅读记录，当前 PDF 哈希均与已有来源证据一致。适用完整原段与页码收在 `evidence.json` 的 `sources` 中，正向材料仍通过候选现有三层学习资源使用，审计原文和案例诊断不进入正常写作上下文。

## 失效证据与定位

段号按首次英文中贡献引导之前的六个正文段计算。[Writing 首稿](../../effect-test/E04-introduction-delivery-22cc2ca-2026-10-07/drafting/first-introduction.en.txt) 与 [Polishing 首稿](../../effect-test/E04-introduction-delivery-22cc2ca-2026-10-07/polishing/first-introduction.en.txt) 保持原样。

| 已确认问题 | 两阶段证据及原始科学输入 | 机制与实际执行的区别 |
| --- | --- | --- |
| P4 归纳较泛 | 两端都用 `These studies establish a basis for diffusion representations of trajectories and policies.` 收束。前面已有得分学习、轨迹规划、Q 值策略和同期模仿学习的具体能力，但这一总结没有把它们的相关能力与条件充分收束到当前采用选择。Writing 随后虽提出反馈和视觉需要，仍有相同问题；Polishing 将设计移到下一段，没有修复这项连接。 | 索引已有真实能力、条件、采用理由及设计作用要求；P17 I04–I05、P05 I02 和 Fuzzy 的适用英文实际返回。不能判成范例不存在或入口失效。观察支持采用关系的实际组织未充分落实，不能由成稿确定唯一生成原因。 |
| P5 理由与设计职责错接 | Polishing 先说明执行反馈和重复视觉编码，接着 `To address these requirements, we propose Diffusion Policy...`，随后先讲噪声预测、分布梯度及避免归一化估计；执行窗口与特征复用的对应职责到 P6 才展开。全文确实保留了这些需要和设计，但局部理由没有紧接其对应职责。Writing P4 已把反馈、视觉需要接到分布机制上，Polishing 的重排继续留下这一问题。 | 既有两端接口已要求需要先于设计、理由与职责相接；Polishing `item_24` 明说会把反馈和视觉需要放在核心设计前并以职责承接，`item_33` 声称已对照完整英文。成稿与公开计划不一致，支持执行结果和交付复核不足；日志没有可用于确定其内部检查过程的证据。 |
| P3 S6 科学分工退化 | Writing：`Its contrastive training uses demonstrated actions and sampled negative actions, with the negatives used to approximate the normalization term of the conditional distribution.` Polishing：`Its contrastive training uses demonstrated actions and sampled negative actions to approximate the normalization term of the conditional distribution.` 原始 B03 明确对比训练使用示范正样本及负例，归一化项由负例近似。压缩后共同目的分句模糊了这一区分，中文对应稿也继承它。 | 原始事实不缺，Writing 原本正确。两端初始请求完整包含 B03，Polishing 已加载科学表达与动作归属检查。问题发生在润色合并及未纠正的交付结果；不能据此认定需要新增“归一化项”专用规则，也不能说模型没读过科学事实。 |

原始日志重算结果见 `evidence.json/stages`。两端均为一次有效会话，`gpt-6.1-sol / high`；首次输出哈希与历史审计一致。专用索引、Introduction 整节材料和科学表达文件有完整非空行返回；P17 I04/I05、Fuzzy I02/I03、E19/E22 的完整英文均返回。英文返回与分析表完整程度分开判断，不能把任一返回统计补记成采用成功。旧检测字段 `selected_cards: {}` 面向另一组卡片，不代表这些 Introduction 单元未读。

两端日志均未见再次显式打开 `background-facts.md`、`scientific-facts.md`、`citation-facts.md` 的文件命令；三者已完整进入初始请求。这个事实只支持把压缩后的核对明确绑定回原始科学材料，不证明不存在内部复核，也不证明增加文件读取必然修好。

因此，未发现本轮三项问题所对应的机制缺失或有效入口冲突。可确认的是：已有关系要求和可用范例未充分体现在实际成稿，Polishing 的合并发生了科学分工退化。范例利用不足与生成/复核执行不可靠均有结果层面的迹象，但现有日志不能区分其内部原因或给出稳定性判断。本轮优先改变已有学习与复核的执行接点，没有新增规则层或改执行器。

## 直接复用的英文与科学关系

以下英文来源定位及完整适用原段见 `evidence.json/sources`；学习层保留现有原文选取、适配及连续句分析，不复制本案例目标英文。

- **P17 I04→I05，PDF pp.1–2／刊页777–778。** I04 从概率编码保存示教变异进入具体 GMM/GMR 文献机制，再综合 DS 与概率学习各自能力。其末句 `Both methods exploit the robustness and generalization capability of the DS as well as the excellent learning performance of the probabilistic methods.` 直接进入 I05：`To take advantage of the performance of the DS and the probabilistic approach, we integrate DMP and GMM into our proposed system, where the nonlinear function of DMP is modeled with GMM and its estimate is retrieved through GMR. This modification enables the robot to extract more features of the motions from multiple demonstrations and to generate motions that synthesize these features.` 成熟关系是前文具体能力→为何组合→组成部分各自操作→组合的作用。作者应换成自己的能力、需要、对象与职责；不搬入 DS、GMM 或控制保证。
- **P05 I02，PDF p.1／刊页1010右栏。** 完整段先连续说明协作操作、力/位置调节、增广物体模型约束内力与抓持空间负载分析；随后才明确牢固抓持、无相对运动条件，接到表面操作中的滑动需要。`... the object is firmly held by the robotic arms such that no relative motion occurred between the arms and the objects.` 接 `However, in practical applications, such as polishing, grinding, and welding, the robot end-effectors need to operate along the object’s surface ...`。适用关系是具体文献能力与真实条件共同形成当前需要；不能仅因设置不同就虚构文献不足。
- **Fuzzy I02–I03，PDF pp.1–2／刊页1041–1042。** I02 经 BLF 约束能力与具体文献，落到 `In this article, a novel symmetric BLF is designed to guarantee the desired transient performance of the robot system.`；下一段另开 `In many industrial systems, the system states are required to achieve fast convergence speed for better control performance.`，经有限时间的初始条件依赖进入固定时间方向。两项需要分别得到对应论证，不由一个泛化目的统辖所有设计。这是可选组织关系，不要求作者照搬两段或先瞬态后时间。
- **ESO I07→I08，PDF p.2／刊页6786右栏。** 传感器所得位置和缺失速度先建立输出反馈与状态估计需要；I08 续写 `Motivated by the ESO model [32] and the high-gain observer [39], a MIMO-ESO is proposed to estimate the unknown disturbances and the unmeasured states. The bounds of the uncertainties are also estimated using the adaptive control technique.` 观察器估计的扰动/状态与自适应技术估计的界有明确分工。只借鉴启发、设计及估计对象的连续英文，具体作用和证据强度来自作者材料；完整审计原段中的实验信息不进入当前作者 Introduction。

P17 的 `its estimate`、`This modification` 及原文联合分句在该语境下清楚，继续保留；采用具名适配或清楚指代由作者语境决定。问题是合并后的实际科学归属，不能按代词、分词开头或语法形式一概判错。

## 最小改动及执行动作

| 修改文件 | 替换了什么执行判断／动作 | 为何预期有效及限度 |
| --- | --- | --- |
| [共用引言索引](../../skill-candidate/nature-shared/core/robotics-introduction-examples.md) | 设计采用任务的检索从独立 I05 改为 P17 I04→I05 连读；在已有 Drafting 的具体文献到设计说明处，用实际过渡句对照该完整英文，逐项对应“何种已有能力或任务条件支持何种设计职责”，随后说明同一对象上的动作与作用。Polishing 复用同一比较；Fuzzy 保留并列需要的另一种实现。 | 改变范例选取单元和实际句间对应，不只重申“理由充分”。可帮助发现泛化总结与后续设计之间的缺项、目的和职责错接；不规定段数、句序或每段 gap，不把设置差异当作文献缺陷。实际能否落实待效果验证。 |
| 同一共用索引的现有 Polishing 检查 | 替换泛化的旧/新动作、指代复核：压缩、重组、重排后回到相关原始作者段落，逐动作比较原始含义及旧/新英文中的对象和目的，包含并列对象与共享分句的作用范围；按需调用 P17 各组成职责或 ESO 估计分工英文。来源明确的错配在交付前纠正；科学含义不明确才标注。 | 把检查的事实依据从编辑后读感或旧稿记忆绑定回作者原始科学关系，针对润色合并可能改变作用范围的位置落实已有科学保障；不写入示范/负例术语或 E04 修复句。无法保证模型执行可靠。 |
| [Polishing 引言接口](../../skill-candidate/nature-polishing/static/fragments/section/intro.md) | 就地替换交付前的笼统邻句检查，显式调用共用索引上述源材料比较与实际过渡比较，再继续现有全文取舍、相邻交接和贡献回收。 | 让正常润色入口在真正重组后的交付位置执行该比较；不新增独立审计报告或新检查阶段。 |

Writing 引言接口本来就从现有 manifest 读取共用索引及匹配完整英文，并在步骤7–8对照原始作者材料与范例，故无需再次修改。两端 manifest、router、成熟 Shared 核心、三层英文资源及执行器原样保留；没有增加重复依赖或修改其他 section。贡献引导与编号列项、全文排除本研究实验内容、合理变体按语境判断等当前要求继续有效。

## 静态核对与下一轮验收

[static-check.json](static-check.json) 保存静态实际读取文件、选中单元哈希和结果；[check_static.py](check_static.py) 只做文件与日志核对，不调用写作模型。三包 `quick_validate` 通过；所有声明依赖与索引链接/锚点可解析。两端在本地和仅含候选的临时目录均能实际读到入口、manifest、核心、Introduction 片段、专用索引及所选完整英文，无需项目分析报告。此核对由人工确定正常路由轴，不是自然语言路由或写作效果测试。

候选改动仅上表两文件。基线其他9492个已跟踪文件的聚合哈希在核对前后相同，见 [protected-snapshot.json](protected-snapshot.json)；包括历史首次稿、日志、事实、作者要求、基座、执行器和未受影响的候选文件。`git diff --check` 通过。审计证据只在本记录新增。

下一轮按 AGENTS 冻结当时根目录四份要求，用确认过的原样科学材料与标准请求开展独立首次自主交付；写作端不得获得本报告、问题清单、诊断、历史修订稿或预期英文。本轮不启动该验证。下一轮应分别保存并评判 Drafting、无逐句反馈 Polishing 和组合交付，不能相互补记通过：

1. 相关研究是否保留其具体能力、条件及真实归属，并在需要处形成当前采用理由；不能用泛化相关性或虚构缺陷替代。
2. 实际采用理由是否紧接对应设计职责与作用；多个需要与职责的排列按科学依赖判断，不能只检查“需求在设计之前”或要求复现本案例句序。
3. 压缩、合并和重排后的动作、对象、目的及作用范围是否仍忠实于原始科学分工；同时检查其他对象、输入输出及条件是否发生新退化。
4. 已合适英文、贡献引导与实质编号列项、当前实验信息排除是否保持；方法信息是否仍限于采用理由、职责、接口和贡献所需。具体英文按完整连续上下文验收。

原始材料明确的科学错误应由正常生成/检查自行修正，不预先交给人工修稿。真实含义或证据缺失时才记录必要作者介入。若上述任一真实问题仍在首次交付中存在，应如实判未通过；这个已知案例也不能记作迁移或稳定性通过。提交同步后停止，交负责人独立验收。

"""Render human-authored sentence analysis beside complete freshly checked source paragraphs."""
from pathlib import Path
import json

OUT = Path(__file__).resolve().parent
SOURCE = json.loads((OUT/'curated-introductions.json').read_text(encoding='utf-8'))
SENTENCES = json.loads((OUT/'source-sentences.json').read_text(encoding='utf-8'))
NOTES = {}

def add(paper, unit, task, link, rows):
    notes = [s.strip() for s in rows.strip().splitlines() if s.strip()]
    assert len(notes) == len(SENTENCES[paper][unit]), (paper, unit, len(notes),len(SENTENCES[paper][unit]))
    NOTES.setdefault(paper,{})[unit] = {'task':task,'paragraph_handoff':link,'sentences':notes}

add('P17','I01','制造业变化如何把机器人学习落到运动建模责任。',
    '先使 robot learning 有具体任务来源；末句交给 I02 的 motion modeling 工具，而不是泛泛说学习重要。', '''
已有应用事实，先定机器人与制造业场景。`robots have been widely applied in ...` 用主体＋现在完成时被动表述使用范围，不先喊新颖性。
从产品快速更新推出适应性要求。`Adaptable robots are required due to ...` 将需要的机器人性质置为主语，due to 后给可指认的变化。
把适应性要求转成学习方法需求。`Hence, it is necessary to develop methods for enhancing robot learning` 的因果依赖上一句，而非仅靠 Hence。
引入可承担学习任务的 LfD。完整术语先作主语，`is a valuable technique to simplify ...` 交代它在当前问题中的用途，引用放句末。
解释 LfD 怎么发生。`The human tutor shows ... and then the robot learns, via motion modeling, to reproduce ...` 先人与任务，再机器人、建模手段与重现输出。
从刚说明的过程取出本节第一项责任。`Therefore, it is essential to consider how to model motions effectively` 不是全面 gap，而是选择后文要展开的具体对象。
''')
add('P17','I02','选择 DMP 的依据来自 DS 能力与具体示范需求比较。',
    '接 I01 的 motion modeling；以 spring-damper 的运动性质收尾，使 I03 能讨论 DMP 的实际用途和进一步多示范需求。', '''
段首直接定义工具位置。`The dynamic system (DS) is a powerful tool for motion modeling` 回答上一段的技术对象，不重开应用背景。
比较 DS 与明确举例的传统工具。`DS offers a flexible solution to model ... trajectories` 的对象是轨迹，stable／extensible 是所列能力维度。
补充另一个任务相关性质。主语转为 `the motion encoded with the DS`，`is robust to perturbations` 把性质落到生成运动。
举出 DS 学习实例及未知映射的实现。`An approach based on DS was used to learn ... , where ... was approximated using ...` 主句讲用途，where 从句讲建模责任与 NN 类型。
承认该实例的效果。`The learned model showed adequate stability and generalization` 仍指上一句同一模型，先保留能力再比较。
用训练数据代价限定该实例。`this DS-based method required considerable demonstration data` 的 this 限定特定方法，不把所有 DS 说成耗数据。
以另一方案回应示范代价，并解释运动模型组成。`the ... DMP ... only requires one demonstration to model motion` 接比较，随后说明 spring-damper 和待学习函数。原句含分号与 here，保留证据，不能固化为作者必选句法。
说明 spring-damper 性质如何影响输出。`The inherent property ... enhances the stability and robustness ... of the generated motion` 命名作用来源与被改善对象；此强度属于源文科学主张。
''')
add('P17','I03','从 DMP 多种用法中区分“多个 DMP”与“多个示范”，提出一个 DMP 整合多示范。',
    '接上段已选择的 DMP；末句提出多示范整合，I04 才引入能保留示范变异的概率方法。', '''
段首亮出 DMP 用途并给理由。`DMPs have been often employed to solve ... because of their flexibility` 用技术名而非笼统“研究很多”。
第一篇文献讲对 DMP 做了什么修改及目标运动。`In [7], DMPs were modified to model fast movement inherent in hitting motion` 中 modified／model 分属修改动作和建模用途。
第二篇用主动研究主体变体。`Another study used reinforcement learning to combine DMP sequences so that ...` 把手段、组合对象和复杂任务作用接在一条句链中。
归纳前两项共同点后引入第三种用途。`While both these studies employed multiple DMPs ... , another study ...` 先说明可比对象；where 从句将风格调节接到目标耦合权重。并非只换引用编号。
从文献用法切换到示范质量这一信息条件。`optimal demonstration is difficult to obtain and multiple demonstrations can encode ... implicitly` 的后一分句给当前选择的正向依据。
用 Therefore 收成具体建模决定。`we consider integrating multiple demonstrations into one DMP model` 清楚保留 multiple demonstrations／one DMP，而不是声称多个 DMP 本身失败。
''')
add('P17','I04','解释概率方法可继承的多示范信息能力，并建立其与 DS 组合的先例。',
    '回应 I03 的多示范整合需求；段末总结已有 DS＋统计学习能力，为 I05 的 DMP＋GMM 组合提供可继承基础，没有额外制造缺口。', '''
段首先承认研究路线能力。`Probabilistic approaches have shown good performance in motion encoding` 用明确领域限定 performance。
解释该能力为何有用。`variability ... can be extracted` 接 `more features ... can be preserved`，从数据差异到信息保留，两个被动对象有因果联系。
文献主句交代所用模型及提取对象。`an LfD framework using ... was used to extract the features from multiple demonstrations`，GMM／Bernoulli mixture 是手段，多示范特征是输出。
下一句继续同一流程的生成环节。`A new motion was generated through ... GMR` 区分上一句特征提取与此句新运动生成，避免模型名并列。
比较组合方式的额外信息能力。`GMM combined with GMR can provide additional motion information ... when ...` 保留比较对象和多示范条件，不笼统宣称最好。
再列 DS 与统计模型结合的实例。`a learning approach named ... SEDS was proposed for motion modeling, where ... was modeled using GMR` 名称、用途、未知函数的实现逐层相接。
用 `DS-GMR is another method that combines ...` 补足第二个组合实例，another 指已有同类路线。
段末归纳前两种方法怎样利用双方能力。`Both methods exploit ... as well as ...` 是选择依据总结，不是 gap 句。
''')
add('P17','I05','DMP＋GMM／GMR 的分工、具体作用与原有学习方法比较。',
    '接 I04 可继承的组合能力，先给当前实现，再比较数据需求及计算效率；I06 随后指出运动模型之外还有跟踪责任。', '''
设计首先命名组合，随后分配具体对象。`we integrate DMP and GMM into ...` 接 `the nonlinear function ... is modeled with GMM` 与 `its estimate is retrieved through GMR`，不是只说融合两个优点。
马上解释上一修改的任务作用。`This modification enables the robot to extract ... and to generate motions that synthesize ...` 的特征提取和运动生成共享多示范信息来源。
回查原 DMP 如何学习，并补充核带宽优化。`was learned using ... LWR` 与 `was employed to optimize the bandwidth of each kernel` 各有对象，不能把 LWR／LWPR 当两个泛化标签。
承认比较对象仍有单示范能力。`Despite the added complexity ... these methods enable ...` 不让当前组合抹去前作能力；only one demonstration 限定所述学习方式。
以替代近似路线和效率维度收尾。`Reservoir computing ... is another method used to approximate ... , but its computing efficiency is less than that of GMR` 比的是具体函数近似的计算效率。
''')
add('P17','I06','任务效果还取决于执行跟踪，从未知动力学推出函数近似并选择 RBFNN。',
    '不是突然添加控制模块：首句用 imitation performance 接前文运动生成，依次推出动力学、载荷不确定性、NN 和 RBFNN；I07 因而能给出控制与输出接口。', '''
桥接整个系统的另一项责任。`The imitation performance of robots also depends on the accuracy of the trajectory tracking controller`，also 保留生成已解释而执行尚待解释的关系。
先说准确模型的正向作用。`a model-based control performs better if the model is accurate enough` 将性能依赖写成 if 条件。
再说当前为什么得不到这种模型。`an accurate dynamic model ... cannot be obtained in advance due to ... unknown payload` 的时间条件和载荷例子支撑后面的补偿。
由上述未知项引入可用控制路线。`The approximation-based controllers have been designed to overcome such uncertainties`，such 指动力学未知项。
补充该路线的实现动作。`utilize function approximation tools to learn the nonlinear characteristics ...` 将 compensate／approximate 前的技术对象讲清。
缩到 NN 的选择理由。`NNs have been widely used ... because of their approximation ability` 是具体工具能力，不是只写流行。
连续比较 BPNN 与 RBFNN 应用。两半均以具体 NN 为主语，`was utilized to approximate` 接各自系统未知非线性，而不是声称两项工作任务相同。
沿局部近似解释源文宣称的优化与收敛优势。`the learning procedure ... is based on local approximation` 接避免局部最优和更快收敛；这些强结论不能变成所有 RBFNN 的通则。
增加结构适应能力。`the number of hidden layer units ... can be adaptively adjusted during the training phase` 命名可调整数量与发生阶段，后接源文的灵活性解释。
以 `Therefore, RBFNN is more appropriate for the design of real-time control` 完成局部选择，不再泛泛说 NN 有意义。
''')
add('P17','I07','说明控制责任、保证与生成—跟踪的同一轨迹接口。',
    '接 I06 选出的 RBFNN；将前文多示范生成和当前控制组合为系统，为 I08 按整体责任比较前作创造对象。', '''
设计句并列控制责任与近似责任。`an NN-based controller is designed to guarantee ... in joint space` 接 RBFNN 所近似的机器人动力学非线性，joint space 不应丢失。
将稳定性与作者使用的分析依据联系。`The stability of the controller is guaranteed by ...` 是源文保证陈述；借句式时仍须替换证明对象与实际前提。
命名两组件。`the robot learning system consists of ...` 只在系统确有这两个责任时可借用，不作为引言固定双模块。
先定义生成组件输出。`utilizes ... to learn and generalize ...` 接 `represented as a set of trajectories in joint space`，形成下句要接收的轨迹。
跟踪组件接收上一句相同轨迹。`track the trajectories generated from the former` 后命名 RBFNN 补偿 uncertain dynamics，清楚区分生成输出、跟踪目标与补偿对象。
''')
add('P17','I08','把运动生成和轨迹跟踪综合为整体贡献，并作限定前作比较。',
    '接 I07 已有完整接口；最后落到学得运动在真实世界的执行，I09 转入文章安排，不再需要段末 gap。', '''
合并两种任务责任。`we present ... framework that considers ... both motion generation and trajectory tracking` 的 both 有前文铺垫；Here、novel、complete 是源文选择，不是必抄装饰。
先承认相似前作。`The SEDS presented in [3] is similar to our DMP-based model` 保持技术继承关系。
沿这一具体前作解释约束与学习复杂度。`the constraints that guarantee ... are derived ...` 不能扩展为所有稳定运动模型都难学习。
按责任范围比较所列 [3]／[25]。`our system is enhanced by ...` 后接动态环境影响的补偿；only motion modeling 仅属所列对象。
段末以设计接任务效果。`This design enables the robot to perform the learned motions ... in the real world` 将前文 learned motions 交给真实执行，而非另添新目标。
''')
add('P17','I09','按方法依赖给出论文安排。','DMP 基础→学习→RBFNN 控制及稳定性→实验→结论；章节序列呼应生成到执行的主线。', '''
`The remainder of this paper is organized as follows` 是组织提示，不承载科学创新。
`Section II introduces the DMP and its relevant characteristics` 先给要使用的运动模型基础。
`The learning process ... is introduced in Section III` 再给生成模型的学习。
`In Section IV ... controller ... is designed with the proof of stability` 将控制设计与其分析放在同一责任下。
`The experiments are presented in Section V` 只承诺实验呈现，没有给出结果数值。
`Section VI concludes this paper` 完成 roadmap；引言没有强制以实验提升数字结束。
''')

add('P05','I01','并列交代双臂的任务优势与协调控制／规划复杂性，共同构成应用动机。','优势引出应用；协调运动控制／路径规划的复杂性另行引出控制研究。I02 再具体看已有控制怎么处理对象。', '''
以研究对象及应用优势开篇。`coordination control of dual-arm robots has received increasing attention due to ...` 后列 payload／workspace／flexibility，attention 有技术原因。
把上一优势接到应用。`Thus, the dual-arm robots have been involved in ... such as ...` 的应用举例不等于本文验证范围。
另行说明控制挑战的原因。`controlling ... is challenging due to ... complexity in motion control and path planning` 将控制困难归于协调运动控制与规划复杂性，与前述载荷／空间优势并列。
以已有控制研究接到下一段。`advanced control technologies have been extensively studied for ...` 给文献展开入口，不假设所有前作失效。
''')
add('P05','I02','从前作控制能力中提取紧持物体／无相对运动的共同条件，再用真实任务改变该条件。','I01 的控制问题具体化为物体操作；段末工具沿物面滑动，为 I03 的 relative motion 提供物理含义。', '''
文献首句直接讲方案与功能。`An adaptive decentralized control scheme was proposed to address ... , where ... was employed to simultaneously regulate the force and position` 用 where 解释方案内部的力／位置责任。
第二项讲不同控制对象。`a decentralized control structure ... was developed` 接 internal forces 的约束与 augmented object model／virtual linkage 手段。
第三项从问题作主语。`the loading problem ... was addressed by analyzing the grasp space`，addressed 的是载荷问题，by 后是分析方式。
把前三项放进有证据的共同条件。`controllers were developed under the assumption that ... firmly held ... such that no relative motion occurred ...` 指手臂与对象之间的运动，不是双臂彼此的相对运动。
用当前应用真正改变条件。`robot end-effectors need to operate along the object's surface, where sliding movements ...` 将 polishing／grinding／welding 接到沿表面滑动这一要求，下一段才有理由研究 relative motion。
''')
add('P05','I03','在相对运动任务内再次承认已有工作，再定位动力学先验和接触力分析。','任务条件已从 I02 推出；本段不是说没人研究相对运动，而是明确已有相对运动控制仍有什么假定。I04 接 dynamics fully available。', '''
`coordination control ... with relative motion deserves further investigation` 承接已证明的任务差异，不单独声称无人研究。
`The relative motion is also known as the asymmetric bimanual task` 给当前文献使用的术语对应，避免名称切换丢失对象。
第一项已有相对运动控制讲方法与建模作用。`a relative impedance controller was developed by using a relative Jacobian method such that ...`，结果是把双臂系统作为单臂系统处理。
另一项讲控制架构及输入。`architecture was proposed ... to perform ... , where ... signals ... were employed to send control command` 将 EEG／视觉刺激接到 brain–machine interface，不说它解决动力学未知。
比较严格限于 `In these works`。`controllers were designed under the assumption that ... fully available` 与 `stability analysis ... was not given` 是两个不同限制，不能合成泛泛“性能差”。
''')
add('P05','I04','用抓取物动力学未知的实际原因解释为何需要 NN 补偿。','接 I03 的动力学先验；段末把不确定性补偿落到 NN，I05 才检查已有 NN 控制解决了什么、还需学到什么。', '''
段首双面说明建模地位。`The dynamic model ... is of great importance ... , but it is often unavailable in practice` 直接给有用性与可得性差别。
以具体任务解释 unavailable。`in carrying tasks, the dynamics of the grasped object is hard to obtain in advance` 的对象是抓取物，而不是机器人所有信息。
说精确模型缺失对 model-based control 的后果。`Without a precise dynamics model ... may cause ...` 中 became invalid 是源文较强判断，不能移成所有模型误差必失稳。
由后果引出补偿路线。`strategies have been presented to compensate for the model uncertainties` 将 compensate 接到明确不确定项。
给 NN 为什么能承担该责任。`Neural network ... alleviating modeling difficulties ... due to ... approximation ability` 是工具能力理由。
归纳 NN 已用于控制器开发。`have been widely implemented in developing controllers ...` 承接 I05 的实际例子；原文 `NN control synthesizes` 用词保留作核对，不作推荐搭配。
''')
add('P05','I05','区别已有跟踪控制能力与 NN 权重学习问题。','接已选 NN 路线；以 weights convergence 将下一段从跟踪指标带到参数／激励条件，不能把二者当同一个误差。', '''
先举模糊 NN 的具体适用系统及手段。`approach was presented for ... by using a semi-Nussbaum function` 是方案—系统—工具的文献句。
再举不确定机器人中的状态约束。`strategy was proposed ... to ensure the state not to violate ...` 保留 state constraints 对象，而非笼统保证性能。
第三例给交互任务和 NN 手段。`a sensorless admittance controller was designed ... by using the NN technique`，sensorless 是方法条件，不等于本文无传感器。
这是综述／可理解性贡献的文献句。`Significant works have been done ... to make a complex topic understandable ...` 并非“使用方法解决控制问题”的实例；与权重收敛主线联系较松，不推广为每个文献句范式。
先承认开发成功，再换评价对象。`While ... successfully developed ... , a major limitation ... lies in that ...` 对比 tracking errors convergence 与 NN weights convergence，不凭空说没有跟踪能力。
说明作者认为权重未收敛会影响补偿与系统表现。`Without ... may be degraded ...` 是源文论述，其失稳概括不能当所有自适应 NN 的数学结论。
以 `control scheme with guaranteed NN convergence` 定义下一段要研究的学习问题，而不是再做一般应用宣传。
''')
add('P05','I06','从 NN 权重估计推出激励条件，承认 PPE 局部能力并保留剩余限制。','接 I05 的参数学习问题；末句留下 recurrent trajectory 与 excitation strength，I07 再解释额外误差信息及当前估计设计。', '''
从作者前作继承已完成能力。`a filtered operation was presented ... with finite-time convergence under ... LIP ... model` 将保证附在模型条件下。
用 Nevertheless 改换更难的对象。`the guaranteed convergence of the NN weights is more difficult`，不是否认上一句 LIP 情形的能力。
引入估计收敛所依赖的信息条件。`the ... PE condition is important to guarantee the estimation convergence` 把 PE 与 estimation 接起来。
解释条件为什么严格。`due to the sparse characteristics of the NN regressor vector` 给技术原因，不只说 challenging。
介绍有用替代条件。`Recent research ... presented a ... PPE condition instead of ... PE` 把前作的进展说出来，不能藏掉以夸大改进。
明确前作局部结果的边界。`for ... RBFNN defined in a regular lattice ... partially activated ... recurrent ... local region` 的网格、局部区域、重复轨迹都是能力条件。
继续说明这一思想的后续用途。`In the subsequent work ... this idea was employed ... to guarantee ...` 连接研究序列，稳定性与准确近似各有对象。
最后保留尚需的输入条件和速度影响。`inputs still need to satisfy ... recurrent trajectory` 接 `small input excitation strength may lead to slow learning speed`；still／may 各控制判断范围。
''')
add('P05','I07','把估计误差信息接入更新的已有思想应用到当前双臂任务，并分别比较条件与信息用法。','响应 I06 学习条件问题；末两句的 PPE 和估计误差信息正好交给 C03／C02，不用一个全体前作 gap 替代不同责任。', '''
段首用研究证据句引入改进原则。`The work in [43] indicates that ... can be improved if ...` 中 if 后给估计误差信息进入 adaptation 的条件。
参数估计前作给方案与两个实现工具。`a ... estimation law was proposed ... by using ... sliding mode ... finite-time estimator`，对象是 unknown dynamics 的机器人。
第三句追踪同一种信息的已有用途。`the estimation error was integrated into the adaptation scheme ... to achieve ... NN weights` 明确 information→update→weights 的链。
再做当前任务设计。`we develop a composite learning controller for ... to perform bimanual relative motion tasks`，Motivated by 只是源文过渡，具体设计动作来自 develop。
新颖性范围是任务条件交集。`few studies ... dual-arm ... relative motion and unknown dynamics` 不声称全体 NN／双臂／相对运动都无人研究。
与 [46] 比较的是激励要求。`PPE condition ... introduced in the estimation scheme to achieve a relaxation ... PE` 仍有条件，不是完全无需激励。
与 [45] 比较的是误差信息表达与使用。`estimation error ... is properly expressed and employed to enhance ...` 不把这个信息改进与上一条件改进合成笼统“更优”。
''')
add('P05','I08','把技术铺垫收成双臂相对运动跟踪目标，并引出贡献。','不是首次宣布所有方案，而是汇总 I02–I07 已逐步建立的任务和学习条件；三条贡献继续分开列责。', '''
`The objective ... is to develop a control framework for ... under relative motion` 用目标句汇总任务和明确条件。
`The main contributions ... can be summarized as follows` 是列点接口，不应替代前段具体设计关系。
''')
add('P05','C01','任务框架贡献：未知动力学下的非对称双臂任务。','对应 I02–I04 的物理条件和先验问题。', '''
`framework is developed ... to perform ... with no prior knowledge of the dynamics` 同句给任务与先验边界；不等于没有任何几何、任务或传感信息。
''')
add('P05','C02','学习贡献：估计误差信息进入 NN 权重更新。','对应 I05–I07 的参数学习对象与信息使用。', '''
`algorithm is designed for NN weights adaptation such that information ... integrated into ... law to improve ...` 逐级交代设计对象、进入的信息、作用位置与估计性能，不暗示未知真实权重直接可测。
''')
add('P05','C03','条件贡献：PPE 放松 PE 要求。','对应 I06–I07，三条分别覆盖任务、信息、激励条件。', '''
`condition is introduced for ... such that the requirement ... can be ... relaxed` 描述条件替换的作用；relaxed 不等于 removed。
''')
add('P05','I09','按建模、控制分析、仿真安排后文。','段落链在建模条件和学习控制上汇总；这里仅承诺 simulation，不补造实机实验。', '''
先说后文详述 modeling／control procedures。`are detailed` 是组织动词而非性能动词。
`Section II discusses ... modeling ... preliminaries` 先交代系统与基础条件。
`Section III presents ... algorithm ... with stability analysis` 将控制实现与分析相接，command filtered backstepping 是本文真实实现。
`Section IV demonstrates the simulation results` 命名证据类型。
`A brief conclusion is given in Section V` 结束 roadmap，原引言没有量化结果收束。
''')

add('Fuzzy2023','I01','未知非线性如何引出 NN／FLS，以及瞬态性能和收敛时间的联合目标。','本段先承认已有多种能力，其中包括 fixed-time＋user-defined performance；计算量与未来拓扑优化是未进入后续设计的旁支，末句才把 I02／I03 的两个目标合到一起。', '''
首句直接给物理系统困难及来源。`uncertain nonlinear terms ... exist due to ... time-varying model parameters ... external disturbance`，不是先用泛泛应用背景。
引入 NN／FLS 在自适应控制中的任务能力。`have been widely applied to handle ... because of ... approximation capability`；Combined with 是原文句首实现，不意味着必须模仿这种句法。
具体例子给输出约束及输入饱和。`an NN control scheme has been proposed ... to achieve trajectory tracking with ...` 将作用与条件放在同句。
另一例子并列交互方法和 NN 跟踪保证。`method has been proposed for ... , and ... tracking can be achieved by ...`，不是把 admittance adaptation 与 tracking controller 混作一个对象。
介绍详述控制算法的文献。`algorithms have been introduced in detail for nonlinear systems` 是系统化介绍，不是新控制方案证明。
模糊控制例子给外骨骼对象和康复用途。`scheme has been proposed for ... to enhance ...` 体现任务不同，不能全部说成当前机械臂实验。
明确承认前作已同时支持两性质。`to achieve fixed-time convergence and user-defined performance simultaneously`，是核对后文概括范围的重要证据。
增加 NN／FLS 之外的 active inference 路线。`controller ... to handle large model uncertainties ...` 的对象仍是不确定性，不能声称仅 NN／FLS 可用。
转到传统模糊权重迭代的计算代价。`large calculation ... because of the weight iterative process` 是源文支线动机，不属于后文三个主要贡献。
介绍作者前作 WSN 拓扑优化，并明确只是未来启发。`may ... in our future work` 限定尚未实施，不能借成本文已有 FLS 降计算设计。
末句抽出联合目标。`desired transient performance and convergence time ... discussed simultaneously` 接 I02／I03；rarely／most 不能抹去第7句刚承认的前作能力。
''')
add('Fuzzy2023','I02','从不良瞬态的后果推出 BLF 约束工具，再给本文 symmetric BLF。','展开 I01 的第一个目标；段末当前设计已出现，I03 接着解释第二个时间目标，不再回到总 gap。', '''
段首说为什么瞬态要求不能忽略。`undesirable transient performance may lead to ... instability ... safety problems`，may 表达可能后果，不是无条件失稳定理。
把性能要求接到具体可用工具。`BLFs have been widely used to achieve the state and output constraints` 同时保留 state／output 的不同对象。
文献给 exponential-type BLF 与 event-triggered prescribed-time 方案。`with ... , ... controller has been proposed for ...` 将工具、控制特性、对象放在完整句中。
另例在 unknown nonlinear systems 下同时处理全状态约束与 finite-time 收敛。`to handle ... and ... simultaneously` 不等于 fixed-time。
第三例换到多智能体的 finite-time output constraints。`scheme ... for ... with ...` 保留约束类型与系统类别。
末句直接给本稿工具及责任。`a ... symmetric BLF is designed to guarantee the desired transient performance` 不是机械用 However 制造每段缺口。
''')
add('Fuzzy2023','I03','时间要求从 finite-time 的初值依赖转到 fixed-time，并承认已有约束组合。','与 I02 并行展开第二目标；末两句保留 fixed-time＋BLF／约束前作，I04／贡献因而必须讲本稿真正改变的保证依据。', '''
段首给时间目标的任务理由。`system states are required to achieve fast convergence ... for better control performance` 指收敛速度，不是约束违背问题。
概述已有收敛时间研究。`works focused on the convergence time` 给后面两项 finite-time 实例范围。
第一实例是 observer-based fuzzy control。`scheme ... for ... to achieve finite-time convergence` 保留适用的 strict-feedback 类别。
第二实例是 adaptive finite-time sliding-mode。`scheme ... for ... with some matched uncertainties` 明确匹配不确定性条件，不笼统归于任意扰动。
用 Nevertheless 指出时间界对初值的关系。`convergence time ... related to the initial conditions, which are sometimes unavailable` 提供改换 fixed-time 的技术理由；always 是源文概括，不作为无条件数学分类定义移用。
引入 fixed-time 路线作为上述关系的回应。`fixed-time control schemes have been proposed and applied ...` 不是本文首创 fixed-time 的声明。
保留已有 fixed-time＋BLF 实例。`controller combined with the BLF technique ... for uncertain nonstrict-feedback ...` 说明工具组合已有先例。
末句再承认 predefined constraints 已被保证的前作。`predefined constraints can be guaranteed` 使段落终点是可继承能力，不是“此前没有联合性能”。
''')
add('Fuzzy2023','I04','把 FLS、BLF 与 fixed-time tracking 的范围汇总为当前研究。','两项目标已分别解释；后接贡献的设计对象及证明改变，没有 roadmap 段。', '''
`the problem of fixed-time tracking control is discussed for uncertain robot systems based on the FLS and the BLF technique` 汇总对象、任务、工具。Motivated by 只是原文起句方式。
`major contributions ... can be listed as follows` 将科学范围交给三条具体责任，不另起应用背景。
''')
add('Fuzzy2023','C01','约束工具如何保证瞬态性能。','回应 I02 的责任，句内因果以输出约束不被违反为支撑。', '''
`symmetric BLF is designed to avoid the violation of the output constraints` 接 `thus ... transient performance ... guaranteed`；设计工具→约束作用→性能保证，而不是一句“提高鲁棒性”。分号为源文标点。
''')
add('Fuzzy2023','C02','用自适应律证明信号有界，从而放松既有权重估计有界假设。','补充“保证依赖什么”的实质改进：将前作作为假定的性质转成本文证明责任。', '''
`adaptive law is proposed such that the boundedness of all the closed-loop signals can be proved`，设计对象是律，证明对象是信号有界性，不是权重值可以精确测得。
`Then, the assumption that the weight estimation is bounded ... can be relaxed` 的 Then 连接上一证明与假设变化；不等于全部前提被删除。
''')
add('Fuzzy2023','C03','将实际固定时间跟踪保证与初始条件关系写清。','回应 I03 的时间要求；结束贡献后直接进 §II。', '''
`tracking performance ... can achieve practical fixed-time convergence regardless of the initial conditions`，practical 修饰保证，不能移成无条件精确到零；regardless of 只点出初值关系。
''')

add('ESO2017','I01','海洋应用对精确控制提出轨迹跟踪／定点保持责任。','应用只用两句完成；下一段直接解释实现这些控制要求面临哪些真实物理未知项。', '''
以机器人类型及海洋任务界定对象。`robots, including ... , have been increasingly employed to expand ...` 的 including 是系统范围，employed 后给用途。
由应用收益推出控制精度要求及其作用。`high-precision controller ... is required, such that ... data ... and ... tracking or station keeping ...` 同时说明数据质量和运动任务，原句 To exploit 是源文目的起句。
''')
add('ESO2017','I02','展开未知扰动和模型不确定性的不同物理来源。','把 I01 的精度要求分解为需补偿的项；末句补充姿态导致参数变化，I03 可以按这些对象回查控制路线。', '''
段首亮出技术对象类别。`technical challenges ... such as ... disturbances and model uncertainties`，后面分别展开，不把二者同义化。
明确外界扰动来源。`disturbances ... include waves, tides, currents ...` 是扰动类型列表，不是文献堆砌。
给 ROV 特有的系缆外力。`external force caused by the cable ... should also be considered`，also 是向上一扰动集合添加一项带平台条件的力。
解释模型不确定性从哪里来。`are usually caused by the inaccurate hydrodynamic coefficients` 后接 CFD／水池数据的估计来源，和外部海流分开。
补充运行时参数变化。`different attitude ... cause the variation of the hydrodynamic coefficient` 将姿态变化接到同一系数，为未知动力学建立任务内来源。
''')
add('ESO2017','I03','承认已有不确定性／扰动控制，并用多句解释部分方案的机制与验证。','按 I02 两种未知项回查方法；I04 对刚列的 NN／模糊路线提出调参问题，而不是否认其近似能力。', '''
段首按科学困难归类路线。`Several methods, such as ... , have been introduced to address ...` 给 adaptive／robust／observer-based 的共同任务，不替代下文具体实例。
先给 ROV 的速度约束控制。`a robust adaptive controller considering the velocity constraints is proposed for ...`，considering 的对象是该文献的条件。
紧接上一控制方案内部动作。`model parameters are estimated online` 与 `Barrier Lyapunov function is applied in the Lyapunov synthesis` 不跳到另一篇。
第三句交代同一方案验证类型。`results are validated ... simulation`，原文 thought 保留但不推荐；这构成方案→机制→证据连续句组。
从函数近似能力推出 NN／FLS 路线。`Since ... approximate nonlinearities ... controllers ... applied ...` 的 Since 有明确能力原因。
实例给 AUV 跟踪和组合技术。`controller combining NN approximation with dynamics surface control is presented for trajectory tracking`，不是只说 NN 被用过。
继续解释上一例子减少计算的手段。`computational load is reduced by introducing ... minimal number of learning parameters`，结果对象与技术动作相接。
另一例子给低速欠驱动系统、未知参数与实验。`SMC is presented to steer ... and an experiment has justified ...`，原词 justified 不等于理论证明。
扩展到多水下机器人并交代仿真。`controller is extended to control ... and simulation results ...` 同句明确扩展对象与证据范围。
''')
add('ESO2017','I04','一整段承认近似能力，同时指出实用学习参数调整困难。','单句独立桥段：从 I03 的 NN／模糊方案切换到 I05 的扰动抑制路线，不是所有段都要长篇文献。', '''
`Although ... have the advantages ... , it is still a challenging task to adjust ... in real applications` 同时保留能力与实施限制；比较对象是 learning parameters，不是所有不确定性都不可近似。原文其数／代词不齐不需照抄。
''')
add('ESO2017','I05','SMC／ISMC 的跟踪能力、抖振代价及为何需要扰动补偿器。','由 I04 的实用限制转向另一可用路线；末句 compensator 接 I06 的估计后补偿，形成具体设计责任。', '''
段首先给 SMC 的扰动抑制作用。`SMC ... for ... with disturbances` 提供路线理由；As an／obvious attentions 为源文表达，不是共同必选写法。
穿插 ESO 自适应控制的跨域例子。`control ... for power converters to reject ...` 是扰动／参数抑制能力的旁证，不是 SMC 分类下纯粹同类实例。
下一句继续该 power converter 的真实原型证据。`experiment ... prototype ... control performance`，原文主谓一致错误保留，不从字面推出本文实验结论。
给 surface vessel 控制的两种滑模面。`controller, which uses two sliding surfaces for ... , is applied to ...` 分别指 surge 与 lateral 误差。
又给 switched stochastic systems 的控制路线。`SMC is proposed ...` 接不同系统的技术挑战，不应把这些系统默认为水下机器人。
再缩到 ROV 的 ISMC。`ISMC ... proposed for trajectory tracking of ROVs` 将跟踪目标接到积分滑模。
连续解释 ISMC 为什么改善跟踪。`Because of ... additional error-integral term ... more accurate ... than conventional SMC` 明确改动项、性能维度和比较对象。
补充 AUV 数据获取不足／时延的 ISMC 用途。`ISMC is introduced to overcome ...` 是另一个任务条件，原句重复 overcome 不推广为成熟共性。
明确这条路线的剩余代价。`major shortcoming ... chattering ... not only causes energy losses but also reduces ... smoothness` 抖振后果分为能耗和运动平滑。
先承认已有减抖方法。`several methods, such as ... , have been proposed` 回应代价，而不是冒称此前无人减抖。
给自适应连续补偿的具体实例。`SMC is presented via an adaptive term, which continuously compensates for ...` 命名补偿项及未知动力学对象。
给当前选择补偿器的条件性理由。`upper bound ... may be large` 接 `SMC without a compensator ... serious chattering`，不是任意 SMC 必定严重抖振。
将论述收成待设计对象。`Therefore, it is necessary to design a compensator ... to reduce chattering` 交给下一段观察器提供补偿信息。
''')
add('ESO2017','I06','先定义估计—补偿信息链，再比较扰动观察器的估计对象与整定折中。','接 I05 的补偿器需求；已有观察器同时估计未知项和不可测状态的能力接到 I07 当前速度不可直接测量的条件。段末带宽折中限定观察器整定。', '''
段首不是纯报术语，而是给动作顺序。`design an observer to estimate ... , followed by ... compensate for the estimated disturbance` 将估计输出明确交给控制输入。
`Such disturbance observers include ...` 给上一角色的可用类型，sliding mode／high-gain／ESO 不是无目的目录。
文献方案给 launch vehicle 的 observer-based SMC。`controller based on ... observer is proposed for ...` 保留对象所属领域。
下一句接同一 observer 的两项作用。`observer ... to estimate ... and to reduce the control gain`，估计扰动与降低控制增益并非同一输出对象。
另例给 ROV output feedback 及所考虑未知项。`control that considers ... is presented` 的从句列 unmodeled dynamics／measurement errors 等，用来界定范围。
再举 hydraulic systems 的 mismatched disturbance。`backstepping control based on an ESO ... to handle ...` 保留扰动类型，不把 mismatched 丢成一般未知扰动。
下一句补充该 observer 的估计责任。`estimates not only ... model uncertainties but also ... unmeasured states` 为本文联合扰动与速度估计提供前作能力。
另一个 ESO 例子讲大外扰抑制。`backstepping control ... to suppress large ... disturbances` 不否认先前 ESO 已处理大扰动。
段末承认观察器带宽选择的折中。`bandwidth ... chosen in accordance with two conflicting aspects ...`，两个方面是最大负载能力与动态性能，不是为了造段末 gap。
''')
add('ESO2017','I07','真实传感条件推出速度状态估计与输出反馈责任，并回查相应前作。','先宣布平台和拟采用路线，但随后继续解释设计为何需要；无直接速度测量把 I06 的 observer 能力接到当前任务，I08 才汇总 MIMO-ESO。', '''
先给当前控制路线和抓取试验台。`we design ... controller ... and experiment ... test bed` 是局部作者设计已出现，不代表文献讨论必须结束。
命名 onboard sensors 与可测量量。`sensors ... are equipped to measure the depth and attitude` 给深度传感器／IMU 的实际输出。
再命名外部 VPS 测位置。`position ... is measured by ...` 后补光源怎样被捕获，形成位置获取条件。
明确缺失的可测量量。`there is no direct measurement of velocity` 是由前两句形成的本平台条件，不是整个领域无速度传感。
从这个缺失推出 output feedback，并给直接微分的控制代价。`output feedback is required ... as ... differential ... may degrade ...` 的 as 给因果依据。
将未测量状态交给 observer。`... used to estimate the unmeasured states` 接回 I06 的信息链；原文 observes／always 保留，不作为统一用词与普遍性断言。
第一状态估计文献给 ROV 速度、NN terminal sliding mode 和模型条件。`observer is presented to estimate ... which considers ...`，把不可测量量命名为 velocity。
另一项 NN observer 仍针对速度测量缺失。`observer ... to address the problem of estimating ... velocities`，不是改变本文测量事实。
terminal sliding mode observer 例子分别给估计动作及误差保证。`estimate the velocity` 接 `estimation error ... converge to zero in a finite time`，finite-time 是该文献保证。
插入 human upper limbs 的 adaptive backstepping。`control ... in the presence of ...` 展示跨系统不确定性条件，但未像相邻句一样明确状态估计动作，和本段主线联系较弱。
给 quadrotor 的 output feedback 跟踪任务。`controller is designed to address ... with ... disturbances ... uncertainties` 保留系统对象。
下一句说明同一文献怎样得到未测速度。`unmeasurable linear and angular velocities are estimated by ... filters` 明确 filters 的估计输出。
UAV 文献同时给 controller 及 observer 两种角色。`controller is designed ... and ... observer is applied to estimate ...`，不可测状态和未知外扰各自保留。
high-gain observer 例子给电液系统的 full states 估计，为 I08 引用 high-gain 思想提供来源。
末句按模拟／实验归纳水下机器人文献证据。`controllers ... are verified by simulations ... other ... by experiments` 承認已有实机研究，不把本文实现写成首个水下控制实验。
''')
add('ESO2017','I08','把减抖、扰动／状态估计、自适应界估计、控制分析及平台实现连成当前方案。','回应 I02 未知项、I05 减抖、I07 不可测速度；随后贡献把观察器、控制律和实机比较分列。', '''
段首给补偿作用和实现路线。`disturbance compensation approach is utilized ... based on ... MIMO-ESO`，eliminate chattering 是源文自己的主张强度，不能视为通用保证。
说明技术继承并明确估计对象。`a MIMO-ESO is proposed to estimate the unknown disturbances and the unmeasured states` 引用 ESO model／high-gain observer，不虚构完全新来源。
用自适应控制补充另一种估计责任。`The bounds of the uncertainties are also estimated` 区分界估计与上一句状态／扰动估计。
将 Lyapunov analysis 接到最终控制律设计。`analysis is involved to design ...` 不是只在结尾点名分析工具。
分开 equivalent 与 switch controller，再给理论跟踪误差结论。`controller ... includes two parts ... guarantees ... error ... zero theoretically`，保证属于源文研究，不由“有两部分”本身自动成立。
把 proposed controller 接到真实六推进器平台。`is successfully implemented on ... propelled by six thrusters` 是实现证据，不是新增第四种控制模块。
`main contributions ... summarized as follows` 接分工清单，前六句已给具体内容。
''')
add('ESO2017','C01','观察器责任：未测速度和未知外扰估计。','同时回应 I07 的信息缺失和 I02 的物理扰动。', '''
`MIMO-ESO is developed to estimate the unmeasured velocity and the unknown external disturbances` 两个明确估计对象，不把估计改成直接测量。
''')
add('ESO2017','C02','控制责任：MIMO-ESO-based ISMC 的跟踪误差保证。','估计模块继续进入控制设计，而不是与控制器并列不相接。', '''
`ISMC is designed to ensure ... trajectory tracking error ... zero` 同时命名控制技术、依据和保证对象；原语法问题保留，保证条件须按作者实际研究替换。
''')
add('ESO2017','C03','证据责任：真实平台上的对照试验。','与前两条估计和控制不同，这一条承担实际比较验证。', '''
`Comparative studies with ... are carried out experimentally on ... to demonstrate ...` 将比较对象、实验类型、平台和证明目的写在一起。原词 `potential difference (PD)` 保留，复用前需核对术语，不默改源文。
''')
add('ESO2017','I09','按模型、观察器、ISMC 和实机证据安排文章。','观察器→控制器的章节次序与 I06／I08 的信息交接一致；没有要求所有贡献都在引言报告数值。', '''
组织提示后接 `Section II presents ... model and formulates the problem`，present 与 formulate 各有对象，原文用冒号。
`MIMO-ESO is derived to estimate ... disturbances ... velocities` 把下一章节的估计输出明确重复，保留接口。
`ISMC is proposed` 位于观察器之后，符合估计进入控制的依赖。
`Experimental results are shown ... followed by ... conclusion` 仅为后文安排，不是此处给比较结果数值。
''')

CHAINS = {
 'P17':'产品更新要求机器人适应 → 人示教经运动建模重现技能 → DS／DMP 提供稳定、可扩展运动表示 → 最优示范难得，多示范中有可保留的运动信息 → DMP 的非线性函数用 GMM 建模、GMR 检索估计，综合多示范生成运动 → 重现效果还取决于跟踪，未知载荷使动力学难预先获得 → RBFNN 近似动力学，控制器跟踪前一组件生成的关节轨迹 → 生成与跟踪共同承担真实执行。',
 'P05':'双臂协作具有载荷／空间优势，协调运动控制与路径规划也更复杂 → 紧持物体的前作不对应工具沿物面滑动的相对运动任务 → 该任务已有控制仍依赖已知动力学，且缺接触力分析 → 抓取物动力学难预知，NN 用于补偿 → 跟踪误差收敛与 NN 权重估计收敛不是同一责任 → NN 稀疏回归使 PE 严格，PPE 有局部重复输入能力但仍有输入／学习速度要求 → 将估计误差信息接入复合学习更新，在相对运动及未知动力学条件下设计控制，并以 PPE 放松激励要求 → 分别汇总任务框架、学习信息、条件放松及仿真分析。',
 'Fuzzy2023':'时变参数与外扰形成未知非线性 → NN／FLS 能近似并用于控制，已有工作已涉及固定时间与用户性能 → 本文选择同时关注瞬态约束和收敛时间 → 不良瞬态有风险，BLF 可处理约束，设计 symmetric BLF → 快速收敛另有需要，finite-time 时间与初值相关，转向 fixed-time 并承认已有约束组合 → 在 FLS＋BLF 的机器人跟踪设置中，分别设计输出约束工具、证明闭环信号有界的自适应律、建立不依赖初值的 practical fixed-time 跟踪 → 贡献包括从权重估计有界假定转向有界性证明。计算量及拓扑优化只是一条未来工作支线。',
 'ESO2017':'海洋探测的数据质量与轨迹／定点精度要求 → 海流等外扰、系缆力、流体参数误差及姿态变化妨碍控制 → NN／模糊自适应有近似能力但实际调参困难 → SMC／ISMC 能抑制扰动和改善跟踪，抖振造成能耗和平滑性代价 → 扰动补偿需要估计信息，观察器先估计再供控制补偿 → 当前深度／姿态／位置可测而速度不可直接测，直接微分又有代价 → MIMO-ESO 同时估计扰动和未测速度，自适应方法估计未知项的界 → ESO-based ISMC 由分析设计跟踪控制，并在六推进器平台做实机对照。'
}
TITLES = {
 'P17':'Robot Learning System Based on Adaptive Neural Control and Dynamic Movement Primitives',
 'P05':'Composite-Learning-Based Adaptive Neural Control for Dual-Arm Robots With Relative Motion',
 'Fuzzy2023':'Fixed-Time Fuzzy Control of Uncertain Robots With Guaranteed Transient Performance',
 'ESO2017':'Extended State Observer-Based Integral Sliding Mode Control for an Underwater Robot With Unknown Disturbances and Uncertain Nonlinearities'
}
for paper, units in SOURCE.items():
    assert set(NOTES[paper]) == {u['id'] for u in units}
    rows = [f'# {paper}：整节、完整段落及逐句表达分析','',TITLES[paper],'',
            f'[重新核对的完整引言](<{paper}-introduction.md>)｜[三层综合总结](report.md)','',
            'I／C 是定位号；S 是本段句号。英文完整段落按源文顺序保留，表中的句号对应其句子边界。长句中的分号、where／which 从句不另算独立句，表内仍分别解释不同科学动作。分析是本轮中文判断，不是论文原文。','',
            '## 完整科学主线','',CHAINS[paper],'',
            '## 各段任务与段间交接','',
            '| 原段 | 科学任务 | 承接和交出什么 |','|---|---|---|']
    for u in units:
        n=NOTES[paper][u['id']]
        rows.append(f"| [{u['id']}](#{u['id'].lower()}) | {n['task']} | {n['paragraph_handoff']} |")
    rows += ['', '## 完整段落与逐句拆解','']
    for u in units:
        n=NOTES[paper][u['id']]
        rows += [f'<a id="{u["id"].lower()}"></a>','',f'### {u["id"]}：{n["task"]}','',
                 '来源块：'+', '.join(u['blocks'])+'。','',
                 '> '+u['text'],'',n['paragraph_handoff'],'',
                 '| 句号 | 该句的科学动作、与相邻句的关系、真实英文实现 |','|---|---|']
        for i, note in enumerate(n['sentences'],1):
            rows.append(f'| S{i:02d} | {note} |')
        rows += ['']
    (OUT/f'{paper}-analysis.md').write_text('\n'.join(rows),encoding='utf-8')
(OUT/'analysis-notes.json').write_text(json.dumps(NOTES,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Rendered four complete paragraph/sentence analyses; no Skill or effect-test operations.')

"""One-off, source-mapped edits to the three Introduction learning drafts.

Publication text and earlier source audits remain untouched. Each replacement
below is an explicit local adaptation, not a new scientific claim.
"""
from pathlib import Path
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
SOURCE = ROOT / 'analysis/introduction-section-review-2026-10-06'
split = lambda s: re.split(r'(?<=[.!?])\s+(?=[A-Z])', s)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
curated = json.loads((SOURCE / 'curated-introductions.json').read_text(encoding='utf-8'))
units = {(p, u['id']): u for p, us in curated.items() for u in us}
original = {k: split(u['text']) for k, u in units.items()}
changes = {}

def adapt(paper, unit, sentence, *text):
    changes[(paper, unit, sentence)] = list(text)

adapt('P17', 'I01', 1,
      'Recently, robots have been widely applied in various fields, especially in manufacturing.')
adapt('P17', 'I02', 2,
      'In comparison to conventional methods, such as interpolation techniques, DS offers a flexible solution to model stable and extensible trajectories.')
adapt('P17', 'I02', 4,
      'In [4], an approach based on DS was used to learn human motions.',
      'The unknown mapping of the DS was approximated using a neural network (NN) called extreme learning machine [5].')
adapt('P17', 'I02', 5,
      'The DS-based motion model learned using extreme learning machine showed adequate stability and generalization.')
adapt('P17', 'I02', 6,
      'However, the DS-based motion learning approach using extreme learning machine required considerable demonstration data for training.')
adapt('P17', 'I02', 7,
      'In contrast, the dynamic movement primitive (DMP), which is based on a nonlinear DS [6], only requires one demonstration to model motion.',
      'The DMP models the movement trajectory as a spring-damper system integrated with an unknown function to be learned.')
adapt('P17', 'I03', 4,
      'While the studies in [7] and [8] employed multiple DMPs to compose a complete action, another study [9] used multiple DMPs to model a style-adaptive trajectory.',
      'The style of the generated motion could be changed by modulating the weight parameters that were coupled with the goals.')
adapt('P17', 'I03', 1,
      'DMPs have often been employed to solve robot learning problems because of their flexibility.')
adapt('P17', 'I03', 5,
      'The work in [10] indicates that optimal demonstration is difficult to obtain and multiple demonstrations can encode the ideal trajectory implicitly.')
adapt('P17', 'I04', 6,
      'In [3], a learning approach named stable estimator of dynamical systems (SEDS) was proposed for motion modeling.',
      'The unknown function in SEDS was modeled using GMR.')
adapt('P17', 'I04', 5,
      'In contrast with the DS-based and DMP-based motion-learning methods discussed above, GMM combined with GMR can provide additional motion information for robots when learning from multiple demonstrations.')
adapt('P17', 'I04', 8,
      'Both SEDS and DS-GMR exploit the robustness and generalization capability of the DS as well as the excellent learning performance of the probabilistic methods.')
adapt('P17', 'I05', 1,
      'To take advantage of the performance of the DS and the probabilistic approach, we integrate DMP and GMM into our robot learning system.',
      'The nonlinear function of DMP is modeled with GMM.',
      'The estimate of the nonlinear function of DMP is retrieved through GMR.')
adapt('P17', 'I05', 2,
      'The DMP motion model integrating GMM and GMR enables the robot to extract more features of the motions from multiple demonstrations and to generate motions that synthesize these features.')
adapt('P17', 'I05', 3,
      'In [16], the original DMP was learned using locally weighted regression (LWR).',
      'In [17], locally weighted projection regression (LWPR) was employed to optimize the bandwidth of each kernel of LWR.')
adapt('P17', 'I05', 4,
      'Despite the added complexity of the learning procedure, LWR and LWPR enable the DMP to learn from only one demonstration.')
adapt('P17', 'I05', 5,
      'Reservoir computing [18] is another method used to approximate the nonlinear function of DMP, but its computing efficiency is less than that of GMR.')
adapt('P17', 'I06', 2,
      'Generally, model-based control performs better if the robot dynamic model is accurate enough [19].')
adapt('P17', 'I06', 4,
      'Approximation-based controllers have been designed to overcome uncertainties in the robot dynamics.')
adapt('P17', 'I06', 5,
      'Approximation-based controllers utilize function approximation tools to learn the nonlinear characteristics of the robot dynamics.')
adapt('P17', 'I06', 7,
      'In [23], the backpropagation NN (BPNN) was utilized to approximate the unknown nonlinear function in the model of the vibration suppression device.',
      'In [24], the radial basis function NN (RBFNN) was utilized to approximate the unknown nonlinearity of the telerobot system.')
adapt('P17', 'I06', 8,
      'In comparison to BPNN, the learning procedure of RBFNN is based on local approximation.',
      'Thus, RBFNN can avoid getting stuck in the local optimum and has a faster convergence rate.')
adapt('P17', 'I06', 9,
      'Besides, the number of hidden layer units of RBFNN can be adaptively adjusted during the training phase.',
      'The adaptive adjustment of the number of hidden layer units makes RBFNN more flexible and adaptive.')
adapt('P17', 'I07', 1,
      'In this paper, an NN-based controller is designed to guarantee the tracking performance of the manipulator in joint space.',
      'RBFNN is employed in the NN-based controller to approximate the nonlinear functions of the robot dynamics.')
adapt('P17', 'I07', 2,
      'The stability of the NN-based controller is guaranteed by the Lyapunov stability theory.')
adapt('P17', 'I07', 3,
      'The robot learning system consists of the motion generation component and the trajectory tracking component (Fig. 1).')
adapt('P17', 'I07', 4,
      'The motion generation component utilizes the DMP-based motion model to learn and generalize motion skills.',
      'The motion skills learned and generalized using the DMP-based motion model are represented as a set of trajectories in joint space.')
adapt('P17', 'I07', 5,
      'The trajectory tracking component employs the adaptive controller to track the joint-space trajectories generated by the motion generation component.',
      'RBFNN is incorporated into the adaptive controller to compensate for the uncertain robot dynamics.')
adapt('P17', 'I08', 1,
      'We present a novel and complete robot learning framework that considers the performance of both motion generation and trajectory tracking.')
adapt('P17', 'I08', 3,
      'However, the constraints that guarantee the stability of SEDS are derived by the Lyapunov theory.',
      'The Lyapunov-derived stability constraints of SEDS increase the complexity of learning the SEDS motion model.')
adapt('P17', 'I08', 4,
      'In contrast to [3] and [25] which considered only motion modeling, our robot learning system is enhanced by an NN-based controller.',
      'The effect of dynamic environments on the robot can be compensated by neural learning.')
adapt('P17', 'I08', 5,
      'The robot learning framework integrating motion generation and NN-based trajectory tracking enables the robot to perform the learned motions steadily and more robustly in the real world.')

adapt('P05', 'I01', 1,
      'Coordination control of dual-arm robots has received increasing attention due to the advantages of dual-arm robot systems over traditional single-arm robot systems, including stronger payload capability, larger workspace, and more flexibility.')
adapt('P05', 'I01', 2,
      'Thus, dual-arm robots have been involved in many applications, such as intelligent assembly, repair in space, and assistance for elderly people [1]–[3].')
adapt('P05', 'I02', 1,
      'In [9], an adaptive decentralized control scheme was proposed to address the object handling problem of a cooperative robot.',
      'An implicit force control scheme was employed to simultaneously regulate the force and position.')
adapt('P05', 'I02', 2,
      'In [10], a decentralized control structure for multiple mobile manipulators was developed.',
      'The internal forces were constrained by employing an augmented object model for the multiple systems with a virtual linkage.')
adapt('P05', 'I02', 4,
      'The adaptive decentralized controller in [9], the decentralized control structure in [10], and the grasp-space analysis method in [11] were developed under the assumption that the object is firmly held by the robotic arms such that no relative motion occurs between the arms and the object.')
adapt('P05', 'I02', 5,
      'However, in practical applications, such as polishing, grinding, and welding, the robot end-effectors need to operate along the object’s surface.',
      'Sliding movements usually occur between the robotic arm and the object in these surface operations [12]–[14].')
adapt('P05', 'I03', 4,
      'In [16], a brain-actuated control architecture was proposed for dual-arm robots to perform the asymmetric bimanual task.',
      'Electroencephalogram signals and visual stimulation were employed to send control commands through a brain–machine interface.')
adapt('P05', 'I03', 5,
      'However, the relative impedance controller in [15] and the brain-actuated control architecture in [16] were designed under the assumption that the robot dynamics are fully available.',
      'The studies in [15] and [16] did not provide a stability analysis of the contact force between the robotic arm and the object.')
adapt('P05', 'I04', 3,
      'Without a precise dynamic model, model-based control becomes invalid and may degrade control performance.')
adapt('P05', 'I04', 1,
      'The dynamic model of the robot system is of great importance in controller design [17]–[22].',
      'However, the robot dynamic model is often unavailable in practice.')
adapt('P05', 'I04', 2,
      'For example, in carrying tasks, the dynamics of the grasped object are hard to obtain in advance.')
adapt('P05', 'I04', 5,
      'Neural networks (NNs) alleviate the modeling difficulties of nonlinear systems through their powerful approximation ability [23].')
adapt('P05', 'I04', 6,
      'Thus, NN-based control has been widely used in controller design for nonlinear robotic systems [24]–[32].')
adapt('P05', 'I06', 5,
      'In [41], a partial persistent excitation (PPE) condition was presented as an alternative to the traditional PE condition for neural networks.')
adapt('P05', 'I06', 2,
      'Nevertheless, convergence guarantees for the NN weights are more difficult to establish.')
adapt('P05', 'I06', 3,
      'It is well known that the persistent excitation (PE) condition is important to guarantee convergence of NN weight estimation [40].')
adapt('P05', 'I06', 6,
      'For a radial basis function neural network (RBFNN) defined in a regular lattice, it has been proven that neural nodes can be partially activated by any recurrent NN input trajectory that remains in the local region [41].')
adapt('P05', 'I06', 7,
      'In [42], the PPE-based partial activation of RBFNN nodes was employed in the control design of nonlinear strict-feedback systems to guarantee system stability and accurate NN approximation.')
adapt('P05', 'I06', 8,
      'However, the NN input trajectory still needs to be recurrent.',
      'A small input excitation strength may lead to slow NN learning.')
adapt('P05', 'I07', 4,
      'We therefore develop a composite learning controller for the dual-arm robot to perform bimanual relative motion tasks.')
adapt('P05', 'I07', 1,
      'The work in [43] indicates that parameter convergence can be improved if information about the parameter estimation error can be integrated into the parameter adaptation.')
adapt('P05', 'I07', 3,
      'In [45], the NN weight estimation error was integrated into the adaptation scheme of a class of nonlinear systems to achieve convergence of the NN weights.')
# The existing selection audit excludes self-reported scarcity/priority claims
# from default learning. Keep S5 in the audit; the design-to-PPE handoff remains.
adapt('P05', 'I07', 5)
adapt('P05', 'I07', 6,
      'Moreover, in contrast to the work in [46], a PPE condition is also introduced in the NN weight estimation scheme to relax the requirement of the PE condition.')
adapt('P05', 'C2', 1,
      '2) A novel composite learning algorithm is designed for NN weight adaptation.',
      'The composite learning algorithm allows information about the NN weight estimation errors to be appropriately integrated into the NN weight adaptation law to improve estimation performance.')
adapt('P05', 'C3', 1,
      '3) A partial persistent excitation condition is introduced for NN weight adaptation such that the requirement of the conventional PE condition can be greatly relaxed.')

adapt('ESO2017', 'I01', 1,
      'Underwater robots, including autonomous underwater vehicles (AUVs), remotely operated vehicles (ROVs), and underwater gliders, have been increasingly employed to expand human capabilities in marine resource exploration and marine scientific research.')
adapt('ESO2017', 'I01', 2,
      'To exploit the full potential benefits provided by underwater robots, a high-precision controller for underwater robots is required to guarantee the quality of the collected data and to secure high precision in trajectory tracking or station keeping [1]–[6].')
adapt('ESO2017', 'I03', 6,
      'In [7], an adaptive controller combining NN approximation with dynamic surface control is presented for trajectory tracking of an AUV.')
adapt('ESO2017', 'I03', 7,
      'The computational load is reduced by introducing an NN learning method using a minimal number of learning parameters.')
adapt('ESO2017', 'I06', 4,
      'The sliding mode observer is presented to estimate the unknown external disturbances and to reduce the control gain.')
adapt('ESO2017', 'I06', 6,
      'In [32], backstepping control based on an ESO is proposed to handle mismatched disturbances in hydraulic systems.')
adapt('ESO2017', 'I06', 7,
      'The ESO estimates not only the model uncertainties but also the unmeasured states.')
adapt('ESO2017', 'I08', 1,
      'In this paper, a disturbance compensation approach based on a multiple-input multiple-output extended state observer (MIMO-ESO) with a simple structure is utilized to eliminate chattering.')
adapt('ESO2017', 'I08', 2,
      'The ESO model [32] and the high-gain observer [39] motivate the design of the MIMO-ESO.',
      'The MIMO-ESO is proposed to estimate the unknown disturbances and the unmeasured states.')

adapt('Fuzzy2023', 'I02', 1,
      'In practice, undesirable transient performance may lead to system instability and sometimes even safety problems.')
adapt('Fuzzy2023', 'I02', 2,
      'Recently, barrier Lyapunov functions (BLFs) have been widely used to enforce state and output constraints in nonlinear control problems [12]–[16].')
adapt('Fuzzy2023', 'I02', 4,
      'In [14], a new command-filtered fuzzy controller has been proposed for a class of unknown nonlinear systems to handle full-state constraints and finite-time convergence simultaneously.')
adapt('Fuzzy2023', 'I03', 1,
      'In many industrial systems, fast convergence of the system states is required for better control performance.')
adapt('Fuzzy2023', 'I03', 2,
      'Previous studies have focused on the convergence time of the systems [17]–[19].')
adapt('Fuzzy2023', 'I03', 5,
      'Nevertheless, for existing finite-time control schemes, the convergence time of the systems is always related to the initial conditions.',
      'The initial conditions are sometimes unavailable.')
adapt('Fuzzy2023', 'I03', 8,
      'In [21], an adaptive event-based fixed-time control scheme has been proposed for active vehicle suspension systems.',
      'The predefined constraints on the active vehicle suspension systems can be guaranteed.')
adapt('Fuzzy2023', 'I04', 1,
      'We therefore investigate fixed-time tracking control for uncertain robot systems using fuzzy logic systems (FLSs) and the BLF technique.')
adapt('Fuzzy2023', 'C1', 1,
      '1) A novel symmetric BLF is designed to avoid violation of the output constraints.',
      'Thus, the desired transient performance of the robot system can be guaranteed.')
adapt('Fuzzy2023', 'C3', 1,
      '3) Robot tracking can achieve practical fixed-time convergence regardless of the initial conditions.')
adapt('Fuzzy2023', 'C2', 1,
      '2) A novel adaptive law for fuzzy weight estimation is proposed such that the boundedness of all the closed-loop signals can be proved.')
adapt('Fuzzy2023', 'C2', 2,
      'Then, the assumption that fuzzy weight estimates are bounded in recent fixed-time control research [23]–[25] can be relaxed.')

# Positive analysis of adapted clauses. Only affected expression table cells are
# replaced. The accepted scientific relationships remain their organizing basis.
expression_cells = {}
def cell(p, u, s, subjects, implementation):
    expression_cells[(p, u, s)] = (subjects, implementation)

cell('P17','I02',2,'`DS`—`offers`—`a flexible solution to model stable and extensible trajectories`。',
     '`In comparison to` 给传统方法这一参照；DS 作主语，`offers a ... solution to` 写表示能力，`stable and extensible` 同时限定轨迹。')
cell('P17','I02',4,'`an approach based on DS`—`was used`—`to learn human motions`；`the unknown mapping of the DS`—`was approximated`—通过 extreme learning machine。',
     '`In [4],` 后给方法和任务。续句用 DS 的未知映射作主语，`approximated using` 写逼近手段，[5] 定位所用 NN 工具。')
cell('P17','I02',5,'`The DS-based motion model learned using extreme learning machine`—`showed`—`adequate stability and generalization`。',
     '主语同时明确运动模型的 DS 身份和学习工具；`showed` 接已有能力，`adequate` 保留该语境下的满足程度。')
cell('P17','I02',6,'`the DS-based motion learning approach using extreme learning machine`—`required`—`considerable demonstration data for training`。',
     '`However` 从已承认的能力进入训练需求；主语明确同一模型的学习方法，`required A for B` 给数据量和用途。')
cell('P17','I02',7,'`the DMP`—`only requires`—一次示教；`The DMP`—`models`—轨迹为弹簧阻尼系统及待学习未知函数。',
     '`In contrast` 保持示教量比较；下一句以 DMP 作主语，用 `models A as B integrated with C` 写同一方法的表示组成。')
cell('P17','I03',4,'`the studies in [7] and [8]`—`employed`—多个 DMP；`another study [9]`—`used`—多个 DMP 表示风格可调轨迹；`The style`—`could be changed`—通过目标耦合权值。',
     '`While` 保持动作组合与轨迹风格的对照。续句让生成运动的风格作主语，用 `by modulating` 和 `coupled with` 写调节手段及权值与目标的联系。')
cell('P17','I03',1,'`DMPs`—`have often been employed`—`to solve robot learning problems`。',
     '`employed to solve` 给方法用途；`because of their flexibility` 说明选择理由，`their flexibility` 在同句中保留 DMP 的能力身份。')
cell('P17','I03',5,'`The work in [10]`—`indicates`—最优示教难得，多次示教可以隐含编码理想轨迹。',
     '`The work in [xx] indicates that` 接文献判断；`difficult to obtain` 写可得性，`encode ... implicitly` 写信息能力，二者共同支持下一句的整合方向。')
cell('P17','I04',6,'`a learning approach named SEDS`—`was proposed`—`for motion modeling`；`The unknown function in SEDS`—`was modeled`—`using GMR`。',
     '`In [3], ... named ... was proposed for` 命名方法和任务；续句以 SEDS 中的未知函数作主语，`modeled using` 给 GMR 的建模职责。')
cell('P17','I04',5,'`GMM combined with GMR`—`can provide`—多示教学习中的额外运动信息。',
     '`In contrast with` 保留前文 DS／DMP 运动学习方法这一比较范围；`combined with` 写组合，`provide A for B` 给信息与使用者，`when learning from multiple demonstrations` 保留情境。')
cell('P17','I04',8,'`Both SEDS and DS-GMR`—`exploit`—DS 的鲁棒／泛化能力及概率方法的学习性能。',
     '两个具体方法名称共同作主语；`exploit` 接可利用的能力，`as well as` 连接另一类能力，为组合设计提供依据。')
cell('P17','I05',1,'`we`—`integrate`—DMP 与 GMM 进入机器人学习系统；`The nonlinear function of DMP`—`is modeled`—用 GMM；同一函数的估计—`is retrieved`—通过 GMR。',
     '`To take advantage of` 接前文能力，`integrate A and B into C` 写组合。两句接续命名 DMP 非线性函数及其估计，`modeled with` 和 `retrieved through` 分别给建模与回归职责。')
cell('P17','I05',2,'`The DMP motion model integrating GMM and GMR`—`enables`—多示教特征提取与合成运动生成。',
     '组合后的具体运动模型作主语，`enables A to B and to C` 写两项相接作用。`extract ... from` 给输入来源，`motions that synthesize these features` 保持输出与同一特征的关系。')
cell('P17','I05',3,'`the original DMP`—`was learned`—使用 LWR；`LWPR`—`was employed`—优化 LWR 的核带宽。',
     '`In [16]` 和 `In [17]` 分别定位学习与带宽优化工作；`learned using`、`employed to optimize` 区分两个工具的责任，`bandwidth of each kernel` 明确被优化量。')
cell('P17','I05',4,'`LWR and LWPR`—`enable`—DMP 从一次示教学得。',
     '`Despite` 保留学习复杂性这一代价；两个学习工具具名作主语，`enable ... to learn from only one demonstration` 保留能力范围及示教量。')
cell('P17','I05',5,'`Reservoir computing`—`is another method used to approximate`—DMP 的非线性函数；`its computing efficiency`—`is less than`—GMR 的计算效率。',
     '函数名称接住同一 DMP 学习对象；`but` 引入效率比较，`its computing efficiency` 与 `that of GMR` 保持明确的技术指标及比较双方。')
cell('P17','I06',2,'`model-based control`—`performs better`—在机器人动力学模型足够准确时。',
     '`Generally` 给概括语境；`if the robot dynamic model is accurate enough` 明确模型身份，保留性能改善所需的精度条件。')
cell('P17','I06',4,'`Approximation-based controllers`—`have been designed`—`to overcome uncertainties in the robot dynamics`。',
     '逼近控制器直接接机器人动力学不确定性，`designed to overcome` 使控制职责与前句的信息条件连续。')
cell('P17','I06',5,'`Approximation-based controllers`—`utilize`—函数逼近工具，`to learn` 机器人动力学非线性特征。',
     '重复逼近控制器名称；`utilize A to B` 交代工具及职责，`characteristics of the robot dynamics` 保持被学习对象的技术身份。')
cell('P17','I06',7,'`the BPNN` 和 `the RBFNN`—分别 `was utilized`—逼近振动抑制装置与遥操作机器人中的未知非线性。',
     '两句分别用 `In [23]` 与 `In [24]` 定位同一功能的文献；`utilized to approximate` 保持方法、系统及各自逼近对象的对应。')
cell('P17','I06',8,'`the learning procedure of RBFNN`—`is based on`—局部逼近；`RBFNN`—`can avoid ... and has ...`—局部最优及收敛速率。',
     '`In comparison to BPNN` 明确参照。下一句用 `Thus` 和 RBFNN 名称连接局部逼近基础与作用，`local approximation`、`local optimum`、`convergence rate` 保留不同科学身份。')
cell('P17','I06',9,'`the number of hidden layer units of RBFNN`—`can be adaptively adjusted`；该数量的自适应调节—`makes`—RBFNN 更灵活、更具适应性。',
     '`Besides` 补充能力，`during the training phase` 限定调节阶段。下一句明确以该数量的自适应调节作主语，接相应属性变化。')
cell('P17','I07',1,'`an NN-based controller`—`is designed`—保证机械臂关节空间跟踪性能；`RBFNN`—`is employed`—逼近机器人动力学非线性函数。',
     '`In this paper` 进入当前设计，`designed to guarantee` 写职责，`in joint space` 给范围。续句明确 RBFNN 在同一控制器中的函数逼近职责。')
cell('P17','I07',2,'`The stability of the NN-based controller`—`is guaranteed`—`by the Lyapunov stability theory`。',
     '性质主语保留 NN 控制器身份，`stability of` 接同一设计，`guaranteed by` 给理论依据。')
cell('P17','I07',3,'`The robot learning system`—`consists of`—运动生成与轨迹跟踪模块。',
     '系统名称直接作主语，`consists of A and B` 写组成；框架图定位附在句末，后文继续用具体模块名称连接职责。')
cell('P17','I07',4,'`The motion generation component`—`utilizes`—DMP 模型以学习和泛化技能；同一 DMP 模型学得并泛化的运动技能—`are represented`—为关节空间轨迹。',
     '两句分别命名模块与运动技能，`utilizes ... to learn and generalize` 给职责，`represented as` 接技能表示和轨迹输出。')
cell('P17','I07',5,'`The trajectory tracking component`—`employs`—自适应控制器以跟踪生成模块产生的关节空间轨迹；`RBFNN`—`is incorporated`—进入同一控制器以补偿不确定动力学。',
     '跟踪模块接同一关节空间轨迹，`generated by` 命名来源。续句 `incorporated into ... to compensate for` 保持工具、控制器及补偿对象的连接。')
cell('P17','I08',1,'`We`—`present`—同时考虑运动生成和跟踪性能的完整机器人学习框架。',
     '`We present` 直接给总体工作，`framework that considers the performance of both A and B` 明确两项责任范围。贡献强度按作者证据选择。')
cell('P17','I08',3,'SEDS 稳定性约束—`are derived`—通过 Lyapunov 理论；同一约束—`increase`—SEDS 运动模型的学习复杂性。',
     '`However` 进入 SEDS 条件，两句分别交代约束依据及学习代价。约束与运动模型均保留 SEDS 身份，使理论条件与作用对象连续。')
cell('P17','I08',4,'`our robot learning system`—`is enhanced`—由 NN 控制器增补；动态环境对机器人的影响—`can be compensated`—通过神经学习。',
     '`In contrast to [3] and [25]` 保留仅考虑运动建模的指定范围。两句分别用 `enhanced by` 写控制增补、`compensated by` 写相应环境影响的补偿来源。')
cell('P17','I08',5,'整合运动生成与 NN 轨迹跟踪的机器人学习框架—`enables`—机器人稳定、稳健地执行学得运动。',
     '完整框架名称接 `enables ... to perform`，`steadily`、`more robustly` 修饰运动执行，`in the real world` 给作用场景，回收生成与跟踪两项责任。')
cell('P05','I01',1,'`Coordination control of dual-arm robots`—`has received increasing attention`—由于双臂系统相对单臂系统的负载、工作空间和灵活性优势。',
     '`due to the advantages of A over B` 明确优势属于哪类系统及其参照；`including` 给具体能力，领域价值与后续应用连续。')
cell('P05','I01',2,'`dual-arm robots`—`have been involved`—智能装配、空间修理及老年人辅助等应用。',
     '`Thus` 接能力与应用，`such as` 引入真实用途，应用名称直接写 `intelligent assembly`、`repair in space`、`assistance for elderly people`。')
cell('P05','I02',1,'`an adaptive decentralized control scheme`—`was proposed`—处理协作机器人物体操作；`An implicit force control scheme`—`was employed`—同时调节力与位置。',
     '`In [9], ... was proposed to address` 定位方法与问题。续句 `employed to simultaneously regulate A and B` 补充同一文献的控制机制和两个量。')
cell('P05','I02',2,'`a decentralized control structure`—`was developed`—用于多移动机械臂；`The internal forces`—`were constrained`—通过含虚拟连杆的增广物体模型。',
     '`In [10]` 后给结构及适用系统。续句让内力作主语，`constrained by employing` 给约束手段，`with a virtual linkage` 保持模型组成。')
cell('P05','I02',4,'[9] 自适应分散控制器、[10] 分散结构与 [11] 抓持空间负载方法—`were developed`—在牢固抓持和无相对运动假设下。',
     '以具体控制类型及引文共同作主语，`under the assumption that` 保留条件，`such that` 连接牢固抓持与臂／物体之间无相对运动。')
cell('P05','I02',5,'`the robot end-effectors`—`need to operate`—沿物体表面；`Sliding movements`—`usually occur`—在这些表面操作的机械臂与物体之间。',
     '`However` 对接任务条件，`such as` 给应用。两句分别写末端运动需要和相应滑动，`along`、`between` 保持空间关系，[12]–[14] 定位这组应用。')
cell('P05','I07',4,'`We`—`therefore develop`—复合学习控制器，供双臂机器人完成相对运动任务。',
     '`therefore` 接估计误差信息改善学习的依据，`develop A for B to C` 写设计、系统及任务。')
cell('P05','I07',1,'`The work in [43]`—`indicates`—参数收敛可以在参数估计误差信息进入参数自适应时改善。',
     '`The work in [xx] indicates that` 给文献判断，`if` 保留改善条件；`information about the parameter estimation error` 和 `integrated into the parameter adaptation` 明确所用信息及其去向。')
cell('P05','I07',3,'`the NN weight estimation error`—`was integrated`—进入非线性系统自适应方案以实现 NN 权值收敛。',
     '`In [45]` 定位工作，被利用的 NN 权值估计误差作主语，`integrated into ... to achieve` 连接信息、去向与权值收敛目标。')
cell('P05','I07',6,'`a PPE condition`—`is also introduced`—进入 NN 权值估计方案以放宽 PE 要求。',
     '`Moreover` 增加设计职责，`in contrast to the work in [46]` 保留比较对象；`introduced in ... to relax` 明确加入位置和条件作用。')
cell('P05','C2',1,'`A novel composite learning algorithm`—`is designed`—用于 NN 权值自适应；同一算法—`allows`—估计误差信息进入权值自适应律以改善估计。',
     '设计句给用途，续句重复复合学习算法名称，`allows ... to be integrated into ... to improve` 保留信息、去向和估计作用。')
cell('P05','C3',1,'`A partial persistent excitation condition`—`is introduced`—用于 NN 权值自适应；传统 PE 要求—`can be greatly relaxed`。',
     '`introduced for` 给作用环节，`such that` 接条件改善；`partial persistent excitation` 使用与前文 PPE 一致的完整技术名称。')
cell('ESO2017','I01',1,'`Underwater robots`—`have been increasingly employed`—扩展海洋资源探索与科研能力。',
     '`including` 列对象类别，`employed to expand` 直接给用途；`human capabilities in` 明确能力及其领域，ROV 使用准确名称 `remotely operated vehicles`。')
cell('ESO2017','I01',2,'`a high-precision controller for underwater robots`—`is required`—保证数据质量及轨迹跟踪／定点保持精度。',
     '`To exploit ... benefits` 接前句价值，主句给所需控制器；两个平行 `to` 接相应目标，`quality of`、`precision in` 保持各自作用对象。')
cell('ESO2017','I03',6,'`an adaptive controller combining NN approximation with dynamic surface control`—`is presented`—用于 AUV 轨迹跟踪。',
     '`In [7]` 后给控制器，`combining A with B` 限定组合，`presented for` 指任务；`dynamic surface control` 保留该控制技术的准确名称。')
cell('ESO2017','I03',7,'`The computational load`—`is reduced`—通过采用学习参数数目很少的 NN 学习方法。',
     '计算指标作主语，`reduced by introducing` 把作用连接手段；`using a minimal number of learning parameters` 给计算作用的具体来源。')
cell('ESO2017','I06',4,'`The sliding mode observer`—`is presented`—估计未知外扰并降低控制增益。',
     '滑模观察器名称接上句同一工具，两个平行 `to` 分别给 `estimate ... disturbances` 和 `reduce ... gain` 的职责。')
cell('ESO2017','I06',6,'`backstepping control based on an ESO`—`is proposed`—处理液压系统中的非匹配扰动。',
     '`In [32]` 定位工作，`based on` 指 ESO 基础，`handle mismatched disturbances in` 保持问题类别与系统范围。')
cell('ESO2017','I06',7,'`The ESO`—`estimates`—模型不确定性和未测状态。',
     'ESO 名称接同一观察器，主动 `estimates` 给职责；`not only A but also B` 保持两个同层估计对象。')
cell('ESO2017','I08',1,'`a disturbance compensation approach based on ... MIMO-ESO`—`is utilized`—消除抖振。',
     '`In this paper` 进入当前工作，`based on` 将补偿方法与简单结构的 MIMO-ESO 直接连接，`utilized to eliminate` 给设计目的。')
cell('ESO2017','I08',2,'`The ESO model [32] and the high-gain observer [39]`—`motivate`—MIMO-ESO 设计；`The MIMO-ESO`—`is proposed`—估计未知扰动与未测状态。',
     '两个已有方法具名作主语，`motivate the design of` 保留启发关系。续句重复当前观察器名称，`proposed to estimate A and B` 保持估计范围。')
cell('Fuzzy2023','I02',2,'`barrier Lyapunov functions (BLFs)`—`have been widely used`—约束非线性系统状态与输出。',
     '`Recently` 给时间背景，`used to enforce` 接状态与输出约束，`in nonlinear control problems` 限定领域。')
cell('Fuzzy2023','I02',4,'`a new command-filtered fuzzy controller`—`has been proposed`—用于未知非线性系统，同时处理全状态约束与有限时间收敛。',
     '`In [14], ... for ... to handle A and B simultaneously` 写方法、系统范围和联合能力，`command-filtered fuzzy controller` 保留技术身份。')
cell('Fuzzy2023','I03',5,'有限时间方案的 `convergence time`—`is always related to`—初始条件；`The initial conditions`—`are sometimes unavailable`。',
     '`Nevertheless, for existing finite-time control schemes` 保留方法范围。两句分别写依赖和可得性，重复初始条件名称，限定强度仍是 `always` 与 `sometimes`。')
cell('Fuzzy2023','I03',8,'`an adaptive event-based fixed-time control scheme`—`has been proposed`—用于主动悬架；主动悬架的预设约束—`can be guaranteed`。',
     '`In [21]` 定位方法，续句以同一系统的约束作主语，`predefined` 保留约束性质，`can be guaranteed` 给相应保证。')
cell('Fuzzy2023','C1',1,'`A novel symmetric BLF`—`is designed`—避免输出约束被违反；期望瞬态性能—`can be guaranteed`。',
     '`designed to avoid violation of` 写职责，后续完整句以 `Thus` 连接相应性能保证，系统范围保持为同一机器人。')
cell('Fuzzy2023','C3',1,'`Robot tracking`—`can achieve`—实用固定时间收敛，不依赖初始条件。',
     '跟踪任务作主语，`practical fixed-time convergence` 保留完整性质范围，`regardless of the initial conditions` 回收时间性能需要。')
cell('Fuzzy2023','C2',1,'`A novel adaptive law for fuzzy weight estimation`—`is proposed`；全部闭环信号的有界性—`can be proved`。',
     '自适应律名称明确模糊权值估计职责；`proposed such that` 接闭环信号有界性，`all` 保留证明对象的范围。')
cell('Fuzzy2023','C2',2,'`the assumption that fuzzy weight estimates are bounded`—`can be relaxed`。',
     '`Then` 将闭环有界性接到假设改善，具体命名模糊权值估计量，`in ... research [23]–[25]` 保留指定文献范围。')

# For paragraph analysis, split rows only where the English was split. The four
# cells are the concrete task, received content, added information and next link.
paragraph_rows = {}
def rows(p, u, s, *r):
    paragraph_rows[(p, u, s)] = r

rows('P05','I02',1,
     ('给出 [9] 处理协作机器人物体操作的自适应分散控制。','接住前段的双臂协调控制问题。','已有方法能够处理物体操作任务。','下一句继续说明同一工作的力与位置控制机制。'),
     ('补充 [9] 中隐式力控制的职责。','接住上一句同一协作操作方案。','隐式力控制同时调节力与位置。','下一句用 [10] 扩充协作系统的内力控制能力。'))
rows('P05','I02',2,
     ('给出 [10] 面向多移动机械臂的分散控制结构。','接住已有协作控制方向。','适用对象扩展到多移动机械臂。','下一句说明这项结构怎样约束内力。'),
     ('说明 [10] 中内力约束的模型手段。','接住同一分散控制结构。','含虚拟连杆的增广物体模型用于约束内力。','下一句补充 [11] 基于抓持空间的负载处理。'))
rows('P05','I02',5,
     ('建立末端沿物体表面操作的实际需要。','接住前句牢固抓持且无相对运动的条件。','抛光、磨削和焊接要求沿表面操作。','下一句明确这类操作中的相对运动关系。'),
     ('明确表面操作通常包含臂与物体之间的滑动。','接住前句同一组表面操作。','滑动发生在机械臂与物体之间，[12]–[14] 支持应用关系。','后段 I03 接收这一需要，讨论双臂相对运动控制。'))
rows('P17','I04',6,
     ('给出 [3] 中 SEDS 的运动建模任务。','接住 GMM／GMR 的多示教信息能力，并联系动态系统表示。','已有 SEDS 方法把相关学习方向用于运动建模。','下一句继续说明同一方法中 GMR 的对象。'),
     ('明确 SEDS 中 GMR 对未知函数的建模职责。','接住前句已命名的 SEDS。','GMR 可以对运动动态系统中的未知函数建模。','下一句用 DS-GMR 补充动态系统与统计学习结合的依据。'))
rows('Fuzzy2023','I03',5,
     ('明确有限时间控制收敛时间对初始条件的依赖。','接住前面已有有限时间控制能力。','收敛时间与初始条件相关，讨论范围仍是有限时间方案。','下一句说明这些条件在实际中的可得性。'),
     ('交代初始条件有时不可得。','接住前句同一初始条件对象。','依赖的信息可能不可用。','下一句由这一时间性能需要进入固定时间控制方向。'))
rows('Fuzzy2023','I03',8,
     ('给出 [21] 面向主动悬架的事件式固定时间方案。','接住已有固定时间控制方向，以并列工作扩充依据。','固定时间方案可用于主动悬架。','下一句补充同一工作的约束保证。'),
     ('说明主动悬架预设约束可以得到保证。','接住前句的同一控制方案与系统。','时间性能之外还具备预设约束保证。','本段完成时间与约束联合能力说明，后段汇合控制目标。'))
rows('P17','I05',1,
     ('基于前文两类方法能力提出 DMP 与 GMM 的组合。','接住 I04 的 DS 鲁棒／泛化能力及概率学习能力。','两类方法共同进入机器人学习系统。','下一句说明 GMM 在同一组合中的建模对象。'),
     ('明确 GMM 建模 DMP 的非线性函数。','接住刚提出的 DMP／GMM 组合。','GMM 的职责落到 DMP 非线性函数。','下一句说明同一函数的估计怎样获得。'),
     ('明确 GMR 取得 DMP 非线性函数的估计。','接住前句已命名的同一函数。','GMR 承担函数估计的回归职责。','下一句说明整合后的模型怎样支持特征提取与运动合成。'))
rows('P17','I05',3,
     ('给出 [16] 中原 DMP 的 LWR 学习途径。','接住当前组合模型的多示教作用，进入同一函数学习任务的比较。','LWR 是原 DMP 的学习方法。','下一句补充 [17] 对同一 LWR 学习的带宽优化。'),
     ('说明 [17] 中 LWPR 优化 LWR 核带宽。','接住前句的 LWR 学习。','LWPR 增加了核带宽优化步骤。','下一句综合两项方法的复杂性与示教信息能力。'))
rows('P17','I07',1,
     ('给出当前 NN 控制器的关节空间跟踪职责。','接住 I06 已建立的未知动力学下准确执行需要。','本文设计用 NN 控制保证机械臂跟踪性能。','下一句明确 NN 控制器中的逼近工具及其对象。'),
     ('明确 RBFNN 逼近机器人动力学非线性函数。','接住前句同一 NN 控制器。','RBFNN 在控制器内承担动力学函数逼近。','下一句给出同一控制器的稳定性依据。'))
rows('P17','I07',4,
     ('说明运动生成模块利用 DMP 模型学习与泛化技能。','接住前句系统组成中的运动生成模块。','该模块的职责是学习与泛化运动技能。','下一句说明同一技能的轨迹表示。'),
     ('将 DMP 模型学得并泛化的技能表示为关节空间轨迹。','接住上一句具体 DMP 运动技能。','技能输出具有明确关节空间轨迹表示。','下一句让跟踪模块接收生成模块的同一轨迹。'))
rows('P17','I07',5,
     ('说明轨迹跟踪模块用自适应控制器接收并跟踪生成轨迹。','接住前句关节空间轨迹及其运动生成来源。','生成输出成为跟踪输入。','下一句继续说明同一控制器中的动力学补偿。'),
     ('说明 RBFNN 进入自适应控制器补偿不确定动力学。','接住同一跟踪控制器。','补偿使执行责任与前文未知动力学问题对应。','本段完成生成与执行接口，后段 I08 回收框架贡献。'))
rows('P17','I08',3,
     ('交代 SEDS 稳定性约束的 Lyapunov 理论依据。','接住前句已经命名的 SEDS 比较对象。','稳定性保证依赖对应理论约束。','下一句继续说明该约束的学习代价。'),
     ('交代 SEDS 稳定性约束增加模型学习复杂性。','接住同一 Lyapunov 稳定性约束。','学习代价具体落到 SEDS 运动模型。','下一句把比较接回完整框架覆盖的跟踪责任。'))
rows('P17','I08',4,
     ('相对 [3]、[25] 的运动建模范围，说明机器人学习系统增补 NN 控制器。','接住前面的框架范围及运动模型比较。','完整系统还承担轨迹跟踪控制。','下一句明确这一控制补充的环境影响补偿作用。'),
     ('说明神经学习补偿动态环境对机器人的影响。','接住前句的 NN 控制设计及前文不确定动力学问题。','补偿作用与运动执行需要联系起来。','下一句以稳健执行学得运动收束总体贡献。'))

paths = {
    'section': ROOT/'analysis/introduction-section-learning-draft-2026-10-06/learning-draft.md',
    'paragraph': ROOT/'analysis/introduction-paragraph-learning-2026-10-06/learning-draft.md',
    'expression': ROOT/'analysis/introduction-expression-learning-2026-10-06/learning-draft.md',
}
before = {n: subprocess.check_output(['git','show','bf8b444:'+p.relative_to(ROOT).as_posix()],cwd=ROOT).decode('utf-8').replace('\r\n','\n') for n,p in paths.items()}
mapping = {}
for k, ss in original.items():
    at = 1
    mapping[k] = {}
    for i, s in enumerate(ss, 1):
        aa = changes.get((*k, i), [s])
        mapping[k][i] = (at, at + len(aa) - 1, aa)
        at += len(aa)

def alabel(k, i):
    lo, hi, _ = mapping[k][i]
    return f'A{lo}' if lo == hi else f'A{lo}–A{hi}'

def span_text(k, lo, hi):
    return ' '.join(t for i in range(lo, hi+1) for t in mapping[k][i][2])

selected_expression = json.loads((ROOT/'analysis/introduction-expression-learning-2026-10-06/audit/selected-expressions.json').read_text(encoding='utf-8'))
expr_specs = {e['id']: e['selections'] for e in selected_expression}
used = set()
block_records = []

def evidence(k, lo, hi, stage):
    ss = original[k][lo-1:hi]
    aa = span_text(k,lo,hi)
    changed = aa != ' '.join(ss)
    for i in range(lo, hi+1): used.add((*k,i))
    block_records.append({'stage':stage,'paper':k[0],'unit':k[1],
                          'source_range':[lo,hi], 'adapted_range':[mapping[k][lo][0],mapping[k][hi][1]],
                          'based_on_original_adaptation':changed,'learning_text':aa})
    note = '**英文学习示例（基于原文的适配）。**' if changed else '**英文学习示例（原文选取）。**'
    return note+'\n\n> '+aa

# Section: preserve the six tasks and all complete paragraph groups.
s=before['section']
for k,u in units.items():
    raw='> '+u['text']
    if raw in s:
        s=s.replace(raw,evidence(k,1,len(original[k]),'section'))
# Original paragraph-opening locator fragments belong to the source audit.
def opening_line(match):
    prefix=match.group(1).rstrip('.')
    for k, ss in original.items():
        if ss[0].startswith(prefix):
            return '**示例段首。** `'+mapping[k][1][2][0]+'`'
    raise AssertionError(('unmatched opening',prefix))
s=re.sub(r'^`([^`]+\.\.\.)`$',opening_line,s,flags=re.M)
s=s.replace('英文保留已核验的出版原文，I／C 编号沿用来源底稿，仅作定位。',
            '英文示例按块标为“原文选取”或“基于原文的适配”，I／C 编号用于定位来源。出版原文与逐句适配对应保留在[来源审计](../introduction-default-learning-cleanup-2026-10-06/audit/adaptation-map.json)中。')
s=s.replace('[原文定位]','[来源审计定位]')
paths['section'].write_text(s,encoding='utf-8')

# Paragraph: keep each complete paragraph and accepted relations; map every
# adapted sentence to its own task row, including clauses split into sentences.
s=before['paragraph']
chunks=re.split(r'(?=^### |^## )',s,flags=re.M)
for ci, chunk in enumerate(chunks):
    m=re.match(r'### \S+ (P17|P05|Fuzzy2023|ESO2017) (I\d+)',chunk)
    if not m: continue
    k=m.groups()
    chunk=chunk.replace('> '+units[k]['text'],evidence(k,1,len(original[k]),'paragraph'))
    chunk=re.sub(r'^`([^`]+\.\.\.)`$',opening_line,chunk,flags=re.M)
    old_rows=re.findall(r'^\| S(\d+) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|$',chunk,re.M)
    def refs(text):
        # Range first, then individual sentence references.
        text=re.sub(r'S(\d+)–S(\d+)',lambda m: f'A{mapping[k][int(m[1])][0]}–A{mapping[k][int(m[2])][1]}',text)
        return re.sub(r'S(\d+)',lambda m: alabel(k,int(m[1])),text)
    for i_str,*fields in old_rows:
        i=int(i_str);lo,hi,_=mapping[k][i]
        rr=paragraph_rows.get((*k,i))
        if rr is None:
            assert lo==hi,(*k,i)
            rr=[tuple(refs(f) for f in fields)]
        assert len(rr)==hi-lo+1,(*k,i)
        new='\n'.join('| A'+str(lo+j)+' | '+' | '.join(r)+' |' for j,r in enumerate(rr))
        old='| S'+i_str+' | '+' | '.join(fields)+' |'
        chunk=chunk.replace(old,new)
    # Remaining narrative references outside replaced rows.
    lines=chunk.splitlines()
    chunk='\n'.join(line if line.startswith('| A') else refs(line) for line in lines)+'\n'
    chunks[ci]=chunk
s=''.join(chunks)
s=s.replace('以下保留九个完整出版原段，共五十句，', '以下保留九个基于完整出版原段的英文学习示例，')
s=s.replace('每段的 S1、S2 等按原文句序定位；英文整段保持原样，句位的完整英文也保存在来源审计中。',
            '每段的 A1、A2 等按当前示例句序定位，分句后的每一句分别说明其推进任务。示例按块标为“原文选取”或“基于原文的适配”；完整出版原文与逐句对应保留在[来源审计](../introduction-default-learning-cleanup-2026-10-06/audit/adaptation-map.json)中。')
s=s.replace('段落推进与原样英文共同作为参照','段落推进与适用英文示例共同作为参照')
s=s.replace('[完整原文定位]','[来源审计定位]')
# The final cross-paragraph call refers to adapted local sentence positions.
s=s.replace('P17 I05 的 S1–S2','P17 I05 的 A1–A4').replace('P17 I07 的 S3–S5','P17 I07 的 A4–A8').replace('P17 I04 的 S3–S4','P17 I04 的 A3–A4')
paths['paragraph'].write_text(s,encoding='utf-8')

# Expression: preserve groups and mature collocations. Replace only the source
# realizations and table cells affected by style, naming, or sentence splitting.
s=before['expression']
chunks=re.split(r'(?=^### E\d+)',s,flags=re.M)
for ci,chunk in enumerate(chunks):
    em=re.match(r'### (E\d+)',chunk)
    if not em: continue
    eid=em[1]
    for sel in expr_specs[eid]:
        k=sel['paper'],sel['unit'];lo,hi=sel['sentence_range']
        raw='> '+sel['selected_text']
        assert raw in chunk,(eid,k)
        chunk=chunk.replace(raw,evidence(k,lo,hi,'expression'))
        for i in range(lo,hi+1):
            match=re.search(r'^\| '+k[1]+r'-S'+str(i)+r' \| (.*?) \| (.*?) \|$',chunk,re.M)
            assert match,(eid,k,i)
            fields=expression_cells.get((*k,i),match.groups())
            fields=tuple(re.sub(r'S(\d+)',lambda m: alabel(k,int(m[1])),f) for f in fields)
            new='| '+k[1]+'-'+alabel(k,i)+' | '+' | '.join(fields)+' |'
            chunk=chunk.replace(match[0],new)
    chunk=chunk.replace('| 原文句位 |','| 示例句位 |')
    # Clause descriptions refer to the current example rather than rejected
    # source wording; S source locators in metadata remain for audit lookup.
    chunk=chunk.replace('采用原文的“系统范围＋具体能力”组织','采用示例的“系统范围＋具体能力”组织')
    chunks[ci]=chunk
s=''.join(chunks)
s=s.replace('原文中的 S 编号对应所属 I／C 单元的句位；引文数字仍是各篇原文的文献编号。',
            '来源标识中的 S 编号对应出版原文句位，分析表中的 A 编号对应当前完整单元的示例句位。英文按块标为“原文选取”或“基于原文的适配”；逐句对应及完整出版原文保留在[来源审计](../introduction-default-learning-cleanup-2026-10-06/audit/adaptation-map.json)中。引文数字沿用各篇论文的文献编号。')
s=s.replace('[完整原文定位]','[来源审计定位]')
s=s.replace('提供这些主语变化及连续句的原文','提供这些主语变化及适用的连续句示例')
s=s.replace('选择同一关系的原文实现','选择同一关系的英文实现')
s=s.replace('读取其连续原文和分析','读取其连续示例和分析')
# Align the affected call examples with their concrete adapted evidence.
s=s.replace('`While 〈前述工作〉 employed 〈共同方法〉 to 〈任务A〉, another study [xx] used 〈方法〉 to 〈任务B〉, where 〈机制或调节关系〉.`',
            '`While the studies in [xx] and [yy] employed 〈共同方法的准确名称〉 to 〈任务A〉, another study [zz] used 〈方法的准确名称〉 to 〈任务B〉. The 〈生成运动的风格或属性的准确名称〉 could be changed by 〈调节动作及对象〉.`')
s=s.replace('`In [xx], a 〈方法类别〉 named 〈方法名〉 was proposed for 〈任务〉, where 〈处理对象〉 was 〈动作〉 using 〈工具〉.`',
            '`In [xx], a 〈方法类别〉 named 〈方法名〉 was proposed for 〈任务〉. The 〈该方法中待建模函数的准确名称〉 was modeled using 〈工具的准确名称〉.`')
s=s.replace('`In [xx], a 〈控制结构／方法〉 was developed for 〈系统〉, where 〈受控量〉 was constrained by employing 〈手段〉.`',
            '`In [xx], a 〈控制结构的准确名称〉 was developed for 〈系统〉. The 〈同一系统中受控量的准确名称〉 was constrained by employing 〈手段〉.`')
s=s.replace('`〈方法〉 was proposed to address 〈问题〉, where 〈工具〉 was employed to simultaneously regulate 〈量A〉 and 〈量B〉 [xx].`',
            '`In [xx], a 〈方法的准确名称〉 was proposed to address 〈问题〉. A 〈同一工作中控制机制的准确名称〉 was employed to simultaneously regulate 〈量A〉 and 〈量B〉.`')
s=s.replace('`Nevertheless, for the existing 〈方法类〉, 〈具体性能〉 is related to 〈条件〉, which 〈条件的可得性或性质〉.`',
            '`Nevertheless, for existing 〈方法类〉, 〈具体性能的准确名称〉 is related to 〈条件的准确名称〉. The 〈同一条件名称〉 〈可得性或性质的谓语〉.`')
s=s.replace('或 `..., and 〈具体性质〉 can be guaranteed`',
            '或续句 `The 〈同一系统的具体约束名称〉 can be guaranteed.`')
s=s.replace('`〈模型〉 was learned using 〈工具〉 [xx], and 〈另一工具〉 was employed to optimize 〈对象〉 [yy].`',
            '`In [xx], the 〈模型的准确名称〉 was learned using 〈工具的准确名称〉. In [yy], 〈另一工具的准确名称〉 was employed to optimize 〈前一工具中被优化量的准确名称〉.`')
s=s.replace('`In this paper, a 〈设计〉 is utilized to 〈有依据的目的〉 based on 〈基础工具的准确名称〉.`',
            '`In this paper, a 〈设计的准确名称〉 based on 〈基础工具的准确名称〉 is utilized to 〈有依据的目的〉.`')
s=s.replace('`A 〈自适应律〉 is proposed such that',
            '`A 〈自适应律的准确名称〉 is proposed such that')
paths['expression'].write_text(s,encoding='utf-8')

# The ledger retains all selected publication sentences, unchanged context and
# exact source spans. It is audit material, never a default imitation resource.
ledger=[]
for p,u,i in sorted(used):
    k=p,u;lo,hi,aa=mapping[k][i]
    ledger.append({'paper':p,'unit':u,'source_sentence':f'S{i}',
                   'source_spans':units[k]['source_spans'],
                   'publication_sentence':original[k][i-1],
                   'adapted_sentence_range':[lo,hi] if aa else None, 'learning_sentences':aa,
                   'audit_only':not aa,
                   'adapted':aa != [original[k][i-1]]})
(OUT/'adaptation-map.json').write_text(json.dumps({
    'baseline':'bf8b4444da73916c70df3a3180b10b5286cb0d7f',
    'source':'analysis/introduction-section-review-2026-10-06/curated-introductions.json',
    'source_sha256':sha(SOURCE/'curated-introductions.json'),
    'selected_publication_units':[{**units[k],'paper':k[0]} for k in sorted({(p,u) for p,u,i in used})],
    'sentence_mapping':ledger, 'learning_blocks':block_records,
},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'blocks':len(block_records),'source_sentences':len(ledger),
                  'adapted_source_sentences':sum(r['adapted'] for r in ledger)},ensure_ascii=False))

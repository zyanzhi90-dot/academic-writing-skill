# 两篇指定范例：正文贡献与完整摘要的对应

本文件只分析范例。句号顺序用于定位，不是待写摘要的句数或结构配额。正文依据是本轮从两份原始 PDF 新提取的完整文本；摘要和贡献段另经 PDF 首页及第2页视觉核对。页码以下先写 PDF 页，再写印刷页。英文只合并版面换行和断词，不改变来源内容。

## A06：Robot Learning System Based on Adaptive Neural Control and Dynamic Movement Primitives

**真正的贡献及层次。** §I p.2/778 在 Fig.1 后说明，系统把运动生成和轨迹跟踪连在一起：前者由多次示教学习并泛化关节轨迹，后者用自适应控制执行这些轨迹并补偿不确定动力学。系统整合由两条具体设计支撑：其一，GMM 编码多示教产生的相位—非线性函数数据，GMR 估计一个 DMP 的非线性函数，克服本文所比较原始单示教 DMP 不能把多示教特征整合进同一模型的问题；其二，为生成轨迹配备 RBFNN 自适应跟踪控制，处理例如未知负载造成的动力学影响。§III.A–B pp.3–5/779–781，尤其式(5)、(23)–(24)，落实第一条；§IV.C pp.5–7/781–783 落实第二条。§VI p.10/786 按相同两条路线总结。DMP、GMM/GMR、RBFNN 和一般 Lyapunov 工具均有既有来源；这里不是四项基础方法发明，也没有另列“时空缩放”为独立新算法。

**完整摘要的连续选择。** p.1/777 Abstract 共8句；完整原文就在 [A06 PDF](source-examples/A06.pdf) 和 [新提取全文](source-examples/A06-full-text.txt) 开头。下面保留每句完整英文，分析其在已核实贡献中的实际作用。

| 句子及真实英文 | 为什么写、与相邻句怎样推进 |
|---|---|
| S1: This paper proposes an enhanced robot skill learning system considering both motion generation and trajectory tracking. | 直接提出系统，`considering both … and …`先确定两项共同职责。`enhanced`的内容要由后文两条设计兑现，不是独立优势论据。没有把机器人应用背景或各组件名单放在首句。 |
| S2: During robot learning demonstrations, dynamic movement primitives (DMPs) are used to model robotic motion. | 首先进入首句的运动生成分支：`During …`限定数据取得阶段，`DMPs`是明确组件，`are used to model …`说明职责。它为下一句解释模型性质、第四句解释学习改进提供对象，不是在宣称发明 DMP。 |
| S3: Each DMP consists of a set of dynamic systems that enhances the stability of the generated motion toward the goal. | `Each DMP`承接已命名组件，说明选这种表示的稳定运动基础；`generated motion`限定为模型产生的运动，未保证实际机器人零误差跟踪。它为“为何用 DMP”提供支持。源文关系从句的单复数搭配可在适配时校正，不能为了照抄保留不适用语法。 |
| S4: A Gaussian mixture model and Gaussian mixture regression are integrated to improve the learning performance of the DMP, such that more features of the skill can be extracted from multiple demonstrations. | 从已有模型转到作者的学习增强：组合的主语—`are integrated to improve`—同一个 DMP—`such that`接多示教特征利用。这一句同时给设计和作用，没有罗列 GMM 的密度、EM 更新或回归公式。正文将 `more features`具体化为多示教非线性函数的估计与综合；其比较强度必须由这层意义支持。 |
| S5: The motion generated from the learned model can be scaled in space and time. | `The motion generated …`接上一句学习输出，给出运动表示可泛化的性质，同时为下一句准备要执行的轨迹。`can be scaled`是模型能力，不是证明所有真实任务成功；具体缩放参数和实验轨迹未搬入摘要。 |
| S6: Besides, a neural-network-based controller is designed for the robot to track the trajectories generated from the motion model. | 转入首句第二分支，但仍沿同一输出对象推进：`trajectories generated from the motion model`接 S5 的生成运动，`is designed … to track …`说明控制器存在的必要性。`Besides`只是连接手段，科学承接在“生成轨迹交给控制器”，不是两个组件的无关并列。 |
| S7: In this controller, a radial basis function neural network is used to compensate for the effect caused by the dynamic environments. | `In this controller`定位在刚命名控制器内部，RBFNN—补偿作用—动力学影响，一句解释第二条设计如何支撑真实执行。正文实验主要核查未知负载影响；不能仅凭摘要的 `dynamic environments`扩大为任意外界扰动都被完全消除。 |
| S8: The experiments have been performed using a Baxter robot and the results have confirmed the validity of the proposed methods. | 将两个分支收束到真实机器人证据。§V pp.7–10/783–786 分别检验神经控制的负载补偿和 DMP 模型的泛化／多示教学习；实验不是第三项独立贡献。摘要保留平台，省去负载数值、神经节点数、关节清单、倾倒／画图流程。`validity`较概括，正文有具体发现时可以准确替换结果补语；不能把这句当成泛化所有场景的保证。 |

**整段为何这样组织。** 开头提出完整系统的两项职责，然后集中完成“表示—表示性质—多示教增强—学习输出能力”，再以同一输出进入“跟踪控制—不确定性补偿”，最后由两组实验支持系统。这不是按 §II–V 顺序压缩每个方法步骤，而是把两项设计的必要作用和二者之间的交接讲完整。摘要没单列 Lyapunov 证明句，正文仍有控制分析；理论是否进入摘要由当前贡献需要决定，不是必须照搬该省略。

## A07：Composite-Learning-Based Adaptive Neural Control for Dual-Arm Robots With Relative Motion

**真正的贡献及层次。** §I p.2/1011 明列三项：①在动力学未知情况下完成非对称双臂相对运动任务的神经控制框架；②将估计误差信息整合进神经权值更新的复合学习，提高估计性能；③把 PPE 引入权值适应，放宽传统 PE 要求。相对运动不是双臂共同刚性搬运：§II.A p.2/1011 中一臂抓持物体，另一臂沿物体表面用工具运动，产生相对运动并需控制接触力。§III.A p.5/1014 用命令滤波反步法服务轨迹／力控制；§III.B pp.6–7/1015–1016 用历史回归信息构造与权值估计误差有关的辅助量，并进入更新律(48)。PPE 的概念和局部激活性质有先前文献来源，本文贡献是引入该框架，不是原创 PPE 定义。Theorem 1 p.6/1015 及后续证明在 PPE 等相应控制条件下给出跟踪／估计误差收敛至原点邻域、接触力误差有界，不能把摘要的“收敛”解读为所有权值无条件精确辨识。§IV pp.7–10/1016–1019 只有数值比较证据，没有实机实验。

| 句子及真实英文 | 为什么写、与相邻句怎样推进 |
|---|---|
| S1: This article presents an adaptive control method for dual-arm robot systems to perform bimanual tasks under modeling uncertainties. | 方法—对象—任务—不确定性范围同时给出，先定位第一项贡献。`to perform … under …`把设计目标和实际难点连在一起；没有先罗列所有后续算法。 |
| S2: Different from the traditional symmetric bimanual robot control, we study the dual-arm robot control with relative motions between robotic arms and a grasped object. | 立刻将泛称双臂任务限定成真实区别：机械臂与物体存在相对运动。`between … and …`给出区别的两个对象。该区别决定下一句的两种机械臂职责和随后接触控制的必要性，不能移植成没有事实依据的“不同于传统方法”。 |
| S3: The robot system is first divided into two subsystems: a settled manipulator system and a tool-used manipulator system. | `The robot system`承接刚限定的任务对象，两子系统是任务建模的关键职责区别，给 S4 的控制设计提供对象。摘要不展开坐标系、雅可比及完整约束方程；冒号列举是源文实现，是否适配取决于新稿是否真有必须命名的角色。 |
| S4: Then, a command filtered control technique is developed for trajectory tracking and contact force control. | 从职责／建模转到实现其两项控制目标。`is developed for … and …`把技术名直接接职责，滤波过程和反步计算细节没展开。命令滤波是一项实现设计，不因独立成句就升格为第四项原创工具。 |
| S5: In addition, to deal with the inevitable dynamic uncertainties, a radial basis function neural network (RBFNN) is employed for the robot, with a novel composite learning law to update the NN weights. | 接 S1 的不确定性问题，在既有控制框架中引入近似组件，并把作者复合学习接到具体权值更新对象。`to deal with …`解释为何需要该组件，`with … to update …`为 S6 留下学习律。`inevitable`和`novel`不是不可替代科学内容，必须对应具体证据和当前表达作用。 |
| S6: The composite learning is mainly based on an integration of the historic data of NN regression such that information of the estimate error can be utilized to improve the convergence. | 重复命名 `The composite learning`是有用的对象交接，不是冗余同义改写。历史回归数据—估计误差信息—更新作用—收敛，兑现第二项贡献及相对普通权值更新的优势。只保留最能解释优势的信息机制，没有搬入 P/Q、遗忘因子、投影算子和证明交叉项。 |
| S7: Moreover, a partial persistent excitation condition is employed to ensure estimation convergence. | 从学习作用接必要条件，同时呈现第三项贡献。`estimation convergence`明确是估计对象，不能与运动跟踪互换；PPE 本身有放宽传统激励要求的贡献作用，保留它不是照例加一个条件标签。正文结论仍是有条件的邻域收敛。 |
| S8: The stability analysis is performed by using the Lyapunov theorem. | 给已说明的控制及估计作用提供理论依据，但只说分析工具，没有再次列举每个算法或全部定理。它不能替代 S7 的激励条件，也不能凭这句把正文保证升格。 |
| S9: Numerical simulation results demonstrate the validity of the proposed control and learning algorithm. | 将数值证据直接接控制与学习这两个贡献对象。§IV 比较 PID、普通神经学习控制与本文方法的跟踪、近似和权值变化；摘要省去仿真机器人参数、曲线编号、比较百分比。`Numerical simulation results demonstrate …`有清楚的证据主体和发现谓语；`validity`可按当前确切发现适配，仿真不能换成实机或无条件理论保证。 |

**整段为何这样组织。** 首句定控制任务及未知动力学；S2–S4 让相对运动区别决定系统职责和控制目标；S5–S6 让不确定性处理进入作者的复合学习创新，并用信息机制解释其优势；S7 把估计收敛接到 PPE；S8–S9 分别支持理论和数值层面。前三项贡献并非平均各占一句：任务框架需要 S1–S5 说明，核心学习机制需要连续的 S5–S6，而条件的贡献与限定作用集中在 S7。保留哪些细节由理解贡献所需决定，不由固定词数或方法章节篇幅决定。

## 两篇之间可核对的选择原则

A06 的优势在于“前一设计的输出如何成为后一设计的输入”，A07 的优势在于“任务区别为什么需要该控制框架、学习信息为什么提供优势、什么条件限定其主张”。选主范例时应对照实际科学关系，不能只看到标题含学习或控制就决定；辅助表达应接入同一对象链，而不是再加一份方法清单。成熟英文可直接沿用其普通主语—谓语、目的关系、输出回指和结果句实现；每个来源科学对象都必须替换准确。`Besides`、`Then`或重复技术名只有承担真实联系时才保留。直接借鉴不要求复制来源的含混结论、句法瑕疵、无作用修饰词、所有步骤或全部句子；也不能把必要保证条件仅压成工具名称。整段、相邻句及有意义词组要一起校验。

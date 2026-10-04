# 范例核对依据（协调端，不交写作端）

复用[已核验的逐句分析](../../E02-specified-example-feedback-revision-5b8bbca-2026-10-04/materials/example-analysis.md)，并对照冻结 fd7dbcb 的 A06／A07 卡片、其中完整英文及两篇正文。以下记录分析依据，不提供 E03 主线、目标句或替换清单。写作端仅能读候选中已有的分析及声明原件。

**A06。** 正文 §I p.2、§III pp.3–5、§IV–VI pp.5–10支持两条设计的整合：GMM／GMR 把多示教信息用于同一个 DMP；RBFNN 自适应控制使生成轨迹在不确定动力学下执行。DMP、GMM、GMR、RBFNN 不是四项原创方法，时空缩放也不是额外新算法。摘要首句 `considering both motion generation and trajectory tracking` 给两项职责，S2–S3 用已有 DMP 表示及趋向目标的性质解释其基础，才接 S4 的 `are integrated to improve …, such that …`，把设计、改进对象与多示教作用连在一起。S5 承接学得运动的可缩放性质，S6 的 `track the trajectories generated from the motion model` 将同一输出交给控制器，S7 的 `In this controller … is used to compensate for …` 再解释为什么能处理执行中的动力学影响。末句 Baxter 实验对应正文两组验证，省去执行流程和超参数。摘要省略正文的有条件有界性分析，是服务贡献的取舍，不能解释为其他研究也必须省略理论。

**A07。** 正文 §I p.2 三项贡献是相对运动任务的未知动力学双臂控制框架、利用估计误差信息的复合权值学习、在该框架引入较宽松的 PPE；命令滤波、RBFNN 与 PPE 概念有已有来源。摘要 S1 的 `to perform … under modeling uncertainties` 给任务及难点；S2 相对运动的区别使 S3 两种机械臂职责和 S4 轨迹／接触力控制成为必要内容，三句不能拆成三张方法名称清单。S5 把不确定性处理与权值更新相连，S6 的历史回归数据—估计误差信息—收敛作用才兑现学习优势。S7 限定估计收敛，S8–S9 分别提供 Lyapunov 与数值支持；正文保证是相应条件下的邻域收敛和有界性，不是所有权值无条件精确辨识。结句 `Numerical simulation results demonstrate …` 的主体准确区分仿真证据；对象补语可按本文确有发现替换，不能扩大证据类型。

两篇均围绕贡献选择必要设计和支持，不按章节均分，也不按句数配额组织。普通目的句法、具体对象复现和结论搭配可以直接沿用；方法输出交接、并行设计或条件承接究竟是哪一种，必须重新核对当前科学关系。引用某个成熟短语、读取卡片或得到语法正确的英文，都不自动证明整段适配完成。源文的宽泛 `validity`、不适用修饰或语法瑕疵不作为质量要求。

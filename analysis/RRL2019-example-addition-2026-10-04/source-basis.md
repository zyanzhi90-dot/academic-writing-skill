# Residual RL 范例：版本、原文及取舍依据

本次补充在 [E03 首次输出](../../effect-test/E03-independent-transfer-fd7dbcb-valid-2026-10-04/drafting/first-output.md)保存、冻结输入和加载审计完成后进行。测试仍记录 fd7dbcb；新增 A08／B14 没有进入该会话，不据本次测试认定新增材料的效果。

## 版本和原件

主依据为用户放入[文献资料的本地 PDF](../../文献资料/Residual_Reinforcement_Learning_for_Robot_Control.pdf)。首页会议头、页码与 PDF 元数据一致：Tobias Johannink 等，*Residual Reinforcement Learning for Robot Control*，2019 International Conference on Robotics and Automation，6023–6029，7 页；DOI 10.1109/ICRA.2019.8794127。保留收到的 PDF 字节，SHA-256 `885f62e07ee4bd37fb0e08bdaa6068fd5e4e473d11e0be239ba8bdd2d8c393db`，未重新下载或改写。

对照原先归档的[作者 v2 PDF](../../effect-test/E03-independent-transfer-fd7dbcb-2026-10-04/coordinator/source/target.pdf)及[其原始提取全文](../../effect-test/E03-independent-transfer-fd7dbcb-2026-10-04/coordinator/source/target-full-text.txt)：arXiv:1812.03201v2，2018-12-18，8 页，SHA-256 `c6279120f9e0a799a9d7a943a5624a5738250e588f99c5fc8a9fac28e2039641`。作者页及下载依据保留在原记录，不重复提取 v2。两版不是同一文件，也不声称全文相同。

本地出版版经 pdftotext -raw -enc UTF-8 提取，原返回字节保留于 [local-full-text.txt](local-full-text.txt)；[RRL2019.txt](../reading/RRL2019.txt)沿仓库方式加 PDF 页标记，保留原连字及正文，供按页定位。卡片英文只规范化版面断词、连字及换行；公式下标以提取文本的线性写法显示，sm、so 分别指 PDF 的机器人及物体状态，不另造变量。首页、方法、结果段及表格已对照 [p.1](publisher-page-1.png)、[p.3](publisher-page-3.png)、[p.4](publisher-page-4.png)、[p.5](publisher-page-5.png)图像核验。

## 核实的相同与差别

[元数据和字节比较](source-version-comparison.json)／[所用段落比较](selected-text-version-comparison.json)保留实际依据。

- 完整摘要、§I 贡献段、§III.A 耦合优化三句、§VI.A 比较及作用解释前三句，在版面规范化后相同。两版均有固定控制信号与学习残差相加、完整任务优化、15/20 对 2/20 的错位实机结果；千步迁移均限于固定侧块。
- 出版版 §IV.A–B（pp.3／6025）缩短了实验环境说明。v2 保留的完整观测通道、块运动自由度、奖励公式(6)–(7)等展开，在出版版未完整重述；出版版仍说明实机阻抗控制、摄像位置估计及仿真位置控制。控制噪声公式从 v2 的(8)变为出版版的(6)，页码和版面也不同。不能交叉使用公式号或把这些删节称为所有科学事实变化。
- 本轮测试使用归档 v2 的原样中文事实包及必要条件，保持不变；范例引用采用本地出版版页码和英文。未使用缺失观测公式或未逐项复算的曲线作为新增论据。

## 贡献—摘要—正文对应

真正贡献是常规控制与深度 RL 的相加组合及真实接触操作中的实现／验证。§III 式(5)规定固定基准加学习策略，机器人—物体耦合使残差仍须针对完整任务回报优化；已有 TD3、阻抗控制和神经网络不各算发明。§VII 将同期独立 residual policy learning 与本文实机接触任务重心区分，卡片据此避免普遍首创宣称。

新增 **A08** 保留完整 7 句摘要：先给常规控制能力和建模依据，接具体接触难点及其控制后果，再给既有 RL 的互补能力；这些内容使职责分工有理由。随后以 `decomposing … into …`安排本文两部分，以 `superposition of both control signals`明确相加关系，最后以真实装配证据回到接触和不稳物体。句序分析逐句解释相邻关系与具体 `by`／`which`／`both` 的对象，而不只列功能标签。没有把背景句数或概括成功的结尾设为固定组织，也没有把该写法改为 E03 首稿的目标顺序。

新增 **B14** 保留两个有明确定位的连续三句组：§III.A 先说残差职责，再用状态耦合限制独立控制的直觉，才接整体优化及基准结构的作用；§VI.A 先界定比较方法／任务，再报告两个指标，最后解释从零学习的负担区别。它补充 A08 摘要未写出的耦合关系，及抽象有效性怎样落实到作用解释。两组来自不同段落，未伪称为相邻连续原文。`less samples`等源文搭配瑕疵在引用中保留，并说明新文如何准确自然地表达。

共用范例仍是唯一正文，分析指针不复制卡片。只增加 A08／B14、摘要和正文的按需索引及 RRL2019 原件链接；原 20 卡、A06 默认锚点及既有主要参考分工不改。两端 Abstract、共用表达核心、入口、manifest、router 和 workflow 均保持原实现。完整性、格式和选择加载只证明材料可调用；新增材料的写作效果尚未单独验证。

# 机器人 Introduction：三层范例与实际起草／复核的衔接

基线：`369d1538cb35df8d0b87d357288770b28dca4d40`。开始时本地 HEAD、origin/main 与 GitHub 最新 main 一致，工作区干净。本轮仅落实已验收写法，没有生成、润色新稿或运行效果测试。

## 核对依据与实际缺口

依据当前《核心要求.txt》《我自己的经验和做法.txt》《引言写作方法.txt》及最新明确调整：先确定作者科学含义，再从适用完整范例学习组织与具体英文。最新语境判断继续有效，不能单凭开句形式或代词判错；旧作者文本中的默认实验排除表述按最新调整撤回，未接入候选。

现有能力已经提供科学主线规划、段落任务、范例选择、科学内容转换和表达复核。共享索引的 Selection、Use during Drafting、Use during Polishing 及任务表也已连接三个正向学习层，P17 为默认锚点，P05／Fuzzy2023／ESO2017 按科学关系补充。本轮没有发现需要新建材料库或改变路由的缺口。

需要落实的是角色执行片段中的衔接。原 Writing 片段用“Determine the author's scientific line and paragraph tasks before drafting, then draft along that line using the selected complete English and analysis”概括整个过程；原 Polishing 片段用“first assess the scientific line, paragraph tasks and sentence links, then repair affected English from the complete examples”概括复核。它们未在各自实际执行位置明确：规划所得的科学任务怎样对应选中的连续英文，转换后的作者对象／动作／条件怎样带入成稿，以及保留和替换表达怎样接受同一组科学与英文对照。共享索引已说明这些能力，因此仅替换两端这段概括性调用，不再在共享学习层增加同义规则。这是静态执行衔接的定位，不是对某次生成失败原因的认定。

## 两处必要修改

| 修改位置 | 接入现有步骤的实际决策 | 既有依据与作用 |
| --- | --- | --- |
| [Writing Introduction fragment](../../skill-candidate/nature-writing/static/fragments/section/intro.md)，Robotics-centred Introduction 块 | 明确执行索引的 Selection 和 Use during Drafting。在 workflow 1–3 的科学主线与段落规划中，把当前任务接到完整段落或连续句及其上下文、推进分析、具体英文；在写该段之前确定作者对象、动作、作用对象、条件和效果的对应，并将选中实现带入 step 4。step 4 直接从所选英文起草，保留适用推进、主语动作、句式、搭配和用词，按作者科学关系组合或调整。steps 7–8 对实际连续成稿同时核对作者材料和所选英文。 | 复用 workflow 的规划→起草→段落／表达检查；将共享材料的选择与适配落实为这些步骤的输入和判断。完整范例参与英文形成，不只作为事后的功能标签。引用身份、事实、条件、比较及结论均按作者材料转换。 |
| [Polishing Introduction fragment](../../skill-candidate/nature-polishing/static/fragments/section/intro.md)，Robotics-centred Introduction 块 | 明确执行索引的 Selection 和 Use during Polishing。在原有 diagnosis 中以作者材料确定科学任务，选择相应完整连续例子，先明确作者科学关系与英文实现的对应，再判断保留或修改。实际句段同时与作者材料、所选英文比较；受影响单元从适用英文实现修复。交付前同样核对保留句与替换句，并复读相邻句段的动作职责、条件、设计理由、作用与输入输出。 | 复用原有先诊断、按范围修复和交付表达检查；保留已经准确且符合范例的表达。沿用共享语境标准判断开句与短称，不增加机械禁词，也不把语法正确等同于已实现范例写法。 |

科学内容转换承接已验收材料中的真实关系。例如，段落层 P17 I04-A3–A4 与表达层 E06 提供“同一文献的方法／输入→生成输出”的连续实现；P17 I05-A1–A4 与 E19 提供“组合理由→组成职责→组合作用”；P17 I07 与 E23 提供“前一部分输出→后一部分接收并继续作用”。新执行片段要求在当前作者对象和关系与这些实现对应后，再形成或修复英文。作者科学关系决定选择、组合和调整，范例的技术事实和保证不成为作者事实。

## 执行路径与保护范围

Writing：`SKILL.md`／manifest 的 `section=intro` → 本轮修改的 Introduction fragment → 专用共享索引及按当前科学任务读取的三层正向材料；起草仍使用 `static/core/workflow.md` 的 1–3、4、7–8，科学表达核心由 always_load 提供。

Polishing：`SKILL.md`／manifest 的 `section=intro` → 本轮修改的 Introduction fragment → 同一专用共享索引和三层正向材料；执行仍位于 router step 4 的 section-specific job 与 `static/core/failure-modes.md` 的诊断、局部修复和交付检查中，科学表达核心仍由 always_load 提供。

实际候选差异仅为这两个文件的 Robotics-centred Introduction 块。已验收的共享索引、整节／段落／表达三层材料、scientific-expression、两端 SKILL／manifest、共用 workflow／failure-modes、其他 Introduction 指导及其他 section 均保持原样。P17 锚点、单次示教能力的正确说明、上下文表达判断、generic 隔离和总索引读取边界均保留。不固定段数、句序或范例与段落的一一对应，不增加独立输出表或执行器步骤。出版审计原文、未采用项与历史诊断仍留在 analysis／audit，未新增任何进入运行模仿库的路径。E04、历史输出与作者原材料均未改动。

## 静态核对与结论边界

核对了两端 manifest 的 intro 映射、router 的专用索引入口、三层任务链接与英文示例、工作步骤及科学表达检查的对应关系，并检查差异范围与空白格式。机器人专用块之后的其他科学主题入口和相容指导保持原样；候选其余文件无差异。

本轮完成的是现有执行片段的必要衔接，不证明实际会话一定按此选择和转换范例，也不证明全文科学忠实、英文成熟或自主复核有效。未安装 Skill、未调用写作／润色模型、未运行 E04 或其他效果测试，不补记效果通过、迁移或稳定性。按 AGENTS.md 提交同步并核对工作区干净及本地与远端一致后停止，交负责人独立验收。

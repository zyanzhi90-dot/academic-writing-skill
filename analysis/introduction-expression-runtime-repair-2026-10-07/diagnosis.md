# 剩余自主表达失效与读取边界：定位及最小修改依据

基线 `836b01aa7c45b14133452ebdf21cf3660b20a741` 与本地、origin/main、最新远端一致。只诊断 E04 a29f1e1 的原始运行、首次输出和阶段差异；有效作者要求及 current-author-adjustment.txt 优先，不恢复旧实验排除默认规则。

## 可观察失效

| 环节 | 实际证据 | 可以确认的结论 |
| --- | --- | --- |
| 生成 | Writing P01-S03 为 “Learning from demonstration provides …”；P05-S05 为 “It therefore allows …”；P06-S04 为 “This reduces …”。item_8 完整返回科学表达核心；item_38 返回 P17 I01 的命名对象以及 E01–E03；item_40/42 返回 E19/E23 等完整英文及对象—动作分析。 | 不是表达要求或成熟实现缺失；生成的学习路线和作用句未持续保留相应对象身份。不能把准确句意当作构造已经对齐。 |
| 保留 | Polishing P06-S04 原样保留 “This reduces …”。科学表达核心 item_9、E19 item_36、E23 item_37 已返回。 | 技术身份不清的实现没有被独立复核修复。原句科学关系可恢复，不等于符合当前作者具体表达偏好。 |
| 替换 | Writing P05-S09 的 “This execution scheme balances …” 在 Polishing P05-S09 变为 “This balances …”；P02-S09 的 “These requirements motivate a policy representation …” 变为 Polishing P02-S08 的 “This motivates …”。 | 替换删除了原本存在的技术类别；失效发生在压缩实现中，不只是继承旧句。动名词开句虽被修复，不能据此判整节表达复核通过。 |
| 公开判断与交付 | Writing item_43 宣称范例连续句已与本稿对应，item_44 的可见核对集中于历史观测/未来动作、训练稳定性对象及 CNN 实机范围。Polishing item_21 明确要压缩重复能力说明，item_42 保留文献能力和比较范围，随后首次输出仍含上述失效。 | 公开规划和最终替换能证明范围/压缩决策与对象身份保留之间有缺口；不能证明隐藏复核是否执行、哪一条内部推理造成遗漏。 |

有依据的解释是：以整句科学意思、同主题信息或简短流畅为单位的保留与压缩，没有持续对齐所选连续句中的具体科学名词和作用责任。拟修接点是源例对象—动作—作用绑定以及替换前后的身份比较，不是再添加一个 “避免 This/It/Learning” 的词表或同义规则。适用短称仍可保留，例如具备技术类别和作用的 this controller、the motion model、this comparison；判断取决于当前作者对象与句间关系。

## 实际读取越界

Writing item_20 从 robotics-writing-examples.md 返回 1–230 行；Polishing item_17 返回 1–240 行。正文卡片开始于第 164 行，摘要英文从第 168 行开始：A01 包含 “Implemented as an iterative learning controller …” 和冒号长列举；后续 A02–A06 的摘要出版原句也已进入上下文。Polishing item_20 再读任务索引时返回 147–170 行，仍带入 A01 原文。

Writing 后续 item_23 读 1–145、Polishing item_19 读 1–150，均不能撤回先前已返回的原文。原总索引把共用说明、任务表和不同 section 的出版卡片放在一个长文件里，宽幅首读跨过任务边界。这是已证实的任务范围越界，不是文件系统目录越界：旧记录的 outside_explicit_reads=0 仍可成立。旧的 selected_cards 审计只识别 B 卡，不能据其空集合宣称 A 摘要卡没有返回。

没有因果对照证据证明摘要同载造成对象命名失效；本轮分别处理读取范围和表达决策。

## 必要修改及保护范围

1. Introduction-only 在 Writing/Polishing 的 router、manifest、section fragment 中直接读取既有 robotics-introduction-examples.md。其 Selection 与科学任务表承担本节参考协调及检索；原总范例文件完整不动，其他 section 仍按原路径读取。
   引言入口的默认身份只保留 B15/P17，去掉同篇摘要卡 A06 的别名，避免引言检索返回到摘要卡。
2. 两端已加载的 workflow/failure-modes/language 指引及机器人正文入口中，原总索引的无条件调用改为 router 选择的任务索引或明确的 Introduction/其他任务分支。否则旧入口仍可能重新加载整本卡片。这些接点只改索引引用，不修改全局语法、其他 section 内容或科学要求。
3. 在共享 Introduction 既有适配说明中，用 P17 I01、E19/E23 的现有完整英文及分析绑定作者对应科学对象与有限动作，再实现同一对象的作用句；文献仍用 E05–E13 的具体主体与机制/输出。
4. 既有润色复核从笼统“检查替换”收敛为新旧科学主体与相邻句职责的比较。压缩修饰、重复结论时保留承接作用的技术名词；替换丢失身份时保留已有适合实现或从相应真实单元修复。不强制具体词语、句序、句数或打印审计表，不含 E04 专属主线/开篇/修法。

四篇认可引言、三层正向学习资源、generic 隔离、科学表达核心、总范例卡片、摘要/其他 section 正文与执行器保持原样。参考中的制造应用、动力学补偿、BLF/ESO 与理论保证不能成为本次作者事实。

静态检查只验证范围、路径和源资源保留。冻结后以不含诊断、旧稿、协调端规划或纠错反馈的正常输入，各做一次独立 Writing/Polishing；新旧主体比较是否真正落实，以首次全文为准。失败也原样保存并停止，不继续改到通过，不推断迁移或稳定性。

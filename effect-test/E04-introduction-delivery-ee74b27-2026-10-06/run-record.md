# 运行记录

冻结候选：`ee74b27dffa59ba79b5f14cf18687f60e0d866c5`。开始时本地 HEAD、origin/main、实时远端一致，工作区干净。

按以下顺序执行；所有首次输出保存后才进行协调端全文评价：

1. `python -X utf8 effect-test/E04-introduction-delivery-ee74b27-2026-10-06/prepare_runner.py`：复制原样输入和既有任务，保存冻结身份及执行器来源；加入本轮最新作者调整，原作者文件保持原样。未调用模型。
2. `execute_once.py prepare drafting --commit ee74b27dffa59ba79b5f14cf18687f60e0d866c5`：冻结 Writing／Shared 与已声明来源材料，生成外部独立目录、完整请求、命令和实际输入返回。
3. `preflight.py drafting`：输入身份、候选字节、完整返回及目标原文排除核对通过。
4. `execute_once.py run drafting`：仅一次有效调用，退出 0，328.96 秒，原始事件和首次输出保存。
5. `execute_once.py audit drafting`、`verify_stage.py drafting`、`retain_sections.py drafting`：核对首次输出与最终事件一致、材料不变、没有显式越界读取；按原样子串分离英文、逐段中文、引用和唯一英文／引用交接。
6. `execute_once.py prepare polishing --commit ee74b27dffa59ba79b5f14cf18687f60e0d866c5 --draft effect-test/E04-introduction-delivery-ee74b27-2026-10-06/drafting/raw-introduction-and-references.md`：另一个外部独立目录与 Polishing／Shared；科学及作者输入与 Writing 相同。
7. `preflight.py polishing`：身份和交接一致性通过。
8. `execute_once.py run polishing`：仅一次有效调用，退出 0，388.25 秒，原始事件和首次输出保存。
9. `execute_once.py audit polishing`、`verify_stage.py polishing`、`retain_sections.py polishing`：首次输出与日志一致，输入和候选不变，显式越界读取为零。
10. `save_delivery.py`：原样复制 Polishing 为最终交付，保存两阶段信息与英文差异。
11. `summarize_loading.py`：基于冻结文件与实际编号行逐行对应；区分全单元、英文块和分析表的覆盖，不推断采用正确。单元边界按锚点和任务标题界定。派生摘要的边界计算调整没有改动原事件或模型输出。
12. `index_outputs.py`：保存原句定位及少量表面观察；不由句式数量或标点检查推出效果。
13. 两份完整英文、中文、引用与实际返回的正向例子事后核验，报告分别判断科学、推进和表达；结果为执行完成、两阶段效果均未达标。没有反馈或修稿。
14. `verify_records.py` 和 `git diff --check`：提交前记录一致性、范围、链接与凭据模式核对。新目录沿用旧记录的 `* -text` 属性；`verify_git_bytes.py` 逐个比较 Git 暂存 blob 与原保存文件的字节，保留原始换行及哈希。用项目 `./sync.ps1` 提交同步后，再核对所有存档文件字节、本地干净、HEAD／origin/main／实时远端一致。

原模型请求和命令分别为各阶段 `execution-prompt.txt`、`execution-command.json`；候选、CLI、执行器和输入哈希在 `frozen-run.json`。完整输入的实际 PowerShell 返回位于 `execution-read-before-invocation.*`。CLI 0.160.0 在已有安装位置运行，未安装或更新软件；旧位置失效是在调用前发现，不是另一次模型启动。

stderr 保留模型列表刷新超时的非终止信息。两阶段各只一个 `thread.started`，随后正常 `turn.completed`，没有补跑。程序内部各次工具读取属于同一次独立会话，不是新的人工反馈调用。

本轮仅新增本目录。Skill、三层学习、作者原文件、E04 历史记录及已验收摘要不变；没有提供目标原文、旧引言、预设主线或历史诊断。本次不补记迁移、可靠遗漏检测或稳定性通过。

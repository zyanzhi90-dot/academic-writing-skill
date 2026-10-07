# E04 Introduction：冻结 447c0c4 的一次独立 Writing＋Polishing

远端核对：开始时本地 HEAD、origin/main、GitHub main 均为 `447c0c4165afb7fdc08a0458d534042a8704dc94`，工作区干净。候选按该提交的 Git 原始字节复制；两阶段均使用 `gpt-6.1-sol`、`high`。候选、作者原文件及已有 E04 记录未修改，未安装 Skill。

科学、背景、引用和已验收摘要及两端自主任务，从 ed9e42b 的已确认记录原样复制，其科学来源仍是 253dae3 E04。三份作者原要求使用当前项目文件并校验既有身份。current-author-adjustment 保留已撤回实验规则的有效优先关系，另追加最新明确的语境判断澄清，未追加历史 failure、句子定位或纠错提示。具体字节来源、正常要求及候选文件身份见 [runner-provenance.json](runner-provenance.json) 和 [coordinator/input-identity.json](coordinator/input-identity.json)。

复用既有 `execute_once.py`，字节完全一致；仅在准备脚本及身份检查中绑定新候选、新记录和正常作者澄清。每阶段先 prepare→preflight，再且仅再 run 一次；运行结束后 audit、原样分离正文与引用并保留交付。执行 prompt、command、stdout events、stderr、版本、模型配置、输入返回、冻结文件及哈希均存于各阶段目录。

Writing thread：`01a11587-4949-7b83-bdd5-d2e92c1d6c15`；exit 0；346.77 秒。Polishing thread：`01a1158d-6835-7060-a24c-7e7d84efb335`；exit 0；343.10 秒。两者是新独立会话，没有恢复旧线程；各阶段 attempt=1，没有反馈重跑或结果选择。

Polishing 的正常科学、作者及摘要输入与 Writing 相同。唯一额外交接是本轮 Writing 原样英文及引用；只分离原输出中的这两个连续部分并处理外部换行，未修改文字。中文译文、作者说明、协调端评价和运行记录未交给 Polishing。交接字节在 preflight 和最终 verification 中核对。

实际入口：两端 router／manifest→各自 section/intro.md→共享专用 Introduction 索引→按任务选择的三层正向材料。Writing 的 Introduction fragment 在 `item_18`、索引在 `item_19` 完整返回；Polishing 的 fragment 在 `item_13`、索引在 `item_17` 完整返回。三层返回命令和覆盖由 [loading-summary.json](loading-summary.json) 精确记录；两端科学表达核心及必需 core 均完整返回。没有冲突 generic 指导、其他 section 卡集、额外出版来源或显式目录外读取。隔离沿用外部材料目录、禁用自动上下文／已安装 Skills 和命令审计机制，未宣称操作系统级读隔离。

Writing 8 段／917 词，Polishing 8 段／828 词。完整首次输出含英文、逐段中文、实际九条参考文献及原样作者说明。delivery 只是首次 Polishing 的精确复制；[English-stage-diff.patch](delivery/English-stage-diff.patch) 记录两阶段变化，不是协调端改稿。

先保存两阶段完整首次输出，再进行协调端全文评价。执行／加载身份验证与科学、逻辑、表达判断分别保留，前者不证明效果。完成后只提交本次记录并停止，不继续修改或测试候选；本例不补记迁移、可靠遗漏检测或稳定性。

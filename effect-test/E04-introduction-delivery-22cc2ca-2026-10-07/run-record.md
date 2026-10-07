# 冻结 22cc2ca：E04 独立 Writing＋独立 Polishing

开始时工作区干净，本地 HEAD、fetch 后 origin/main 与 live GitHub main 均为 `22cc2ca4a7329e2a905a71e151ce589b114416e5`。默认 Git 代理 127.0.0.1:7897 不可连接，使用单命令空代理配置后 fetch 和 ls-remote 成功；未修改全局 Git 配置。本轮只新增本目录记录。

作者输入按 AGENTS.md 从根目录当前《核心要求.txt》《我自己的经验和做法.txt》《引言写作方法.txt》及 current-author-adjustment.txt 原样冻结，fresh 哈希分别为：

| 文件 | SHA-256 |
| --- | --- |
| 核心要求.txt | `81df9c6b40105b9c63ce142122506160bd675401a7906c43f7d8a8d3ebfe498e` |
| 我自己的经验和做法.txt | `22e9ed26bc6dd28a6b248e47d82ba1f35714617d312f5d06dfcc6b58e0b7d0f2` |
| 引言写作方法.txt | `2cb1795a8dece2abdcb2e773218a197a4d7d2801e25b1c845248697e9843bc9b` |
| current-author-adjustment.txt | `1e91e62c04650a99c962aada26bc9e282a7e3eb888e5108a1e1dbed46a151d85` |

作者原文件及 current-author-adjustment 在本目录保留，并分别进入两阶段 materials/inputs；Polishing 与 Writing 的八项共同科学／作者材料逐字节相同。前三份 root 作者文件与 Git 原始 blob 的差异仅为换行，本轮使用 root 字节。历史身份只抽取已确认科学来源字段，没有继承历史作者哈希、override 或追加澄清。

科学、背景、引用、已验收摘要和两阶段自主 task 原样复制既有 447c0c4 记录，科学来源仍是已确认的 E04 253dae3 输入。`execute_once.py` 和所有执行、留存、加载工具为既有文件的字节一致副本；prepare_runner、preflight 与记录核验只绑定本轮候选和当前作者身份。未修改执行逻辑、隔离参数、模型或推理强度。

两阶段均先 prepare→preflight，再 run 一次。Writing 的新 thread 为 `01a115e3-be83-75b2-8ce4-dce9e9db7e19`，463.49 秒，exit=0；Polishing 的新 thread 为 `01a115eb-3da1-7203-914f-9d99a18f6a3d`，243.35 秒，exit=0。均为 `gpt-6.1-sol / high`，Codex CLI `0.160.0`，attempt=1。stderr 保留模型目录刷新 timeout 的原始提示；两次正文调用都实际执行并成功结束，没有启动失败后的重跑。

执行 prompt、command、runner snapshot、候选与材料清单及哈希、调用前完整输入实际返回、stdout events、stderr、run-meta 和完整 first-output 均在各阶段目录。完整首次输出与 terminal 消息一致（允许文件末尾换行）；材料和外部临时运行目录未被执行端修改。

沿用 ephemeral 新 CLI、项目外材料目录、关闭自动规则／安装 Skill／plugins／apps／memories／multi_agent／web search 的协议，允许材料范围内只读操作并核对显式命令。没有声称操作系统级读隔离。两阶段审计均未发现显式越界读取。目标论文原文、目标原引言、历史稿、诊断、预拟主线、修法及执行记录均不在正常材料中。

实际加载：两阶段 router、manifest、必需 core、algorithmic／intro／generic／相应 language fragment 均完整返回；Writing 使用 zh-to-en 并加载 en，Polishing 按英文首稿使用 en。两者直接进入专用 robotics-introduction-examples 索引，完整返回六项整节任务与九个完整段落范例。Writing 完整返回 26 个表达组，Polishing 完整返回 17 个表达组：E01–E06、E09–E11、E17–E19、E22–E26。各组逐行范围、英文、分析表返回和文件身份见 loading-summary.json 及原始 events；未读取其他 section 的卡集、冲突 generic Introduction 指导或额外出版来源。材料可用、实际返回与效果采纳分别判断。

Writing 首次输出保存后，仅机械分离其英文和引用，保持措辞与顺序，仅规范外部换行。Polishing current-draft 与该原样交接文件逐字节相同；中文、Writing 作者说明及协调评价未交接。Polishing 完整首次输出保存后，再执行原样交付保留及协调端全文评价。英文 906→852 词，均为六个论述段落、一个贡献引导、三项贡献；中文与九条实际引用完整留存。

交付文件为首次 Polishing 原样复制，未修稿。协调端评价独立保存在报告.md，未反馈给任一执行会话。所有身份、加载、交接、字节、链接与凭据模式核验是记录核验，不是额外模型调用或候选测试。按 AGENTS.md 完成新记录后运行根目录 sync.ps1 提交推送，再核实分支干净且本地、origin/main、live main 一致；实际同步提交号在本次用户答复中报告。

完成后停止，不追加候选修改、安装、反馈重跑或测试。

# 独立 review-only 运行记录

起点核对：本地 HEAD、origin/main 与最新 GitHub refs/heads/main 均为 `02152cb71f4db89c9b4851b4a5edaacf70e73aea`，工作区干净。候选仍冻结在 `ed9e42bd68634d611dab0874d07c0ec200cbaabd`；与当前候选逐文件 Git 字节相同。

本次复用上轮 Polishing 材料快照中的冻结 nature-polishing/nature-shared 候选及声明依赖，用其复核能力审查原样 Writing 英文首稿和引用。八份科学／背景／引用／摘要／作者要求／最新调整输入逐字节复用，原 Writing 任务另按原字节保留，用于理解稿件的作者任务；新的 task.md 只提出中性的 review-only 请求。没有提供后续 Polishing 输出、作者说明、协调端评价、诊断、错误定位或期待问题清单。

原 Writing 英文与引用是上轮 raw-introduction-and-references.md 原字节，未加入其规划、中文或备注，也未预先编号错误。最新 current-author-adjustment.txt 按原字节提供，覆盖冲突旧要求。本次不新增实验取舍规则。

prepare_review.py 只准备材料、审查请求和原参数；execute_once.py 的 run/audit 按原字节复用，其 prepare 分支未使用。CLI 仍为原0.160.0，gpt-6.1-sol/high、独立 ephemeral 会话、禁用自动规则／安装技能／插件／记忆／多代理／联网、外部材料目录、stdin 输入和仅一次调用保护保持原样；命令参数仅更换运行目录与首次输出保存路径。任务请求由“生成润色全文”改为“审查并报告，不提供替换稿”，这一改变是本轮作者指令，不是执行器或候选改造。

11份输入逐行读取并与 PowerShell 实际返回核对后纳入请求。冻结清单、原始提示、CLI 配置、材料快照、完整 events.jsonl、stderr、首次输出和实际返回审计保留。本次材料目录约束来自明确指令及日志核验，不声称操作系统强制读取沙箱。

每阶段只有一个 review 会话，无反馈、重新调用、输出选择或协调端编辑审查文本。首次输出保存后才进行协调端评价；识别、漏检、误报及下一步依据仅保存在执行端材料之外。本次只验证单独审查能力，不计为自主写作通过，不推断旧会话的隐藏检查、迁移或稳定性。

所有新增记录仅写入本目录；三层材料、候选、上轮全部输出与既有历史记录保持原样。按 AGENTS.md 提交同步后停止，无论首次审查表现如何均不追加修复或重跑。

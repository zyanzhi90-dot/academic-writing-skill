# 实际写作首次运行记录（2026-10-02）

本轮仅执行并保存，不评价、修订生成稿，不安装或修改 Skill。候选冻结为 `e126a659d77195f79416815db6ddb5827e60588e`：writing `1.5.1-rc.3`、polishing `6.6.1-rc.3`、shared `1.6.1-rc.2`。沿用旧 F1 成功运行的 `gpt-6-sol / medium`，分别启动一次独立 `codex exec --ephemeral --ignore-user-config` 会话；没有重跑、挑选答案或覆盖旧记录。下述成功仅指运行正常结束和记录保存，不是写作质量通过。

| 任务 | 冻结输入 | 原样首次完整输出 | 运行状态 |
|---|---|---|---|
| Drafting：整体论证思路、摘要及连贯正文 | [drafting.md](inputs/drafting.md) | [first-output.md](drafting/first-output.md) | 退出码 0；135.57 秒；15,537 字节 |
| Polishing：同一事实包与原样输入正文，润色完整正文 | [polishing.md](inputs/polishing.md) | [first-output.md](polishing/first-output.md) | 退出码 0；121.56 秒；9,527 字节 |

两份任务输入均逐字节包含 `effect-test/inputs/F1.md` 中完整的作者事实段及《我自己的经验和做法.txt》的原文偏好，没有添加科学材料。Polishing 正文从 `effect-test/runs/F1/candidate-repair-2/first-output.md` 的 `### Introduction` 开始，至 `## Notes` 前结束，保持原字节、顺序和标点；路由、central argument 和文外 Notes 不进入待润色正文。它不使用本轮 Drafting 输出。来源 SHA-256、提取字节范围、133 个候选文件的哈希、输入和保护文件的哈希见 [provenance.json](provenance.json)。

执行者仅获当前冻结任务（含作者材料、偏好及 Polishing 原样正文）、对应候选入口与声明依赖，可按需读取范例、`文献资料/` 原文及 `analysis/reading/`、`analysis/extracted/` 的提取文本；未提供旧评价、诊断、预期答案或其他旧输出。项目 AGENTS 作为继承的环境同步指令，不含写作答案。

运行工具 [run_once.py](../run_once.py)仅增加本轮所需的自定义冻结输入/新记录目录、F1 Polishing 角色、允许声明原文回查和本机原生 CLI 入口选项；旧任务默认仍禁止原文回查，拒绝覆盖既有目录的保障保留。每次调用前保存实际执行提示、命令、输入哈希和模型设置，再执行。实际提示及完整原始日志分别见：

- Drafting：[execution-prompt.txt](drafting/execution-prompt.txt)、[execution-command.json](drafting/execution-command.json)、[frozen-run.json](drafting/frozen-run.json)、[run-meta.json](drafting/run-meta.json)、[events.jsonl](drafting/events.jsonl)、[stderr.txt](drafting/stderr.txt)、[loaded-files.json](drafting/loaded-files.json)。
- Polishing：[execution-prompt.txt](polishing/execution-prompt.txt)、[execution-command.json](polishing/execution-command.json)、[frozen-run.json](polishing/frozen-run.json)、[run-meta.json](polishing/run-meta.json)、[events.jsonl](polishing/events.jsonl)、[stderr.txt](polishing/stderr.txt)、[loaded-files.json](polishing/loaded-files.json)。

加载记录从完成的真实读取/检索命令提取文件路径与哈希，并保留命令、退出码、范围和检索表达式。Polishing 的批量 `Join-Path` 读取按实际 role root 解析，并以每文件输出标记核对；目录列举单独记录。Drafting 记录 30 个候选文件，Polishing 记录 23 个；两项均记录到共用范例参考和 `analysis/reading/P17.txt` 的按需回查。各自明确读取的非候选/语料文件只有自己的冻结输入，没有记录到旧评价、诊断、其他输出、baseline 或现装 Skill 的读取。文件检索或局部读取不等于通读全部内容；原日志保留供负责人核查。

[verification.json](verification.json)核对候选、全部保护项目文件（运行器的授权适配除外）、两用户安装目录、冻结输入和执行提示均未变化，Polishing 正文原样保留；两份首次输出与各自日志最终回复一致（仅忽略 CLI 末尾换行差异）。输出本身未改写；其 SHA-256 已记录。原运行日志中的失败工具命令亦保留，不清除记录。

[prepare_inputs.py](prepare_inputs.py)记录输入提取与冻结方法，拒绝替换已有冻结材料；[collect_records.py](collect_records.py)仅整理执行证据与保护检查，不分析稿件质量。任务内容和执行提示已固定后才启动模型，未由前一输出或运行过程诊断改写后续输入。此次不形成评分、通过结论或修改稿，供负责人后续验收；反馈修改等待派发。

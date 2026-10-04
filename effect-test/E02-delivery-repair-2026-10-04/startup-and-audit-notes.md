# 启动与审计补记

这些情况不计作摘要重跑，也不隐去：

1. 首次准备中 Python 的 `shutil.which('codex')`解析到非 exe 入口，原生 exe 校验失败；没有 subprocess 模型调用。目录 `preparation-cli-resolution-no-invocation`保留该次材料及执行层输入返回。随后以 PowerShell Get-Command 取得现有原生入口。
2. 原生 CLI 的第一次启动在配置解析时报错，`skills.config`需要 TOML sequence，JSON对象表达被解释成 string。`startup-config-error-no-model-session/stderr.txt`及 run-meta 原样保留，events为空，没有 thread.started，没有摘要。改为 TOML inline table sequence 后才产生第一次有效模型会话。
3. drafting-frozen 准备命令返回持续运行的终端会话时，协调端过早执行 run，因 frozen-run.json 尚不存在而在 subprocess 之前报 FileNotFoundError。随后等准备退出0才启动实际模型。drafting-frozen/events.jsonl只有一个 thread.started、一个有效会话；无首次稿被覆盖。此项协调端执行错误不归入写作效果。
4. 旧基线 runner 没在准备时复制快照；后续按实际补丁逆向还原，其字节 SHA-256 与调用前冻结值完全一致。`polishing-baseline/runner-snapshot.py`明确是事后恢复的准确源码，不伪称当时已复制。新两阶段均在调用前保存 runner 快照。
5. 首版逐行审计只识别 `1: …`，未识别 PowerShell `{0,4}`输出的左侧空格，因此曾保守记录 Polishing 新模块未完整返回。原始证据未改；后续 `loading-and-retention-padded-number-audit.json`按空白填充的行号逐行复核，确认 polishing-source-check 实际完整读取新模块。Drafting 没有读模块的判断不变。这是审计实现修正，没有模型重跑或稿件编辑。
6. 两份启动失败的重复材料已与有效基线材料逐字节比较相同；清理副本的原生 PowerShell命令被工具策略拒绝，未给具体理由。未换其他工具规避，副本仍保留，duplicate-material-retention.json只记录其对应关系，不表示已经删除。

各阶段 raw events、输入、参数和完整首稿是主证据；上述说明不是其替代。未安装 Skill，未改项目外文件或凭据，运行材料副本置于普通临时目录。

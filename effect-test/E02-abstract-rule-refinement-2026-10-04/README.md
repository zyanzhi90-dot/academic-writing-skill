# 已知 E02 案例自主回归：Abstract 规则精简与衔接

负责人核对起点 420b711；上一测试候选 7f76312；新候选冻结为 fd7dbcb7f8c6bc5d40e2396c2aa9f3571cbb3eee。仅修改两端 Abstract 专属文件，共三处，其他 Skill 实现未改。

- [具体问题、改动、判断影响与收益](change-rationale.md)；[实际补丁](candidate-change.patch)；[格式、UTF-8 与静态加载核对](preflight.json)。
- [原样首次英文、中文译文及模型说明](drafting/first-output.md)；[英文原样截取](abstract.en.txt)；[中文原样截取](abstract.zh.txt)。
- [正文评价、合理变体及必要人工调整](evaluation.md)：外环信息关系已有进展；内环 PD／PD-like 类别错误必须修正，补偿作用与保证限定需局部完善。不是因“还能优化”判失败。
- [冻结输入和运行副本](frozen-materials.json)；[运行参数](drafting/frozen-run.json)；[完整日志](drafting/events.jsonl)；[原始加载记录](drafting/loaded-files.json)；[实际返回内容核对](first-output-audit.json)；[原样留存核对](verification.json)。

单次 gpt-6.1-sol／high、新隔离 ephemeral 会话，原样保存首稿，无反馈、重跑、挑选或改稿。材料文件完整，但核心要求的单行读取只返回首字；本轮记录此限制，不补读或再测，不能作为完整输入的自主通过证据。未安装 Skill、未覆盖历史材料、未推进 E03。交负责人决定下一阶段。

本目录的局部 `.gitattributes` 保持输入、输出、参数和日志的实际字节；提交后运行 verify_git_bytes.py 核对，不作换行转换。

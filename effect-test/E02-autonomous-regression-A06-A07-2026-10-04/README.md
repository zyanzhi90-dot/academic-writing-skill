# 已知 E02 案例自主回归

负责人验收起点 e18c516；原候选 5b8bbca；本轮 A06／A07 分析补充后的实际候选冻结为 7f7631279920a08ef93108c8a23512ccacaff479。

只修改共享范例文件中 A06／A07 分析，保留完整英文与其他实现。没有安装 Skill，未覆盖历史材料，未推进 E03。

- [实际修改及正文依据](card-change-rationale.md)；[改动补丁](candidate-change.patch)；[范围、格式、UTF-8 与加载核对](preflight.json)。
- [首次完整英文摘要、中文译文与模型作者说明](drafting/first-output.md)；[英文原样截取](abstract.en.txt)；[中文原样截取](abstract.zh.txt)。
- [协调端独立评价与剩余调整](evaluation.md)：主线可保留，需要局部方法／验证句群修订；本轮未判自主写作通过。
- [实际材料清单和冻结证据](frozen-materials.json)；[完整运行日志](drafting/events.jsonl)；[参数](drafting/frozen-run.json)；[加载记录](drafting/loaded-files.json)；[首次输出与输入边界核对](first-output-audit.json)；[原样留存核对](verification.json)。

沿用单次 gpt-6.1-sol／high、新隔离 ephemeral 会话；同次调用自动恢复连接后成功退出，没有反馈、重跑、挑选或改首次输出。标准请求与原样事实／经验／核心要求在 materials/inputs；模型只接收该目录内冻结候选与声明依赖。author-request.txt、本轮来源分析和评价留在协调端，未进入写作输入。

这是已知 E02 案例自主回归，加载正确不能代替效果通过，不外推新论文迁移或整体写作通过。结果交负责人独立验收。

本目录用局部 `.gitattributes` 禁止换行转换，使 Git 留存的输入、输出、参数及日志保持实际运行字节；未修改首次摘要或运行材料。提交后的全目录字节核对由 verify_git_bytes.py 执行。

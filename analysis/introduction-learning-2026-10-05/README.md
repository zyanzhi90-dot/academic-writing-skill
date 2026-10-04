# Introduction 学习分析材料

先读 [分析报告](report.md)。本轮只分析四篇引言，未修改 Skill，未运行写作测试。

完整英文与段落定位：

- [P17／A06](P17-introduction.md)：默认表达锚点，示教表征到轨迹执行。
- [P05／A07](P05-introduction.md)：双臂相对运动与学习条件。
- [Fuzzy2023／A02](Fuzzy2023-introduction.md)：瞬态约束、收敛时间与保证依据。
- [ESO2017／A04](ESO2017-introduction.md)：扰动来源、补偿和可测信息。

源文身份、旧材料复用及作者输入哈希见 [source-provenance.json](source-provenance.json)；逐块提取见各 `*-page-blocks.json`／`.txt`，版面核对图见 `page-previews/`，排版规范化记录见 [normalization-log.json](normalization-log.json)。旧 P17／P05 全文提取保留在上一级 `reading/`，本轮没有覆盖。

[evidence-checks.json](evidence-checks.json) 记录来源、引文、链接、作者输入和候选未改动的完整性核对。它不是生成测试、加载测试、效果或迁移验收。

`root1.pdf` 未在已搜索位置检出，没有用其他作者稿替代。仓库开始时已有的《核心要求.txt》作者更新原样保留；同步提交包含该已有更新与本目录分析材料。

三个数据处理脚本 `read_sources.py`、`curate_introductions.py`、`resolve_report_quotes.py` 分别生成提取／版面证据、整理原文、填入报告引文；`verify_evidence.py` 做只读完整性核对。脚本不调用模型，不修改 Skill，不启动测试。`resolve_report_quotes.py` 仅用于报告写作时的占位符解析，当前报告已填好引文，重跑不会改写分析。

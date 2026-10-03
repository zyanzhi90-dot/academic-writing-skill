# E01 Abstract 定点反馈 Polishing（c2c0953）

本记录为一次针对验证部分的反馈修订，**不是独立首次 Drafting 的通过证据**。使用冻结 nature-polishing、原样 E01 中文科学事实包、个人经验、指定首次稿及作者本次原话反馈。修订全文及执行者说明原样保留，未人工改写；原始首次稿和日志不变，不修改或安装 Skill，不推进其他 section。

## 输入、冻结和唯一运行

候选提交 `c2c09537e4f1f944eb8a8aa82cbc7ecf5203b6a7`；polishing／shared 的58个文件直接取自该提交，逐字节等于 Git blob，没有副本改写。版本 `6.6.1-rc.6`／`1.6.1-rc.5`；未提供 writing 包。

[任务](materials/inputs/task.md)、[作者原话反馈](materials/inputs/feedback.md)、[事实包](materials/inputs/scientific-facts.md)、[个人经验](materials/inputs/personal-experience.txt)、[当前稿](materials/inputs/current-draft.md)共5个输入。后3项与项目来源逐字节一致；当前稿 SHA-256 `7a3ca0c8db8519e17ff41b86d2b0bbf74d4d47eab131764c2584b6348a363fa6`。反馈直接保存作者关于模拟目的、实机结果、移动目标及限定修改范围的原话，不给预先写好的替换句。

允许参考库复用已核实的前次材料，只复制当前21篇学习 PDF、3份独立归档原文及与其一致的24份提取文本；字节哈希均不变，20张卡片均可按需读取。没有复制前次运行记录、诊断、评价、来源定位或其他输出；只有本次明确授权的当前稿作为输入。111个允许文件及哈希见 [frozen-materials.json](frozen-materials.json)，启动前核对见 [preflight.json](preflight.json)。

采用项目外纯材料目录，`codex exec --ephemeral --ignore-user-config --ignore-rules` 新线程；禁用自动项目说明、发现的现装 Skill 入口、网络搜索及 plugins／remote_plugin／apps／hooks／memories／multi_agent，不改现装文件或用户配置。隔离证据为材料边界、自动加载限制和实际命令核对，不宣称操作系统权限隔离。

模型参数 `gpt-6.1-sol / high`，CLI `codex-cli 0.159.2`，线程 `01a10019-117d-7812-926e-2c739898ec46`。唯一调用，退出码 **0**，耗时 **142.89秒**。prepare／run 拒绝覆盖材料或第二次调用；工具沿既有机制，只适配 Polishing 包、目标目录、明确授权输入和反馈任务标记。原有收集逻辑仅改留存目录，并沿用前次已补的显式 UTF-8 检索识别。

## 原样交付与实际加载

- [polishing/first-output.md](polishing/first-output.md)：本次唯一反馈修订全文，英文摘要、中文翻译及执行者说明；**3229字节**，SHA-256 `7ea27d55626e65dfb3e1ad96954618f6e99031e57ccd31a60aa0fe250223f082`，与原始事件最后交付消息一致，仅不计末尾换行。
- [execution-prompt.txt](polishing/execution-prompt.txt)、[execution-command.json](polishing/execution-command.json)、[frozen-run.json](polishing/frozen-run.json)：提示、参数、模型／CLI版本及工具／输入哈希。
- [events.jsonl](polishing/events.jsonl)、[stderr.txt](polishing/stderr.txt)、[run-meta.json](polishing/run-meta.json)：原始完整运行记录；[loaded-files.json](polishing/loaded-files.json)、[loading-audit.json](polishing/loading-audit.json)保存实际路径、读取顺序和返回范围。

实际读取5个输入及15个候选文件，包含 nature-polishing 入口、manifest、全部 always-load（含修正后的 stance 和 scientific-expression）、methods、abstract、generic、en；未调用 nature-writing 或写其他 section。共24条工具命令，23条成功返回显式 UTF-8 文本，1条标题检索未匹配（退出码1、无返回内容，日志原样保留）；这是同一修订调用中的工具检索，不是重跑写作。

共用说明／索引先于卡片完整返回。A04、A05、A06、A07完整返回，其中执行者明确以 A06 的对象／句法、A04 的目的表达、A07 的结果表达作为修改依据；A05的实际读取不等于已采用其全部实现。1083行返回内容与冻结文本一致，无文本差异、未映射返回、显式目录外材料读取或未解析读取命令。没有整库预加载或直接回查 PDF／提取文本。

## 修改位置、依据与科学核对

对照原始稿和本次输出，英文和中文均只改第7–9句，前6句逐句原样保留；正文外说明更新为本次实际依据。没有扩展方法、稳定性、模型能力或其他 section。

| 位置 | 原表达与实际修订 | 匹配范例及适配依据 |
|---|---|---|
| 模拟目的（S7） | `Numerical simulations of … are used to evaluate …` → `Numerical simulation studies are carried out to evaluate …` | [A04 的实际英文](materials/skill-candidate/nature-shared/core/robotics-writing-examples.md)含 `Experimental studies are also carried out to …`。将研究对象和目的适配为数值模拟与运动再现评价；20种手写运动来自事实包。只陈述开展研究的目的，不补造模拟发现，不为使用 demonstrate 将目的升级成结果 |
| 实机发现（S8） | `Experiments with … demonstrate …` → `Experimental results obtained with … demonstrate that …` | A07 的 `Numerical simulation results demonstrate …` 提供结果作主语的实现，改为实机证据及作者自己已观察的示范位置／速度特点再现、不同起点向目标生成运动。保留 iCub／Katana-T 的证据归属，没有引入统一成功率、精度增益或无条件保证 |
| 移动目标观察（S9） | `The Katana-T experiments further show …` → `The Katana-T results further show …` | 沿 A07 的结果对象及 A06 的对象交接，用具体实验结果接到模型动作和目标在执行中被移动的条件。事实包直接支持轨迹朝新目标调整；不把这一空间调整观察写成独立时间扰动试验或额外控制保证 |

两类验证句式均从已认可的实际英文适配，不机械把所有证据写成 `Numerical simulation results demonstrate …` 或泛称 validity。中文末三句与英文逐句对应，保留目的／结果、实验对象和目标移动条件。这里仅核对本次反馈范围和科学依据，不给全文顶刊风格或独立起草通过结论，表达质量交作者验收。

[verification.json](verification.json)记录范围、科学支持、材料／运行副本、全部既有已追踪项目文件和六个现装包的哈希保留核对，以及唯一调用、原始输出和日志一致性。`* -text` 保留输入／输出／日志原始字节。新记录目录为本轮唯一项目变更，提交同步后停止。

同步工具适配：首次 `sync.ps1` 在 Git 索引归档 PDF 时遇到 Windows 文件名长度限制，尚未提交或推送。后续仅在当前 Git 命令环境中启用 `core.longpaths=true` 后同步，保留候选声明的目录和原始文件字节；不改 Git 全局配置、不重跑写作。

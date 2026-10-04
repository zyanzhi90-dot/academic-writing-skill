"""Save the reviewed human revision; retain the model's raw revision unchanged."""
from pathlib import Path
import hashlib
import json

RECORD = Path(__file__).resolve().parent
raw_path = RECORD / "drafting/first-output.md"
raw = raw_path.read_text(encoding="utf-8")
english = raw.split("**English abstract**\n\n", 1)[1].split("\n\n", 1)[0]
chinese = raw.split("**中文翻译**\n\n", 1)[1].split("\n\n", 1)[0]
edits = [
    {"english_before": "a residual policy learned from robot and object states",
     "english_after": "a residual policy based on robot and object states",
     "chinese_before": "根据机器人和物体状态学习的残差策略",
     "chinese_after": "基于机器人和物体状态的残差策略",
     "basis": "F07、式(5)：机器人和物体状态是策略输入；学习来源在下一句明确为环境交互。区分输入与数据来源，保持相加结构。"},
    {"english_before": "on a seven-degree-of-freedom Sawyer arm",
     "english_after": "on a Sawyer arm",
     "chinese_before": "仿真和七自由度 Sawyer 机械臂",
     "chinese_after": "仿真和 Sawyer 机械臂",
     "basis": "F01、A06 末句及其分析：保留实机平台和任务范围；自由度数不解释残差方法或所选比较，不承担本稿的必要范围。"},
]
for edit in edits:
    assert english.count(edit["english_before"]) == chinese.count(edit["chinese_before"]) == 1
    english = english.replace(edit["english_before"], edit["english_after"])
    chinese = chinese.replace(edit["chinese_before"], edit["chinese_after"])
content = (
    "# E03 人工反馈修订稿\n\n"
    "本稿使用 `ff1def8` 的当前 Writing 候选及声明依赖，以 `gpt-6.1-sol / high` 完成一次人工反馈修订，再作两处交付检查中的局部精修。模型原始修订输出另存；不计作自主写作或独立迁移通过，待负责人验收。\n\n"
    "**English abstract**\n\n" + english + "\n\n"
    "**中文译文**\n\n" + chinese + "\n\n"
    "**实际修改依据**\n\n"
    "- 增补模型结构可利用、接触与摩擦难以准确建模的组合理由，并把残差修正接到环境交互学习。借鉴 A08 的能力—难点—互补设计关系，保持方法开篇。\n"
    "- 保留信号相加与完整任务回报优化；将状态表述为策略输入，交互表述为学习来源，避免混淆两种关系。\n"
    "- 删除固定侧块的迁移分支及千步结果，保留对纯 RL 的样本与最终表现比较，以及初始错位实机的 15/20 对 2/20。两项分别支持利用既有结构的优势与接触修正的作用，不展开实验清单。\n"
    "- 保留 Sawyer 和块插入任务，删去自由度数；前者限定实机证据，后者不影响本稿的贡献或结论范围。其余准确成熟的原句保留。\n\n"
    "逐句、关键词组及原文依据见 [修改核对](revision-basis.md)；模型未经改动的修订输出见 [原始输出](drafting/first-output.md)。\n"
)
for name, data in (("feedback-revision.md", content), ("abstract.en.txt", english), ("abstract.zh.txt", chinese)):
    path = RECORD / name
    assert not path.exists(), name
    path.write_text(data, encoding="utf-8")
report = {"run_kind": "人工反馈修订", "autonomous_pass": False, "transfer_pass": False,
          "raw_model_revision_sha256": hashlib.sha256(raw_path.read_bytes()).hexdigest(),
          "raw_model_revision_unchanged": True, "delivery_check_local_edits": edits,
          "english_words": len(english.split()),
          "delivery_files_sha256": {name: hashlib.sha256((RECORD / name).read_bytes()).hexdigest()
                                    for name in ("feedback-revision.md", "abstract.en.txt", "abstract.zh.txt")}}
target = RECORD / "delivery-edits.json"
assert not target.exists()
target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"saved_feedback_revision": True, "local_delivery_edits": len(edits), "english_words": report["english_words"]}))

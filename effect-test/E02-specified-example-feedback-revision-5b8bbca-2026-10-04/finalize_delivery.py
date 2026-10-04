"""Apply two explicit delivery-level wording edits; retain the raw model response."""
from pathlib import Path
import hashlib
import json

RECORD = Path(__file__).resolve().parent
SOURCE = RECORD / "drafting/first-output.md"
TARGET = RECORD / "反馈修订稿.md"
assert not TARGET.exists() and not (RECORD / "delivery-edits.json").exists()
raw = SOURCE.read_bytes()
text = raw.decode("utf-8")
edits = [
    {
        "before": "proportional–derivative (PD)-like control",
        "after": "PD-like control",
        "reason": "Use the control category explicitly requested by the author and used in E02 §IV.A. The expanded name with (PD)-like makes the category needlessly awkward; no later standalone PD abbreviation requires this expansion.",
    },
    {
        "before": "类比例—微分控制加入了自适应补偿，以补偿机器人不确定动力学的影响",
        "after": "类比例—微分控制通过自适应补偿应对机器人不确定动力学的影响",
        "reason": "Remove the consecutive repetition of 补偿 while retaining the same control category, compensation mechanism, scientific object and purpose as the English sentence.",
    },
]
for edit in edits:
    assert text.count(edit["before"]) == 1
    text = text.replace(edit["before"], edit["after"])
text += (
    "\n- **交付检查微调：** 将模型返回的 `proportional–derivative (PD)-like control`简化为作者指定的 `PD-like control`，"
    "保留准确类别并省去绕口的展开；中文将连续的“自适应补偿，以补偿”整理为“通过自适应补偿应对”，"
    "补偿对象和作用不变。其余模型正文与修改依据保留。\n"
)
TARGET.write_text(text, encoding="utf-8")
assert SOURCE.read_bytes() == raw
(RECORD / "delivery-edits.json").write_text(json.dumps({
    "scope": "Two coordinator delivery edits after one model revision; no second model invocation",
    "source": "drafting/first-output.md", "source_sha256": hashlib.sha256(raw).hexdigest(),
    "delivery": TARGET.name, "delivery_sha256": hashlib.sha256(TARGET.read_bytes()).hexdigest(),
    "edits": edits, "added_rationale": "Final delivery-check bullet only",
    "raw_model_output_unchanged": True, "run_kind": "人工反馈修订",
    "autonomous_pass": False, "transfer_pass": False,
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("Two delivery edits recorded; raw model response unchanged.")

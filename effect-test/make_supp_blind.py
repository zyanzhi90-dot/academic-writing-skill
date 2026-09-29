"""Create anonymous copies of the supplemental D1v2 first outputs."""

import json
from pathlib import Path
import random
import shutil

test = Path(__file__).resolve().parent
blind = test / "blind"
versions = ["baseline", "candidate"]
for version in versions:
    if not (test / "runs" / "D1v2" / version / "first-output.md").is_file():
        raise SystemExit(f"D1v2 {version} is not complete")
random.SystemRandom().shuffle(versions)
mapping = dict(zip(("A", "B"), versions))
for label, version in mapping.items():
    target = blind / f"D1v2-{label}.md"
    if target.exists():
        raise SystemExit(f"Refusing to replace {target}")
    shutil.copy2(test / "runs" / "D1v2" / version / "first-output.md", target)
(blind / "D1v2-mapping.json").write_text(json.dumps(mapping, ensure_ascii=False, indent=2), encoding="utf-8")
print("Anonymous D1v2 A/B copies created; mapping withheld until evaluation is written.")

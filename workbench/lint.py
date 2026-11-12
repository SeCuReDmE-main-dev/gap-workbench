"""Entry linter: checks the 8 fields before submission.

Reads entry/fields.md (one '## N. Title' section per field) and reports:
word counts, negations (written or implied), links, and numbers that are not
found in the repository's data or evidence files.
Consistency review only; it gives no score.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NEGATION = re.compile(
    r"\b(not|no|never|haven'?t|hasn'?t|isn'?t|aren'?t|won'?t|can'?t|cannot|yet|pending|unsigned|"
    r"to be signed|sign (one|a) )\b", re.I)
URL = re.compile(r"https?://[^\s)>\]]+")
NUMBER = re.compile(r"(?<![\w.])\d[\d,]*(?:\.\d+)?")
LIMITS = {7: 150}


def fields(text: str) -> dict[int, str]:
    out, cur = {}, None
    for line in text.splitlines():
        m = re.match(r"##\s+(\d+)\.", line)
        if m:
            cur = int(m.group(1)); out[cur] = ""
        elif cur:
            out[cur] += line + "\n"
    return out


def corpus() -> str:
    parts = []
    for p in list((ROOT / "data").glob("*")) + [ROOT / "docs" / "evidence.md"]:
        if p.is_file():
            parts.append(p.read_text(encoding="utf-8", errors="ignore"))
    return "\n".join(parts)


def lint(text: str) -> list[str]:
    issues, known = [], corpus().replace(",", "").replace(" ", "")
    for n, body in fields(text).items():
        words = len(body.split())
        if n in LIMITS and words > LIMITS[n]:
            issues.append(f"field {n}: {words} words > {LIMITS[n]}")
        for m in NEGATION.finditer(re.sub(URL, "", body)):
            issues.append(f"field {n}: negation '{m.group(0)}'")
        for num in NUMBER.findall(re.sub(URL, "", body)):
            key = num.replace(",", "")
            if len(key) >= 2 and key not in known:
                issues.append(f"field {n}: number {num} not found in data/ or docs/evidence.md")
    return issues


if __name__ == "__main__":
    path = Path(sys.argv[1] if len(sys.argv) > 1 else ROOT / "entry" / "fields.md")
    found = lint(path.read_text(encoding="utf-8"))
    print("\n".join(found) or "0 issues")
    sys.exit(1 if found else 0)

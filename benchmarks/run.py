"""Benchmarks for the workbench. Writes data/benchmark.csv and prints a summary.

1. Engine vs published rates: 12 hand-computed cases from the LogisVert page.
2. Page vs engine parity: every capacity from 0 to 200,000 BTU/h in steps of 1,000 (node required).
3. Linter on a labelled corpus: 20 sentences, 10 with a negation or admission, 10 clean.
4. Speed: subsidy() calls per second.
"""
from __future__ import annotations

import csv
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from workbench.lint import lint  # noqa: E402
from workbench.subsidy import load, subsidy  # noqa: E402

GOLDEN = [  # (measure, BTU/h at -8 C, dollars computed by hand from the published rate)
    ("energy-star", 12000, 600), ("energy-star", 24000, 1200), ("energy-star", 36000, 1800),
    ("cold-climate", 12000, 1440), ("cold-climate", 24000, 2880), ("cold-climate", 48000, 5760),
    ("cold-climate-multiunit", 24000, 5280), ("cold-climate-multiunit", 9000, 1980),
    ("geothermal", 12000, 9000), ("geothermal", 36000, 18000), ("geothermal", 72000, 18000),
    ("geothermal-replacement", 36000, 9000),
]

NEG = [
    "We will sign one partner before October.", "The partner is not confirmed yet.",
    "Revenue depends on a deal we haven't closed.", "No installer has agreed so far.",
    "Pending approval from Hydro-Québec.", "We cannot guarantee the subsidy amount.",
    "The tool isn't finished.", "We won't have data before spring.",
    "It has never been tested with users.", "The agreement is unsigned.",
]
CLEAN = [
    "Installers already buy exclusive leads at 57 $ on Google.", "Pompon is live and tested.",
    "The rate is 120 $ per 1,000 BTU/h for cold-climate units.", "A human approves each rule change.",
    "Each answer links to the official page.", "The page reads the same rules file as the engine.",
    "Season 1 measures the send rate.", "Quebec homeowners compare two or three quotes.",
    "The checker writes the email to installers.", "Tests run in CI on every push.",
]


def bench_golden():
    rules = load()
    return [(m, b, want, subsidy(m, b, rules)) for m, b, want in GOLDEN]


def bench_parity():
    node = shutil.which("node")
    if not node:
        return None
    html = (ROOT / "docs" / "index.html").read_text(encoding="utf-8").replace("\r", "")
    fn = re.search(r"function subsidy\(m, btuh\) \{.*?\}", html).group(0)
    rules = load()
    caps = list(range(0, 200001, 1000))
    js = fn + "\nconst rules=" + json.dumps(rules) + ";const caps=" + json.dumps(caps) + \
        ";console.log(JSON.stringify(rules.measures.map(m=>caps.map(c=>subsidy(m,c)))));"
    out = json.loads(subprocess.run([node, "-e", js], capture_output=True, text=True, check=True).stdout)
    py = [[subsidy(m["id"], c, rules) for c in caps] for m in rules["measures"]]
    cases = len(caps) * len(rules["measures"])
    diff = sum(a != b for ra, rb in zip(out, py) for a, b in zip(ra, rb))
    return cases, diff


def bench_lint():
    flag = lambda s: bool(lint("## 6. Money\n" + s + "\n"))  # noqa: E731
    tp = sum(flag(s) for s in NEG)
    fp = sum(flag(s) for s in CLEAN)
    return tp, len(NEG), fp, len(CLEAN)


def bench_speed(n=100_000):
    rules = load()
    t = time.perf_counter()
    for i in range(n):
        subsidy("cold-climate", (i % 200) * 1000, rules)
    return n / (time.perf_counter() - t)


if __name__ == "__main__":
    rows = []
    g = bench_golden()
    ok = sum(w == got for _, _, w, got in g)
    rows.append(("engine_vs_published_rates", f"{ok}/{len(g)} exact"))
    p = bench_parity()
    rows.append(("page_vs_engine_parity", "node missing" if p is None else f"{p[0] - p[1]}/{p[0]} identical"))
    tp, n_neg, fp, n_clean = bench_lint()
    rows.append(("linter_recall_on_negations", f"{tp}/{n_neg}"))
    rows.append(("linter_false_alarms_on_clean_text", f"{fp}/{n_clean}"))
    rows.append(("engine_calls_per_second", f"{bench_speed():,.0f}"))
    with (ROOT / "data" / "benchmark.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["benchmark", "result"]); w.writerows(rows)
    for k, v in rows:
        print(f"{k:<36} {v}")
    for m, b, want, got in g:
        if want != got:
            print("MISMATCH", m, b, want, got)

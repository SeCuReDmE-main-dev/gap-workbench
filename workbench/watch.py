"""Rule watcher: re-reads the official page and reports any rate that no longer matches the data.

    python -m workbench.watch            # fetch the live page
    python -m workbench.watch page.html  # check a saved copy

Every rate in data/logisvert.json must appear on the source page as "<rate> $ par 1 000 BTU/h"
(French page). A rate that disappears, or a new rate that appears, is reported for a human to review.
"""
from __future__ import annotations

import html as htmllib
import re
import sys
import urllib.request
from pathlib import Path

from .subsidy import load

RATE = re.compile(r"(\d{2,4})\s*\$\s*par\s*(?:tranche\s*de\s*)?1\s*000\s*BTU", re.I)


def rates_on_page(html: str) -> set[int]:
    text = htmllib.unescape(re.sub(r"<[^>]+>", " ", html)).replace(" ", " ").replace(" ", " ")
    return {int(x) for x in RATE.findall(text)}


def check(html: str, rules: dict | None = None) -> dict:
    rules = rules or load()
    expected = {m["per_1000_btuh"] for m in rules["measures"]}
    known = {k["per_1000_btuh"] for k in rules.get("known_other_rates", [])}
    found = rates_on_page(html)
    return {"expected": sorted(expected), "found": sorted(found),
            "missing_on_page": sorted(expected - found), "new_on_page": sorted(found - expected - known)}


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "gap-workbench-watch/0.1"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", errors="ignore")


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    rules = load()
    html = Path(argv[0]).read_text(encoding="utf-8") if argv else fetch(rules["source"])
    r = check(html, rules)
    print(r)
    return 0 if not r["missing_on_page"] and not r["new_on_page"] else 1


if __name__ == "__main__":
    sys.exit(main())

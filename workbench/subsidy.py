"""LogisVert subsidy calculator (standard library only)."""
from __future__ import annotations

import json
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "logisvert.json"


def load() -> dict:
    return json.loads(DATA.read_text(encoding="utf-8"))


def subsidy(measure_id: str, btuh_at_minus8: int, rules: dict | None = None) -> int:
    """Dollar subsidy for one measure and a capacity in BTU/h at -8 °C."""
    if not isinstance(btuh_at_minus8, int) or btuh_at_minus8 < 0 or btuh_at_minus8 > 200_000:
        raise ValueError("capacity must be an integer between 0 and 200,000 BTU/h")
    rules = rules or load()
    m = next((x for x in rules["measures"] if x["id"] == measure_id), None)
    if m is None:
        raise ValueError(f"unknown measure {measure_id!r}")
    amount = round(m["per_1000_btuh"] * btuh_at_minus8 / 1000)
    return min(amount, m["cap"]) if m["cap"] else amount


def compare(btuh_at_minus8: int) -> list[tuple[str, int]]:
    """Every measure for the same capacity, highest first: what to ask the installer for."""
    rules = load()
    rows = [(m["id"], subsidy(m["id"], btuh_at_minus8, rules)) for m in rules["measures"]]
    return sorted(rows, key=lambda r: -r[1])

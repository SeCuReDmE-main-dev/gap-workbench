# AGENTS.md

Instructions for AI agents working in this repository. Read `HUMAN.md` first.

## Map

- `data/logisvert.json`: single source of truth for rates. `docs/logisvert.json` must be an exact copy.
- `workbench/subsidy.py`, `workbench/lint.py`, `workbench/watch.py`: standard library only.
- `docs/index.html`: the Pompon page; its `subsidy()` must match `workbench/subsidy.py` (benchmark checks 1,005 cases).
- `research/log.md`: one timed line per step.

## Commands

```bash
python -m unittest discover -s tests   # must pass before any commit
python benchmarks/run.py               # must stay 12/12, 1,005/1,005, 10/10, 0/10
python -m workbench.watch              # network
```

## Rules

1. Every rate needs an official `https://` source and a test.
2. A rate seen on the page but not applied goes in `known_other_rates` with the reason.
3. Never describe the output as advice.
4. No new runtime dependencies without a human decision.
5. Never commit entry texts for the hackathon (rights assigned to We The Flywheel), secrets, or personal data. `entry/` is git-ignored.
6. Commits use the GitHub noreply identity and `git commit -s`.

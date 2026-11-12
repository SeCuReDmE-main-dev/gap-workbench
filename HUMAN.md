# HUMAN.md

For the person who owns this repository. Version 0.1.0.

## In five lines

1. Pompon tells a Quebec homeowner, before any quote, what LogisVert pays for each type of heat pump.
2. The rates live in one file, `data/logisvert.json`, each with its official source.
3. `workbench/watch.py` re-reads the official page every Monday (GitHub Actions) and fails when a rate changes.
4. `workbench/lint.py` checks any text before it is published: word limits, negations, unsourced numbers.
5. Nothing here is advice; Hydro-Québec confirms the exact amount.

## The next human decision

The watcher found a **140 $ per 1,000 BTU/h** rate (very-high-efficiency unit with caulking work) still on the official page, which Protégez-vous reported ended in August 2025. Decide: add it to the checker, or keep it out. It is listed in `known_other_rates` until then.

## Who does what

| Task | Human | Agents |
|---|---|---|
| Approve a rate change | yes | open the pull request |
| Add an installer to the request network | yes | check licence and region |
| Weekly page check | read the failure | run `watch.py` |
| New copy on the page | approve | draft, run `lint.py` |

## When something breaks

| Symptom | Look at |
|---|---|
| Rule watcher badge red | `python -m workbench.watch` output: which rate is missing or new |
| Page shows no table | `docs/logisvert.json` exists and matches `data/logisvert.json` (a test checks it) |
| CI red | `python -m unittest discover -s tests` |

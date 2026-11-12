<p align="center"><img src="docs/banner.svg" width="100%" alt="Pompon: for the same 24,000 BTU/h, LogisVert pays 1,200 $ for an ENERGY STAR heat pump and 2,880 $ for a Cold Climate unit. Engine 12/12, page 1,005/1,005, linter 10/10, weekly rule watcher."></p>

# gap-workbench · Pompon

[![CI](https://github.com/SeCuReDmE-main-dev/gap-workbench/actions/workflows/ci.yml/badge.svg)](https://github.com/SeCuReDmE-main-dev/gap-workbench/actions/workflows/ci.yml)
[![Rule watcher](https://github.com/SeCuReDmE-main-dev/gap-workbench/actions/workflows/watch.yml/badge.svg)](https://github.com/SeCuReDmE-main-dev/gap-workbench/actions/workflows/watch.yml)
![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue)
![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)
![Tests: 11 passing](https://img.shields.io/badge/tests-11%20passing-brightgreen)
![Concept submitted to We The Flywheel – Find the Gap 2026](https://img.shields.io/badge/concept%20submitted%20to-We%20The%20Flywheel%20%E2%80%93%20Find%20the%20Gap%202026-7c3aed)

> **Information, not advice.** Pompon applies the public LogisVert rates. The exact amount is confirmed by Hydro-Québec from the model's AHRI number.

**Try it:** https://securedme-main-dev.github.io/gap-workbench/?btuh=24000 · **Evidence:** [docs/evidence.md](docs/evidence.md) · **Step log:** [research/log.md](research/log.md)

---

## English

### What this is

Two tools, built in one 45-minute window by one operator with AI agents:

| Tool | For whom | What it does |
|---|---|---|
| **Pompon** (`docs/index.html`) | Quebec homeowners comparing heat pump quotes | Shows the LogisVert subsidy for each type of unit at the reader's capacity, before any quote, then writes the email that asks installers for the unit that pays the most. |
| **Workbench** (`workbench/`) | The operator who runs the guide | Rules engine, entry linter, and a watcher that re-reads the official page and flags any changed rate. |

### The finding

For the same 24,000 BTU/h, an ENERGY STAR heat pump brings **1,200 $** and an ENERGY STAR Cold Climate unit brings **2,880 $**. The difference is the certification the quote names. Hydro-Québec's own estimator starts from a model or AHRI number, which buyers usually get with the quote.

### Quick start

```bash
python -m unittest discover -s tests          # 11 tests
python benchmarks/run.py                       # benchmarks -> data/benchmark.csv
python -m workbench.watch                      # re-read the official page (network)
python -m workbench.lint path/to/fields.md     # check an entry draft before submitting
python -c "from workbench.subsidy import compare; print(compare(24000))"
```

Standard library only. Python 3.10 or later. `node` is optional (page/engine parity benchmark).

### Workbench modules

| Module | Role | Proof |
|---|---|---|
| `workbench/subsidy.py` | LogisVert rates per 1,000 BTU/h at −8 °C, caps, comparison | 12/12 cases match the published rates |
| `workbench/lint.py` | Word limits, negations, every number checked against `data/` and `docs/evidence.md` | 10/10 negations caught, 0/10 false alarms |
| `workbench/watch.py` | Fetches the official page, compares each rate with `data/logisvert.json`, exits 1 on any change | First run found a 140 $ rate held for human review |
| `benchmarks/run.py` | Engine vs published rates, page vs engine (1,005 cases), linter accuracy, speed | `data/benchmark.csv` |

### Benchmarks (2026-11-12)

| Benchmark | Result |
|---|---|
| Engine vs published rates | 12/12 exact |
| Page vs engine parity | 1,005/1,005 identical |
| Linter: negations caught | 10/10 |
| Linter: false alarms on clean text | 0/10 |
| Tests in an E2B sandbox (`code-interpreter-v1`) | 7/7 in 2.0 s including clone |

### Data

`data/logisvert.json` is the single source of truth: each measure has a rate, a cap and the official source. `known_other_rates` lists rates seen on the page that the checker does not apply, each with the reason. `docs/logisvert.json` is the copy the page reads; a test keeps both identical.

### How it was built

Every step has a time in [research/log.md](research/log.md), from the empty repository at minute 1. The entry text itself stays out of this repository: its rights belong to We The Flywheel.

---

## Français

### En bref

**Pompon** montre, avant toute soumission, combien LogisVert verse pour chaque type de thermopompe à votre capacité, puis écrit le courriel qui demande aux installateurs l'appareil qui rapporte le plus. Pour 24 000 BTU/h : 1 200 $ en ENERGY STAR, 2 880 $ en ENERGY STAR Climat froid.

L'**atelier** (`workbench/`) sert à l'opérateur du guide : moteur de règles, relecteur de texte, et surveillant qui relit la page officielle chaque semaine et signale tout taux modifié.

### Démarrer

```bash
python -m unittest discover -s tests
python -m workbench.watch
```

Information, pas un conseil. Le montant exact est confirmé par Hydro-Québec à partir du numéro AHRI du modèle.

---

## Project files

[HUMAN.md](HUMAN.md) (for the person in charge) · [AGENTS.md](AGENTS.md) (for AI agents) · [CONTRIBUTING.md](CONTRIBUTING.md) · [SECURITY.md](SECURITY.md) · [CHANGELOG.md](CHANGELOG.md) · [CITATION.cff](CITATION.cff) · [NOTICE](NOTICE)

## License

Apache-2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).

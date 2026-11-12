# Evidence sheet: Pompon / thermopompe.guide

Every figure below comes from a public page read on 2026-11-12, inside the timed window, or from a file in this repository.

## Demand

| Fact | Source |
|---|---|
| A Quebec homeowner reading about LogisVert is "still a bit confused about how it works and what kind of rebate I could expect" | https://www.reddit.com/r/QuebecFinance/comments/1nixyd0/heat_pump_installationmural_system/ |
| Installers "rushing me to sign the contract" before a rumoured LogisVert end date | https://www.reddit.com/r/Quebec/comments/1mndbwg/la_subvention_logisvert_%C3%A7a_fini_tu_vraiment_le_25/ |
| Advice repeated to Canadians: check subsidies before buying a heat pump | https://www.reddit.com/r/heatpumps/comments/1umo4la/looking_to_swap_my_aging_ac_with_a_heat_pump/ |
| LogisVert funded 208,000 heat pumps, close to 80,000 in a single year (Hydro-Québec filing to the Régie de l'énergie) | https://www.regie-energie.qc.ca/storage/app/media/Suivis/Suivi%20D-2025-033/hqd-suivi-d-2025-033-programme-ee-gdp.pdf |
| 170,000 heat pumps installed last year through Hydro-Québec subsidies (Radio-Canada) | https://ici.radio-canada.ca/nouvelle/2255330/hydro-quebec-facture-electricite |
| Google autocomplete (fr-CA): "logisvert thermopompe admissible / liste / date limite / 2026", "subvention thermopompe fédéral", "subvention thermopompe hydro-québec liste 2026" | https://suggestqueries.google.com/complete/search?client=firefox&hl=fr&gl=ca&q=logisvert%20thermopompe |
| A buyer working out the LogisVert rebate on a Costco mini-split by hand | https://forums.redflagdeals.com/costco-danby-18-000-btu-quick-connect-mini-split-1399-300-off-1099-2730754/ |
| Free heat pumps for 20,000 modest-income households (Ottawa, Québec, Hydro-Québec) | https://www.lapresse.ca/affaires/economie/2026-06-29/quebec/des-thermopompes-gratuites-pour-20-000-menages-a-revenus-modestes.php |
| A LogisVert bonus worth up to 7,840 $ ended in August 2025 | https://www.protegez-vous.ca/nouvelles/habitation/fin-d-une-des-subventions-du-programme-logisvert |
| LogisVert requirements changed on 26 November 2025 | https://www.novairplus.com/post/changes-to-logisvert-program-heat-pumps-quebec-2025 |
| Installer guide: "Vous n'avez pas besoin de comprendre les calculs" | https://www.climatexpress.ca/subvention-gouvernementale-electricite.html |
| On 8 October 2026 the federal government announced heat pump subsidies from 2027; LogisVert stays in force | https://www.hydroquebec.com/residentiel/mieux-consommer/aides-financieres/logisvert/ |

## The gap

Hydro-Québec's own estimator works from a model or AHRI number: https://www.hydroquebec.com/residentiel/mieux-consommer/aides-financieres/logisvert/recherche-themopompes-efficaces.html . A homeowner has that number only once a quote names the unit, so the estimator answers after the choice. The rate depends on the certification written on the quote:

| Unit on the quote | LogisVert rate per 1,000 BTU/h at −8 °C | For 24,000 BTU/h |
|---|---|---|
| ENERGY STAR | 50 $ | 1,200 $ |
| ENERGY STAR Cold Climate | 120 $ | 2,880 $ |
| Cold climate, multi-unit bonus | 220 $ | 5,280 $ |
| Geothermal | 750 $ (cap 18,000 $) | 18,000 $ |

The 220 $ multi-unit bonus applies to buildings from 1995 or earlier in an eligible zone: https://www.kgconfort.com/subvention-maisons-vertes.php

Source: https://www.hydroquebec.com/residentiel/mieux-consommer/aides-financieres/logisvert/residentiel.html . Computed by `workbench/subsidy.py`, tested in `tests/test_workbench.py`.

## The product

- Pompon, live: https://securedme-main-dev.github.io/gap-workbench/
- Same rules in Python (`workbench/subsidy.py`) and in the page; tests in CI.
- Ends with an action: one click writes the email that asks 3 installers for a cold-climate unit with the model, AHRI number and capacity at −8 °C on the quote.

## Money

Contractors already pay for qualified leads. Google Local Services Ads: 57 $ per lead and a 43.9 % booking rate (SearchLight Digital benchmark, February 2026, 888 contractors): https://pipelineon.com/blog/best-lead-generation-platforms-plumbing-contractors-2026/ . Thumbtack: 15 $ to 75 $ per lead: https://fieldcamp.ai/hvac-software/lead-generation/ .

Funnel per 1,000 checker users (assumptions marked):

| Step | Value | Basis |
|---|---|---|
| Send a quote request | 10 % → 100 leads | assumption, measured in season 1 |
| Lead type | exclusive, one installer, with the reader's consent | product design |
| Price per lead | 50 $ | below Google's 57 $ for an exclusive lead |
| Revenue | 5,000 $ | 100 × 50 $ |
| Jobs booked | 44 | 43.9 % booking rate, SearchLight benchmark |
| Market | close to 80,000 heat pumps a year | Régie de l'énergie filing |
| Season-1 target | 1 buyer in 8: 10,000 users → 1,000 leads → 50,000 $, 439 booked jobs | target |
| At a 5 % send rate | 25,000 $ | sensitivity |

## Operator workbench

`workbench/lint.py` checks the entry before submission: word limits, negations, and every number against `data/` and this sheet. It caught one unsourced figure in this entry.

`workbench/watch.py` re-reads the official page and compares every rate with `data/logisvert.json`. On its first live run (2026-11-12) it found all 5 rates in use, plus a 140 $ rate for very-high-efficiency units with caulking work that Protégez-vous reported ended in August 2025; that rate is held for human review and left out of the checker.

Benchmarks (`benchmarks/run.py`, results in `data/benchmark.csv`): engine vs published rates 12/12 exact; page vs engine 1,005/1,005 identical; linter catches 10/10 negations with 0/10 false alarms. `research/log.md` records each step with its time. The 7 tests also run in an E2B microVM (template `code-interpreter-v1`, the fastest of 12 images in a startup benchmark): 7/7 pass in 2.0 s including the clone.

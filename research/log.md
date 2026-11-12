# Research log

Everything in this repository was made inside one 45-minute We The Flywheel *Find the Gap* window, which started at 07:31 UTC on 2026-11-12. Each line is written when the step happens.

| Time (UTC) | Step | Result |
|---|---|---|
| 07:31 | Window opened; empty repository created | GitHub noreply identity set before the first commit |
| 07:32 | Searched 3 angles (subsidy rules, Reddit demand, lead prices); chose Quebec heat pump subsidies | rules encoded in data/logisvert.json |
| 07:34 | Evidence sheet, README, CI; page published | docs/evidence.md |
| 07:35 | Ran the 7 tests in an E2B microVM (template code-interpreter-v1, chosen by an earlier startup benchmark) | 7/7 pass, 2.0 s including clone |
| 07:35 | Searched market size and rule changes | free heat pumps for 20,000 modest-income households (La Presse, 2026-06-29); rules changed 2025-11-26 |
| 07:37 | Drafted the entry fields locally (kept out of the repo); linter caught 1 number missing from the evidence sheet, fixed | 0 issues |
| 07:39 | Live check: page loaded but docs/logisvert.json was missing (404); copied it and added 2 tests (same rules, fetched file exists) | 9 tests |
| 07:43 | Hostile review of the draft: money switched to exclusive leads at 50 $ per lead with unit economics per 1,000 users; gap sentence tied to certification | linter 0 issues, 9 tests |
| 07:47 | Redrew Pompon and logo; added rule watcher (first live run found a 140 $ rate held for review) and benchmarks (12/12, 1,005/1,005, linter 10/10 with 0/10 false alarms) | 11 tests |
| 07:52 | Documentation: bilingual README with badges, HUMAN.md, AGENTS.md, SECURITY.md, CONTRIBUTING.md, CITATION.cff, NOTICE, CHANGELOG; weekly rule watcher in Actions; benchmarks in CI | 11 tests |
| 07:52 | Wide banner infographic at the top of the README | docs/banner.svg |
| 07:53 | Code of conduct, issue and PR templates, .claude/settings.json, private vulnerability reporting, topics | |
| 07:54 | WTF hackathon banner linked from wetheflywheel.com at the top of the README | |
| 07:55 | Banner redrawn in the WTF palette (#7C3AED, #EDE9FE, #1F1D2B, square corners, Dosis titles) | |
| 07:57 | Mapped the workbench to the five Flywheel businesses in the README; added docs/llms.txt | |

# gap-workbench

Built inside one 45-minute We The Flywheel *Find the Gap* window (concept submitted to WTF; WTF does not endorse this repository).

- **Pompon** (client tool): https://securedme-main-dev.github.io/gap-workbench/ . Shows the LogisVert subsidy for each heat pump type before you sign a quote, then writes the email that asks installers for the right unit.
- **Workbench** (operator tool): `workbench/subsidy.py` (rules engine), `workbench/lint.py` (entry linter), `workbench/watch.py` (re-reads the official page and flags any changed rate), `benchmarks/run.py`.
- Evidence: `docs/evidence.md`. Step log with times: `research/log.md`.

```bash
python -m unittest discover -s tests
python -m workbench.lint entry/fields.md   # the entry text stays local (rights assigned to WTF); entry/ is git-ignored
```

Information, not advice. Licence: Apache-2.0.

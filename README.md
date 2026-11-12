# gap-workbench

Built inside one 45-minute We The Flywheel *Find the Gap* window (concept submitted to WTF; WTF does not endorse this repository).

- **Pompon** (client tool): https://securedme-main-dev.github.io/gap-workbench/ . Shows the LogisVert subsidy for each heat pump type before you sign a quote, then writes the email that asks installers for the right unit.
- **Workbench** (operator tool): `workbench/subsidy.py` (rules engine), `workbench/lint.py` (entry linter: word limits, negations, numbers checked against the data).
- Evidence: `docs/evidence.md`. Step log with times: `research/log.md`.

```bash
python -m unittest discover -s tests
python -m workbench.lint entry/fields.md
```

Information, not advice. Licence: Apache-2.0.

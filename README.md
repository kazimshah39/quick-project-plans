# quick-project-plans

**Short plans. Actionable tasks. Fast implementation with enough checking.**

A portable AI skill that produces `plan.md` and `tasks.md`. Small changes stay
small; long projects get as many tasks and milestones as needed. No mandatory
review agents, test-writing phase or test run after every task.

## Use

> Use quick-project-plans to plan task-name filtering. Plan only.

The agent reads relevant code, writes both files and stops. To execute afterward:

> Approved. Implement this plan autonomously.

Or request both steps together:

> Use quick-project-plans to plan and implement task-name filtering.

Existing authorization is recorded once; no second approval prompt is needed.
Routine technical choices are made autonomously. Genuine external blockers are
reported while independent work continues.

## What stays lightweight

- Inspect only relevant code; no exploratory test runs without a concrete need.
- Brief approach, actionable outcomes, no fixed task-count limit.
- One review while writing, no separate audit or review report.
- Shared checks at useful milestones, not one test run per task.
- Existing tests first; new tests only when requested, required or clearly useful.
- No unrelated refactors, infrastructure, coverage work or optional polish.
- Necessary high-risk safeguards and mandatory project checks still apply.

## Outputs

```text
~/.agent/plans/<project-path-slug>--<first-10-sha256>/
└── <YYYY-MM-DD-HHmmss>-<outcome-slug>/
    ├── plan.md
    └── tasks.md
```

An explicit external location or `AGENT_PLANS_ROOT` overrides the default root.
Packages stay outside the project and never overwrite existing plans. See
[SKILL.md](SKILL.md) and the [output template](references/output-template.md).

## Install

Place `SKILL.md` and `references/` together in a new `quick-project-plans/`
folder at your agent's skill location, such as `~/.agents/skills/`. Reload the
agent's skill list if needed. Do not overwrite another installation accidentally.
This skill does not install itself or publish anything.

## Validate skill changes

No third-party dependencies:

```sh
python3 -m unittest discover -s tests -p 'test_*.py'
```

These checks cover document structure and core guidance, not actual agent speed
or obedience. [Evaluation scenarios](tests/scenarios.md) are optional review cases,
not recorded model results. They are not steps to run on every project.

## License

[MIT](LICENSE).

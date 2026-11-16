# quick-project-plans

**Short plans. Actionable checklists. Autonomous execution after approval.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Dependencies: none](https://img.shields.io/badge/dependencies-none-brightgreen.svg)](#lightweight-validation)

A lightweight AI skill for short plans, useful task checklists and autonomous
implementation **after approval**. It always produces `plan.md` and `tasks.md`.
No mandatory planning agents, comprehensive specifications or repeated review loops.

## Use

Load [SKILL.md](SKILL.md) in a skill-compatible coding agent, or explicitly ask the
agent to read it and follow it. Example planning-only request:

> Use quick-project-plans to plan task-name filtering in the existing task list.

The agent inspects relevant code, picks the simplest complete approach, creates
both planning files and reports their paths. It does not implement a planning-only
request. To approve the resulting package:

> Approved. Implement this plan and complete its tasks.md autonomously.

If more than one package is relevant, include the package or checklist path. Or
request both steps at once:

> Use quick-project-plans to plan and implement task-name filtering.

The checklist records approval and includes the execution contract: work without
routine check-ins, verify critical flows, update completed tasks with brief notes,
continue independent work around genuine blockers, and report exact external needs.
Approval is not unlimited authority for production changes, purchases or publishing.

## What makes it quick

- Small relevant-code inspection and early prerequisite checks.
- Meaningful working slices using existing architecture, rather than one task per file.
- One self-check; independent review only when requested or required by project rules.
- Bounded investigation, no endless blocker retries, and takeover of stuck workers.
- Focused tests, reuse of valid evidence, no unrelated full-suite runs or new test
  frameworks by default. Necessary higher-risk and mandatory project checks remain.

Ordinary plans target about 20–60 lines and often 2–6 tasks; these are not hard
caps or completion-time promises. Large requests retain their full scope and get
honest milestones. A Markdown skill guides an agent; it does not enforce spending,
time limits or model obedience at runtime.

## Planning output layout

```text
~/.agent/plans/
└── <canonical-project-path-slug>--<first-10-sha256>/
    └── <YYYY-MM-DD-HHmmss>-<outcome-slug>/
        ├── plan.md
        └── tasks.md
```

An explicit external plans root or `AGENT_PLANS_ROOT` overrides the default.
Names and paths are resolved at runtime; collisions get a numeric suffix.
Planning files stay outside the target repository, are written using absolute
paths, and are checked together before completion. The slug/hash, local timestamp,
collision suffixes and root precedence follow the former skill's
[upstream path convention](https://github.com/kazimshah39/writing-project-plans/blob/main/references/path-layout.md).
POSIX, Windows drive and UNC project paths are canonicalized on the relevant host;
`datas.md` is treated as a typo for `tasks.md` unless explicitly requested otherwise.
See the compact formats in [references/output-template.md](references/output-template.md).

The **generated plan layout** is preserved; the **skill's internal layout** is
intentionally simpler. One `references/output-template.md` replaces the old set
of comprehensive templates and reviewer references. No mandatory review loops
are restored.

## Install

Clone the public repository:

```sh
git clone https://github.com/kazimshah39/quick-project-plans.git
cd quick-project-plans
```

For an agent that supports `~/.agents/skills`, install without overwriting an
existing skill directory:

```sh
python3 - <<'PY'
from pathlib import Path
import shutil

source = Path.cwd()
target = Path.home() / '.agents' / 'skills' / 'quick-project-plans'
if not (source / 'SKILL.md').is_file() or not (source / 'references').is_dir():
    raise SystemExit('Run this from the cloned quick-project-plans directory.')
try:
    target.mkdir(parents=True, exist_ok=False)
except FileExistsError:
    raise SystemExit(f'Refusing to overwrite existing directory: {target}')
shutil.copy2(source / 'SKILL.md', target / 'SKILL.md')
shutil.copytree(source / 'references', target / 'references')
print(f'Installed to {target}')
PY
```

Use the documented location for your agent if it differs, then reload its skill
list or start a new session. There is no installer hook or remote script to execute.
The installation commands are optional; cloning alone does not activate the skill.

## Project layout and manual installation

```text
quick-project-plans/
├── SKILL.md
├── README.md
├── references/output-template.md
└── tests/
    ├── test_skill.py
    └── scenarios.md
```

The repository also contains `LICENSE` and `.gitignore` for distribution.

For manual installation, copy `SKILL.md` and `references/` together into a new
`quick-project-plans` directory at your coding agent's documented skill location.
Consult that agent's loading/reload instructions. Do not overwrite an existing
skill directory. This project does not install itself or publish anything.

This skill was built after the former comprehensive `writing-project-plans` skill
was removed locally. Its [upstream repository](https://github.com/kazimshah39/writing-project-plans)
is an optional historical reference, not a dependency. Do not restore it as part
of this project. If another planning skill is independently installed, explicitly invoking
this skill avoids ambiguity; exclusive automatic routing is not guaranteed.

## Lightweight validation

Requires Python 3.9+; no third-party packages or application services:

```sh
python3 -m unittest discover -s tests -p 'test_*.py'
```

The tests inspect metadata, links, output structure and essential policy text.
They do **not** prove model behavior, actual path creation, speed or screen-level
application behavior. The three [evaluation scenarios](tests/scenarios.md) provide
bounded behavioral prompts and review criteria. Reading those scenarios is not the
same as executing them with a model. No paid evaluation service is required.

## Contributing

Keep changes small and portable. Preserve the two-file output contract, approval
boundary, autonomous execution rules and proportional verification. Run the
lightweight validation command above, and describe the behavior and verification
limits in your pull request. Do not add mandatory infrastructure or review loops.
Never include private plans, credentials or application data in issues or patches.

## License

[MIT](LICENSE) © 2026 Kazim (kazimshah39).

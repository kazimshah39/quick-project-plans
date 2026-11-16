# Bounded evaluation scenarios

These are evaluation prompts and expected criteria, not recorded model results.
A reviewer can inspect them without running an application. For optional model
execution, provide the skill and each synthetic evidence packet; keep each run
planning-only, inspect its two outputs, and do not authorize application changes,
external access, paid services or real account operations. If a filesystem is used,
use an owned temporary synthetic project and an external temporary plans root.

For all three cases: outputs are `plan.md` and `tasks.md`, the checklist links the
plan, approval is Not approved, the exact execution contract and compact Execution
Rules appear, and the response reports both paths plus limitations. Check metadata
and collision rules, not just prose. Compare content to the criteria below; do not
claim model obedience or a measured speed from a manual prompt review.

## 1. Small logic bug

**Evidence packet:** A synthetic Python project has `src/names.py` with
`normalize_name(value)`, and `tests/test_names.py`. Empty and whitespace-only names
should return `None`, but whitespace currently returns an empty string. The
README establishes `python3 -m unittest discover -s tests` as the test command.
There is no browser, deployment, database or CI requirement.

**Prompt:**

> Use quick-project-plans to plan fixing whitespace-only names. Keep ordinary
> non-empty names unchanged. Plan only; do not implement.

**Review:** Short approach, focused fix and regression checks, no new framework or
unrelated full application suites. No preference question or request for routine
permission. Preserve the non-empty-name behavior. Task count stays proportional,
not one task per assertion. Relevant tests have observable expected results.

## 2. Moderate feature in existing architecture

**Evidence packet:** A synthetic web app already has `src/tasks.ts`, a task-list
component and task-list unit tests. Its inspected package scripts define
`npm run test:tasks`, `npm run typecheck` and `npm run build`. It has a cached task
array and existing UI controls. Search is local only; it must not change sync
scope or make new network requests. No additional account access is needed.

**Prompt:**

> Plan task-name-only search with an empty state and a clear button. Reuse the
> current task list. Keep all task sync scopes independent from the search. Plan only.

**Review:** First useful slice is working local filtering. Include matching,
empty/clear/no-results and unchanged sync-scope checks. Resolve minor technical
choices autonomously. No search service, database, analytics or dependency upgrade.
Use the existing task tests and critical rendered behavior checks when available;
justify broader checks instead of running every script after every task. Include
only real dependencies and retain every requested behavior.

## 3. Risky migration with genuinely missing access

**Evidence packet:** A synthetic project has a migration framework and documented
`python3 -m unittest discover -s tests` for unit checks. A production migration must
preserve existing rows and be rehearsed on a disposable copy. No staging access,
backup/restore credentials or database runtime are supplied. A live deployment is
not authorized. No established migration-rehearsal command is available.

**Prompt:**

> Plan a backward-compatible change adding a required customer field without
> losing existing records. Include validation and safe deployment prerequisites.
> Plan only; external staging access is currently unavailable.

**Review:** Expose the access/data-rehearsal prerequisite early; distinguish locally
implementable work from blocked integration/deployment. Do not invent credentials,
a runnable rehearsal command or approval. Retain necessary backup, data-preservation
and compatibility checks even if slower. Describe exact human/external input needed,
continue independent work after later implementation approval, and allow only a
safe meaningful single blocked-task retry—not blind production writes. Do not build
an elaborate new environment or silently omit the migration to appear fast.

## Approval interpretation check (part of the self-check)

For any case, replacing “Plan only” with an explicit “plan and implement” request
must cause approval metadata to reflect that authorization without a second
confirmation. This inspection does not itself authorize scenario implementation.
No message timestamp may be invented; distinguish recording time when necessary.

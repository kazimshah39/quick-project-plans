---
name: quick-project-plans
description: >-
  Create a quick plan.md and actionable tasks.md for small changes or long
  projects. Use for quick planning, implementation checklists, or explicit
  quick-project-plans requests. Keep process and testing proportional; implement
  immediately when requested, but do not implement planning-only requests.
license: MIT
metadata:
  version: "1.1.0"
---

# Quick Project Plans

Find the shortest practical route to the complete requested outcome. Spend effort
on implementation, not planning paperwork. Follow applicable project instructions.

## Workflow

1. **Inspect narrowly.** Read the relevant code and instructions. Reuse existing
   architecture. Investigate only what is needed to choose a sound approach;
   check prerequisites early only when they affect that approach. Do not scan
   the whole repository or run tests during planning unless needed to resolve
   a specific uncertainty.
2. **Write a short plan and actionable checklist.** Use the
   [template](references/output-template.md). Keep the approach brief. Use as many
   tasks as needed, with no fixed limit. Group long projects into milestones.
   Each task states what to change, where when known, and what counts as done.
   Split by working outcomes, not individual files. List dependencies only when
   useful. Detail known work now; investigate uncertain parts when reached unless
   the uncertainty blocks the overall approach.
3. **Review once, then proceed.** Check scope and obvious omissions while writing.
   No separate audit, review report or default delegation. Report both file paths.
   Stop for a planning-only request. If implementation is requested, record that
   authorization and start without asking again.

## Output files

Create only `plan.md` and `tasks.md` in a new external package:

```text
<plans-root>/<project-path-slug>--<path-hash>/<YYYY-MM-DD-HHmmss>-<outcome-slug>/
```

- Project: explicit user path, otherwise Git root, workspace root or current
  directory. Expand and resolve the absolute path, including existing symlinks.
  Do not create an uncreated project just to plan.
- Plans root: explicit external location, `AGENT_PLANS_ROOT` or `~/.agent/plans`.
- Project slug: canonical project path with separators/unsupported filename
  characters replaced by hyphens; collapse and trim hyphens, or use `project`.
  Hash: first 10 lowercase hex characters of SHA-256 of the canonical UTF-8 path.
- Use local time and a short kebab-case outcome slug. Create the package
  exclusively; append `-2`, `-3`, etc. on collision. Never overwrite old plans.
- Keep resolved destinations under the plans root and outside the project.
  Write using absolute paths, confirm both files exist, and report their paths.
  Do not include secrets or create extra logs or planning documents.

## Implementation

- Record approval once in `tasks.md`: Not approved for planning only, or Approved
  with the requested scope. An explicit “plan and implement” request is enough.
  Authorization applies to that scope, not unrelated publishing or operations.
- Work autonomously: make routine choices, implement, diagnose and fix. Do not add
  speculative features, unrelated refactors, new infrastructure or optional polish.
- Reassess repeated failures instead of looping. Ask only for a genuine missing
  external input, human-only step, material conflict or action outside authority.
  Continue independent tasks; retry blocked work only when conditions change and
  it is safe. Do not blindly repeat uncertain external writes.
- Mark tasks complete when their stated outcomes are met. Related tasks may share
  checks; do not require a test run or evidence note for every checkbox. Finish
  when the requested outcome is implemented and the selected checks pass. If
  blocked, leave unfinished work unchecked and report the exact remaining need.

## Minimal sufficient verification

- Prefer existing checks. Write new tests only when requested, required by project
  rules, or clearly useful for changed logic, a recurring bug or a high-risk action.
  Do not add tests merely for coverage or create a new harness by default.
- Check at meaningful milestones, not after every edit or task. Choose the cheapest
  check that can meaningfully catch mistakes in the change. A text-only edit may
  need only diff inspection; logic may need a targeted test; UI may need a focused
  interaction check. Do not require browser/device testing for every UI change.
- No full suites, repeated builds, broad browser walkthroughs or benchmarks without
  a concrete reason. Reuse passing results while they remain relevant; rerun only
  checks affected by later changes or fixes. Use real commands, not invented ones.
- Keep mandatory user/project checks and necessary safeguards for authentication,
  payments, migrations or destructive actions. Report failed or important unrun
  checks briefly; never claim unverified behavior works.

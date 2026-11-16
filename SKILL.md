---
name: quick-project-plans
description: >-
  Create short, implementation-ready plan.md and tasks.md files with minimal
  planning overhead. Use when the user asks for a quick or lightweight project
  plan, an actionable task checklist, or explicitly invokes quick-project-plans.
  Always include tasks.md, approval status, autonomous execution rules and focused
  verification. Planning alone does not authorize implementation.
license: MIT
metadata:
  version: "1.0.0"
---

# Quick Project Plans

Plan the shortest practical route to the user's complete requested outcome.
Prefer useful working increments over long documents. Do not turn this workflow
into a comprehensive specification or promise that every project takes minutes.

## Workflow

1. **Inspect only relevant evidence.** Read applicable project instructions, likely
   entry points, related tests and real verification commands. Reuse existing
   architecture and tools. Check the riskiest prerequisite early: access, runtime,
   device, fixture or external service. Do not scan the whole repository by default.
2. **Choose the simplest complete approach.** Preserve requested behavior and
   important constraints. Resolve routine choices yourself; note material
   assumptions briefly. Do not add speculative features, refactors or infrastructure.
3. **Write both files.** Follow [the output template](references/output-template.md).
   Always create `plan.md` and `tasks.md` for a completed planning request. Start
   with a useful end-to-end slice; separate implementation, integration acceptance
   and external release gates. Use only actual dependencies, not an automatic chain.
4. **Self-check once.** Confirm scope, actionable tasks, genuine prerequisites,
   evidenced checks, approval and output paths. Correct concrete defects; do not
   start repeated audits or mandatory reviewer/subagent workflows. Follow explicit
   user or project review requirements when applicable.
5. **Report and honor approval.** Give both absolute file paths, important blockers
   and approval status. Stop for a planning-only request. If implementation was
   explicitly requested, execute the checklist under its contract without asking again.

Aim for a few minutes of planning for ordinary work, roughly 20–60 lines in
`plan.md` and often 2–6 meaningful tasks. These are targets, not limits that permit
omitting requirements. Larger work needs honest milestones, not hidden scope cuts.
Timebox uncertain investigation; after two failed attempts, reassess with new
evidence. Do not research the same blocker indefinitely or create extra reports.

## Output paths

Keep planning outputs outside the target project, using the existing convention:

```text
<plans-root>/<project-path-slug>--<path-hash>/
└── <YYYY-MM-DD-HHmmss>-<outcome-slug>/
    ├── plan.md
    └── tasks.md
```

- Resolve the project from the user's explicit path, otherwise the Git root,
  otherwise the supplied workspace root, otherwise the current directory.
  Canonicalize absolute paths: expand `~`, resolve relative segments and symlinks,
  and normalize native separators, including Windows drive and UNC paths where
  applicable. Reject unresolved `..` components. Separate checkouts at separate
  canonical paths intentionally receive separate planning roots.
  For an uncreated project, resolve its nearest existing ancestor
  and append the missing path components; do not create the project just to plan.
- Resolve the plans root from an explicit external location, `AGENT_PLANS_ROOT`,
  or `~/.agent/plans`. Expand it at runtime; never hard-code a home or project path.
- Replace separators and unsupported filename characters with `-`, collapse
  repeated hyphens and trim them to derive the project slug. Preserve readable
  letter case. Append `--` plus the first 10 lowercase hex characters of the
  SHA-256 of the full canonical project path encoded as UTF-8. Use `project` if
  the readable slug is empty; the hash still identifies the path.
- Derive a lowercase kebab-case outcome slug from the request. Use current local
  time with seconds and record its timezone in metadata. On collision, atomically
  create a new package with suffix `-2`, `-3`, etc.; never adopt/overwrite a package.
- Before writing, verify resolved destinations stay under the plans root and
  outside the project. Reject an inside-project root or unsafe symlink destination;
  choose a valid external destination under the rules above, or report the blocker.
  Do not move or delete unrelated historical plans. Keep the plans root private.
- Create exactly `<package>/plan.md` and `<package>/tasks.md`, using their full
  absolute paths in file-writing tools. Treat `datas.md` as a typo for `tasks.md`
  unless the user explicitly requires a separate filename. No separate review logs.
  Exclude secrets and sensitive data from paths and content; use project-relative
  code paths inside the plan and absolute paths only for package/project identity.
- Before reporting, verify both files exist together at their resolved paths and
  check that this operation created no planning files in the project (including
  its root and `docs/`). Correct only files proven misplaced by this operation;
  never move or delete pre-existing plans. Report the package and both file paths.

## Approval

Include **Implementation approval: Not approved** for planning-only requests.
“Approved, implement this plan” or “plan and implement” is sufficient authorization;
record its scope, reference and date/time with timezone when known. If the message
has no reliable timestamp, label the current recording time as such, not as the
message's exact time. Never invent approval or ask the user to repeat it.

Approval covers the requested implementation, not unrelated purchases, publishing,
production changes or destructive actions. This skill does not install itself or
publish a repository. Prefer explicit invocation if another planning skill overlaps.

## Autopilot after approval

Include the execution contract from the template verbatim in every `tasks.md`,
plus its compact Execution Rules. Resolve routine technical choices, set up
authorized tools/isolated fixtures, implement, debug and fix autonomously. Do not
ask preference questions or “should I continue?” for routine work.

Ask only for an evidenced human-only step, unavailable external access, action
outside authority, or a material conflicting requirement. First inspect authorized
sources and try reasonable alternatives. State the exact blocker, attempts and
smallest user action needed; continue independent tasks. Retry a blocked task once
when a corrective step or changed condition makes it meaningful. Never blindly
repeat an uncertain external write without established idempotency/reconciliation.

Do not delegate by default; use permitted delegation only when it clearly helps.
Inspect and take over stalled workers when appropriate. Reassess after two failed
attempts, avoid endless review loops and optional polish while the critical path
is blocked. If all independent work is verified and an external blocker remains,
report partial completion and stop instead of spinning or claiming full success.
Mark tasks `[x]` only after their own verification passes, with a brief evidence
note. Overall completion still requires the approved acceptance criteria.

## Focused verification

- Select the smallest useful checks for changed behavior and critical integration
  points. Reuse existing tests; add a focused regression for bugs when practical.
  Do not create elaborate harnesses for a small change without a concrete need.
- Use accuracy/link checks for documentation, focused rendered checks for relevant
  UI behavior, targeted tests for logic, and request plus saved-result checks for
  API writes. Do not run unrelated application suites for documentation changes.
- Run broader checks only at appropriate milestones, or when shared code,
  dependencies, project instructions or risk justify them—not after every task.
  Keep necessary authentication, financial, destructive-operation, migration and
  recovery checks even if slower. A unit test cannot replace required real proof.
- Reuse passing evidence only while relevant code, configuration, environment and
  tested artifact remain unchanged. Diagnose failures before rerunning. Disclose
  unresolved intermittent results and important checks not run.
- Use commands supported by repository evidence or exact observable procedures.
  A new test command can be a task deliverable, not a claim that it already exists.
  State expected results and why any expensive check is needed. Honor mandatory
  user/project checks; surface a speed conflict rather than silently skipping them.

Do not add cost metering, CI, release infrastructure or broad fault matrices unless
requested or necessary for the actual change. Fast means avoiding unnecessary work,
not hiding risk, missing requirements or verification limits.

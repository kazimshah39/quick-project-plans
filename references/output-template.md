# Compact output template

Replace placeholders with inspected evidence. Omit irrelevant plan headings rather
than filling them with boilerplate. Keep every material requirement. Do not put
application changes or secret values in a planning package.

## plan.md

```markdown
# <Outcome>

- Project: <canonical absolute project path>
- Original project path: <user-supplied path, or Same as canonical>
- Plans root: <resolved absolute global plans root>
- Project planning root: <absolute slug--hash directory>
- Package: <absolute planning package path>
- Created: <ISO-8601 timestamp with timezone>
- Status: Planned | Implementation approved | In progress | Blocked | Complete

## Outcome and evidence
<Requested behavior and important constraints; relevant existing code/tests.>

## Approach
<Simplest complete solution using existing tools. First working slice and any
later milestones; real prerequisites and meaningful assumptions.>

## Constraints and blockers
<Concrete risks requiring protection, unavailable access, or None. Say what
unblocks each blocker; do not invent a solution or expand scope.>

## Verification
<Targeted evidenced commands/procedures and expected results. Critical integration
checks; broader/slower checks only with a reason. Important unavailable checks.>
```

## tasks.md

Always link the source plan. Copy the Execution Contract paragraph exactly;
keep the Execution Rules, adapting only project-specific constraints. Use as few
coherent tasks as needed, not one task per file. Each task includes its own checks;
the final task/check confirms the complete approved outcome without needless reruns.

```markdown
# Tasks: <Outcome>

- Source plan: [plan.md](./plan.md)
- Project: <canonical absolute project path>
- Package: <absolute planning package path>
- Status: Not started | In progress | Blocked | Complete
- Implementation approval: Not approved
- Approval recorded at: Not applicable
- Authorization reference/scope: Planning only

## Execution Contract — After Approval

Complete all tasks in `tasks.md` and the approved plan as quickly as possible. Avoid unnecessary work and repeated tests. Implement, fix, verify critical flows, and mark completed tasks `[x]` with brief notes. Work autonomously without stopping or asking questions unless genuinely blocked by external dependencies, access, or required decisions. Record blockers, continue other tasks, and retry blocked tasks once. Stop only when all possible work is verified. Finally, summarize completed tasks, verification results, remaining blockers, and exactly what you need from me.

## Execution Rules

- Start implementation only after explicit authorization, including authorization
  in the original request. Record approval once with its scope and timestamp when
  known; otherwise label the recording time. Do not ask for approval again.
- Work autonomously within scope: resolve routine choices, set up authorized tools,
  implement, diagnose and fix. Ask only for an evidenced human-only step, missing
  external access, action outside authority or material conflicting requirement.
- Continue independent work; report exact blockers, attempts and smallest needed
  user action. Retry blocked work once only when safe and meaningful. Never blindly
  replay uncertain writes; honor established idempotency/reconciliation rules.
- Use existing tools, focused tests and critical integration checks. Avoid unrelated
  suites, duplicate successful runs and unnecessary harnesses. Reuse evidence only
  while relevant code, config, environment and artifact remain unchanged. Retain
  required risk-based/user/project checks and disclose important checks not run.
- Timebox uncertain investigations; reassess after two failed attempts and take over
  stalled workers when appropriate. No default delegation, endless audits or optional
  polish while the critical path is blocked. A timebox is not a speed guarantee.
- Mark a task complete only after its checks pass, with a brief evidence note. Keep
  blocked tasks unchecked. If independent work is exhausted, summarize partial
  completion and external needs instead of looping or claiming complete acceptance.

## Tasks

- [ ] **T01 — <Specific working outcome>**
  - **Files:** <project-relative files or precise areas>
  - **Do:** <concrete behavior and necessary failure handling>
  - **Verify:** <evidenced command or exact procedure> — <expected result>
  - **Depends on:** None

- [ ] **T02 — <Integrate and verify the approved outcome>**
  - **Files:** <relevant areas>
  - **Do:** <finish the milestone, confirm requirements and documentation>
  - **Verify:** <remaining applicable checks; reuse still-valid evidence> — <result>
  - **Depends on:** T01

## Blockers

None, or <task ID, blocker, evidence/attempts, safe retry status, exact next action>.
```

For approved implementation, replace the approval defaults with the actual
authorization and scope; never manufacture a message timestamp. Keep implemented,
integration-verified and externally blocked release work distinguishable. Do not
silently waive required acceptance criteria to mark the overall plan complete.

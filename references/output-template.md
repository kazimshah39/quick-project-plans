# Output template

Keep both files short and specific. Omit irrelevant headings and empty fields.
No task-count limit; repeat tasks and add milestones as the project needs.

## plan.md

```markdown
# <Outcome>

Project: <absolute project path>

## Goal
<Requested behavior and important constraints.>

## Approach
<Shortest complete solution using existing code; relevant files and material
assumptions. Mention blockers only when present.>

## Checks
<Smallest sufficient checks and expected results. Related tasks share checks;
name milestone checks for larger projects. Use known commands or exact procedures.>
```

## tasks.md

```markdown
# Tasks: <Outcome>

Plan: [plan.md](./plan.md)
Implementation approval: <Not approved — planning only | Approved — requested scope>

## Execution
- After authorization, implement within scope without routine check-ins.
- Reuse existing tools; avoid unrelated changes and unnecessary tests.
- Use the plan's shared checks; mark tasks done when their outcomes are met.
- Finish when the requested outcome and selected checks are complete, or report
  genuine blockers after independent work is exhausted.

## Tasks

- [ ] <Action and working outcome>
  - Where: <relevant files or area, when known>
  - Done when: <observable result, not a mandatory separate test run>

## Results
<Fill at completion: brief check results and any remaining blockers or limits.>
```

Use approval from the actual request; do not ask for it again or invent it.
Add task dependencies, milestone headings or task-specific checks only when useful.
Do not add a separate testing, documentation or release task unless the work needs it.

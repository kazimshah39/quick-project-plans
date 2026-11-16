"""Lightweight text/structure checks, not a model-obedience benchmark."""

from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / "SKILL.md").read_text(encoding="utf-8")
TEMPLATE = (ROOT / "references/output-template.md").read_text(encoding="utf-8")
README = (ROOT / "README.md").read_text(encoding="utf-8")
SCENARIOS = (ROOT / "tests/scenarios.md").read_text(encoding="utf-8")
CONTRACT = (
    "Complete all tasks in `tasks.md` and the approved plan as quickly as possible. "
    "Avoid unnecessary work and repeated tests. Implement, fix, verify critical flows, "
    "and mark completed tasks `[x]` with brief notes. Work autonomously without "
    "stopping or asking questions unless genuinely blocked by external dependencies, "
    "access, or required decisions. Record blockers, continue other tasks, and retry "
    "blocked tasks once. Stop only when all possible work is verified. Finally, "
    "summarize completed tasks, verification results, remaining blockers, and exactly "
    "what you need from me."
)


class SkillStructureTests(unittest.TestCase):
    def test_frontmatter_and_name(self):
        match = re.match(r"\A---\n(.*?)\n---\n", SKILL, re.S)
        self.assertIsNotNone(match)
        metadata = match.group(1)
        self.assertIn("name: quick-project-plans", metadata)
        self.assertIn("description: >-", metadata)
        self.assertIn("tasks.md", metadata)

    def test_bundled_markdown_links_resolve(self):
        for path in ROOT.rglob("*.md"):
            # Fenced examples describe generated files, not repository links.
            prose = re.sub(r"^```[^\n]*\n.*?^```\s*$", "", path.read_text(),
                           flags=re.M | re.S)
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", prose):
                if "://" in target or target.startswith("#"):
                    continue
                resolved = (path.parent / target.split("#")[0]).resolve()
                self.assertTrue(resolved.is_relative_to(ROOT))
                self.assertTrue(resolved.is_file(), f"{path}: missing {target}")

    def test_both_outputs_and_task_fields(self):
        for name in ("plan.md", "tasks.md"):
            self.assertIn(f"## {name}", TEMPLATE)
            self.assertIn(name, SKILL)
        self.assertIn("[plan.md](./plan.md)", TEMPLATE)
        tasks = re.split(r"^- \[ \] \*\*T\d+", TEMPLATE, flags=re.M)[1:]
        self.assertEqual(len(tasks), 2)
        for task in tasks:
            for field in ("**Files:**", "**Do:**", "**Verify:**", "**Depends on:**"):
                self.assertIn(field, task)

    def test_exact_execution_contract(self):
        self.assertEqual(TEMPLATE.count(CONTRACT), 1)

    def test_approval_not_implicit(self):
        self.assertIn("Implementation approval: Not approved", TEMPLATE)
        self.assertIn("Approval recorded at: Not applicable", TEMPLATE)
        self.assertIn("Authorization reference/scope: Planning only", TEMPLATE)
        self.assertIn("Stop for a planning-only request", SKILL)
        self.assertIn("Never invent approval", SKILL)
        self.assertIn("not as the\nmessage's exact time", SKILL)

    def test_autopilot_and_bounded_blockers(self):
        rules = TEMPLATE.split("## Execution Rules", 1)[1].split("## Tasks", 1)[0]
        for phrase in (
            "Work autonomously within scope",
            "human-only step",
            "Continue independent work",
            "Retry blocked work once",
            "idempotency/reconciliation",
            "reassess after two failed attempts",
            "stalled workers",
            "Keep\n  blocked tasks unchecked",
        ):
            self.assertIn(phrase, rules)
        self.assertIn("instead of looping", rules)

    def test_testing_is_focused_but_preserves_required_checks(self):
        for phrase in (
            "focused tests",
            "unrelated\n  suites",
            "duplicate successful runs",
            "required risk-based/user/project checks",
            "disclose important checks not run",
        ):
            self.assertIn(phrase, TEMPLATE)
        for phrase in (
            "Authentication",
            "financial",
            "migration",
            "tested artifact remain unchanged",
            "not after every task",
        ):
            self.assertIn(phrase.lower(), SKILL.lower())

    def test_no_mandatory_overhead(self):
        self.assertIn("Self-check once", SKILL)
        self.assertIn("Do not delegate by default", SKILL)
        self.assertIn("mandatory reviewer/subagent workflows", SKILL)
        self.assertIn("Do not add speculative features", SKILL)
        self.assertIn("not limits that permit\nomitting requirements", SKILL)

    def test_portable_external_path_convention(self):
        for text in (SKILL, TEMPLATE):
            self.assertNotRegex(text, r"(?:/home/|/Users/|[A-Za-z]:\\Users\\)")
        for phrase in (
            "AGENT_PLANS_ROOT",
            "~/.agent/plans",
            "first 10 lowercase hex",
            "SHA-256",
            "YYYY-MM-DD-HHmmss",
            "atomically",
            "symlink",
            "outside the project",
            "Do not move or delete unrelated",
        ):
            self.assertIn(phrase, SKILL)

    def test_legacy_layout_details_remain_explicit(self):
        for phrase in (
            "full\n  absolute paths in file-writing tools",
            "datas.md",
            "Windows drive and UNC paths",
            "Reject unresolved `..`",
            "supplied workspace root",
            "Separate checkouts",
            "verify both files exist together",
            "never move or delete pre-existing plans",
        ):
            self.assertIn(phrase, SKILL)
        for field in (
            "Original project path:", "Plans root:", "Project planning root:"
        ):
            self.assertIn(field, TEMPLATE)

    def test_docs_and_scenarios_are_honest(self):
        self.assertIn("does not install itself", README)
        self.assertIn("removed locally", README)
        self.assertIn("not a dependency", README)
        self.assertIn("do **not** prove model behavior", README)
        self.assertEqual(len(re.findall(r"^## [123]\. ", SCENARIOS, re.M)), 3)
        for phrase in (
            "No preference question",
            "Resolve minor technical",
            "Retain necessary backup",
            "No message timestamp may be invented",
            "not recorded model results",
        ):
            self.assertIn(phrase, SCENARIOS)


if __name__ == "__main__":
    unittest.main()

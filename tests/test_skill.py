"""Small document checks; not a benchmark of agent behavior or speed."""

from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / "SKILL.md").read_text(encoding="utf-8")
TEMPLATE = (ROOT / "references/output-template.md").read_text(encoding="utf-8")


class SkillTests(unittest.TestCase):
    def test_metadata_and_local_links(self):
        self.assertRegex(SKILL, r"\A---\nname: quick-project-plans\n")
        self.assertIn("description: >-", SKILL)
        for path in ROOT.rglob("*.md"):
            content = path.read_text(encoding="utf-8")
            self.assertNotIn("\x00", content)
            prose = re.sub(r"^```[^\n]*\n.*?^```\s*$", "", content,
                           flags=re.M | re.S)
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", prose):
                if "://" in target or target.startswith("#"):
                    continue
                resolved = (path.parent / target.split("#")[0]).resolve()
                self.assertIn(ROOT, resolved.parents)
                self.assertTrue(resolved.is_file(), f"Missing link: {target}")

    def test_two_outputs_and_actionable_tasks(self):
        for name in ("plan.md", "tasks.md"):
            self.assertIn(f"## {name}", TEMPLATE)
            self.assertIn(f"`{name}`", SKILL)
        self.assertIn("[plan.md](./plan.md)", TEMPLATE)
        self.assertIn("- [ ]", TEMPLATE)
        self.assertIn("Where:", TEMPLATE)
        self.assertIn("Done when:", TEMPLATE)
        self.assertIn("no fixed limit", SKILL)
        self.assertIn("milestones", SKILL)

    def test_authorization_and_completion(self):
        self.assertIn("Stop for a planning-only request", SKILL)
        self.assertIn("start without asking again", SKILL)
        self.assertIn("Not approved", TEMPLATE)
        self.assertIn("Approved", TEMPLATE)
        self.assertIn("requested outcome is implemented", SKILL)
        self.assertIn("leave unfinished work unchecked", SKILL)
        self.assertNotIn("all possible work is verified", SKILL + TEMPLATE)

    def test_proportional_checks(self):
        self.assertIn("Write new tests only when", SKILL)
        self.assertIn("not after every edit or task", SKILL)
        self.assertIn("Related tasks may share", SKILL)
        self.assertIn("mandatory user/project checks", SKILL)
        self.assertIn("payments, migrations or destructive actions", SKILL)
        self.assertNotIn("**Verify:**", TEMPLATE)
        self.assertNotIn("Execution Contract", TEMPLATE)

    def test_external_package_convention(self):
        for phrase in ("AGENT_PLANS_ROOT", "~/.agent/plans", "SHA-256",
                       "first 10 lowercase hex", "YYYY-MM-DD-HHmmss",
                       "outside the project", "Never overwrite old plans"):
            self.assertIn(phrase, SKILL)
        self.assertNotRegex(SKILL + TEMPLATE, r"(?:/home/|/Users/)")


if __name__ == "__main__":
    unittest.main()

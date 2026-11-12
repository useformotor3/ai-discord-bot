import json
import tempfile
import unittest
from pathlib import Path

from scripts.audit_archive import audit_repository


class ArchiveAuditTests(unittest.TestCase):
    def make_repo(self, root: Path):
        (root / "research_archive").mkdir()
        (root / "research_archive" / "one.md").write_text("one", encoding="utf-8")
        (root / "history.json").write_text(
            json.dumps([{"file": "research_archive/one.md", "count": 1}], ensure_ascii=False),
            encoding="utf-8",
        )
        (root / "state.json").write_text(
            json.dumps({"date": "2026-11-12", "count": 1}), encoding="utf-8"
        )

    def test_consistent_archive_and_history(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_repo(root)
            report = audit_repository(root)
            self.assertTrue(report["consistent"])
            self.assertEqual(report["archive_count"], 1)
            self.assertEqual(report["history_entry_count"], 1)
            self.assertEqual(report["state"]["count"], 1)
            self.assertIn("daily counter", report["state_warning"])

    def test_detects_orphan_and_missing_history(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_repo(root)
            (root / "research_archive" / "two.md").write_text("two", encoding="utf-8")
            history = [{"file": "research_archive/one.md"}, {"file": "research_archive/missing.md"}]
            (root / "history.json").write_text(json.dumps(history), encoding="utf-8")
            report = audit_repository(root)
            self.assertFalse(report["consistent"])
            self.assertEqual(report["archive_missing_history"], ["research_archive/two.md"])
            self.assertEqual(report["history_orphans"], ["research_archive/missing.md"])

    def test_detects_duplicate_history_and_malformed_entry(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_repo(root)
            history = [
                {"file": "research_archive/one.md"},
                {"file": "research_archive/one.md"},
                {"snippet": "missing file field"},
            ]
            (root / "history.json").write_text(json.dumps(history), encoding="utf-8")
            report = audit_repository(root)
            self.assertFalse(report["consistent"])
            self.assertEqual(report["duplicate_history_paths"], ["research_archive/one.md"])
            self.assertEqual(report["malformed_history_entry_indexes"], [2])


if __name__ == "__main__":
    unittest.main()

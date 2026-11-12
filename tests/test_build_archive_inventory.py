import json
import tempfile
import unittest
from pathlib import Path

from scripts.build_archive_inventory import classify, inventory


class ArchiveInventoryTests(unittest.TestCase):
    def make_repo(self, root: Path):
        archive = root / "research_archive"
        archive.mkdir()
        (archive / "2026-11-12_test.md").write_text(
            "# SBOM and Secure Boot\n\nArticle 13(8) and Annex I Part II point (8).\n"
            "Source: https://eur-lex.europa.eu/test\n",
            encoding="utf-8",
        )
        (root / "history.json").write_text(
            json.dumps([{"file": "research_archive/2026-11-12_test.md", "date": "2026-11-12", "count": 1}]),
            encoding="utf-8",
        )

    def test_inventory_extracts_metadata_without_verifying_claims(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_repo(root)
            report = inventory(root)
            self.assertEqual(report["archive_file_count"], 1)
            record = report["records"][0]
            self.assertIn("sbom_supply_chain", record["topic_candidates"])
            self.assertIn("secure_boot_hardware", record["topic_candidates"])
            self.assertIn("https://eur-lex.europa.eu/test", record["source_url_candidates"])
            self.assertEqual(record["verification_status"], "UNVERIFIED_AI_ARCHIVE")
            self.assertTrue(record["sha256"])

    def test_classify_marks_unknown_as_unclassified(self):
        self.assertEqual(classify("No matching security topic here"), ["unclassified"])

    def test_duplicate_history_entries_do_not_duplicate_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_repo(root)
            history = [
                {"file": "research_archive/2026-11-12_test.md", "date": "2026-11-12"},
                {"file": "research_archive/2026-11-12_test.md", "date": "2026-11-12"},
            ]
            (root / "history.json").write_text(json.dumps(history), encoding="utf-8")
            report = inventory(root)
            self.assertEqual(report["archive_file_count"], 1)
            self.assertEqual(report["history_entry_count"], 2)


if __name__ == "__main__":
    unittest.main()

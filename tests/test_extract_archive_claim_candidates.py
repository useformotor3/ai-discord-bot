import tempfile, unittest
from pathlib import Path
from scripts.extract_archive_claim_candidates import build, extract_file

class ExtractArchiveClaimsTests(unittest.TestCase):
    def test_extracts_claims_urls_articles_and_keeps_unverified(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); d=root/"research_archive"; d.mkdir()
            f=d/"sample.md"
            f.write_text("# Test CRA\n\n제조사는 보안 업데이트를 무상으로 제공해야 합니다. 이 의무는 CRA Annex I Part II point 8의 문맥과 예외 조건을 함께 검토해야 합니다.\n\nArticle 13(8) and Annex I Part II.\n\nSource: https://eur-lex.europa.eu/example\n\nRaw Text Quote: sample text", encoding="utf-8")
            r=extract_file(f,root)
            self.assertEqual(r["verification_status"],"UNVERIFIED_AI_ARCHIVE")
            self.assertIn("Article 13(8)",r["article_reference_candidates"])
            self.assertIn("https://eur-lex.europa.eu/example",r["source_url_candidates"])
            self.assertTrue(r["claim_candidates"])
            self.assertTrue(r["quote_section_candidates"])
    def test_build_counts_all_markdown_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); d=root/"research_archive"; d.mkdir()
            (d/"a.md").write_text("# A\n\nMust be checked.",encoding="utf-8")
            (d/"b.md").write_text("# B\n\nNo claim.",encoding="utf-8")
            result=build(root)
            self.assertEqual(result["archive_file_count"],2)
            self.assertEqual(len(result["records"]),2)
            self.assertIn("limitations",result)
    def test_flags_fixed_five_year_claim_as_candidate_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); d=root/"research_archive"; d.mkdir()
            f=d/"five.md"; f.write_text("최소 5년 지원해야 합니다.",encoding="utf-8")
            r=extract_file(f,root)
            self.assertIn("SUPPORT_PERIOD_FIXED_5Y",r["heuristic_risk_flags"])
            self.assertEqual(r["verification_status"],"UNVERIFIED_AI_ARCHIVE")

if __name__ == "__main__":
    unittest.main()

import csv
import shutil
from pathlib import Path

import pytest

from cra_traceability import TraceabilityError, validate_traceability


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "reports/CRA_GUIDANCE_CLAIM_REGISTER_2026-11-17.csv",
    "reports/CRA_SERVO_DRIVE_INTERFACE_APPLICABILITY_2026-11-17.csv",
    "reports/CRA_REQUIREMENTS_TRACEABILITY_2026-11-17.csv",
    "reports/CRA_SERVO_DRIVE_SECURITY_CONTROL_TEST_MATRIX_2026-11-17.csv",
    "reports/CRA_M606_ANNEX_I_SERVO_DRIVE_RELEVANCE_2026-11-17.csv",
    "reports/CRA_PDF_SOURCE_PROVENANCE_2026-11-17.json",
    "PROJECT_LOG.jsonl",
    "README.md",
    "reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md",
    "reports/CRA_EVD_SEC_TRACEABILITY_CROSSWALK_2026-11-19.csv",
    "reports/CRA_PRODUCT_EVIDENCE_REGISTER_TEMPLATE_2026-11-19.csv",
    "reports/CRA_PRODUCT_BOUNDARY_AND_EVIDENCE_INTAKE_2026-11-17.md",
    "reports/CRA_INTEGRATED_REPORT_INDEPENDENT_AUDIT_2026-11-17.md",
)


def _copy_required_tree(destination):
    for relative in REQUIRED:
        source = ROOT / relative
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)


def test_repository_guidance_and_m606_traceability_is_consistent():
    summary = validate_traceability(ROOT)
    assert summary["guidance_claims"] == 13
    assert summary["interfaces"] == 15
    assert summary["requirements"] == 35
    assert summary["security_controls"] == 36
    assert summary["linked_claims"] == 13
    assert 41 in summary["referenced_m606_items"]
    assert summary["pdf_sources"] == 3
    assert summary["m606_mapping_items"] == 41


def test_unknown_guidance_claim_reference_fails_closed(tmp_path):
    _copy_required_tree(tmp_path)
    path = tmp_path / REQUIRED[1]
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
        fieldnames = list(rows[0])
    rows[0]["Commission Guidance claim IDs (non-binding)"] = "G-999"
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    with pytest.raises(TraceabilityError, match="unknown Guidance claim IDs"):
        validate_traceability(tmp_path)


def test_out_of_range_m606_reference_fails_closed(tmp_path):
    _copy_required_tree(tmp_path)
    path = tmp_path / REQUIRED[2]
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
        fieldnames = list(rows[0])
    rows[0]["M/606 Annex I candidate items (conditional; not product classification)"] = "42"
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    with pytest.raises(TraceabilityError, match="outside 1–41"):
        validate_traceability(tmp_path)


def test_duplicate_m606_mapping_item_fails_closed(tmp_path):
    _copy_required_tree(tmp_path)
    path = tmp_path / REQUIRED[4]
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
        fieldnames = list(rows[0])
    rows[0]["M/606 Annex I item"] = "2"
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    with pytest.raises(TraceabilityError, match="each item 1–41 exactly once|duplicate item numbers"):
        validate_traceability(tmp_path)


def test_wrong_m606_eso_deadline_fails_closed(tmp_path):
    _copy_required_tree(tmp_path)
    path = tmp_path / REQUIRED[4]
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
        fieldnames = list(rows[0])
    rows[0]["ESO adoption deadline (not manufacturer compliance deadline)"] = "31/01/2027"
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    with pytest.raises(TraceabilityError, match="incorrect ESO adoption deadline"):
        validate_traceability(tmp_path)


def test_m606_item18_wrong_printed_page_fails_closed(tmp_path):
    _copy_required_tree(tmp_path)
    path = tmp_path / REQUIRED[5]
    import json
    provenance = json.loads(path.read_text(encoding="utf-8"))
    provenance["visual_verification"][0]["printed_page_number"] = 3
    path.write_text(json.dumps(provenance), encoding="utf-8")
    with pytest.raises(TraceabilityError, match="printed EN 2"):
        validate_traceability(tmp_path)


def test_duplicate_integrated_report_section_number_fails_closed(tmp_path):
    _copy_required_tree(tmp_path)
    path = tmp_path / "reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md"
    with path.open("a", encoding="utf-8") as stream:
        stream.write("\n\n## 14. Duplicate section number regression\n")
    with pytest.raises(TraceabilityError, match="duplicate top-level section numbers"):
        validate_traceability(tmp_path)

def test_missing_official_oj_guidance_source_fails_closed(tmp_path):
    _copy_required_tree(tmp_path)
    path = tmp_path / REQUIRED[5]
    import json
    provenance = json.loads(path.read_text(encoding="utf-8"))
    provenance["sources"] = [
        item for item in provenance["sources"]
        if item.get("id") != "CRA-GUIDANCE-OJ-2026-6013"
    ]
    path.write_text(json.dumps(provenance), encoding="utf-8")
    with pytest.raises(TraceabilityError, match="PDF provenance missing"):
        validate_traceability(tmp_path)


def test_oj_guidance_fallback_is_rejected(tmp_path):
    _copy_required_tree(tmp_path)
    path = tmp_path / REQUIRED[5]
    import json
    provenance = json.loads(path.read_text(encoding="utf-8"))
    source = next(
        item for item in provenance["sources"]
        if item.get("id") == "CRA-GUIDANCE-OJ-2026-6013"
    )
    source["fallback_used"] = True
    path.write_text(json.dumps(provenance), encoding="utf-8")
    with pytest.raises(TraceabilityError, match="fetched directly from EUR-Lex"):
        validate_traceability(tmp_path)

def test_claim_to_matrix_link_requires_reverse_link(tmp_path):
    _copy_required_tree(tmp_path)
    path = tmp_path / REQUIRED[1]
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
        fieldnames = list(rows[0])
    row = next(row for row in rows if row["ID"] == "IF-015")
    row["Commission Guidance claim IDs (non-binding)"] = "G-010; G-011"
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    with pytest.raises(TraceabilityError, match="G-005: IF-015 missing reverse Guidance link"):
        validate_traceability(tmp_path)


def test_matrix_claim_link_requires_claim_register_reverse_link(tmp_path):
    _copy_required_tree(tmp_path)
    path = tmp_path / REQUIRED[1]
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
        fieldnames = list(rows[0])
    row = next(row for row in rows if row["ID"] == "IF-015")
    row["Commission Guidance claim IDs (non-binding)"] = "G-005; G-010; G-011; G-013"
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    with pytest.raises(TraceabilityError, match="IF-015: G-013 missing claim-register reverse link"):
        validate_traceability(tmp_path)


def test_claim_related_foreign_key_must_exist(tmp_path):
    _copy_required_tree(tmp_path)
    path = tmp_path / REQUIRED[0]
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
        fieldnames = list(rows[0])
    row = next(row for row in rows if row["Claim ID"] == "G-005")
    row["Related interface IDs"] = "IF-999"
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    with pytest.raises(TraceabilityError, match="G-005: unknown interface ID IF-999"):
        validate_traceability(tmp_path)


def test_evd_sec_crosswalk_covers_all_evidence_and_controls():
    summary = validate_traceability(ROOT)
    assert summary["evd_sec_crosswalk_rows"] == 16
    assert summary["crosswalk_sec_controls_linked"] == 36


def test_evd_sec_crosswalk_rejects_unknown_control_reference(tmp_path):
    _copy_required_tree(tmp_path)
    path = tmp_path / "reports/CRA_EVD_SEC_TRACEABILITY_CROSSWALK_2026-11-19.csv"
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
        fieldnames = list(rows[0])
    rows[0]["Related_SEC_control_IDs"] = "SEC-999"
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    with pytest.raises(TraceabilityError, match="unknown SEC control refs"):
        validate_traceability(tmp_path)


def test_evd_sec_crosswalk_rejects_missing_evidence_row(tmp_path):
    _copy_required_tree(tmp_path)
    path = tmp_path / "reports/CRA_EVD_SEC_TRACEABILITY_CROSSWALK_2026-11-19.csv"
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    path.write_text("\n".join(lines[:-1]) + "\n", encoding="utf-8")
    with pytest.raises(TraceabilityError, match="expected 16 rows|cover EVD-01"):
        validate_traceability(tmp_path)


def test_evd_sec_crosswalk_rejects_orphaned_control(tmp_path):
    _copy_required_tree(tmp_path)
    path = tmp_path / "reports/CRA_EVD_SEC_TRACEABILITY_CROSSWALK_2026-11-19.csv"
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
        fieldnames = list(rows[0])
    row = next(row for row in rows if row["Evidence_ID"] == "EVD-03")
    row["Related_SEC_control_IDs"] = row["Related_SEC_control_IDs"].replace("SEC-008", "")
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    with pytest.raises(TraceabilityError, match="SEC controls missing from EVD/SEC crosswalk"):
        validate_traceability(tmp_path)


def test_product_evidence_register_template_has_15_unprovided_records():
    summary = validate_traceability(ROOT)
    assert summary["product_evidence_register_rows"] == 15
    assert summary["product_evidence_register_states"] == ["not_provided"]


def test_product_evidence_register_rejects_accepted_without_provenance(tmp_path):
    _copy_required_tree(tmp_path)
    path = tmp_path / "reports/CRA_PRODUCT_EVIDENCE_REGISTER_TEMPLATE_2026-11-19.csv"
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
        fieldnames = list(rows[0])
    rows[0]["Evidence_Record_State"] = "accepted"
    rows[0]["Decision"] = "accepted"
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    with pytest.raises(TraceabilityError, match="E-001: accepted requires Evidence_File_Name"):
        validate_traceability(tmp_path)


def test_product_evidence_register_rejects_unknown_evd_reference(tmp_path):
    _copy_required_tree(tmp_path)
    path = tmp_path / "reports/CRA_PRODUCT_EVIDENCE_REGISTER_TEMPLATE_2026-11-19.csv"
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
        fieldnames = list(rows[0])
    rows[0]["Related_EVD_IDs"] = "EVD-99"
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    with pytest.raises(TraceabilityError, match="E-001: unknown EVD refs"):
        validate_traceability(tmp_path)


def test_product_evidence_register_requires_reasoned_not_applicable(tmp_path):
    _copy_required_tree(tmp_path)
    path = tmp_path / "reports/CRA_PRODUCT_EVIDENCE_REGISTER_TEMPLATE_2026-11-19.csv"
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
        fieldnames = list(rows[0])
    rows[0]["Evidence_Record_State"] = "not_applicable_with_rationale"
    rows[0]["Decision"] = "not_applicable"
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    with pytest.raises(TraceabilityError, match="E-001: not_applicable_with_rationale requires Product_Variant_ID"):
        validate_traceability(tmp_path)

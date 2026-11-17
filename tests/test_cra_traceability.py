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
    assert summary["pdf_sources"] == 2
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

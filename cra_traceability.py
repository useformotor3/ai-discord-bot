"""Validate CRA guidance claim, matrix and source-provenance cross-links."""
import argparse
import csv
import json
import re
from pathlib import Path


class TraceabilityError(RuntimeError):
    """Raised when CRA traceability artifacts are inconsistent."""


CLAIM_RE = re.compile(r"\bG-\d{3}\b")
REQUIREMENT_RE = re.compile(r"\bCRA-\d{3}\b")
CONTROL_RE = re.compile(r"\bSEC-\d{3}\b")
INTERFACE_RE = re.compile(r"\bIF-\d{3}\b")
ITEM_RE = re.compile(r"(?<![A-Za-z])(?P<start>\d{1,2})(?:\s*[–-]\s*(?P<end>\d{1,2}))?")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")

FILES = {
    "claims": "reports/CRA_GUIDANCE_CLAIM_REGISTER_2026-11-17.csv",
    "interfaces": "reports/CRA_SERVO_DRIVE_INTERFACE_APPLICABILITY_2026-11-17.csv",
    "requirements": "reports/CRA_REQUIREMENTS_TRACEABILITY_2026-11-17.csv",
    "controls": "reports/CRA_SERVO_DRIVE_SECURITY_CONTROL_TEST_MATRIX_2026-11-17.csv",
    "m606_map": "reports/CRA_M606_ANNEX_I_SERVO_DRIVE_RELEVANCE_2026-11-17.csv",
    "provenance": "reports/CRA_PDF_SOURCE_PROVENANCE_2026-11-17.json",
    "project_log": "PROJECT_LOG.jsonl",
    "readme": "README.md",
    "integrated_report": "reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md",
    "product_intake": "reports/CRA_PRODUCT_BOUNDARY_AND_EVIDENCE_INTAKE_2026-11-17.md",
}


def _read_csv(path):
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def _claim_ids(value):
    return set(CLAIM_RE.findall(value or ""))


def _m606_items(value):
    items = set()
    for match in ITEM_RE.finditer(value or ""):
        start = int(match.group("start"))
        end = int(match.group("end") or start)
        if end < start:
            raise TraceabilityError(f"descending M/606 item range: {match.group(0)}")
        items.update(range(start, end + 1))
    invalid = sorted(item for item in items if item < 1 or item > 41)
    if invalid:
        raise TraceabilityError(f"M/606 item references outside 1–41: {invalid}")
    return items


def _require(condition, message, errors):
    if not condition:
        errors.append(message)


def validate_traceability(root="."):
    root = Path(root)
    errors = []
    data = {}
    for key, relative in FILES.items():
        path = root / relative
        if not path.is_file():
            errors.append(f"missing required file: {relative}")
            continue
        data[key] = path

    if errors:
        raise TraceabilityError("\n".join(errors))

    claims = _read_csv(data["claims"])
    interfaces = _read_csv(data["interfaces"])
    requirements = _read_csv(data["requirements"])
    controls = _read_csv(data["controls"])
    m606_map = _read_csv(data["m606_map"])

    expected_counts = {
        "claims": (claims, 13),
        "interfaces": (interfaces, 15),
        "requirements": (requirements, 35),
        "controls": (controls, 36),
    }
    for label, (rows, expected) in expected_counts.items():
        _require(len(rows) == expected,
                 f"{label}: expected {expected} rows, found {len(rows)}", errors)

    id_columns = {
        "claims": ("Claim ID", "G-"),
        "interfaces": ("ID", "IF-"),
        "requirements": ("ID", "CRA-"),
        "controls": ("ID", "SEC-"),
    }
    id_sets = {}
    rows_by_label = {label: rows for label, (rows, _expected) in expected_counts.items()}
    for label, rows in rows_by_label.items():
        field, prefix = id_columns[label]
        ids = [row.get(field, "") for row in rows]
        _require(all(value.startswith(prefix) for value in ids),
                 f"{label}: missing/invalid {field}", errors)
        _require(len(ids) == len(set(ids)),
                 f"{label}: duplicate {field}", errors)
        id_sets[label] = set(ids)

    guidance_col = "Commission Guidance claim IDs (non-binding)"
    m606_col = "M/606 Annex I candidate items (conditional; not product classification)"
    used_claims = set()
    referenced_items = set()
    for label, rows in (("interfaces", interfaces), ("requirements", requirements), ("controls", controls)):
        for index, row in enumerate(rows, start=2):
            if guidance_col not in row:
                errors.append(f"{label} row {index}: missing column {guidance_col}")
                continue
            if m606_col not in row:
                errors.append(f"{label} row {index}: missing column {m606_col}")
                continue
            used_claims.update(_claim_ids(row.get(guidance_col, "")))
            try:
                referenced_items.update(_m606_items(row.get(m606_col, "")))
            except TraceabilityError as exc:
                errors.append(f"{label} row {index}: {exc}")

    unknown_claims = sorted(used_claims - id_sets.get("claims", set()))
    _require(not unknown_claims, f"unknown Guidance claim IDs in matrices: {unknown_claims}", errors)
    orphan_claims = sorted(id_sets.get("claims", set()) - used_claims)
    _require(not orphan_claims, f"Guidance claims not linked to any matrix: {orphan_claims}", errors)

    # Validate the complete M/606 Annex I crosswalk and every candidate foreign key.
    _require(len(m606_map) == 41,
             f"M/606 mapping: expected 41 rows, found {len(m606_map)}", errors)
    item_numbers = []
    expected_categories = {}
    for item in range(1, 42):
        if item <= 14:
            expected_categories[item] = ("horizontal_property", "horizontal_baseline", "30/11/2026" if item == 1 else "30/10/2027")
        elif item == 15:
            expected_categories[item] = ("horizontal_vulnerability_handling", "horizontal_baseline", "30/11/2026")
        elif 28 <= item <= 30 or 37 <= item <= 39:
            expected_categories[item] = ("security_component", "component_due_diligence_conditional", "31/01/2027")
        elif item == 41:
            expected_categories[item] = ("security_component_or_product_type", "component_or_product_type_conditional", "31/01/2027")
        elif item in (16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 31, 32, 33, 34, 35, 36, 40):
            category = "vertical_interface_conditional" if item == 25 else ("vertical_product_type_not_typical" if item in (31, 32, 33, 34, 40) else "vertical_product_type_conditional")
            expected_categories[item] = ("vertical_product_type", category, "31/01/2027")
    for row in m606_map:
        try:
            item = int(row.get("M/606 Annex I item", ""))
        except ValueError:
            errors.append("M/606 mapping contains a non-integer item number")
            continue
        item_numbers.append(item)
        expected = expected_categories.get(item)
        _require(expected is not None, f"M/606 mapping has out-of-range item {item}", errors)
        if expected is None:
            continue
        expected_category, expected_class, expected_deadline = expected
        _require(row.get("Category") == expected_category,
                 f"M/606 item {item}: unexpected category {row.get('Category')}", errors)
        _require(row.get("Servo-drive relevance class") == expected_class,
                 f"M/606 item {item}: unexpected relevance class {row.get('Servo-drive relevance class')}", errors)
        _require(row.get("ESO adoption deadline (not manufacturer compliance deadline)") == expected_deadline,
                 f"M/606 item {item}: incorrect ESO adoption deadline", errors)
        _require("does not make a draft standard harmonised" in row.get("Status note", ""),
                 f"M/606 item {item}: missing non-harmonised-status caveat", errors)
        req_refs = set(REQUIREMENT_RE.findall(row.get("Candidate CRA requirement IDs (conditional)", "")))
        sec_refs = set(CONTROL_RE.findall(row.get("Candidate SEC control IDs (conditional)", "")))
        if_refs = set(INTERFACE_RE.findall(row.get("Related interface IDs", "")))
        _require(req_refs.issubset(id_sets.get("requirements", set())),
                 f"M/606 item {item}: unknown CRA requirement refs {sorted(req_refs - id_sets.get('requirements', set()))}", errors)
        _require(sec_refs.issubset(id_sets.get("controls", set())),
                 f"M/606 item {item}: unknown SEC control refs {sorted(sec_refs - id_sets.get('controls', set()))}", errors)
        _require(if_refs.issubset(id_sets.get("interfaces", set())),
                 f"M/606 item {item}: unknown interface refs {sorted(if_refs - id_sets.get('interfaces', set()))}", errors)
    _require(sorted(item_numbers) == list(range(1, 42)),
             "M/606 mapping must contain each item 1–41 exactly once", errors)
    _require(len(item_numbers) == len(set(item_numbers)),
             "M/606 mapping contains duplicate item numbers", errors)
    item18_map = next((row for row in m606_map if row.get("M/606 Annex I item") == "18"), {})
    _require("EN 3" in item18_map.get("PDF printed page locator", "")
             and "visually confirmed" in item18_map.get("PDF printed page locator", ""),
             "M/606 item 18 must point to visually confirmed EN 3 deadline cell", errors)

    for row in claims:
        _require(row.get("Category") == "official_explanation",
                 f"{row.get('Claim ID')}: Guidance claim must be categorized as official_explanation", errors)
        _require(str(row.get("Legal requirement?", "")).startswith("아니오"),
                 f"{row.get('Claim ID')}: non-binding Guidance claim must not be labeled a legal requirement", errors)
        _require("ANFR mirror raw-byte SHA-256 verified" in row.get("Evidence status", ""),
                 f"{row.get('Claim ID')}: evidence status must state mirror hash scope", errors)

    try:
        provenance = json.loads(data["provenance"].read_text(encoding="utf-8"))
    except Exception as exc:
        raise TraceabilityError(f"invalid PDF provenance JSON: {exc}") from exc

    sources = {item.get("id"): item for item in provenance.get("sources", [])}
    required_sources = {"CRA-GUIDANCE-2026-5252", "CRA-GUIDANCE-OJ-2026-6013", "CRA-M606-C2026-7861-ANNEX"}
    _require(required_sources.issubset(sources),
             "PDF provenance missing one or more required source IDs", errors)
    for source_id in required_sources & set(sources):
        source = sources[source_id]
        _require(bool(SHA_RE.fullmatch(source.get("sha256", ""))),
                 f"{source_id}: invalid raw-byte SHA-256", errors)
        _require(bool(SHA_RE.fullmatch(source.get("extracted_text_sha256", ""))),
                 f"{source_id}: invalid extracted-text SHA-256", errors)
        _require(source.get("byte_count", 0) > 0 and source.get("page_count", 0) > 0,
                 f"{source_id}: missing byte count or page count", errors)

    guidance = sources.get("CRA-GUIDANCE-2026-5252", {})
    _require("ANFR mirror bytes only" in guidance.get("binary_identity_scope", ""),
             "Historical C(2026) 5252 provenance must remain mirror-only", errors)
    oj_guidance = sources.get("CRA-GUIDANCE-OJ-2026-6013", {})
    _require(oj_guidance.get("fallback_used") is False,
             "OJ C/2026/6013 guidance must be fetched directly from EUR-Lex", errors)
    _require("EUR-Lex Official Journal PDF bytes" in oj_guidance.get("binary_identity_scope", ""),
             "OJ guidance provenance must identify EUR-Lex Official Journal bytes", errors)
    _require("C/2026/6013" in oj_guidance.get("document", ""),
             "OJ guidance source must identify C/2026/6013", errors)
    m606 = sources.get("CRA-M606-C2026-7861-ANNEX", {})
    _require(m606.get("fallback_used") is False,
             "M/606 Annex should be sourced directly from Commission register", errors)

    workflow = provenance.get("workflow", {})
    _require(bool(SHA_RE.fullmatch(workflow.get("artifact_zip_sha256", ""))),
             "PDF artifact ZIP SHA-256 missing/invalid", errors)
    _require(workflow.get("artifact_downloaded_and_sha256_reverified") is True,
             "PDF artifact download/hash readback not confirmed", errors)

    item18 = next((item for item in provenance.get("visual_verification", [])
                   if item.get("annex_item") == 18), {})
    _require(item18.get("deadline") == "31/01/2027" and item18.get("status") == "confirmed",
             "M/606 item 18 deadline visual confirmation missing", errors)
    _require(item18.get("printed_page_number") == 3,
             "M/606 item 18 provenance must locate deadline cell on printed EN 3", errors)

    log_lines = data["project_log"].read_text(encoding="utf-8").splitlines()
    log_ids = []
    legacy_keys = []
    for line_number, line in enumerate(log_lines, start=1):
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"PROJECT_LOG.jsonl line {line_number}: invalid JSON ({exc})")
            continue
        event_id = event.get("event_id")
        if event_id:
            log_ids.append(event_id)
        else:
            # Historical records predate event_id and use timestamp/type.
            timestamp = event.get("timestamp")
            event_type = event.get("type")
            if not timestamp or not event_type:
                errors.append(f"PROJECT_LOG.jsonl line {line_number}: missing event_id and legacy timestamp/type")
            else:
                legacy_keys.append((timestamp, event_type))
    _require(len(log_ids) == len(set(log_ids)),
             "PROJECT_LOG.jsonl contains duplicate event_id values", errors)
    _require(len(legacy_keys) == len(set(legacy_keys)),
             "PROJECT_LOG.jsonl contains duplicate legacy timestamp/type keys", errors)

    readme = data["readme"].read_text(encoding="utf-8")
    integrated = data["integrated_report"].read_text(encoding="utf-8")
    section_numbers = re.findall(r"^##\s+(\d+)\.", integrated, flags=re.MULTILINE)
    _require(len(section_numbers) == len(set(section_numbers)),
             "integrated report contains duplicate top-level section numbers", errors)
    _require(FILES["claims"] in readme and FILES["provenance"] in readme and FILES["m606_map"] in readme and FILES["product_intake"] in readme,
             "README must link claim register and PDF provenance manifest", errors)
    _require("CRA_GUIDANCE_CLAIM_REGISTER_2026-11-17.csv" in integrated
             and "CRA_PDF_SOURCE_PROVENANCE_2026-11-17.json" in integrated
             and "CRA_M606_ANNEX_I_SERVO_DRIVE_RELEVANCE_2026-11-17.csv" in integrated
             and Path(FILES["product_intake"]).name in integrated,
             "integrated report must link claim register and PDF provenance", errors)

    if errors:
        raise TraceabilityError("\n".join(errors))

    return {
        "guidance_claims": len(claims),
        "interfaces": len(interfaces),
        "requirements": len(requirements),
        "security_controls": len(controls),
        "linked_claims": len(used_claims),
        "referenced_m606_items": sorted(referenced_items),
        "m606_mapping_items": len(m606_map),
        "pdf_sources": len(sources),
        "project_log_events": len(log_lines),
        "project_log_events_with_event_id": len(log_ids),
        "legacy_project_log_events": len(legacy_keys),
        "pdf_artifact_run": workflow.get("run_number"),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    args = parser.parse_args(argv)
    try:
        summary = validate_traceability(args.root)
    except TraceabilityError as exc:
        print(f"FAIL: CRA traceability validation\n{exc}")
        return 1
    print(
        "PASS: CRA traceability "
        f"claims={summary['guidance_claims']} "
        f"interfaces={summary['interfaces']} "
        f"requirements={summary['requirements']} "
        f"SEC={summary['security_controls']} "
        f"linked_claims={summary['linked_claims']} "
        f"M606_mapping_items={summary['m606_mapping_items']} "
        f"project_log_events={summary['project_log_events']} "
        f"modern_ids={summary['project_log_events_with_event_id']} "
        f"legacy={summary['legacy_project_log_events']} "
        f"PDF_artifact_run={summary['pdf_artifact_run']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

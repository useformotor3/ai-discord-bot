"""Classify the CRA automation run without treating a green job as new research."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Any


def classify_run(log_text: str, exit_code: int | None, step_outcome: str = "success") -> dict[str, Any]:
    """Return a conservative, machine-readable summary of main.py's observed outcome."""
    log = log_text or ""
    lowered = log.lower()

    source_count = None
    marker = "[공식 source gate]"
    for line in log.splitlines():
        if marker in line:
            tail = line.split(marker, 1)[1]
            digits = "".join(ch for ch in tail.split("개", 1)[0] if ch.isdigit())
            if digits:
                source_count = int(digits)
            break

    model_lines = [line.strip() for line in log.splitlines() if "모델 [" in line and "]으로 조사를 시도합니다" in line]
    fallback = any(term in log for term in ("일시적 과부하(503)", "할당량/요청 제한(429)", "동일 모델 재시도를 중단하고 대체 모델로 전환"))
    archive_synced = "깃허브 백서버에 아카이브가 성공적으로 동기화되었습니다." in log
    discord_sent = "Discord 전송 결과: sent" in log
    discord_deferred = "Discord 전송 결과: deferred" in log or "Discord 전송 결과: delivery_unknown" in log

    if exit_code not in (0, None) or step_outcome == "failure" or "❌ [조사 실패]" in log:
        outcome = "FAILED"
        meaning = "실행 실패; 운영 데이터 및 전송 결과를 별도 확인해야 함"
    elif "⚠️ [조사 보류]" in log:
        outcome = "DEFERRED"
        meaning = "모델 장애/할당량/품질 검증으로 신규 조사를 보류함"
    elif "중복/신규 주제 없음" in log:
        outcome = "NO_NEW_TOPIC"
        meaning = "신규 주제가 없어 보고서·아카이브·Discord 변경 없이 종료함"
    elif "중복 주제 차단" in log:
        outcome = "DUPLICATE_BLOCKED"
        meaning = "중복 주제로 판단해 보고서 저장과 전송을 차단함"
    elif archive_synced and discord_sent:
        outcome = "RESEARCH_ARCHIVED_AND_DELIVERED"
        meaning = "보고서 원격 아카이브와 Discord 전송을 확인함"
    elif archive_synced and discord_deferred:
        outcome = "ARCHIVED_DELIVERY_DEFERRED"
        meaning = "보고서는 원격 아카이브했으나 Discord 전송은 보류/미확인"
    elif exit_code == 0 and step_outcome == "success":
        outcome = "SUCCESS_UNCLASSIFIED"
        meaning = "프로세스는 성공 종료했으나 조사 결과 유형을 로그에서 확정하지 못함"
    else:
        outcome = "NOT_RUN_OR_UNKNOWN"
        meaning = "실행되지 않았거나 결과를 판정할 로그가 없음"

    return {
        "outcome": outcome,
        "meaning": meaning,
        "exit_code": exit_code,
        "step_outcome": step_outcome,
        "official_source_count": source_count,
        "models_attempted": model_lines,
        "model_fallback_observed": fallback,
        "archive_synced": archive_synced,
        "discord_sent": discord_sent,
        "discord_deferred_or_unknown": discord_deferred,
    }


def render_summary(result: dict[str, Any]) -> str:
    models = ", ".join(result["models_attempted"]) or "확인 불가"
    source_count = result["official_source_count"]
    source_text = str(source_count) if source_count is not None else "확인 불가"
    return (
        "## CRA 자동조사 실행 결과\n"
        f"- **판정:** `{result['outcome']}` — {result['meaning']}\n"
        f"- **프로세스:** exit={result['exit_code']}; step={result['step_outcome']}\n"
        f"- **공식 출처 확보:** {source_text}개\n"
        f"- **시도 모델:** {models}\n"
        f"- **모델 폴백 관찰:** {'예' if result['model_fallback_observed'] else '아니오'}\n"
        f"- **원격 아카이브 확인:** {'예' if result['archive_synced'] else '아니오'}\n"
        f"- **Discord 전송 확인:** {'예' if result['discord_sent'] else ('보류/미확인' if result['discord_deferred_or_unknown'] else '아니오/미실행')}\n"
        "\n> GitHub Actions의 job success는 이 분류와 별개다. `NO_NEW_TOPIC` 및 `DEFERRED`는 신규 보고서 생성 완료로 계산하지 않는다.\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("log_path", type=Path)
    parser.add_argument("--exit-code", default="not_run")
    parser.add_argument("--step-outcome", default="unknown")
    args = parser.parse_args()

    try:
        log_text = args.log_path.read_text(encoding="utf-8") if args.log_path.exists() else ""
    except (OSError, UnicodeError) as exc:
        log_text = f"log read error: {type(exc).__name__}"

    try:
        exit_code = int(args.exit_code)
    except (TypeError, ValueError):
        exit_code = None

    result = classify_run(log_text, exit_code, args.step_outcome)
    summary = render_summary(result)
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as handle:
            handle.write(summary)
    else:
        print(summary, end="")
    output_path = os.environ.get("GITHUB_OUTPUT")
    if output_path:
        with open(output_path, "a", encoding="utf-8") as handle:
            handle.write(f"research_outcome={result['outcome']}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

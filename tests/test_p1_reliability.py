"""P1-A: 상태·이력 파일의 손상 및 날짜 호환성 검증."""
import json
from datetime import datetime

import pytest

from test_main_characterization import VALID_REPORT


def write_state(path, payload):
    path.write_text(payload, encoding="utf-8")


def assert_safe_failure(run_main, responses):
    with pytest.raises(SystemExit) as exc:
        run_main.execute(responses)
    assert exc.value.code != 0
    assert run_main.captured["model_calls"] == []
    assert run_main.captured["discord_posts"] == []
    assert run_main.captured["git_commands"] == []
    assert not (run_main.workdir / "research_archive").exists()


def test_corrupt_state_json_is_preserved_and_stops_before_external_calls(run_main):
    path = run_main.workdir / "state.json"
    write_state(path, '{"date": ')
    before = path.read_bytes()

    assert_safe_failure(run_main, [VALID_REPORT])

    assert path.read_bytes() == before


@pytest.mark.parametrize(
    "payload",
    [
        '{"date":"2026-11-14","count":"29"}',
        '{"date":"2026-11-14","count":-1}',
        '{"date":"2026-11-14","count":true}',
        '{"date":"not-a-date","count":29}',
        '[]',
    ],
)
def test_invalid_state_schema_is_preserved_and_rejected(run_main, payload):
    path = run_main.workdir / "state.json"
    write_state(path, payload)
    before = path.read_bytes()

    assert_safe_failure(run_main, [VALID_REPORT])

    assert path.read_bytes() == before


def test_invalid_last_health_check_is_preserved_and_rejected(run_main):
    path = run_main.workdir / "state.json"
    payload = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "count": 29,
        "last_health_check": "not-an-iso-datetime",
    }
    path.write_text(json.dumps(payload), encoding="utf-8")
    before = path.read_bytes()

    assert_safe_failure(run_main, [VALID_REPORT])

    assert path.read_bytes() == before


def test_corrupt_history_json_is_preserved_and_stops_before_external_calls(run_main):
    path = run_main.workdir / "history.json"
    write_state(path, '[{"snippet": "existing"},')
    before = path.read_bytes()

    assert_safe_failure(run_main, [VALID_REPORT])

    assert path.read_bytes() == before


@pytest.mark.parametrize("payload", ['{}', '[{"snippet":"ok"}, 7]'])
def test_invalid_history_structure_is_preserved_and_rejected(run_main, payload):
    path = run_main.workdir / "history.json"
    write_state(path, payload)
    before = path.read_bytes()

    assert_safe_failure(run_main, [VALID_REPORT])

    assert path.read_bytes() == before


def test_timezone_aware_health_check_is_compatible_with_local_naive_clock(run_main):
    state = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "count": 4,
        "last_health_check": datetime.now().astimezone().isoformat(),
    }
    (run_main.workdir / "state.json").write_text(
        json.dumps(state), encoding="utf-8"
    )

    run_main.execute([VALID_REPORT])

    updated = json.loads(
        (run_main.workdir / "state.json").read_text(encoding="utf-8")
    )
    assert updated["count"] == 5


def test_legacy_naive_datetime_and_missing_history_remain_compatible(run_main):
    state = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "count": 8,
        "last_health_check": datetime.now().isoformat(),
    }
    (run_main.workdir / "state.json").write_text(
        json.dumps(state), encoding="utf-8"
    )

    run_main.execute([VALID_REPORT])

    updated = json.loads(
        (run_main.workdir / "state.json").read_text(encoding="utf-8")
    )
    assert updated["count"] == 9
    history = json.loads(
        (run_main.workdir / "history.json").read_text(encoding="utf-8")
    )
    assert len(history) == 1

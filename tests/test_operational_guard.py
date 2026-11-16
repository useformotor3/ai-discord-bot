import pytest

from scripts.operational_guard import GuardError, validate_transition


def _baseline():
    state = {"date": "2026-11-16", "count": 10}
    history = [
        {"date": "2026-11-16", "count": 10, "file": "research_archive/old.md"}
    ]
    archives = {"research_archive/old.md"}
    return state, history, archives


def _valid_current():
    old_state, old_history, old_archives = _baseline()
    state = {"date": "2026-11-16", "count": 11}
    history = old_history + [
        {"date": "2026-11-16", "count": 11, "file": "research_archive/new.md"}
    ]
    archives = old_archives | {"research_archive/new.md"}
    return old_state, old_history, old_archives, state, history, archives


def test_accepts_exactly_one_append_only_report():
    result = validate_transition(*_valid_current())
    assert result == {
        "new_archive": "research_archive/new.md",
        "history_count": 2,
        "archive_count": 2,
        "state_count": 11,
    }


def test_rejects_missing_new_archive_reference():
    args = list(_valid_current())
    args[-1] = {"research_archive/old.md"}
    with pytest.raises(GuardError, match="reference sets differ"):
        validate_transition(*args)


def test_rejects_deleted_existing_archive():
    args = list(_valid_current())
    args[-1] = {"research_archive/new.md"}
    with pytest.raises(GuardError, match="reference sets differ|removed"):
        validate_transition(*args)


def test_rejects_non_append_only_history():
    args = list(_valid_current())
    args[4] = [
        {"date": "2026-11-16", "count": 10, "file": "research_archive/changed.md"},
        args[4][-1],
    ]
    args[5] = {"research_archive/changed.md", "research_archive/new.md"}
    with pytest.raises(GuardError, match="history is not append-only"):
        validate_transition(*args)


def test_rejects_wrong_state_count():
    args = list(_valid_current())
    args[3] = {"date": "2026-11-16", "count": 99}
    with pytest.raises(GuardError, match="unexpected state count"):
        validate_transition(*args)


def test_new_day_resets_daily_counter_to_one():
    old_state, old_history, old_archives = _baseline()
    state = {"date": "2026-11-17", "count": 1}
    history = old_history + [
        {"date": "2026-11-17", "count": 1, "file": "research_archive/next-day.md"}
    ]
    archives = old_archives | {"research_archive/next-day.md"}
    result = validate_transition(
        old_state, old_history, old_archives, state, history, archives
    )
    assert result["state_count"] == 1


@pytest.mark.parametrize("bad_ref", [
    "../state.json", "/tmp/escape.md", "research_archive/../state.json",
    "research_archive/subdir/report.md", "README.md",
])
def test_rejects_unsafe_archive_reference(bad_ref):
    state = {"date": "2026-11-16", "count": 1}
    history = [{"date": "2026-11-16", "count": 1, "file": bad_ref}]
    with pytest.raises(GuardError):
        validate_transition(state, history, {bad_ref}, state, history, {bad_ref})

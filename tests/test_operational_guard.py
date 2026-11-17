import json

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


def _git(cwd, *args):
    import subprocess
    return subprocess.run(
        ["git", *args], cwd=cwd, check=True, text=True,
        capture_output=True,
    )


def _git_repo(tmp_path):
    from pathlib import Path

    bare = tmp_path / "origin.git"
    work = tmp_path / "work"
    _git(tmp_path, "init", "--bare", str(bare))
    work.mkdir()
    _git(work, "init", "-b", "main")
    _git(work, "config", "user.name", "Test Runner")
    _git(work, "config", "user.email", "test@example.invalid")
    _git(work, "remote", "add", "origin", str(bare))
    (work / "research_archive").mkdir()
    (work / "research_archive/old.md").write_text("# old report", encoding="utf-8")
    (work / "state.json").write_text(
        '{"date":"2026-11-16","count":10}', encoding="utf-8"
    )
    (work / "history.json").write_text(
        '[{"date":"2026-11-16","count":10,"file":"research_archive/old.md"}]',
        encoding="utf-8",
    )
    _git(work, "add", "state.json", "history.json", "research_archive")
    _git(work, "commit", "-m", "baseline")
    _git(work, "push", "-u", "origin", "main")
    baseline = _git(work, "rev-parse", "HEAD").stdout.strip()
    _git(work, "branch", "safety/pre-run-test")
    _git(work, "push", "origin", "safety/pre-run-test")
    return work, baseline


def _write_one_report(work, count=11):
    import json

    report = "research_archive/new.md"
    (work / report).write_text("# new report", encoding="utf-8")
    (work / "state.json").write_text(
        json.dumps({"date":"2026-11-16","count":count}), encoding="utf-8"
    )
    old = json.loads((work / "history.json").read_text(encoding="utf-8"))
    old.append({"date":"2026-11-16","count":count,"file":report})
    (work / "history.json").write_text(json.dumps(old), encoding="utf-8")


def test_git_integration_accepts_valid_transition(tmp_path):
    from scripts.operational_guard import verify_and_recover

    work, _ = _git_repo(tmp_path)
    _write_one_report(work)
    _git(work, "add", "state.json", "history.json", "research_archive")
    _git(work, "commit", "-m", "valid run")
    _git(work, "push", "origin", "HEAD:refs/heads/main")

    assert verify_and_recover(work, "safety/pre-run-test", "main", "ok-run") == 0
    assert _git(work, "rev-parse", "HEAD").stdout.strip() == _git(
        work, "ls-remote", "origin", "refs/heads/main"
    ).stdout.split()[0]


def test_git_integration_restores_invalid_data_with_new_commit(tmp_path):
    from scripts.operational_guard import verify_and_recover

    work, baseline = _git_repo(tmp_path)
    _write_one_report(work)
    (work / "research_archive/old.md").unlink()
    _git(work, "add", "-A")
    _git(work, "commit", "-m", "faulty run")
    _git(work, "push", "origin", "HEAD:refs/heads/main")

    assert verify_and_recover(work, "safety/pre-run-test", "main", "bad-run") == 1
    restored = _git(work, "rev-parse", "HEAD").stdout.strip()
    assert restored != baseline
    assert _git(work, "diff", "--quiet", baseline, "HEAD", "--",
                "state.json", "history.json", "research_archive/").returncode == 0
    assert (work / "research_archive/old.md").exists()
    assert not (work / "research_archive/new.md").exists()
    assert _git(work, "ls-remote", "origin", "refs/heads/main").stdout.split()[0] == restored


def test_git_integration_resets_unpublished_local_commit_when_remote_is_baseline(tmp_path):
    from scripts.operational_guard import verify_and_recover

    work, baseline = _git_repo(tmp_path)
    _write_one_report(work)
    _git(work, "add", "state.json", "history.json", "research_archive")
    _git(work, "commit", "-m", "local-only run")

    assert verify_and_recover(work, "safety/pre-run-test", "main", "unpublished") == 1
    assert _git(work, "rev-parse", "HEAD").stdout.strip() == baseline
    assert _git(work, "ls-remote", "origin", "refs/heads/main").stdout.split()[0] == baseline
    assert json.loads((work / "state.json").read_text(encoding="utf-8"))["count"] == 10
    assert not (work / "research_archive/new.md").exists()


def test_git_integration_restores_uncommitted_data_and_untracked_archive(tmp_path):
    import json
    from scripts.operational_guard import verify_and_recover

    work, baseline = _git_repo(tmp_path)
    (work / "state.json").write_text(
        '{"date":"2026-11-16","count":99}', encoding="utf-8"
    )
    (work / "history.json").write_text("[]", encoding="utf-8")
    (work / "research_archive/new.md").write_text("# partial report", encoding="utf-8")

    assert verify_and_recover(work, "safety/pre-run-test", "main", "dirty-run") == 1
    assert _git(work, "rev-parse", "HEAD").stdout.strip() == baseline
    assert _git(work, "ls-remote", "origin", "refs/heads/main").stdout.split()[0] == baseline
    assert json.loads((work / "state.json").read_text(encoding="utf-8"))["count"] == 10
    history = json.loads((work / "history.json").read_text(encoding="utf-8"))
    assert len(history) == 1
    assert not (work / "research_archive/new.md").exists()
    assert (work / "research_archive/old.md").exists()
    assert not _git(work, "status", "--porcelain", "--", "state.json", "history.json", "research_archive/").stdout


def test_git_integration_accepts_clean_noop_quota_skip(tmp_path):
    from scripts.operational_guard import verify_and_recover

    work, baseline = _git_repo(tmp_path)
    assert verify_and_recover(work, "safety/pre-run-test", "main", "quota-skip") == 0
    assert _git(work, "rev-parse", "HEAD").stdout.strip() == baseline


def test_current_snapshot_rejects_empty_archive_file(tmp_path):
    from scripts.operational_guard import GuardError, _current_snapshot

    (tmp_path / "state.json").write_text(
        '{"date":"2026-11-16","count":1}', encoding="utf-8"
    )
    (tmp_path / "history.json").write_text("[]", encoding="utf-8")
    archive = tmp_path / "research_archive"
    archive.mkdir()
    (archive / "empty.md").write_text("", encoding="utf-8")
    with pytest.raises(GuardError, match="empty archive"):
        _current_snapshot(tmp_path)


def test_git_integration_restores_missing_state_file(tmp_path):
    from scripts.operational_guard import verify_and_recover

    work, _ = _git_repo(tmp_path)
    _write_one_report(work)
    (work / "state.json").unlink()
    _git(work, "add", "-A")
    _git(work, "commit", "-m", "run with missing state")
    _git(work, "push", "origin", "HEAD:refs/heads/main")

    assert verify_and_recover(work, "safety/pre-run-test", "main", "missing-state") == 1
    assert (work / "state.json").read_text(encoding="utf-8") == (
        '{"date":"2026-11-16","count":10}'
    )

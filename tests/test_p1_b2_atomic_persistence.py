"""P1-B2 journaled persistence failure-injection tests."""
import json

import pytest

import persistence
from test_main_characterization import VALID_REPORT
from persistence import (
    PersistenceError,
    commit_persistence_transaction,
    recover_pending_transactions,
)


def _seed(root):
    (root / "state.json").write_bytes(b'{"date":"2026-11-16","count":4}')
    (root / "history.json").write_bytes(b'[{"count":4}]')
    return {
        "archive": b"# report\nnew\n",
        "history": b'[{"count":4},{"count":5}]',
        "state": b'{"date":"2026-11-16","count":5}',
    }


def _operations(root, payloads):
    return [
        {"target": "research_archive/report.md", "payload": payloads["archive"],
         "expected_old": None},
        {"target": "history.json", "payload": payloads["history"],
         "expected_old": (root / "history.json").read_bytes()},
        {"target": "state.json", "payload": payloads["state"],
         "expected_old": (root / "state.json").read_bytes()},
    ]


def _crash_after(target):
    def hook(stage, value):
        if stage == "after_replace" and value == target:
            raise RuntimeError("simulated process interruption")
    return hook


def test_success_commits_archive_history_and_state_in_order(tmp_path):
    payloads = _seed(tmp_path)
    txn_id = commit_persistence_transaction(tmp_path, _operations(tmp_path, payloads))
    assert len(txn_id) == 32
    assert (tmp_path / "research_archive/report.md").read_bytes() == payloads["archive"]
    assert (tmp_path / "history.json").read_bytes() == payloads["history"]
    assert (tmp_path / "state.json").read_bytes() == payloads["state"]
    assert not list((tmp_path / ".persistence_txn").glob("*/journal.json"))


@pytest.mark.parametrize("target", [
    "research_archive/report.md", "history.json", "state.json",
])
def test_crash_after_each_replace_recovers_idempotently(tmp_path, target):
    payloads = _seed(tmp_path)
    with pytest.raises(RuntimeError, match="simulated"):
        commit_persistence_transaction(
            tmp_path, _operations(tmp_path, payloads), fault_hook=_crash_after(target)
        )
    recover_pending_transactions(tmp_path)
    recover_pending_transactions(tmp_path)
    assert (tmp_path / "research_archive/report.md").read_bytes() == payloads["archive"]
    assert (tmp_path / "history.json").read_bytes() == payloads["history"]
    assert (tmp_path / "state.json").read_bytes() == payloads["state"]


def test_crash_after_prepared_journal_rolls_forward(tmp_path):
    payloads = _seed(tmp_path)

    def hook(stage, value):
        if stage == "after_prepared":
            raise RuntimeError("stop after durable prepare")

    with pytest.raises(RuntimeError):
        commit_persistence_transaction(tmp_path, _operations(tmp_path, payloads), fault_hook=hook)
    recover_pending_transactions(tmp_path)
    assert (tmp_path / "state.json").read_bytes() == payloads["state"]
    assert (tmp_path / "history.json").read_bytes() == payloads["history"]


def test_stage_failure_leaves_targets_byte_identical_and_orphan_is_cleaned(tmp_path):
    _seed(tmp_path)
    before = {
        name: (tmp_path / name).read_bytes()
        for name in ("state.json", "history.json")
    }

    def hook(stage, value):
        if stage == "after_stage_write" and value == "history.json":
            raise OSError("simulated stage write failure")

    with pytest.raises(OSError):
        commit_persistence_transaction(tmp_path, _operations(tmp_path, {
            "archive": b"a", "history": b"h", "state": b"s",
        }), fault_hook=hook)
    assert {name: (tmp_path / name).read_bytes() for name in before} == before
    recover_pending_transactions(tmp_path)
    assert not list((tmp_path / ".persistence_txn").glob("*/manifest.json"))


def test_fsync_failure_before_prepare_does_not_change_targets(tmp_path, monkeypatch):
    _seed(tmp_path)
    before = [(tmp_path / name).read_bytes() for name in ("state.json", "history.json")]

    def fail_fsync(_path):
        raise OSError("simulated directory fsync failure")

    monkeypatch.setattr(persistence, "_fsync_dir", fail_fsync)
    with pytest.raises(OSError):
        commit_persistence_transaction(tmp_path, _operations(tmp_path, {
            "archive": b"a", "history": b"h", "state": b"s",
        }))
    assert [(tmp_path / name).read_bytes() for name in ("state.json", "history.json")] == before


def test_corrupt_journal_fails_closed_and_preserves_targets(tmp_path):
    payloads = _seed(tmp_path)
    with pytest.raises(RuntimeError):
        commit_persistence_transaction(
            tmp_path, _operations(tmp_path, payloads),
            fault_hook=_crash_after("research_archive/report.md"),
        )
    txn_dir = next(path for path in (tmp_path / ".persistence_txn").iterdir() if path.is_dir())
    (txn_dir / "journal.json").write_text("{broken", encoding="utf-8")
    state_before = (tmp_path / "state.json").read_bytes()
    with pytest.raises(PersistenceError, match="journal 손상"):
        recover_pending_transactions(tmp_path)
    assert (tmp_path / "state.json").read_bytes() == state_before


def test_missing_stage_fails_closed_without_overwriting_old_targets(tmp_path):
    payloads = _seed(tmp_path)
    with pytest.raises(RuntimeError):
        commit_persistence_transaction(
            tmp_path, _operations(tmp_path, payloads),
            fault_hook=_crash_after("research_archive/report.md"),
        )
    txn_dir = next(path for path in (tmp_path / ".persistence_txn").iterdir() if path.is_dir())
    (txn_dir / "staged/1.bin").unlink()
    old_state = (tmp_path / "state.json").read_bytes()
    with pytest.raises(PersistenceError, match="staged payload 누락"):
        recover_pending_transactions(tmp_path)
    assert (tmp_path / "state.json").read_bytes() == old_state


def test_unexpected_target_sha_fails_closed(tmp_path):
    payloads = _seed(tmp_path)
    with pytest.raises(RuntimeError):
        commit_persistence_transaction(
            tmp_path, _operations(tmp_path, payloads),
            fault_hook=_crash_after("research_archive/report.md"),
        )
    (tmp_path / "history.json").write_bytes(b'{"external":"change"}')
    with pytest.raises(PersistenceError, match="target SHA"):
        recover_pending_transactions(tmp_path)
    assert (tmp_path / "history.json").read_bytes() == b'{"external":"change"}'


def test_archive_name_collision_never_overwrites_existing_file(tmp_path):
    payloads = _seed(tmp_path)
    archive = tmp_path / "research_archive/report.md"
    archive.parent.mkdir()
    archive.write_bytes(b"preserve existing")
    operations = _operations(tmp_path, payloads)
    with pytest.raises(PersistenceError, match="target이 변경"):
        commit_persistence_transaction(tmp_path, operations)
    assert archive.read_bytes() == b"preserve existing"


def test_stale_read_snapshot_prevents_lost_update(tmp_path):
    payloads = _seed(tmp_path)
    operations = _operations(tmp_path, payloads)
    (tmp_path / "state.json").write_bytes(b'{"external":"newer"}')
    with pytest.raises(PersistenceError, match="읽은 시점 이후"):
        commit_persistence_transaction(tmp_path, operations)
    assert (tmp_path / "state.json").read_bytes() == b'{"external":"newer"}'


def test_backup_sha_corruption_fails_closed(tmp_path):
    payloads = _seed(tmp_path)
    with pytest.raises(RuntimeError):
        commit_persistence_transaction(
            tmp_path, _operations(tmp_path, payloads),
            fault_hook=_crash_after("research_archive/report.md"),
        )
    txn_dir = next(path for path in (tmp_path / ".persistence_txn").iterdir() if path.is_dir())
    (txn_dir / "backup/1.bin").write_bytes(b"tampered")
    with pytest.raises(PersistenceError, match="backup payload SHA"):
        recover_pending_transactions(tmp_path)


@pytest.mark.parametrize("bad_target", [
    "../outside", "/tmp/outside", "", "README.md", ".git/config",
    ".github/workflows/run.yml", "persistence.py",
    "research_archive/nested/report.md", "research_archive/report.txt",
])
def test_invalid_target_path_is_rejected(tmp_path, bad_target):
    with pytest.raises(PersistenceError, match="target 경로"):
        commit_persistence_transaction(tmp_path, [
            {"target": bad_target, "payload": b"x", "expected_old": None},
        ])


def test_recovery_rejects_manifest_target_outside_persistence_allowlist(tmp_path):
    payloads = _seed(tmp_path)
    with pytest.raises(RuntimeError):
        commit_persistence_transaction(
            tmp_path, _operations(tmp_path, payloads),
            fault_hook=lambda stage, value: (
                (_ for _ in ()).throw(RuntimeError("simulated crash"))
                if stage == "after_prepared" else None
            ),
        )
    txn_dir = next(
        path for path in (tmp_path / ".persistence_txn").iterdir()
        if path.is_dir()
    )
    manifest_path = txn_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["operations"][0]["target"] = ".github/workflows/run.yml"
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    before = {
        name: (tmp_path / name).read_bytes()
        for name in ("state.json", "history.json")
    }
    with pytest.raises(PersistenceError, match="target 경로"):
        recover_pending_transactions(tmp_path)
    assert {
        name: (tmp_path / name).read_bytes()
        for name in ("state.json", "history.json")
    } == before


def test_journal_and_manifest_transaction_ids_must_match(tmp_path):
    payloads = _seed(tmp_path)
    with pytest.raises(RuntimeError):
        commit_persistence_transaction(
            tmp_path, _operations(tmp_path, payloads),
            fault_hook=_crash_after("research_archive/report.md"),
        )
    txn_dir = next(path for path in (tmp_path / ".persistence_txn").iterdir() if path.is_dir())
    journal = json.loads((txn_dir / "journal.json").read_text(encoding="utf-8"))
    journal["transaction_id"] = "wrong-id"
    (txn_dir / "journal.json").write_text(json.dumps(journal), encoding="utf-8")
    with pytest.raises(PersistenceError, match="transaction ID"):
        recover_pending_transactions(tmp_path)



def test_main_integration_commits_all_three_local_targets(run_main):
    run_main.execute([VALID_REPORT])
    state = json.loads((run_main.workdir / "state.json").read_text(encoding="utf-8"))
    history = json.loads((run_main.workdir / "history.json").read_text(encoding="utf-8"))
    archives = list((run_main.workdir / "research_archive").glob("*.md"))
    assert state["count"] == 1
    assert len(history) == 1
    assert len(archives) == 1
    assert history[0]["file"] == str(archives[0].relative_to(run_main.workdir))
    assert not list((run_main.workdir / ".persistence_txn").glob("*/journal.json"))


def test_main_recovers_before_any_external_call_when_journal_is_damaged(run_main):
    payloads = {
        "archive": b"# interrupted report",
        "history": b'[{"count":1}]',
        "state": b'{"date":"2026-11-16","count":1}',
    }
    (run_main.workdir / "state.json").write_bytes(b'{"date":"2026-11-16","count":0}')
    (run_main.workdir / "history.json").write_bytes(b"[]")
    operations = _operations(run_main.workdir, payloads)
    with pytest.raises(RuntimeError):
        commit_persistence_transaction(
            run_main.workdir, operations,
            fault_hook=_crash_after("research_archive/report.md"),
        )
    txn_dir = next(
        path for path in (run_main.workdir / ".persistence_txn").iterdir()
        if path.is_dir()
    )
    (txn_dir / "staged/1.bin").unlink()
    with pytest.raises(PersistenceError, match="staged payload 누락"):
        run_main.execute([VALID_REPORT])
    assert run_main.captured["model_calls"] == []
    assert run_main.captured["discord_posts"] == []
    assert run_main.captured["git_commands"] == []



def test_duplicate_targets_are_rejected_before_prepare(tmp_path):
    _seed(tmp_path)
    with pytest.raises(PersistenceError, match="중복 지정"):
        commit_persistence_transaction(tmp_path, [
            {"target": "state.json", "payload": b"one",
             "expected_old": (tmp_path / "state.json").read_bytes()},
            {"target": "state.json", "payload": b"two",
             "expected_old": (tmp_path / "state.json").read_bytes()},
        ])

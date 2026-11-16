"""Crash-recoverable local persistence for archive/state/history."""
from contextlib import contextmanager
import fcntl
import hashlib
import json
import os
from pathlib import Path
import shutil
import tempfile
import uuid


class PersistenceError(RuntimeError):
    """A transaction cannot safely proceed or recover."""


def _sha(data):
    return hashlib.sha256(data).hexdigest()


def read_optional_bytes(path):
    try:
        return Path(path).read_bytes()
    except FileNotFoundError:
        return None


def _fsync_dir(path):
    fd = os.open(str(path), os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def _write_durable(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp_name, path)
        _fsync_dir(path.parent)
    except BaseException:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass
        raise


@contextmanager
def _transaction_lock(root):
    txn_root = root / ".persistence_txn"
    txn_root.mkdir(parents=True, exist_ok=True)
    git_dir = root / ".git"
    lock_dir = git_dir if git_dir.is_dir() else txn_root
    fd = os.open(str(lock_dir / "persistence.lock"), os.O_CREAT | os.O_RDWR, 0o600)
    try:
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise PersistenceError("다른 프로세스가 로컬 저장 트랜잭션을 실행 중입니다.") from exc
        yield
    finally:
        try:
            fcntl.flock(fd, fcntl.LOCK_UN)
        finally:
            os.close(fd)


def _safe_target(root, relative):
    rel = Path(relative)
    if rel.is_absolute() or ".." in rel.parts or not rel.parts:
        raise PersistenceError(f"허용되지 않은 target 경로: {relative}")
    target = root / rel
    if target.is_symlink():
        raise PersistenceError(f"심볼릭 링크 target은 허용되지 않습니다: {relative}")
    resolved = target.resolve()
    if root != resolved and root not in resolved.parents:
        raise PersistenceError(f"저장소 외부 target 경로: {relative}")
    return target


def _load_manifest(txn_dir):
    try:
        manifest = json.loads((txn_dir / "manifest.json").read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise PersistenceError(f"트랜잭션 manifest 손상: {txn_dir.name}") from exc
    if (not isinstance(manifest, dict) or manifest.get("schema_version") != 1
            or not isinstance(manifest.get("operations"), list) or not manifest["operations"]):
        raise PersistenceError(f"트랜잭션 manifest 구조 오류: {txn_dir.name}")
    return manifest


def _target_state(root, operation):
    target = _safe_target(root, operation["target"])
    current = read_optional_bytes(target)
    return target, (None if current is None else _sha(current))


def _verify_staged(txn_dir, operation):
    try:
        data = (txn_dir / operation["staged"]).read_bytes()
    except OSError as exc:
        raise PersistenceError(f"staged payload 누락: {operation['staged']}") from exc
    if _sha(data) != operation["new_sha"]:
        raise PersistenceError(f"staged payload SHA 불일치: {operation['staged']}")
    return data


def _verify_backup(txn_dir, operation):
    if operation.get("old_sha") is None:
        return
    try:
        data = (txn_dir / operation["backup"]).read_bytes()
    except OSError as exc:
        raise PersistenceError(f"backup payload 누락: {operation['backup']}") from exc
    if _sha(data) != operation["old_sha"]:
        raise PersistenceError(f"backup payload SHA 불일치: {operation['backup']}")


def _roll_forward(root, txn_dir, manifest, journal, fault_hook=None):
    operations = manifest["operations"]
    for index, operation in enumerate(operations):
        target, current_sha = _target_state(root, operation)
        old_sha, new_sha = operation.get("old_sha"), operation["new_sha"]
        if current_sha == new_sha:
            continue
        if current_sha != old_sha:
            raise PersistenceError(
                f"target SHA가 old/new와 일치하지 않아 덮어쓰기를 중단합니다: {operation['target']}"
            )
        payload = _verify_staged(txn_dir, operation)
        target.parent.mkdir(parents=True, exist_ok=True)
        temp_path = target.parent / f".{target.name}.{manifest['transaction_id']}.tmp"
        _write_durable(temp_path, payload)
        os.replace(temp_path, target)
        _fsync_dir(target.parent)
        if fault_hook:
            fault_hook("after_replace", operation["target"])
        journal["phase"], journal["completed"] = "APPLYING", index + 1
        _write_durable(txn_dir / "journal.json",
                       json.dumps(journal, ensure_ascii=False, sort_keys=True).encode("utf-8"))
    for operation in operations:
        _, current_sha = _target_state(root, operation)
        if current_sha != operation["new_sha"]:
            raise PersistenceError(f"COMMITTED 전 target SHA 검증 실패: {operation['target']}")
    journal["phase"], journal["completed"] = "COMMITTED", len(operations)
    _write_durable(txn_dir / "journal.json",
                   json.dumps(journal, ensure_ascii=False, sort_keys=True).encode("utf-8"))
    if fault_hook:
        fault_hook("after_committed", manifest["transaction_id"])


def _recover_locked(root):
    txn_root = root / ".persistence_txn"
    txn_root.mkdir(parents=True, exist_ok=True)
    for txn_dir in sorted(path for path in txn_root.iterdir() if path.is_dir()):
        journal_path, manifest_path = txn_dir / "journal.json", txn_dir / "manifest.json"
        if not journal_path.exists():
            if not manifest_path.exists():
                shutil.rmtree(txn_dir)
                continue
            manifest = _load_manifest(txn_dir)
            states = [_target_state(root, op)[1] for op in manifest["operations"]]
            old_states = [op.get("old_sha") for op in manifest["operations"]]
            new_states = [op["new_sha"] for op in manifest["operations"]]
            if states == old_states or states == new_states:
                shutil.rmtree(txn_dir)
                continue
            raise PersistenceError(f"journal 없는 트랜잭션 target이 혼합 상태입니다: {txn_dir.name}")
        try:
            journal = json.loads(journal_path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            raise PersistenceError(f"트랜잭션 journal 손상: {txn_dir.name}") from exc
        if not isinstance(journal, dict) or journal.get("phase") not in ("PREPARED", "APPLYING", "COMMITTED"):
            raise PersistenceError(f"트랜잭션 journal phase 오류: {txn_dir.name}")
        manifest = _load_manifest(txn_dir)
        if journal.get("transaction_id") != manifest.get("transaction_id"):
            raise PersistenceError(f"journal/manifest transaction ID 불일치: {txn_dir.name}")
        for operation in manifest["operations"]:
            _verify_backup(txn_dir, operation)
        if journal["phase"] == "COMMITTED":
            for operation in manifest["operations"]:
                if _target_state(root, operation)[1] != operation["new_sha"]:
                    raise PersistenceError(f"COMMITTED target 불일치: {operation['target']}")
        else:
            for operation in manifest["operations"]:
                _verify_staged(txn_dir, operation)
            _roll_forward(root, txn_dir, manifest, journal)
        shutil.rmtree(txn_dir)


def recover_pending_transactions(root="."):
    """Recover durable transactions before state/history are read."""
    root = Path(root).resolve()
    with _transaction_lock(root):
        _recover_locked(root)


def commit_persistence_transaction(root, operations, fault_hook=None):
    """Commit ordered target/payload/expected_old entries with roll-forward recovery."""
    root = Path(root).resolve()
    if not isinstance(operations, list) or not operations:
        raise PersistenceError("저장 트랜잭션 작업 목록이 비어 있습니다.")
    with _transaction_lock(root):
        _recover_locked(root)
        txn_id = uuid.uuid4().hex
        txn_dir = root / ".persistence_txn" / txn_id
        (txn_dir / "staged").mkdir(parents=True)
        (txn_dir / "backup").mkdir()
        manifest_ops = []
        for index, item in enumerate(operations):
            relative, payload = str(item["target"]), item["payload"]
            target = _safe_target(root, relative)
            expected_old = item.get("expected_old")
            if not isinstance(payload, bytes):
                raise PersistenceError(f"payload는 bytes여야 합니다: {relative}")
            current = read_optional_bytes(target)
            current_sha = None if current is None else _sha(current)
            expected_sha = None if expected_old is None else _sha(expected_old)
            if current_sha != expected_sha:
                raise PersistenceError(f"읽은 시점 이후 target이 변경되어 저장을 중단합니다: {relative}")
            backup_rel = None
            if current is not None:
                backup_rel = f"backup/{index}.bin"
                _write_durable(txn_dir / backup_rel, current)
            staged_rel = f"staged/{index}.bin"
            _write_durable(txn_dir / staged_rel, payload)
            if fault_hook:
                fault_hook("after_stage_write", relative)
            manifest_ops.append({
                "target": relative, "old_sha": current_sha, "new_sha": _sha(payload),
                "staged": staged_rel, "backup": backup_rel,
            })
        manifest = {"schema_version": 1, "transaction_id": txn_id, "operations": manifest_ops}
        _write_durable(txn_dir / "manifest.json",
                       json.dumps(manifest, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        journal = {"transaction_id": txn_id, "phase": "PREPARED", "completed": 0}
        _write_durable(txn_dir / "journal.json",
                       json.dumps(journal, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        if fault_hook:
            fault_hook("after_prepared", txn_id)
        _roll_forward(root, txn_dir, manifest, journal, fault_hook=fault_hook)
        shutil.rmtree(txn_dir)
        return txn_id

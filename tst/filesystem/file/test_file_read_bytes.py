from __future__ import annotations

from pathlib import Path

from rite.filesystem import file_read_bytes, file_write_bytes


def test_file_read_bytes_roundtrip(tmp_path: Path) -> None:
    path = tmp_path / "data.bin"
    file_write_bytes(path, b"payload")
    assert file_read_bytes(path) == b"payload"

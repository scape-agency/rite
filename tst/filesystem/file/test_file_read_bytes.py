# Import | Future
from __future__ import annotations

# Import | Standard Library
from pathlib import Path

# Import | Local Modules
from rite.filesystem import file_read_bytes, file_write_bytes


def test_file_read_bytes_roundtrip(tmp_path: Path) -> None:
    path = tmp_path / "data.bin"
    file_write_bytes(path, b"payload")
    assert file_read_bytes(path) == b"payload"

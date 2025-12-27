from __future__ import annotations

from pathlib import Path

from rite.filesystem import file_read_bytes, file_write_bytes


def test_file_write_bytes_creates_parent_directory(tmp_path: Path) -> None:
    directory = tmp_path / "nested"
    path = directory / "data.bin"
    file_write_bytes(path, b"x")
    assert path.read_bytes() == b"x"
    assert directory.exists()

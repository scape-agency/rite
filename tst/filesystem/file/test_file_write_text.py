# Import | Future
from __future__ import annotations

# Import | Standard Library
from pathlib import Path

# Import | Local Modules
from rite.filesystem import file_read_text, file_write_text


def test_file_write_text_creates_parent_directory(tmp_path: Path) -> None:
    directory = tmp_path / "nested"
    path = directory / "data.txt"
    file_write_text(path, "x", encoding="utf-8")
    assert file_read_text(path, encoding="utf-8") == "x"
    assert directory.exists()

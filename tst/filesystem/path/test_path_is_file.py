# Import | Future
from __future__ import annotations

# Import | Standard Library
from pathlib import Path

# Import | Local Modules
from rite.filesystem import path_is_file


def test_path_is_file_distinguishes_files(tmp_path: Path) -> None:
    directory_path = tmp_path / "dir"
    directory_path.mkdir()
    file_path = directory_path / "file.txt"
    file_path.write_text("data", encoding="utf-8")

    assert path_is_file(file_path)
    assert not path_is_file(directory_path)

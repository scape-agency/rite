# Import | Future
from __future__ import annotations

# Import | Standard Library
from pathlib import Path

# Import | Local Modules
from rite.filesystem import path_exists


def test_path_exists_for_files_and_directories(tmp_path: Path) -> None:
    directory_path = tmp_path / "dir"
    directory_path.mkdir()
    file_path = directory_path / "file.txt"
    file_path.write_text("data", encoding="utf-8")

    assert path_exists(directory_path)
    assert path_exists(file_path)
    assert not path_exists(tmp_path / "missing")

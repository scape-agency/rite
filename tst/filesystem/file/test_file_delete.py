# Import | Future
from __future__ import annotations

# Import | Standard Library
from pathlib import Path

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem import delete_file, file_write_text


def test_delete_file_removes_and_raises_on_missing(tmp_path: Path) -> None:
    directory = tmp_path / "dir"
    directory.mkdir()
    file_path = directory / "file.txt"
    file_write_text(file_path, "x")

    delete_file(str(directory), "file.txt")
    assert not file_path.exists()

    with pytest.raises(FileNotFoundError):
        delete_file(str(directory), "missing.txt")

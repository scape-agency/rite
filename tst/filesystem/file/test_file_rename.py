from __future__ import annotations

from pathlib import Path

from rite.filesystem import file_write_text, rename_file


def test_rename_file_within_directory(tmp_path: Path) -> None:
    directory = tmp_path / "dir"
    directory.mkdir()
    file_path = directory / "old.txt"
    file_write_text(file_path, "x")

    rename_file(str(directory), "old.txt", "new.txt")
    assert not file_path.exists()
    assert (directory / "new.txt").exists()

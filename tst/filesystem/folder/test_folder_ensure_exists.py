from __future__ import annotations

from pathlib import Path

from rite.filesystem.folder.folder_ensure_exists import folder_ensure_exists


def test_folder_ensure_exists_creates_directory(tmp_path: Path) -> None:
    target = tmp_path / "nested" / "dir"
    folder_ensure_exists(target)
    assert target.is_dir()

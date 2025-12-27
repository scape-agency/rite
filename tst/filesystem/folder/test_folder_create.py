# Import | Future
from __future__ import annotations

# Import | Standard Library
from pathlib import Path

# Import | Local Modules
from rite.filesystem.folder.folder_create import create_directory


def test_create_directory_returns_path_and_creates(tmp_path: Path) -> None:
    target = tmp_path / "dir"
    result = create_directory(target)
    assert result == target
    assert result.is_dir()

# Import | Future
from __future__ import annotations

# Import | Standard Library
from pathlib import Path

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem.folder.folder_list_folders import list_folders


def test_list_folders_lists_direct_subdirectories(tmp_path: Path) -> None:
    root = tmp_path / "root"
    root.mkdir()
    (root / "a").mkdir()
    (root / "b").mkdir()
    (root / "file.txt").write_text("x")

    result = sorted(p.name for p in list_folders(root, recursive=False))
    assert result == ["a", "b"]


def test_list_folders_recursive_and_pattern(tmp_path: Path) -> None:
    root = tmp_path / "root"
    (root / "data").mkdir(parents=True)
    (root / "data_logs").mkdir()
    (root / "other").mkdir()

    result = sorted(
        p.name for p in list_folders(root, pattern="data*", recursive=True)
    )
    assert result == ["data", "data_logs"]


def test_list_folders_raises_for_missing_or_non_dir(tmp_path: Path) -> None:
    missing = tmp_path / "missing"
    with pytest.raises(FileNotFoundError):
        list_folders(missing)

    not_a_dir = tmp_path / "file.txt"
    not_a_dir.write_text("x")
    with pytest.raises(NotADirectoryError):
        list_folders(not_a_dir)

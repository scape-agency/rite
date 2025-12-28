# =============================================================================
# Test: folder_list_folders
# =============================================================================

"""
Tests for rite.filesystem.folder.folder_list_folders.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem.folder.folder_list_folders import (
    list_folders,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_list_folders_non_recursive(tmp_path) -> None:
    """list_folders should return only direct subdirectories by default."""
    root = tmp_path
    sub1 = root / "sub1"
    sub2 = root / "sub2"
    nested = root / "nested" / "inner"
    sub1.mkdir()
    sub2.mkdir()
    nested.mkdir(parents=True)

    result = list_folders(root)
    names = {p.name for p in result}
    assert names == {"sub1", "sub2", "nested"}


def test_list_folders_recursive_and_pattern(tmp_path) -> None:
    """list_folders supports recursive search and glob pattern filtering."""
    root = tmp_path
    (root / "sub1").mkdir()
    (root / "sub2").mkdir()
    nested = root / "nested"
    nested.mkdir()
    (nested / "nsub").mkdir()

    recursive = list_folders(root, recursive=True)
    names_recursive = {p.name for p in recursive}
    assert names_recursive >= {"sub1", "sub2", "nested", "nsub"}

    filtered = list_folders(root, pattern="sub*", recursive=True)
    names_filtered = {p.name for p in filtered}
    assert names_filtered == {"sub1", "sub2"}


def test_list_folders_raises_for_missing_or_file(tmp_path) -> None:
    """list_folders should error on missing path or non-directory."""
    missing = tmp_path / "missing"
    with pytest.raises(FileNotFoundError):
        list_folders(missing)

    file_path = tmp_path / "file.txt"
    file_path.write_text("data")
    with pytest.raises(NotADirectoryError):
        list_folders(file_path)

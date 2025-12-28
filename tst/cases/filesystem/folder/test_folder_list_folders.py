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


def test_list_folders_empty_directory(tmp_path) -> None:
    """list_folders should return empty list for empty directory."""
    result = list_folders(tmp_path)
    assert result == []


def test_list_folders_with_string_path(tmp_path) -> None:
    """list_folders should accept string paths."""
    sub = tmp_path / "subdir"
    sub.mkdir()

    result = list_folders(str(tmp_path))

    assert len(result) == 1
    assert result[0].name == "subdir"


def test_list_folders_pattern_filtering(tmp_path) -> None:
    """list_folders should filter results by pattern."""
    (tmp_path / "data_one").mkdir()
    (tmp_path / "data_two").mkdir()
    (tmp_path / "test_dir").mkdir()

    result = list_folders(tmp_path, pattern="data*")
    names = {p.name for p in result}

    assert names == {"data_one", "data_two"}
    assert "test_dir" not in names


def test_list_folders_pattern_with_recursive(tmp_path) -> None:
    """list_folders with pattern should work in recursive mode."""
    (tmp_path / "src_one").mkdir()
    (tmp_path / "src_two").mkdir()
    nested = tmp_path / "build"
    nested.mkdir()
    (nested / "src_three").mkdir()

    result = list_folders(tmp_path, pattern="src*", recursive=True)
    names = {p.name for p in result}

    assert "src_one" in names
    assert "src_two" in names
    assert "src_three" in names


def test_list_folders_recursive_deep_nesting(tmp_path) -> None:
    """list_folders recursive should find deeply nested directories."""
    deep = tmp_path / "a" / "b" / "c" / "d"
    deep.mkdir(parents=True)

    result = list_folders(tmp_path, recursive=True)
    names = {p.name for p in result}

    assert "a" in names
    assert "b" in names
    assert "c" in names
    assert "d" in names

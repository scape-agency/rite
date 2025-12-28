# =============================================================================
# Test: folder_list_files
# =============================================================================

"""
Tests for rite.filesystem.folder.folder_list_files.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.filesystem.folder.folder_list_files import (
    folder_list_files,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_folder_list_files_non_recursive(tmp_path) -> None:
    """folder_list_files yields only top-level files when not recursive.""""
    root = tmp_path
    file_a = root / "a.txt"
    file_b = root / "b.txt"
    subdir = root / "sub"
    subdir.mkdir()
    sub_file = subdir / "c.txt"

    file_a.write_text("A")
    file_b.write_text("B")
    sub_file.write_text("C")

    names = {p.name for p in folder_list_files(root, recursive=False)}
    assert names == {"a.txt", "b.txt"}


def test_folder_list_files_recursive(tmp_path) -> None:
    """folder_list_files yields files from subdirectories when recursive.""""
    root = tmp_path
    (root / "a.txt").write_text("A")
    subdir = root / "sub"
    subdir.mkdir()
    (subdir / "c.txt").write_text("C")

    names = {p.name for p in folder_list_files(root, recursive=True)}
    assert names == {"a.txt", "c.txt"}


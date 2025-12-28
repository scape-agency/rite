# =============================================================================
# Test: folder_size_get
# =============================================================================

"""
Tests for rite.filesystem.folder.folder_size_get.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.filesystem.folder.folder_size_get import (
    get_folder_size,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_get_folder_size_includes_nested_files(tmp_path) -> None:
    """get_folder_size should sum sizes of all files recursively.""""
    root = tmp_path
    file_a = root / "a.bin"
    subdir = root / "sub"
    subdir.mkdir()
    file_b = subdir / "b.bin"

    file_a.write_bytes(b"a" * 10)
    file_b.write_bytes(b"b" * 20)

    total = get_folder_size(root)
    assert total == 30


def test_get_folder_size_empty(tmp_path) -> None:
    """Empty folder should report size 0.""""
    assert get_folder_size(tmp_path) == 0


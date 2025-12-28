# =============================================================================
# Test: file_rename
# =============================================================================

"""
Tests for rite.filesystem.file.file_rename.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem.file.file_rename import (
    rename_file,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_rename_file_renames_existing(tmp_path) -> None:
    """rename_file should rename an existing file in directory."""
    directory = tmp_path
    old_path = directory / "old.txt"
    old_path.write_text("data")

    rename_file(str(directory), "old.txt", "new.txt")

    new_path = directory / "new.txt"
    assert not old_path.exists()
    assert new_path.exists()
    assert new_path.read_text() == "data"


def test_rename_file_missing_raises(tmp_path) -> None:
    """rename_file should raise FileNotFoundError if source is missing."""
    directory = tmp_path

    with pytest.raises(FileNotFoundError):
        rename_file(str(directory), "missing.txt", "new.txt")

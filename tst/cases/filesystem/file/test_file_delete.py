# =============================================================================
# Test: file_delete
# =============================================================================

"""
Tests for rite.filesystem.file.file_delete.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem.file.file_delete import (
    delete_file,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_delete_file_removes_existing(tmp_path) -> None:
    """delete_file should remove an existing file in directory."""
    directory = tmp_path
    file_path = directory / "test.txt"
    file_path.write_text("content")

    delete_file(str(directory), "test.txt")

    assert not file_path.exists()


def test_delete_file_missing_raises(tmp_path) -> None:
    """delete_file should raise FileNotFoundError for missing file."""
    directory = tmp_path

    with pytest.raises(FileNotFoundError):
        delete_file(str(directory), "missing.txt")

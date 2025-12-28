# =============================================================================
# Test: file_copy
# =============================================================================

"""
Tests for rite.filesystem.file.file_copy.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem.file.file_copy import (
    copy_file,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_copy_file_copies_contents(tmp_path) -> None:
    """copy_file should copy file contents to destination."""
    source = tmp_path / "source.txt"
    dest = tmp_path / "dest" / "dest.txt"
    source.write_text("hello")

    copy_file(source, dest)

    assert dest.exists()
    assert dest.read_text() == "hello"


def test_copy_file_missing_source_raises(tmp_path) -> None:
    """copy_file should raise if source file is missing."""
    source = tmp_path / "missing.txt"
    dest = tmp_path / "dest.txt"

    with pytest.raises(FileNotFoundError):
        copy_file(source, dest)


def test_copy_file_no_overwrite(tmp_path) -> None:
    """copy_file should not overwrite if overwrite=False and dest exists."""
    source = tmp_path / "source.txt"
    dest = tmp_path / "dest.txt"
    source.write_text("source")
    dest.write_text("existing")

    with pytest.raises(FileExistsError):
        copy_file(source, dest, overwrite=False)

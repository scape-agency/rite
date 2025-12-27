# =============================================================================
# Test: file_move
# =============================================================================

"""
Tests for rite.filesystem.file.file_move.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from pathlib import Path
import tempfile

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem.file.file_move import (
    move_file,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_move_file() -> None:
    """Test move_file() function."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create source directory and file
        source_dir = Path(tmpdir) / "source"
        source_dir.mkdir()
        test_file = source_dir / "test.txt"
        test_file.write_text("test content")

        # Move file to new directory
        dest_dir = Path(tmpdir) / "dest"
        move_file(str(source_dir), "test.txt", str(dest_dir))

        # Verify file moved
        assert not test_file.exists()
        assert (dest_dir / "test.txt").exists()
        assert (dest_dir / "test.txt").read_text() == "test content"

# =============================================================================
# Test: file_read_text
# =============================================================================

"""
Tests for rite.filesystem.file.file_read_text.
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
from rite.filesystem.file.file_read_text import (
    file_read_text,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_file_read_text() -> None:
    """Test file_read_text() function."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Read existing file
        file_path = Path(tmpdir) / "test.txt"
        file_path.write_text("Test Content")
        result = file_read_text(file_path)
        assert result == "Test Content"

        # Read empty file
        empty_path = Path(tmpdir) / "empty.txt"
        empty_path.write_text("")
        result = file_read_text(empty_path)
        assert result == ""

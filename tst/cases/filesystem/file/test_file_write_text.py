# =============================================================================
# Test: file_write_text
# =============================================================================

"""
Tests for rite.filesystem.file.file_write_text.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Standard Library
import tempfile
from pathlib import Path

# Import | Local Modules
from rite.filesystem.file.file_write_text import (
    file_write_text,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_file_write_text() -> None:
    """Test file_write_text() function."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Write to new file
        file_path = Path(tmpdir) / "test.txt"
        file_write_text(file_path, "Hello World")
        assert file_path.read_text() == "Hello World"

        # Overwrite existing file
        file_write_text(file_path, "New Content")
        assert file_path.read_text() == "New Content"

        # Create parent directories
        nested_path = Path(tmpdir) / "sub" / "dir" / "file.txt"
        file_write_text(nested_path, "Nested")
        assert nested_path.read_text() == "Nested"

# =============================================================================
# Test: file_read_bytes
# =============================================================================

"""
Tests for rite.filesystem.file.file_read_bytes.
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
from rite.filesystem.file.file_read_bytes import (
    file_read_bytes,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_file_read_bytes() -> None:
    """Test file_read_bytes() function."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Read bytes from file
        file_path = Path(tmpdir) / "test.bin"
        test_bytes = b"\x00\x01\x02\x03"
        file_path.write_bytes(test_bytes)
        result = file_read_bytes(file_path)
        assert result == test_bytes

        # Read text as bytes
        text_path = Path(tmpdir) / "text.txt"
        text_path.write_text("Hello")
        result = file_read_bytes(text_path)
        assert result == b"Hello"

# =============================================================================
# Test: file_write_bytes
# =============================================================================

"""
Tests for rite.filesystem.file.file_write_bytes.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.filesystem.file.file_write_bytes import (
    file_write_bytes,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_file_write_bytes_creates_parents_and_writes(tmp_path) -> None:
    """file_write_bytes should create parent dirs and write bytes."""
    target = tmp_path / "nested" / "file.bin"

    data = b"hello world"
    file_write_bytes(target, data)

    assert target.exists()
    assert target.read_bytes() == data

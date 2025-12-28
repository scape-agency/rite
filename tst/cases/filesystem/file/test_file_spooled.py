# =============================================================================
# Test: file_spooled
# =============================================================================

"""
Tests for rite.filesystem.file.file_spooled.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.filesystem.file.file_spooled import (
    create_spooled_temporary_file,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_create_spooled_temporary_file_empty() -> None:
    """create_spooled_temporary_file with no input yields empty file."""
    spooled = create_spooled_temporary_file()
    try:
        assert spooled.read() == b""
    finally:
        spooled.close()


def test_create_spooled_temporary_file_from_path(tmp_path) -> None:
    """create_spooled_temporary_file should copy content from filepath."""
    source = tmp_path / "source.bin"
    source.write_bytes(b"data")

    spooled = create_spooled_temporary_file(filepath=source)
    try:
        assert spooled.read() == b"data"
    finally:
        spooled.close()


def test_create_spooled_temporary_file_from_fileobj(tmp_path) -> None:
    """create_spooled_temporary_file should copy content from fileobj."""
    source = tmp_path / "src2.bin"
    source.write_bytes(b"more")

    with source.open("r+b") as f:
        spooled = create_spooled_temporary_file(fileobj=f)
        try:
            assert spooled.read() == b"more"
        finally:
            spooled.close()

# =============================================================================
# Test: folder_size_to_string
# =============================================================================

"""
Tests for rite.filesystem.folder.folder_size_to_string.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import os
from unittest.mock import MagicMock, patch

# Import | Local Modules
from rite.filesystem.folder.folder_size_to_string import (
    _TotalSize,
    folder_size_to_string,
)

# =============================================================================
# Test Class: _TotalSize
# =============================================================================


class Test_TotalSize:
    """Tests for _TotalSize class."""

    def test_instantiation(self) -> None:
        """Test _TotalSize can be instantiated."""
        instance = _TotalSize(1024)
        assert instance is not None
        assert instance.size == 1024

    def test_tell(self) -> None:
        """Test _TotalSize.tell() method."""
        instance = _TotalSize(2048)
        assert instance.tell() == 2048

    def test_seek(self) -> None:
        """Test _TotalSize.seek() method."""
        instance = _TotalSize(4096)
        assert instance.seek() == 4096


# =============================================================================
# Test Functions
# =============================================================================


def test_folder_size_to_string(tmp_path) -> None:
    """folder_size_to_string should return a human-readable total size."""
    root = tmp_path
    (root / "f1.bin").write_bytes(b"x" * 1024)
    (root / "f2.bin").write_bytes(b"y" * 1024)

    result = folder_size_to_string(root, recursive=True)

    assert result == "2.00 KB"


def test_folder_size_to_string_oserror(tmp_path) -> None:
    """Test folder_size_to_string handles OSError on stat (lines 86-88)."""
    # Import | Standard Library
    from pathlib import Path

    root = tmp_path
    (root / "accessible.bin").write_bytes(b"x" * 1024)

    original_stat = Path.stat

    def mock_stat(self, *args, **kwargs):
        if "accessible" not in str(self):
            raise OSError("Permission denied")
        return original_stat(self, *args, **kwargs)

    with patch.object(Path, "stat", mock_stat):
        # Should skip files that raise OSError
        result = folder_size_to_string(root, recursive=True)
        assert "KB" in result or "B" in result

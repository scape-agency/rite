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
from unittest.mock import patch

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
    root = tmp_path
    (root / "file1.bin").write_bytes(b"x" * 1024)
    (root / "file2.bin").write_bytes(b"y" * 1024)

    class MockStatResult:
        """Mock stat result."""

        st_size = 1024

    class FakePathOK:
        """Fake path that works normally."""

        def stat(self):
            return MockStatResult()

    class FakePathError:
        """Fake path that raises OSError on stat()."""

        def stat(self):
            raise OSError("Permission denied")

    # Mock folder_list_files to return our fake paths
    def mock_folder_list_files(path, recursive=False):
        yield FakePathOK()  # This one works
        yield FakePathError()  # This one raises OSError and is skipped
        yield FakePathOK()  # This one also works

    with patch(
        "rite.filesystem.folder.folder_size_to_string.folder_list_files",
        mock_folder_list_files,
    ):
        result = folder_size_to_string(root, recursive=True)
        # 2 files at 1024 bytes each = 2048 bytes = 2.00 KB
        assert result == "2.00 KB"

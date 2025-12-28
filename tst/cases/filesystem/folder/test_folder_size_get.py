# =============================================================================
# Test: folder_size_get
# =============================================================================

"""
Tests for rite.filesystem.folder.folder_size_get.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.filesystem.folder.folder_size_get import (
    get_folder_size,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_get_folder_size_includes_nested_files(tmp_path) -> None:
    """get_folder_size should sum sizes of all files recursively."""
    root = tmp_path
    file_a = root / "a.bin"
    subdir = root / "sub"
    subdir.mkdir()
    file_b = subdir / "b.bin"

    file_a.write_bytes(b"a" * 10)
    file_b.write_bytes(b"b" * 20)

    total = get_folder_size(root)
    assert total == 30


def test_get_folder_size_empty(tmp_path) -> None:
    """Empty folder should report size 0."""
    assert get_folder_size(tmp_path) == 0


def test_get_folder_size_single_file(tmp_path) -> None:
    """get_folder_size should correctly report single file size."""
    file_path = tmp_path / "file.bin"
    file_path.write_bytes(b"x" * 42)

    assert get_folder_size(tmp_path) == 42


def test_get_folder_size_mixed_sizes(tmp_path) -> None:
    """get_folder_size should sum files with different sizes."""
    (tmp_path / "small.txt").write_bytes(b"x" * 5)
    (tmp_path / "medium.txt").write_bytes(b"y" * 10)
    (tmp_path / "large.txt").write_bytes(b"z" * 100)

    assert get_folder_size(tmp_path) == 115


def test_get_folder_size_deeply_nested(tmp_path) -> None:
    """get_folder_size should count files in deeply nested structure."""
    deep = tmp_path / "a" / "b" / "c"
    deep.mkdir(parents=True)
    (tmp_path / "a").joinpath("file1.bin").write_bytes(b"x" * 10)
    (deep / "file2.bin").write_bytes(b"y" * 20)

    assert get_folder_size(tmp_path) == 30


def test_get_folder_size_with_empty_subdirs(tmp_path) -> None:
    """get_folder_size should handle empty subdirectories."""
    (tmp_path / "empty1").mkdir()
    (tmp_path / "empty2").mkdir()
    (tmp_path / "file.txt").write_bytes(b"data")

    assert get_folder_size(tmp_path) == 4


def test_get_folder_size_multiple_subdirs(tmp_path) -> None:
    """get_folder_size should sum files across multiple subdirectories."""
    (tmp_path / "dir1").mkdir()
    (tmp_path / "dir2").mkdir()
    (tmp_path / "dir1" / "f1.txt").write_bytes(b"x" * 15)
    (tmp_path / "dir2" / "f2.txt").write_bytes(b"y" * 25)

    assert get_folder_size(tmp_path) == 40

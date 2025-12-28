# =============================================================================
# Test: file_copy_multiple
# =============================================================================

"""
Tests for rite.filesystem.file.file_copy_multiple.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem.file.file_copy_multiple import (
    copy_files,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_copy_files_non_recursive(tmp_path) -> None:
    """copy_files should copy only top-level files when non-recursive."""
    source_dir = tmp_path / "src"
    target_dir = tmp_path / "dst"
    source_dir.mkdir()
    (source_dir / "a.txt").write_text("A")
    (source_dir / "b.txt").write_text("B")
    sub = source_dir / "sub"
    sub.mkdir()
    (sub / "c.txt").write_text("C")

    copy_files(source_dir, target_dir, recursive=False)

    names = {p.name for p in target_dir.iterdir()}
    assert names == {"a.txt", "b.txt"}


def test_copy_files_recursive(tmp_path) -> None:
    """copy_files should copy nested files when recursive=True."""
    source_dir = tmp_path / "src2"
    target_dir = tmp_path / "dst2"
    source_dir.mkdir()
    (source_dir / "root.txt").write_text("root")
    sub = source_dir / "sub"
    sub.mkdir()
    (sub / "nested.txt").write_text("nested")

    copy_files(source_dir, target_dir, recursive=True)

    copied_files = {
        str(p.relative_to(target_dir))
        for p in target_dir.rglob("*")
        if p.is_file()
    }
    assert copied_files == {"root.txt", "sub/nested.txt"}


def test_copy_files_missing_source_raises(tmp_path) -> None:
    """copy_files should raise FileNotFoundError if source dir is missing."""
    source_dir = tmp_path / "missing_src"
    target_dir = tmp_path / "dst3"

    with pytest.raises(FileNotFoundError):
        copy_files(source_dir, target_dir, recursive=True)

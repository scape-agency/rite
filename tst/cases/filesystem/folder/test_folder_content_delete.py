# =============================================================================
# Test: folder_content_delete
# =============================================================================

"""
Tests for rite.filesystem.folder.folder_content_delete.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem.folder.folder_content_delete import (
    delete_contents,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_delete_contents_removes_files_and_subfolders(tmp_path) -> None:
    """delete_contents should clear a folder but keep the folder itself."""
    root = tmp_path
    (root / "file1.txt").write_text("data1")
    subdir = root / "sub"
    subdir.mkdir()
    (subdir / "file2.txt").write_text("data2")

    delete_contents(root, dry_run=False, verbose=False)

    assert root.exists()
    assert root.is_dir()
    assert list(root.iterdir()) == []


def test_delete_contents_dry_run_does_not_delete(tmp_path) -> None:
    """delete_contents with dry_run must not modify the filesystem."""
    root = tmp_path
    file_path = root / "file.txt"
    file_path.write_text("content")

    delete_contents(root, dry_run=True, verbose=False)

    assert file_path.exists()


def test_delete_contents_errors_for_invalid_paths(tmp_path) -> None:
    """delete_contents should raise for missing folder or non-directory."""
    missing = tmp_path / "missing"
    with pytest.raises(FileNotFoundError):
        delete_contents(missing, dry_run=False, verbose=False)

    file_path = tmp_path / "not_a_dir.txt"
    file_path.write_text("x")
    with pytest.raises(NotADirectoryError):
        delete_contents(file_path, dry_run=False, verbose=False)


def test_delete_contents_symlink(tmp_path) -> None:
    """delete_contents should handle symlinks properly."""
    root = tmp_path
    target = root / "target"
    target.mkdir()
    symlink = root / "link"
    symlink.symlink_to(target)

    delete_contents(root, dry_run=False, verbose=False)

    assert root.exists()
    assert list(root.iterdir()) == []


def test_delete_contents_verbose_output(tmp_path, capsys) -> None:
    """delete_contents with verbose=True should print messages."""
    root = tmp_path
    (root / "file.txt").write_text("content")
    subdir = root / "sub"
    subdir.mkdir()
    (subdir / "nested.txt").write_text("data")

    delete_contents(root, dry_run=False, verbose=True)

    captured = capsys.readouterr()
    assert "Deleted" in captured.out or "🗑️" in captured.out


def test_delete_contents_empty_folder(tmp_path) -> None:
    """delete_contents should handle empty folders gracefully."""
    root = tmp_path / "empty"
    root.mkdir()

    delete_contents(root, dry_run=False, verbose=False)

    assert root.exists()
    assert list(root.iterdir()) == []


def test_delete_contents_dry_run_verbose(tmp_path, capsys) -> None:
    """delete_contents with dry_run and verbose should show what would delete."""
    root = tmp_path
    (root / "file.txt").write_text("content")

    delete_contents(root, dry_run=True, verbose=True)

    captured = capsys.readouterr()
    assert "DRY-RUN" in captured.out

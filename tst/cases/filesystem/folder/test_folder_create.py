# =============================================================================
# Test: folder_create
# =============================================================================

"""
Tests for rite.filesystem.folder.folder_create.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.filesystem.folder.folder_create import (
    create_directory,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_create_directory_with_path(tmp_path) -> None:
    """create_directory should create nested directories for Path input."""
    target = tmp_path / "a" / "b" / "c"

    assert not target.exists()

    result = create_directory(target)

    assert result == target
    assert target.exists()
    assert target.is_dir()


def test_create_directory_with_str(tmp_path) -> None:
    """create_directory should accept string paths as well."""
    target = tmp_path / "string_path"

    result = create_directory(str(target))

    assert result == target
    assert target.exists()
    assert target.is_dir()


def test_create_directory_already_exists(tmp_path) -> None:
    """create_directory should handle already existing directories."""
    target = tmp_path / "existing"
    target.mkdir()

    result = create_directory(target)

    assert result == target
    assert target.exists()


def test_create_directory_returns_path_object(tmp_path) -> None:
    """create_directory should always return a Path object."""
    result = create_directory(tmp_path / "test")

    # Import | Standard Library
    from pathlib import Path

    assert isinstance(result, Path)


def test_create_directory_with_mode(tmp_path) -> None:
    """create_directory should accept custom mode parameter."""
    target = tmp_path / "with_mode"
    result = create_directory(target, mode=0o755)

    assert result == target
    assert target.exists()


def test_create_directory_deep_nesting(tmp_path) -> None:
    """create_directory should handle deeply nested paths."""
    target = tmp_path / "a" / "b" / "c" / "d" / "e" / "f"
    result = create_directory(target)

    assert result == target
    assert target.exists()

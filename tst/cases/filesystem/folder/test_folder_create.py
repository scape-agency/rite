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

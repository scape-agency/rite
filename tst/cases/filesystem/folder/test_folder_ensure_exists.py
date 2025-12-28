# =============================================================================
# Test: folder_ensure_exists
# =============================================================================

"""
Tests for rite.filesystem.folder.folder_ensure_exists.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.filesystem.folder.folder_ensure_exists import (
    folder_ensure_exists,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_folder_ensure_exists_creates_directory(tmp_path) -> None:
    """folder_ensure_exists should create missing directories."""
    target = tmp_path / "ensure" / "nested"

    assert not target.exists()

    folder_ensure_exists(target)

    assert target.exists()
    assert target.is_dir()


def test_folder_ensure_exists_idempotent(tmp_path) -> None:
    """Calling folder_ensure_exists multiple times should be safe."""
    target = tmp_path / "again"

    folder_ensure_exists(target)
    folder_ensure_exists(target)

    assert target.exists()
    assert target.is_dir()

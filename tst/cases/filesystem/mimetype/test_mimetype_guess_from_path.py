# =============================================================================
# Test: mimetype_guess_from_path
# =============================================================================

"""
Tests for rite.filesystem.mimetype.mimetype_guess_from_path.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from pathlib import Path

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem.mimetype.mimetype_guess_from_path import (
    mimetype_guess_from_path,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_mimetype_guess_from_path(tmp_path: Path) -> None:
    """Guess mimetype and encoding from a path with extension."""
    path = tmp_path / "image.png"
    path.write_bytes(b"")

    mime, encoding = mimetype_guess_from_path(path)

    assert mime in {"image/png", "image/x-png"}
    assert encoding is None

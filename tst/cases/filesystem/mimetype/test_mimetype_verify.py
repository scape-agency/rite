# =============================================================================
# Test: mimetype_verify
# =============================================================================

"""
Tests for rite.filesystem.mimetype.mimetype_verify.
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
from rite.filesystem.mimetype.mimetype_verify import mimetype_verify

# =============================================================================
# Test Functions
# =============================================================================


def test_mimetype_verify_checks_allowed_types(tmp_path: Path) -> None:
    """Verify that allowed types list is honored for a file."""
    image = tmp_path / "image.png"
    image.write_bytes(b"")

    assert mimetype_verify(str(image), ["image/png"])
    assert not mimetype_verify(str(image), ["image/jpeg"])


def test_mimetype_verify_validates_input_type() -> None:
    """Invalid allowed_types input should raise ValueError."""
    with pytest.raises(ValueError):
        mimetype_verify("file.txt", [1, 2, 3])  # type: ignore[list-item]

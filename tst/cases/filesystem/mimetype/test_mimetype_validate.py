# =============================================================================
# Test: mimetype_validate
# =============================================================================

"""
Tests for rite.filesystem.mimetype.mimetype_validate.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import io

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem.mimetype.mimetype_validate import (
    MimeValidationError,
    validate_mimetype,
)

# =============================================================================
# Test Class: MimeValidationError
# =============================================================================


class TestMimeValidationError:
    """Tests for MimeValidationError class."""

    def test_instantiation(self) -> None:
        """Test MimeValidationError can be instantiated."""
        instance = MimeValidationError()
        assert instance is not None


# =============================================================================
# Test Functions
# =============================================================================


def test_validate_mimetype_allows_and_forbids() -> None:
    """Validate that allowed and forbidden patterns are enforced."""
    stream = io.BytesIO(b"\x89PNG\r\n\x1a\nrest")

    mime = validate_mimetype(stream, allowed=["image/*"])
    assert mime == "image/png"

    with pytest.raises(MimeValidationError):
        validate_mimetype(stream, forbidden=["image/png"])

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


def test_validate_mimetype_unknown_type() -> None:
    """Test validation fails when MIME type cannot be determined."""
    unknown_data = io.BytesIO(b"unknown data format")
    with pytest.raises(MimeValidationError, match="Could not determine"):
        validate_mimetype(unknown_data)


def test_validate_mimetype_not_in_allowed() -> None:
    """Test validation fails when MIME not in allowed list."""
    png_stream = io.BytesIO(b"\x89PNG\r\n\x1a\nrest")
    with pytest.raises(MimeValidationError, match="allowed"):
        validate_mimetype(png_stream, allowed=["application/pdf"])


def test_validate_mimetype_no_restrictions() -> None:
    """Test validation passes with no restrictions."""
    png_stream = io.BytesIO(b"\x89PNG\r\n\x1a\nrest")
    mime = validate_mimetype(png_stream)
    assert mime == "image/png"


def test_validate_mimetype_allowed_exact_match() -> None:
    """Test validation with exact MIME type in allowed list."""
    png_stream = io.BytesIO(b"\x89PNG\r\n\x1a\nrest")
    mime = validate_mimetype(png_stream, allowed=["image/png"])
    assert mime == "image/png"


def test_validate_mimetype_forbidden_wildcard() -> None:
    """Test validation with wildcard forbidden pattern."""
    png_stream = io.BytesIO(b"\x89PNG\r\n\x1a\nrest")
    with pytest.raises(MimeValidationError, match="not allowed"):
        validate_mimetype(png_stream, forbidden=["image/*"])

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
        # TODO: Implement test
        instance = MimeValidationError()
        assert instance is not None


# =============================================================================
# Test Functions
# =============================================================================


def test_validate_mimetype() -> None:
    """Test validate_mimetype() function."""
    # TODO: Implement test
    # result = validate_mimetype(test_input)
    # assert result == expected_output
    pytest.skip("Test not implemented")

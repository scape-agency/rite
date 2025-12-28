# =============================================================================
# Test: validation_is_email
# =============================================================================

"""
Tests for rite.net.validation.validation_is_email.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.net.validation.validation_is_email import (
    validation_is_email,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "email,expected",
    [
        ("user@example.com", True),
        ("test.email@domain.co.uk", True),
        ("user+tag@example.com", True),
        ("123@example.com", True),
        ("invalid.email", False),
        ("@example.com", False),
        ("user@", False),
        ("user name@example.com", False),
        ("", False),
        ("user@example", False),
        ("user@.com", False),
        ("user@@example.com", False),
    ],
)
def test_validation_is_email(email: str, expected: bool) -> None:
    """Test validation_is_email() with various email formats.

    Args:
        email: Email address to validate.
        expected: Whether email is valid.
    """
    result = validation_is_email(email)
    assert result == expected

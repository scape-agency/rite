# =============================================================================
# Test: text_is_email
# =============================================================================

"""
Tests for rite.text.validation.text_is_email.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.validation.text_is_email import (
    text_is_email,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "email,expected",
    [
        ("test@example.com", True),   # Valid email
        ("user+tag@domain.co.uk", True), # Valid with plus
        ("invalid.email", False),     # Missing @
        ("@example.com", False),      # Missing local part
        ("test@", False),             # Missing domain
        ("", False),                  # Empty
    ],
)
def test_text_is_email(email: str, expected: bool) -> None:
    """Test text_is_email() with various emails."""
    assert text_is_email(email) == expected

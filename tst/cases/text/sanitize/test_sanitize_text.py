# =============================================================================
# Test: sanitize_text
# =============================================================================

"""
Tests for rite.text.sanitize.sanitize_text.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.sanitize.sanitize_text import (
    sanitize,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_sanitize() -> None:
    """Test sanitize() function."""
    result = sanitize("hello")
    assert isinstance(result, str)
    assert len(result) > 0


def test_sanitize_with_special_chars() -> None:
    """Test sanitize removes special characters."""
    result = sanitize("Hello, World!")
    assert result == "Hello_World"


def test_sanitize_with_unicode() -> None:
    """Test sanitize handles unicode."""
    result = sanitize("Café résumé")
    assert "Cafe" in result
    assert "resume" in result


def test_sanitize_with_custom_replacement() -> None:
    """Test sanitize with custom replacement character."""
    result = sanitize("Hello World", replacement="-")
    assert result == "Hello-World"


def test_sanitize_no_replacement() -> None:
    """Test sanitize with empty replacement (line 60->67)."""
    result = sanitize("Hello World", replacement="")
    # No replacement, just removes non-alphanumeric
    assert result == "HelloWorld"


def test_sanitize_consecutive_specials() -> None:
    """Test sanitize collapses consecutive special chars."""
    result = sanitize("Hello!!!World")
    assert result == "Hello_World"

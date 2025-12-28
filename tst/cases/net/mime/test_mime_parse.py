# =============================================================================
# Test: mime_parse
# =============================================================================

"""
Tests for rite.net.mime.mime_parse.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.net.mime.mime_parse import mime_parse

# =============================================================================
# Test Functions
# =============================================================================


def test_mime_parse_basic_and_with_parameters() -> None:
    """Parse simple MIME types and ones with parameters."""
    assert mime_parse("application/json") == ("application", "json")
    assert mime_parse("text/html; charset=utf-8") == ("text", "html")


def test_mime_parse_invalid_format_raises_value_error() -> None:
    """Invalid MIME strings should raise ValueError."""
    for value in ["text", "", "invalid/too/many"]:
        try:
            mime_parse(value)
        except ValueError:
            pass
        else:  # pragma: no cover - defensive
            raise AssertionError("Expected ValueError for invalid MIME")

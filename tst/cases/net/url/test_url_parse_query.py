# =============================================================================
# Test: url_parse_query
# =============================================================================

"""
Tests for rite.net.url.url_parse_query.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.net.url.url_parse_query import (
    url_parse_query,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "query,expected",
    [
        ("a=1&b=2", {"a": ["1"], "b": ["2"]}),
        ("key=value", {"key": ["value"]}),
        ("a=1&a=2&b=3", {"a": ["1", "2"], "b": ["3"]}),
        ("", {}),
        ("name", {}),
        ("x=hello%20world", {"x": ["hello world"]}),
        ("a&b&c", {}),
    ],
)
def test_url_parse_query(query: str, expected: dict) -> None:
    """Test url_parse_query() with various query strings.

    Args:
        query: Query string to parse.
        expected: Expected parsed result.
    """
    result = url_parse_query(query)
    assert result == expected

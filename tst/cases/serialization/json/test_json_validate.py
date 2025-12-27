# =============================================================================
# Test: json_validate
# =============================================================================

"""
Tests for rite.serialization.json.json_validate.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.serialization.json.json_validate import (
    json_validate,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "json_str,expected",
    [
        ('{"key": "value"}', True),
        ('[1, 2, 3]', True),
        ('true', True),
        ('null', True),
        ('{invalid json}', False),
        ('', False),
    ],
)
def test_json_validate(json_str: str, expected: bool) -> None:
    """Test json_validate() with various JSON strings."""
    assert json_validate(json_str) == expected

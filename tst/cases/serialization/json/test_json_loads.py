# =============================================================================
# Test: json_loads
# =============================================================================

"""
Tests for rite.serialization.json.json_loads.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.serialization.json.json_loads import (
    json_loads,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "json_str,expected",
    [
        ('{"key": "value"}', {"key": "value"}),
        ('{"number": 42}', {"number": 42}),
        ('[1, 2, 3]', [1, 2, 3]),
        ('true', True),
        ('null', None),
    ],
)
def test_json_loads(json_str: str, expected) -> None:
    """Test json_loads() with various JSON strings."""
    assert json_loads(json_str) == expected

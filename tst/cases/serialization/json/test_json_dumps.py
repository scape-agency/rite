# =============================================================================
# Test: json_dumps
# =============================================================================

"""
Tests for rite.serialization.json.json_dumps.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.serialization.json.json_dumps import (
    json_dumps,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_json_dumps() -> None:
    """Test json_dumps() function."""
    # Test dict serialization
    result = json_dumps({"key": "value"})
    assert result == '{"key": "value"}'

    # Test list serialization
    result = json_dumps([1, 2, 3])
    assert result == "[1, 2, 3]"

    # Test bool serialization
    result = json_dumps(True)
    assert result == "true"

    # Test None serialization
    result = json_dumps(None)
    assert result == "null"

# =============================================================================
# Test: dict_merge
# =============================================================================

"""
Tests for rite.collections.dict.dict_merge.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.collections.dict.dict_merge import (
    dict_merge,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_dict_merge() -> None:
    """Test dict_merge() function."""
    # Test basic merge
    result = dict_merge({"a": 1, "b": 2}, {"b": 3, "c": 4})
    assert result == {"a": 1, "b": 3, "c": 4}

    # Test merging multiple dicts
    result = dict_merge({"a": 1}, {"b": 2}, {"c": 3})
    assert result == {"a": 1, "b": 2, "c": 3}

    # Test with empty dict
    result = dict_merge({"a": 1}, {})
    assert result == {"a": 1}

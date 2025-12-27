# =============================================================================
# Test: json_dump
# =============================================================================

"""
Tests for rite.serialization.json.json_dump.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.serialization.json.json_dump import (
    json_dump,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_json_dump(tmp_path) -> None:
    """Test json_dump() function."""
    # Import | Standard Library
    import json

    # Create a temporary JSON file path
    json_file = tmp_path / "output.json"

    # Test dumping
    test_data = {"key": "value", "number": 42}
    json_dump(str(json_file), test_data)

    # Verify the file was created and contains the correct data
    loaded_data = json.loads(json_file.read_text())
    assert loaded_data == test_data

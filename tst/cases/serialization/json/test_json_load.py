# =============================================================================
# Test: json_load
# =============================================================================

"""
Tests for rite.serialization.json.json_load.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.serialization.json.json_load import (
    json_load,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_json_load(tmp_path) -> None:
    """Test json_load() function."""
    # Import | Standard Library
    import json
    from pathlib import Path

    # Create a temporary JSON file
    json_file = tmp_path / "test.json"
    test_data = {"key": "value", "number": 42}
    json_file.write_text(json.dumps(test_data))

    # Test loading
    result = json_load(str(json_file))
    assert result == test_data

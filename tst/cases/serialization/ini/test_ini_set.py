# =============================================================================
# Test: ini_set
# =============================================================================

"""
Tests for rite.serialization.ini.ini_set.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.serialization.ini.ini_set import (
    ini_set,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_ini_set(tmp_path) -> None:
    """Test ini_set() function."""
    # Import | Standard Library
    import configparser

    # Create a test INI file
    ini_file = tmp_path / "test.ini"
    config = configparser.ConfigParser()
    config["section1"] = {"key1": "value1"}
    with ini_file.open("w") as f:
        config.write(f)

    # Test setting a value
    ini_set(str(ini_file), "section1", "key1", "new_value")

    # Verify the value was updated
    result_config = configparser.ConfigParser()
    result_config.read(str(ini_file))
    assert result_config["section1"]["key1"] == "new_value"

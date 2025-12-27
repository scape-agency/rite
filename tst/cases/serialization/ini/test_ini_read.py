# =============================================================================
# Test: ini_read
# =============================================================================

"""
Tests for rite.serialization.ini.ini_read.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.serialization.ini.ini_read import (
    ini_read,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_ini_read(tmp_path) -> None:
    """Test ini_read() function."""
    # Import | Standard Library
    import configparser

    # Create a test INI file
    ini_file = tmp_path / "test.ini"
    config = configparser.ConfigParser()
    config["section1"] = {"key1": "value1", "key2": "value2"}
    config["section2"] = {"key3": "value3"}
    with ini_file.open("w") as f:
        config.write(f)

    # Test reading
    result = ini_read(str(ini_file))
    assert "section1" in result
    assert result["section1"]["key1"] == "value1"
    assert "section2" in result

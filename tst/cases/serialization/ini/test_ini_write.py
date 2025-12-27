# =============================================================================
# Test: ini_write
# =============================================================================

"""
Tests for rite.serialization.ini.ini_write.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.serialization.ini.ini_write import (
    ini_write,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_ini_write(tmp_path) -> None:
    """Test ini_write() function."""
    # Import | Standard Library
    import configparser

    # Prepare data to write
    output_file = tmp_path / "output.ini"
    data = {
        "section1": {"key1": "value1", "key2": "value2"},
        "section2": {"key3": "value3"},
    }

    # Write INI file
    ini_write(str(output_file), data)

    # Verify the file was created and contains the correct data
    result_config = configparser.ConfigParser()
    result_config.read(str(output_file))
    assert result_config["section1"]["key1"] == "value1"
    assert result_config["section2"]["key3"] == "value3"

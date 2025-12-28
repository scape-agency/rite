# =============================================================================
# Test: filename_to_datestring
# =============================================================================

"""
Tests for rite.filesystem.file_name.filename_to_datestring.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem.file_name.filename_to_datestring import (
    date_format_to_regex,
    filename_to_datestring,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_date_format_to_regex() -> None:
    """Test date_format_to_regex() function."""
    # Test basic format conversion
    regex = date_format_to_regex("%Y-%m-%d")
    assert regex.match("2024-01-15") is not None
    assert (
        regex.match("2024-13-01") is not None
    )  # Regex doesn't validate date logic
    assert regex.match("24-01-15") is None

    # Test with time components
    regex = date_format_to_regex("%Y-%m-%d-%H%M%S")
    assert regex.match("2024-01-15-120530") is not None
    assert regex.match("2024-01-15-12:05:30") is None

    # Test alternative format
    regex = date_format_to_regex("%Y_%m_%d")
    assert regex.match("2024_01_15") is not None
    assert regex.match("2024-01-15") is None


def test_filename_to_datestring() -> None:
    """Test filename_to_datestring() function."""
    # Test basic extraction
    result = filename_to_datestring("backup_2024-01-15-120530.tar")
    assert result == "2024-01-15-120530"

    # Test date at different position
    result = filename_to_datestring("2024-06-30-100000_data.csv")
    assert result == "2024-06-30-100000"

    # Test with no date in filename
    result = filename_to_datestring("regular_file.txt")
    assert result is None

    # Test with custom format
    result = filename_to_datestring(
        "log_2023_12_25.txt", date_format="%Y_%m_%d"
    )
    assert result == "2023_12_25"

    # Test alternative format
    result = filename_to_datestring("2024-12-31-235959.log")
    assert result == "2024-12-31-235959"

    # Test no match with wrong format
    result = filename_to_datestring(
        "file_2024/01/15.txt", date_format="%Y-%m-%d"
    )
    assert result is None

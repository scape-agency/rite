# =============================================================================
# Test: filename_to_date
# =============================================================================

"""
Tests for rite.filesystem.file_name.filename_to_date.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem.file_name.filename_to_date import (
    filename_to_date,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_filename_to_date() -> None:
    """Test filename_to_date() function."""
    # Test basic date extraction
    result = filename_to_date("backup_2024-01-15-120530.tar")
    assert result is not None
    assert result.year == 2024
    assert result.month == 1
    assert result.day == 15

    # Test with different format
    result = filename_to_date("log_2023-12-25-235959.log")
    assert result is not None
    assert result.year == 2023
    assert result.month == 12

    # Test with no date in filename
    result = filename_to_date("regular_file.txt")
    assert result is None

    # Test with custom date format
    result = filename_to_date("2024_01_15.txt", date_format="%Y_%m_%d")
    assert result is not None
    assert result.year == 2024

    # Test date at different positions in filename
    result = filename_to_date("2024-06-30-100000_data.csv")
    assert result is not None
    assert result.month == 6
    assert result.day == 30

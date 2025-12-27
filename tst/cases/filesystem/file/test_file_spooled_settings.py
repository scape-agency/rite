# =============================================================================
# Test: file_spooled_settings
# =============================================================================

"""
Tests for rite.filesystem.file.file_spooled_settings.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import pytest

# Import | Local Modules
from rite.filesystem.file.file_spooled_settings import (
    SpooledFileSettings,
)


# =============================================================================
# Test Class: SpooledFileSettings
# =============================================================================


class TestSpooledFileSettings:
    """Tests for SpooledFileSettings class."""

    def test_instantiation(self) -> None:
        """Test SpooledFileSettings can be instantiated."""
        # TODO: Implement test
        instance = SpooledFileSettings()
        assert instance is not None


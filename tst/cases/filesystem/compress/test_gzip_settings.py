# =============================================================================
# Test: gzip_settings
# =============================================================================

"""
Tests for rite.filesystem.compress.gzip_settings.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem.compress.gzip_settings import (
    GzipCompressionSettings,
)

# =============================================================================
# Test Class: GzipCompressionSettings
# =============================================================================


class TestGzipCompressionSettings:
    """Tests for GzipCompressionSettings class."""

    def test_instantiation(self) -> None:
        """Test GzipCompressionSettings can be instantiated."""
        # TODO: Implement test
        instance = GzipCompressionSettings()
        assert instance is not None

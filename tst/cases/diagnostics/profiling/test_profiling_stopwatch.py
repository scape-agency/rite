# =============================================================================
# Test: profiling_stopwatch
# =============================================================================

"""
Tests for rite.diagnostics.profiling.profiling_stopwatch.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import pytest

# Import | Local Modules
from rite.diagnostics.profiling.profiling_stopwatch import (
    profiling_stopwatch,
)


# =============================================================================
# Test Class: profiling_stopwatch
# =============================================================================


class Testprofiling_stopwatch:
    """Tests for profiling_stopwatch class."""

    def test_instantiation(self) -> None:
        """Test profiling_stopwatch can be instantiated."""
        # TODO: Implement test
        instance = profiling_stopwatch()
        assert instance is not None


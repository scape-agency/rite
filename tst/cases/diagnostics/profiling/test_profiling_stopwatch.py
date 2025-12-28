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

# Import | Libraries
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

    def test_instantiation_with_name(self) -> None:
        """Test profiling_stopwatch instantiation with custom name."""
        instance = profiling_stopwatch("my_operation")
        assert instance.name == "my_operation"
        assert instance.elapsed == 0.0
        assert instance.start_time == 0.0
        assert instance.end_time == 0.0

    def test_context_manager(self) -> None:
        """Test profiling_stopwatch as context manager."""
        # Import | Standard Library
        import time

        with profiling_stopwatch("test") as sw:
            time.sleep(0.01)

        assert sw.elapsed > 0.0
        assert sw.start_time > 0.0
        assert sw.end_time > sw.start_time

    def test_string_representation(self) -> None:
        """Test profiling_stopwatch __str__ method."""
        instance = profiling_stopwatch("operation")
        instance.elapsed = 1.234567
        result = str(instance)
        assert "operation" in result
        assert "1.234567" in result
        assert "seconds" in result

    def test_elapsed_calculation(self) -> None:
        """Test that elapsed time is correctly calculated."""
        # Import | Standard Library
        import time

        with profiling_stopwatch("calc_test") as sw:
            time.sleep(0.02)

        assert sw.elapsed >= 0.01
        assert sw.end_time >= sw.start_time

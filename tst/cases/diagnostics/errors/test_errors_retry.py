# =============================================================================
# Test: errors_retry
# =============================================================================

"""
Tests for rite.diagnostics.errors.errors_retry.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.diagnostics.errors.errors_retry import (
    errors_retry,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_errors_retry() -> None:
    """Test errors_retry() decorator."""
    # Import | Standard Library
    import time

    # Test successful call without retry
    call_count = 0

    @errors_retry(max_attempts=3, delay=0.01)
    def success() -> str:
        nonlocal call_count
        call_count += 1
        return "success"

    result = success()
    assert result == "success"
    assert call_count == 1

    # Test retry on failure then success
    attempt_count = 0

    @errors_retry(max_attempts=3, delay=0.01)
    def flaky() -> str:
        nonlocal attempt_count
        attempt_count += 1
        if attempt_count < 3:
            raise ValueError("fail")
        return "success"

    result = flaky()
    assert result == "success"
    assert attempt_count == 3

    # Test max attempts exceeded
    @errors_retry(max_attempts=2, delay=0.01)
    def always_fails() -> None:
        raise RuntimeError("always fails")

    with pytest.raises(RuntimeError):
        always_fails()

    # Test specific exception catching
    @errors_retry(max_attempts=3, delay=0.01, exceptions=(ValueError,))
    def fails_with_type_error() -> None:
        raise TypeError("not caught")

    with pytest.raises(TypeError):
        fails_with_type_error()

    # Test backoff multiplier
    timings = []

    @errors_retry(max_attempts=3, delay=0.01, backoff=2.0)
    def track_delays() -> None:
        timings.append(time.time())
        if len(timings) < 3:
            raise ValueError("fail")

    track_delays()
    assert len(timings) == 3

    # Test catching multiple exceptions
    @errors_retry(
        max_attempts=2, delay=0.01, exceptions=(ValueError, KeyError)
    )
    def multi_exception() -> str:
        raise KeyError("test")

    with pytest.raises(KeyError):
        multi_exception()

    # Test with no exceptions (default)
    @errors_retry(max_attempts=2, delay=0.01)
    def default_exception() -> None:
        raise RuntimeError("caught")

    with pytest.raises(RuntimeError):
        default_exception()

# =============================================================================
# Test: errors_get_chain
# =============================================================================

"""
Tests for rite.diagnostics.errors.errors_get_chain.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.diagnostics.errors.errors_get_chain import (
    errors_get_chain,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_errors_get_chain_single() -> None:
    """Test errors_get_chain with single exception."""
    try:
        raise ValueError("test error")
    except ValueError as e:
        chain = errors_get_chain(e)
        assert len(chain) == 1
        assert isinstance(chain[0], ValueError)


def test_errors_get_chain_with_cause() -> None:
    """Test errors_get_chain with exception cause."""
    try:
        try:
            raise ValueError("root")
        except ValueError as e:
            raise KeyError("wrapped") from e
    except KeyError as e:
        chain = errors_get_chain(e)
        assert len(chain) == 2
        assert isinstance(chain[0], ValueError)
        assert isinstance(chain[1], KeyError)


def test_errors_get_chain_with_context() -> None:
    """Test errors_get_chain with exception context."""
    try:
        try:
            _ = 1 / 0
        except ZeroDivisionError as exc:
            raise ValueError("wrapped") from exc
    except ValueError as e:
        chain = errors_get_chain(e)
        assert len(chain) >= 1
        assert isinstance(chain[-1], ValueError)

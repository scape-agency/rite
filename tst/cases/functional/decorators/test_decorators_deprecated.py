# =============================================================================
# Test: decorators_deprecated
# =============================================================================

"""
Tests for rite.functional.decorators.decorators_deprecated.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.functional.decorators.decorators_deprecated import (
    decorators_deprecated,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_decorators_deprecated() -> None:
    """decorators_deprecated should emit a DeprecationWarning."""

    @decorators_deprecated("Use new_func instead")
    def old_func() -> str:
        return "old"

    with pytest.warns(DeprecationWarning):
        assert old_func() == "old"

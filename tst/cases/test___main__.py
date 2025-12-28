# =============================================================================
# Test: __main__
# =============================================================================

"""
Tests for rite.__main__.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.__main__ import (
    main,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_main() -> None:
    """Test main() function."""
    import io
    import sys

    # Capture output
    captured_output = io.StringIO()
    sys.stdout = captured_output

    main()

    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()

    # Check that main output is printed
    assert "rite is set!" in output
    assert "rite:" in output
    assert "Python:" in output

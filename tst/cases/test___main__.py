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

# Import | Local Modules
from rite.__main__ import (
    main,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_main(monkeypatch, capsys) -> None:
    """Test main() function."""
    # Import | Standard Library
    import sys

    # Mock sys.argv to provide the 'info' command
    monkeypatch.setattr(sys, "argv", ["rite", "info"])

    # Call main
    result = main()

    # Verify it returned successfully
    assert result == 0

    # Check output contains version info
    captured = capsys.readouterr()
    assert "rite v" in captured.out
    assert "collections" in captured.out
    assert "https://www.pyrites.dev" in captured.out

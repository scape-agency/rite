# =============================================================================
# Test: mime_guess_extension
# =============================================================================

"""
Tests for rite.net.mime.mime_guess_extension.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.net.mime.mime_guess_extension import mime_guess_extension

# =============================================================================
# Test Functions
# =============================================================================


def test_mime_guess_extension_known_and_unknown() -> None:
    """Guess extension for known and unknown MIME types."""
    assert mime_guess_extension("application/json") == ".json"
    assert mime_guess_extension("image/png") in {".png", ".png"}
    assert mime_guess_extension("unknown/type") is None

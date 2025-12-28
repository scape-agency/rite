# =============================================================================
# Test: mime_guess_type
# =============================================================================

"""
Tests for rite.net.mime.mime_guess_type.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.net.mime.mime_guess_type import mime_guess_type

# =============================================================================
# Test Functions
# =============================================================================


def test_mime_guess_type_known_and_unknown() -> None:
    """Guess type for known extensions and return None for unknown."""
    assert mime_guess_type("file.json") == "application/json"
    assert mime_guess_type("image.png") in {"image/png", "image/x-png"}
    # Use an unlikely extension so mimetypes has no mapping
    assert mime_guess_type("file.unknownext") is None

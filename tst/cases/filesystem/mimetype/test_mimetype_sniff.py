# =============================================================================
# Test: mimetype_sniff
# =============================================================================

"""
Tests for rite.filesystem.mimetype.mimetype_sniff.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.filesystem.mimetype.mimetype_sniff import mimetype_sniff

# =============================================================================
# Test Functions
# =============================================================================


def test_mimetype_sniff_common_signatures() -> None:
    """Test that common magic numbers are detected correctly."""
    assert mimetype_sniff(b"\x89PNG\r\n\x1a\nrest") == "image/png"
    assert mimetype_sniff(b"\xff\xd8\xffrest") == "image/jpeg"
    assert mimetype_sniff(b"GIF89arest") == "image/gif"
    assert mimetype_sniff(b"%PDF-rest") == "application/pdf"
    assert mimetype_sniff(b"PK\x03\x04rest") == "application/zip"
    assert mimetype_sniff(b"\x1f\x8b\x08rest") == "application/gzip"

from __future__ import annotations

from rite.filesystem.mimetype.mimetype_match import mimetype_match


def test_mimetype_match_exact_and_wildcard() -> None:
    assert mimetype_match("image/png", "image/png")
    assert mimetype_match("image/jpeg", "image/*")
    assert not mimetype_match("text/plain", "image/*")

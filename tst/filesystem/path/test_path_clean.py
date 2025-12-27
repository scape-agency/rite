from __future__ import annotations

from rite.filesystem import path_clean


def test_path_clean_normalizes_leading_and_trailing_slashes() -> None:
    assert path_clean("//a/b//") == "/a/b"
    assert path_clean("a/b") == "/a/b"
    assert path_clean("/a/b") == "/a/b"

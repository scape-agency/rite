from __future__ import annotations

from rite.filesystem import extension_normalize


def test_extension_normalize_various_inputs() -> None:
    assert extension_normalize(".JPG") == "jpg"
    assert extension_normalize(" PDF ", leading_dot=True) == ".pdf"
    assert extension_normalize("   ") is None

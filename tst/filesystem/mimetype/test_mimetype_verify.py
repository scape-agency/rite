from __future__ import annotations

import pytest

from rite.filesystem.mimetype.mimetype_verify import mimetype_verify


def test_mimetype_verify_checks_allowed_types(tmp_path) -> None:
    image = tmp_path / "image.png"
    image.write_bytes(b"")

    assert mimetype_verify(str(image), ["image/png"])
    assert not mimetype_verify(str(image), ["image/jpeg"])


def test_mimetype_verify_validates_input_type() -> None:
    with pytest.raises(ValueError):
        mimetype_verify("file.txt", [1, 2, 3])  # type: ignore[list-item]

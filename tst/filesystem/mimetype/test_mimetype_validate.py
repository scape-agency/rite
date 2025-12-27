from __future__ import annotations

import io

import pytest

from rite.filesystem.mimetype.mimetype_validate import (
    MimeValidationError,
    validate_mimetype,
)


def test_validate_mimetype_allows_and_forbids() -> None:
    stream = io.BytesIO(b"\x89PNG\r\n\x1a\nrest")

    mime = validate_mimetype(stream, allowed=["image/*"])
    assert mime == "image/png"

    with pytest.raises(MimeValidationError):
        validate_mimetype(stream, forbidden=["image/png"])

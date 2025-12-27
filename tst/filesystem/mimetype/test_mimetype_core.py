from __future__ import annotations

import io
import sys
import types
from pathlib import Path

import pytest

from rite.filesystem.mimetype.mimetype_guess import mimetype_guess
from rite.filesystem.mimetype.mimetype_guess_from_path import (
    mimetype_guess_from_path,
)
from rite.filesystem.mimetype.mimetype_match import (
    mimetype_match as simple_match,
)
from rite.filesystem.mimetype.mimetype_read_head_bytes import read_head_bytes
from rite.filesystem.mimetype.mimetype_sniff import mimetype_sniff
from rite.filesystem.mimetype.mimetype_validate import (
    MimeValidationError,
    mimetype_match,
    validate_mimetype,
)
from rite.filesystem.mimetype.mimetype_verify import mimetype_verify


def _make_png_bytes() -> bytes:
    return b"\x89PNG\r\n\x1a\n" + b"rest-of-png"  # minimal PNG header


def _make_pdf_bytes() -> bytes:
    return b"%PDF-1.4" + b" rest"  # minimal PDF marker


def test_mimetype_sniff_common_types() -> None:
    assert mimetype_sniff(_make_png_bytes()) == "image/png"
    assert mimetype_sniff(_make_pdf_bytes()) == "application/pdf"
    assert mimetype_sniff(b"") is None


def test_mimetype_guess_from_path() -> None:
    mime, encoding = mimetype_guess_from_path("example.png")
    assert mime == "image/png"
    assert encoding is None


def test_mimetype_guess_from_bytes_and_uploaded_like() -> None:
    png_bytes = _make_png_bytes()

    # Bytes-like input uses sniffing
    assert mimetype_guess(png_bytes) == "image/png"

    # Uploaded-like object honours explicit content_type
    class UploadedLike:
        def __init__(self) -> None:
            self.name = "file.bin"
            self.content_type = "IMAGE/PNG"

    uploaded = UploadedLike()
    assert mimetype_guess(uploaded) == "image/png"


def test_read_head_bytes_variants(tmp_path: Path) -> None:
    # Bytes-like
    data = b"1234567890"
    assert read_head_bytes(data, 4) == b"1234"

    # Path-like
    path = tmp_path / "data.bin"
    path.write_bytes(data)
    assert read_head_bytes(str(path), 4) == b"1234"

    # File-like with seek/tell
    stream = io.BytesIO(data)
    head = read_head_bytes(stream, 5)
    assert head == b"12345"
    # Position restored
    assert stream.read() == data

    # Non-seekable, non-peek stream returns None
    class NonSeekable:
        def read(self, _n: int) -> bytes:  # pragma: no cover - behavior only
            return b"ignored"

    assert read_head_bytes(NonSeekable(), 4) is None


def test_mimetype_match_modules() -> None:
    # Simple matcher module
    assert simple_match("image/png", "image/png")
    assert simple_match("image/png", "image/*")
    assert not simple_match("text/plain", "image/*")

    # Rich matcher inside validate module
    assert mimetype_match("image/png", "image/*")
    assert mimetype_match("image/png", "image/png")
    assert not mimetype_match("image/png", "text/*")


def test_validate_mimetype_allowed_and_forbidden() -> None:
    png_bytes = _make_png_bytes()

    # Allowed wildcard
    mime = validate_mimetype(png_bytes, allowed=["image/*"])
    assert mime == "image/png"

    # Forbidden specific type
    with pytest.raises(MimeValidationError):
        validate_mimetype(_make_pdf_bytes(), forbidden=["application/pdf"])

    # Unknown type raises
    class Unknown:
        pass

    with pytest.raises(MimeValidationError):
        validate_mimetype(Unknown())


def test_mimetype_verify_with_django_stub(tmp_path: Path) -> None:
    # Provide a lightweight stub for django.utils.translation.gettext_lazy
    django_mod = types.ModuleType("django")
    utils_mod = types.ModuleType("django.utils")
    translation_mod = types.ModuleType("django.utils.translation")

    def gettext_lazy(message: str) -> str:  # pragma: no cover - trivial
        return message

    translation_mod.gettext_lazy = gettext_lazy
    sys.modules.setdefault("django", django_mod)
    sys.modules.setdefault("django.utils", utils_mod)
    sys.modules["django.utils.translation"] = translation_mod

    from importlib import reload

    # Reload module so it picks up the stub
    import rite.filesystem.mimetype.mimetype_verify as verify_module

    reload(verify_module)

    file_path = tmp_path / "image.jpg"
    file_path.write_bytes(b"data")

    assert verify_module.mimetype_verify(str(file_path), ["image/jpeg"])
    assert not verify_module.mimetype_verify(str(file_path), ["image/png"])

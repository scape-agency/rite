# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
MIME Type Guessing Utility
===========================================

Best-effort MIME type detection for heterogeneous inputs. Supports:
- UploadedFile-like objects (honors explicit `content_type` if present)
- File-like objects (reads non-destructive head bytes)
- Bytes-like payloads
- Filenames, paths, and URLs (extension-based guess)

Provides a simple `mimetype_guess()` routine with an optional
`prefer_sniff` mode to prioritize byte-sniffing over extension guessing.
Returns a lowercase MIME string like "image/png", or `None` when unknown.
"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

import mimetypes
import os
from typing import Optional
from urllib.parse import urlsplit

# Import | Local Modules
from .mimetype_sniff import mimetype_sniff


def read_head_bytes(obj: object, n: int) -> bytes:
    """Read up to *n* bytes from a variety of inputs non-destructively.

    Supports bytes-like objects and file-like objects. For streams, the
    original position is restored when possible.
    """

    if isinstance(obj, (bytes, bytearray, memoryview)):
        return bytes(obj[:n])

    # File-like objects with ``read`` (optionally ``tell``/``seek``)
    if hasattr(obj, "read"):
        stream = obj  # type: ignore[assignment]
        try:
            current_position = stream.tell()
        except (AttributeError, OSError):  # pragma: no cover - very uncommon
            current_position = None

        data = stream.read(n)

        if current_position is not None:
            try:
                stream.seek(current_position)
            except (AttributeError, OSError):  # pragma: no cover
                pass

        return data or b""

    return b""


def mimetype_guess(
    input_object: object,
    *,
    prefer_sniff: bool = False,
    max_bytes: int = 8192,
) -> Optional[str]:
    """
    Best-effort MIME detection for:
      - UploadedFile-like objects (uses `.content_type` if present)
      - File-like objects (reads head bytes non-destructively)
      - Bytes-like objects
      - Strings / PathLike (filenames or URLs)

    Order (default):
      1) explicit `.content_type` if present
      2) guess from name/path (extension)
      3) sniff head bytes

    If `prefer_sniff=True`:
      1) explicit `.content_type`
      2) sniff head bytes
      3) guess from name/path

    Returns a lowercase MIME string like "image/png", or `None` if unknown.
    """
    # 0) explicit content_type wins
    content_type = getattr(input_object, "content_type", None)
    if content_type:
        return str(content_type).lower()

    def _from_name(candidate_object: object) -> Optional[str]:
        # Accept:
        #  - UploadedFile-ish: has `.name`
        #  - plain strings / URLs
        #  - os.PathLike
        name = getattr(candidate_object, "name", None)
        if isinstance(candidate_object, (str, os.PathLike)):
            name = os.fspath(candidate_object)

        if not isinstance(name, str) or not name:
            return None

        # If it's a URL, only use the path part for extension-based guessing
        try:
            parts = urlsplit(name)
            path = parts.path or name
        except ValueError:
            path = name

        mime, _enc = mimetypes.guess_type(path)
        return mime.lower() if mime else None

    def _from_bytes(candidate_object: object) -> Optional[str]:
        head = read_head_bytes(candidate_object, n=max_bytes)
        if not head:
            return None
        sniffed = mimetype_sniff(head)
        return sniffed.lower() if sniffed else None

    if prefer_sniff:
        # content_type already checked
        return _from_bytes(input_object) or _from_name(input_object)
    else:
        return _from_name(input_object) or _from_bytes(input_object)


# =============================================================================
# Exports
# =============================================================================

__all__: list[str] = ["mimetype_guess"]

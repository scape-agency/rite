# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

""" """


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

from typing import Any, Iterable, Optional

# Import | Local Modules
from .mimetype_guess import mimetype_guess


class MimeValidationError(ValueError):
    """Raised when a value does not satisfy MIME type constraints."""


def mimetype_match(mime: str, pattern: str) -> bool:
    """Return True if *mime* matches a simple MIME ``pattern``.

    The pattern may contain wildcards in the subtype, such as ``"image/*"``.
    """

    try:
        mime_type, mime_subtype = mime.split("/", 1)
        pattern_type, pattern_subtype = pattern.split("/", 1)
    except ValueError:
        return mime == pattern

    type_matches = pattern_type in {"*", mime_type}
    subtype_matches = pattern_subtype in {"*", mime_subtype}
    return type_matches and subtype_matches


def validate_mimetype(
    input_object: Any,
    *,
    allowed: Optional[Iterable[str]] = None,
    forbidden: Optional[Iterable[str]] = None,
) -> str:
    """
    Validate MIME type of ``input_object`` without any Django dependency.

    Returns the detected MIME string on success.
    Raises MimeValidationError on failure.
    """
    mime = mimetype_guess(input_object)
    if not mime:
        raise MimeValidationError("Could not determine MIME type.")

    if forbidden:
        for pattern in forbidden:
            if mimetype_match(mime, str(pattern)):
                raise MimeValidationError(
                    f"Files of type '{mime}' are not allowed."
                )

    if allowed:
        for pattern in allowed:
            if mimetype_match(mime, str(pattern)):
                break
        else:
            allowed_list = ", ".join(map(str, allowed))
            raise MimeValidationError(
                f"Only the following types are allowed: {allowed_list}."
            )

    return mime


# =============================================================================
# Exports
# =============================================================================

__all__: list[str] = ["validate_mimetype"]

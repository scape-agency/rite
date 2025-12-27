# -*- coding: utf-8 -*-
from __future__ import annotations
import secrets
import string

def random_alphanumeric(length: int = 16, include_lowercase: bool = True, include_uppercase: bool = True) -> str:
    """Generate a random alphanumeric string."""
    charset = string.digits
    if include_lowercase:
        charset += string.ascii_lowercase
    if include_uppercase:
        charset += string.ascii_uppercase
    if charset == string.digits:
        raise ValueError("At least one of include_lowercase or include_uppercase must be True")
    return "".join(secrets.choice(charset) for _ in range(length))


# =============================================================================
# Module Exports
# =============================================================================

__all__: list[str] = [
    "random_alphanumeric",
]

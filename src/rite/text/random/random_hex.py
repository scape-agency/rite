# -*- coding: utf-8 -*-
from __future__ import annotations
import secrets

def random_hex(length: int = 16, uppercase: bool = False) -> str:
    """Generate a random hexadecimal string."""
    charset = "0123456789ABCDEF" if uppercase else "0123456789abcdef"
    return "".join(secrets.choice(charset) for _ in range(length))


# =============================================================================
# Module Exports
# =============================================================================

__all__: list[str] = [
    "random_hex",
]

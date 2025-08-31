from __future__ import annotations

from typing import List, Optional


def convert_string_to_int(val: str) -> Optional[int]:
    """
    Convert a string representation of an integer value to an integer.
    """

    val = (val or "").strip()

    if val == "":
        return None

    try:
        return int(val)

    except ValueError:
        return None

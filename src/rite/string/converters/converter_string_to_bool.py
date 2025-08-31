from __future__ import annotations

from typing import List, Optional


def string_to_bool_converter(val: str) -> Optional[bool]:
    """
    Convert a string representation of a boolean value to a boolean.
    """

    if val is None:
        return None

    v: str = val.strip().lower()

    if v in {
        "t",
        "true",
        "1",
        "yes",
        "y",
        "ja",
        "oui",
        "si",
    }:
        return True

    if v in {
        "f",
        "false",
        "0",
        "no",
        "n",
        "nee",
        "nein",
        "non",
    }:
        return False

    return None

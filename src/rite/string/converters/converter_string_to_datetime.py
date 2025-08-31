from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, Optional, Tuple

from django.utils.dateparse import parse_datetime
from django.utils.timezone import get_current_timezone, is_naive, make_aware


def convert_string_to_datetime(value: Optional[str]) -> Optional[datetime]:
    """
    Convert a string to a timezone-aware datetime object.

    Parse a timestamp like '2024-12-11 11:42:34.049271+00' or ISO-ish strings.
    Returns None on blank/invalid.

    Supports ISO 8601 format, optionally naive or UTC.

    Returns:
        datetime object or None
    """
    if not value or value.strip() == "":
        return None

    dt = parse_datetime(value)
    if not dt:
        return None

    if is_naive(dt):
        # Use current timezone, or utc fallback
        tz = get_current_timezone()
        return make_aware(dt, timezone=tz)
    return dt


# from datetime import datetime
# from typing import Any, Dict, Optional, Tuple


# def convert_string_to_datetime(value: Optional[str]) -> Optional[datetime]:
#     """
#     Parse a timestamp like '2024-12-11 11:42:34.049271+00' or ISO-ish strings.
#     Returns None on blank/invalid.
#     """
#     if not value:
#         return None
#     s = str(value).strip()
#     if not s or s.lower() in {"none", "null"}:
#         return None
#     # Normalize space→T so fromisoformat() accepts it with offset
#     s = s.replace(" ", "T", 1) if " " in s and "T" not in s else s
#     try:
#         return datetime.fromisoformat(s)
#     except ValueError:
#         return None

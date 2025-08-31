from decimal import Decimal, InvalidOperation
from typing import Any, Dict, Optional, Tuple


def convert_string_to_decimal(
    value: Optional[str],
    length: int = 3,
) -> Optional[Decimal]:
    """
    Convert a string to a Decimal, quantized to `length` decimal places.

    Args:
        value: The input string (or None).
        length: Number of decimal places to quantize to. Default is 3.

    Returns:
        Decimal quantized to `length` places, or None if conversion fails.
    """
    if value is None:
        return None

    s = str(value).strip()
    if s == "" or s.lower() in {"none", "null"}:
        return None

    try:
        d = Decimal(s)

        if length <= 0:
            quant = Decimal("1")  # no fractional part
        else:
            quant = Decimal("1").scaleb(-length)  # e.g., -3 → 0.001

        return d.quantize(quant)

    except (InvalidOperation, ValueError):
        return None

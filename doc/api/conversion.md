# Conversion Module

The `rite.conversion` module provides type conversion and format transformation utilities.

## Overview

This section gives a conceptual overview of the conversion helpers.
Individual submodules provide the full reference documentation.

## Submodules

- [Types](conversion/types.md): Convert between Python types.
- [Formats](conversion/formats.md): Convert between data formats.
- [Units](conversion/units.md): Convert between units of measurement.

## Examples

```python
from rite.conversion import (
    types_to_int,
    formats_base64_encode,
    units_temperature
)

# Type conversion
num = types_to_int("42")  # 42

# Format conversion
encoded = formats_base64_encode(b"data")

# Unit conversion
fahrenheit = units_temperature(100, "celsius", "fahrenheit")
```

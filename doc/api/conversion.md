# Conversion Module

The `rite.conversion` module provides type conversion and format transformation utilities.

## Overview

::: rite.conversion
options:
show_root_heading: true
show_source: false
heading_level: 2

## Submodules

### Type Conversions

Convert between Python types.

::: rite.conversion.types
options:
members: - types_to_int - types_to_float - types_to_str - types_to_bool - types_to_list - types_to_dict - types_to_bytes
show_source: false
heading_level: 3

### Format Conversions

Convert between data formats.

::: rite.conversion.formats
options:
members: - formats_base64_encode - formats_base64_decode - formats_hex_encode - formats_hex_decode - formats_url_encode - formats_url_decode - formats_json_encode - formats_json_decode
show_source: false
heading_level: 3

### Unit Conversions

Convert between units of measurement.

::: rite.conversion.units
options:
members: - units_temperature - units_length - units_weight - units_time
show_source: false
heading_level: 3

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

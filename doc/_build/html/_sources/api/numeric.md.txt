# Numeric Module

The `rite.numeric` module provides numerical operations, mathematical utilities, and statistics.

## Overview

::: rite.numeric
    options:
      show_root_heading: true
      show_source: false
      heading_level: 2

## Submodules

### Math

Basic mathematical operations.

::: rite.numeric.math
    options:
      members:
        - math_abs
        - math_clamp
        - math_sign
        - math_pow
      show_source: false
      heading_level: 3

### Rounding

Number rounding utilities.

::: rite.numeric.rounding
    options:
      members:
        - rounding_round
        - rounding_ceil
        - rounding_floor
        - rounding_trunc
      show_source: false
      heading_level: 3

### Statistics

Statistical calculations.

::: rite.numeric.statistics
    options:
      members:
        - statistics_mean
        - statistics_median
        - statistics_sum
        - statistics_min_max
      show_source: false
      heading_level: 3

### Range

Range operations.

::: rite.numeric.range
    options:
      members:
        - range_in_range
        - range_normalize
        - range_scale
      show_source: false
      heading_level: 3

## Examples

```python
from rite.numeric import (
    math_clamp,
    rounding_round,
    statistics_mean
)

# Clamp value
clamped = math_clamp(150, 0, 100)  # 100

# Round number
rounded = rounding_round(3.14159, 2)  # 3.14

# Calculate mean
avg = statistics_mean([1, 2, 3, 4, 5])  # 3.0
```

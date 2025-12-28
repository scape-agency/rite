# Numeric Module

The `rite.numeric` module provides numerical operations, mathematical utilities, and statistics.

## Overview

This section introduces the numeric utilities conceptually. Detailed
APIs for each area are covered on the submodule pages.

## Submodules

- [Math](numeric/math.md): Basic mathematical operations.
- [Rounding](numeric/rounding.md): Number rounding utilities.
- [Statistics](numeric/statistics.md): Statistical calculations.
- [Range](numeric/range.md): Range operations.

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

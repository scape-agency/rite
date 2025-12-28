# Functional Module

The `rite.functional` module provides functional programming utilities including composition, currying, and decorators.

## Overview

This section introduces the functional programming helpers at a high
level. Each submodule has its own page with full API details.

## Submodules

- [Composition](functional/composition.md): Function composition utilities.
- [Currying](functional/currying.md): Currying and partial application.
- [Decorators](functional/decorators.md): Common decorators.
- [Memoization](functional/memoization.md): Function result caching.

## Examples

```python
from rite.functional import (
    composition_compose,
    decorators_debounce,
    memoization_memoize
)

# Compose functions
add_one = lambda x: x + 1
double = lambda x: x * 2
composed = composition_compose(add_one, double)
result = composed(5)  # (5 * 2) + 1 = 11

# Debounce function
@decorators_debounce(seconds=1.0)
def on_input_change(value):
    print(f"Processing: {value}")

# Memoize expensive function
@memoization_memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

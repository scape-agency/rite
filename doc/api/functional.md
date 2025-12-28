# Functional Module

The `rite.functional` module provides functional programming utilities including composition, currying, and decorators.

## Overview

::: rite.functional
options:
show_root_heading: true
show_source: false
heading_level: 2

## Submodules

### Composition

Function composition utilities.

::: rite.functional.composition
options:
members: - composition_compose - composition_pipe - composition_chain
show_source: false
heading_level: 3

### Currying

Function currying and partial application.

::: rite.functional.currying
options:
members: - currying_curry - currying_uncurry
show_source: false
heading_level: 3

### Decorators

Useful decorators.

::: rite.functional.decorators
options:
members: - decorators_debounce - decorators_throttle - decorators_once - decorators_deprecated
show_source: false
heading_level: 3

### Memoization

Function result caching.

::: rite.functional.memoization
options:
members: - memoization_memoize - memoization_lru_cache
show_source: false
heading_level: 3

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

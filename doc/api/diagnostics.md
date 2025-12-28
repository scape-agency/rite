# Diagnostics Module

The `rite.diagnostics` module provides logging, profiling, error handling, and debugging utilities.

## Overview

This section gives a high-level overview of the diagnostics helpers.
Detailed APIs are documented on the submodule pages.

## Submodules

- [Logging](diagnostics/logging.md): Structured logging utilities.
- [Profiling](diagnostics/profiling.md): Performance profiling tools.
- [Error Handling](diagnostics/errors.md): Error management utilities.
- [Metrics](diagnostics/metrics.md): Application metrics collection.

## Examples

```python
from rite.diagnostics import (
    profiling_timer,
    errors_retry,
    metrics_counter
)

# Time function execution
@profiling_timer
def slow_function():
    # ... code ...
    pass

# Retry on failure
@errors_retry(max_attempts=3)
def unstable_operation():
    # ... code ...
    pass

# Count metrics
counter = metrics_counter("requests")
counter.increment()
```

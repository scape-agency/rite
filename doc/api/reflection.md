# Reflection Module

The `rite.reflection` module provides runtime introspection, dynamic
loading, and reflection utilities.

## Overview

This section gives a conceptual overview of the reflection helpers.
Detailed APIs live on the submodule pages.

## Submodules

- [Importing](reflection/importing.md): Dynamic import utilities.
- [Inspection](reflection/inspection.md): Introspection helpers for
  objects and modules.
- [Attributes](reflection/attributes.md): Attribute access helpers.
- [Signature](reflection/signature.md): Function and method signature
  utilities.

## Examples

```python
from rite.reflection import (
    importing_load_class,
    inspection_get_methods,
    signature_get_parameters,
)

# Load class dynamically
MyClass = importing_load_class("mypackage.mymodule.MyClass")

# Inspect methods
methods = inspection_get_methods(MyClass)

# Get function parameters
def example(a: int, b: str = "default") -> None:
    pass

params = signature_get_parameters(example)
```

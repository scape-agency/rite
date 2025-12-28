# Reflection Module

The `rite.reflection` module provides runtime introspection, dynamic loading, and reflection utilities.

## Overview

::: rite.reflection
options:
show_root_heading: true
show_source: false
heading_level: 2

## Submodules

### Importing

Dynamic module and class loading.

::: rite.reflection.importing
options:
members: - importing_load_module - importing_load_class - importing_load_function
show_source: false
heading_level: 3

### Inspection

Inspect Python objects at runtime.

::: rite.reflection.inspection
options:
members: - inspection_get_members - inspection_get_methods - inspection_get_functions - inspection_get_source
show_source: false
heading_level: 3

### Attributes

Attribute access and manipulation.

::: rite.reflection.attributes
options:
members: - attributes_get_attr - attributes_set_attr - attributes_has_attr - attributes_del_attr
show_source: false
heading_level: 3

### Signature

Function signature inspection.

::: rite.reflection.signature
options:
members: - signature_get_signature - signature_get_parameters - signature_get_return_annotation
show_source: false
heading_level: 3

## Examples

```python
from rite.reflection import (
    importing_load_class,
    inspection_get_methods,
    signature_get_parameters
)

# Load class dynamically
MyClass = importing_load_class("mypackage.mymodule.MyClass")

# Inspect methods
methods = inspection_get_methods(MyClass)

# Get function parameters
def example(a: int, b: str = "default"):
    pass

params = signature_get_parameters(example)
```

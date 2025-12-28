# Net Module

The `rite.net` module provides network utilities including URL handling, HTTP operations, and validation.

## Overview

This section gives a high-level overview of the networking helpers.
The full reference for each area is on the submodule pages.

## Submodules

- [URL](net/url.md): Parse and manipulate URLs.
- [HTTP](net/http.md): HTTP utilities and status codes.
- [Validation](net/validation.md): Validate network-related formats.

## Examples

```python
from rite.net import (
    url_parse,
    validation_is_url,
    http_status_code
)

# Parse URL
parts = url_parse("https://example.com/path?key=value")

# Validate URL
is_valid = validation_is_url("https://example.com")

# Get HTTP status message
message = http_status_code(404)  # "Not Found"
```

# Markup Module

The `rite.markup` module provides utilities for working with HTML, XML, and Markdown.

## Overview

This section describes the overall markup utilities at a high level.
The detailed APIs live on the individual submodule pages.

## Submodules

- [HTML](markup/html.md): HTML manipulation and sanitization.
- [XML](markup/xml.md): XML parsing and formatting.
- [Markdown](markup/markdown.md): Markdown processing.
- [Entities](markup/entities.md): HTML entity encoding/decoding.

## Examples

```python
from rite.markup import (
    html_escape,
    xml_format,
    markdown_to_html
)

# Escape HTML
safe = html_escape("<script>alert('xss')</script>")

# Format XML
formatted = xml_format("<root><child>text</child></root>")

# Convert Markdown
html = markdown_to_html("# Heading\n\nParagraph")
```

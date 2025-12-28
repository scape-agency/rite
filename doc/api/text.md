---
title: Text API
description: Comprehensive text processing utilities from rite.text including case conversion, slugging, validation, and sanitization.
keywords: python text utils, slugify, case conversion, sanitize, rite.text
---

# Text Module

The `rite.text` module provides comprehensive text processing utilities
including case conversions, slug generation, text analysis, validation,
manipulation, search operations, and sanitization.

## Overview

This section introduces the text processing helpers at a high level.
Each submodule page provides the detailed API reference.

## Submodules

- [Case](text/case.md): Case conversion utilities.
- [Slug](text/slug.md): Slug generation and validation.
- [Analysis](text/analysis.md): Text analysis helpers.
- [Validation](text/validation.md): Validate text input.
- [Manipulation](text/manipulation.md): Text manipulation helpers.
- [Search](text/search.md): Search within text.
- [Sanitize](text/sanitize.md): Text sanitization utilities.
- [Morse](text/morse.md): Morse code conversion.
- [Random](text/random.md): Random text generation.
```python
from rite.text import to_snake_case, slugify, text_truncate

# Case conversion
text = "HelloWorld"
snake = to_snake_case(text)  # "hello_world"

# Slug generation
title = "Hello World! This is a test."
slug = slugify(title)  # "hello-world-this-is-a-test"

# Text manipulation
long_text = "This is a very long text that needs truncation"
short = text_truncate(long_text, 20)  # "This is a very l..."
```

### Advanced Examples

```python
from rite.text import (
    text_is_email,
    text_pad_left,
    char_frequency,
    text_contains
)

# Validation
email = "user@example.com"
is_valid = text_is_email(email)  # True

# Padding
number = "42"
padded = text_pad_left(number, 5, "0")  # "00042"

# Analysis
text = "hello world"
freq = char_frequency(text)  # {'h': 1, 'e': 1, 'l': 3, ...}

# Search
haystack = "The quick brown fox"
found = text_contains(haystack, "quick")  # True
```

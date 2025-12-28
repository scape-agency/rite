# Rite Documentation

This directory contains the source files for the Rite documentation, which integrates **Sphinx** for API reference and **MkDocs** with Material theme for the main documentation site.

## Structure

```
doc/
├── _static/           # Sphinx static files (CSS, images)
├── _templates/        # Sphinx custom templates
├── api/              # API reference (MkDocs with mkdocstrings)
├── assets/           # Site assets (images, fonts, styles)
├── about/            # About pages
├── development/      # Development guides
├── legal/            # Legal documents
├── resources/        # Additional resources
├── conf.py           # Sphinx configuration
└── index.md          # Documentation home page
```

## Building Documentation

### Prerequisites

Install documentation dependencies:

```bash
# Using pip
pip install -r requirements-docs.txt

# Or using poetry
poetry add --group docs \
    mkdocs \
    mkdocs-material \
    mkdocstrings[python] \
    pymdown-extensions
```

### Build Commands

#### MkDocs (Recommended for development)

```bash
# Build static site
mkdocs build

# Serve with live reload (default: http://127.0.0.1:8888)
mkdocs serve

# Using the build script
./bin/build-docs.sh mkdocs serve
```

#### Sphinx (For API documentation)

```bash
# Build HTML documentation
cd doc
sphinx-build -b html . _build/html

# Using the build script
./bin/build-docs.sh sphinx serve
```

#### All at Once

```bash
# Generate API docs and build everything
./bin/build-docs.sh all
```

## Documentation Style Guide

### Writing Docstrings

All modules, classes, methods, and functions must have Google-style docstrings:

```python
def example_function(param1: str, param2: int = 0) -> bool:
    """
    Brief one-line description.

    Longer description if needed, explaining what the function does
    in more detail.

    Args:
        param1: Description of param1.
        param2: Description of param2. Defaults to 0.

    Returns:
        Description of return value.

    Raises:
        ValueError: When param1 is empty.

    Examples:
        >>> example_function("test", 5)
        True
        >>> example_function("", 10)
        ValueError: param1 cannot be empty

    Notes:
        Additional notes about usage or behavior.
    """
```

### Adding New Pages

1. Create a new `.md` file in the appropriate directory
2. Add it to the navigation in `mkdocs.yml`
3. Use mkdocstrings syntax for API documentation:

```markdown
# Module Name

Description of the module.

::: rite.module.submodule
options:
show_source: false
heading_level: 2
```

### Styling Guidelines

-   **Brand Colors**: Defined in `assets/style/extra.css`
    -   Primary: `rgb(0, 0, 15)` (near black)
    -   Accent: `#2196f3` (blue)
-   **Typography**: Manrope font family
-   **Code**: Roboto Mono for code blocks
-   **Line Length**: 79 characters in code examples

## Configuration Files

### mkdocs.yml

Main configuration for MkDocs:

-   Site metadata
-   Navigation structure
-   Theme configuration
-   Plugin settings
-   Markdown extensions

### conf.py

Sphinx configuration:

-   Project information
-   Extension settings
-   HTML theme options
-   API documentation settings

### assets/style/extra.css

Custom CSS for MkDocs Material theme:

-   Brand colors
-   Typography
-   Component styling
-   Responsive design

## API Reference

API documentation is automatically generated from docstrings using `mkdocstrings`. The API pages in `api/` directory organize modules by category:

-   **Core**: Collections, Conversion, Text
-   **System & I/O**: Filesystem, System, Net
-   **Data**: Serialization, Markup
-   **Security**: Crypto, Numeric, Temporal
-   **Development**: Diagnostics, Functional, Reflection

## Deployment

### GitHub Pages

Documentation is automatically deployed to GitHub Pages on push to the `main` branch.

```bash
# Deploy manually
mkdocs gh-deploy
```

### Custom Domain

The site is configured for `www.pyrites.dev` via the `CNAME` file.

## Maintenance

### Updating Docstrings

When adding or modifying code:

1. Ensure all public APIs have complete docstrings
2. Include examples in docstrings
3. Add type hints for all parameters and returns
4. Build docs locally to verify rendering

### Adding Examples

Examples should be:

-   Runnable code snippets
-   Show common use cases
-   Include expected output
-   Cover edge cases

### Checking Links

```bash
# Check for broken links
mkdocs build --strict

# Validate internal links
find doc -name "*.md" -exec grep -H "\[.*\](.*)" {} \;
```

## Troubleshooting

### Build Errors

**Import errors**: Ensure source directory is in Python path:

```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
```

**Missing dependencies**: Install all documentation dependencies:

```bash
pip install -r requirements-docs.txt
```

**Theme issues**: Clear MkDocs cache:

```bash
rm -rf ~/.mkdocs/
```

### Rendering Issues

**Code blocks not highlighted**: Check language identifier in code fence

**API not showing**: Verify module path in mkdocstrings directive

**Broken navigation**: Validate YAML syntax in mkdocs.yml

## Contributing

When contributing documentation:

1. Follow the style guide
2. Build locally before committing
3. Check for typos and broken links
4. Ensure examples are tested
5. Update navigation if adding new pages

## Resources

-   [MkDocs Documentation](https://www.mkdocs.org/)
-   [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
-   [mkdocstrings](https://mkdocstrings.github.io/)
-   [Sphinx Documentation](https://www.sphinx-doc.org/)
-   [Google Style Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)

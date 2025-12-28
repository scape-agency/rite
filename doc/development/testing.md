# Testing Guide

This guide covers testing practices and guidelines for Rite.

## Testing Framework

Rite uses **Pytest** as the testing framework with **Coverage** for code coverage measurement.

## Running Tests

### Basic Commands

```bash
# Run all tests
make test

# Run with coverage
make coverage

# Run specific test file
poetry run pytest tst/path/to/test_file.py

# Run specific test class
poetry run pytest tst/path/to/test_file.py::TestClassName

# Run specific test method
poetry run pytest tst/path/to/test_file.py::TestClassName::test_method

# Run with verbose output
poetry run pytest -v

# Run with output capture disabled
poetry run pytest -s
```

### Using Test Markers

```bash
# Run only unit tests
poetry run pytest -m unit

# Run only integration tests
poetry run pytest -m integration

# Run only slow tests
poetry run pytest -m slow

# Run everything except slow tests
poetry run pytest -m "not slow"

# Combine markers
poetry run pytest -m "unit and not slow"
```

## Test Structure

### File Organization

Tests mirror the src/ structure:

```
src/rite/
├── crypto/
│   ├── uuid/
│   │   └── uuid_hex.py
│   └── hash/
│       └── hash_sha256.py
└── text/
    └── slug/
        └── slug_is_valid.py

tst/rite/
├── crypto/
│   ├── uuid/
│   │   └── test_uuid_hex.py
│   └── hash/
│       └── test_hash_sha256.py
└── text/
    └── slug/
        └── test_slug_is_valid.py
```

### Test File Template

```python
# =============================================================================
# Test: Module Name
# =============================================================================

"""Tests for rite.module.function."""

# Import | Future
from __future__ import annotations

# Import | Standard Library
import pytest

# Import | Local Modules
from rite.module import function


class TestFunction:
    """Tests for function."""

    def test_basic_usage(self) -> None:
        """Test basic functionality."""
        result = function("input")
        assert result == "expected"

    def test_edge_cases(self) -> None:
        """Test edge cases."""
        # Test empty input
        result = function("")
        assert result == ""

        # Test None input
        with pytest.raises(TypeError):
            function(None)

    @pytest.mark.parametrize(
        "input_val,expected",
        [
            ("test1", "result1"),
            ("test2", "result2"),
            ("test3", "result3"),
        ],
    )
    def test_multiple_cases(
        self, input_val: str, expected: str
    ) -> None:
        """Test multiple parameter combinations."""
        assert function(input_val) == expected

    @pytest.mark.slow
    def test_performance(self) -> None:
        """Test performance with large dataset."""
        large_input = "x" * 1000000
        result = function(large_input)
        assert len(result) > 0
```

## Test Types

### Unit Tests

Test individual functions in isolation:

```python
class TestHashSha256:
    """Unit tests for hash_sha256."""

    @pytest.mark.unit
    def test_basic_hash(self) -> None:
        """Test basic hashing."""
        result = hash_sha256("test")
        assert len(result) == 64  # SHA256 produces 64 hex chars

    @pytest.mark.unit
    def test_empty_string(self) -> None:
        """Test hashing empty string."""
        result = hash_sha256("")
        assert result is not None
```

### Integration Tests

Test multiple components working together:

```python
class TestFileOperations:
    """Integration tests for file operations."""

    @pytest.mark.integration
    def test_file_workflow(self, tmp_path: Path) -> None:
        """Test complete file workflow."""
        # Create test file
        source = tmp_path / "source.txt"
        source.write_text("test content")

        # Copy file
        dest = tmp_path / "dest.txt"
        file_copy(source, dest)

        # Verify
        assert dest.read_text() == "test content"
        assert file_exists(dest)
```

### Parametrized Tests

Test multiple inputs efficiently:

```python
@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("hello", "hello"),
        ("HELLO", "hello"),
        ("Hello World", "hello-world"),
        ("hello_world", "hello-world"),
        ("", ""),
    ],
)
def test_to_slug(input_str: str, expected: str) -> None:
    """Test slug conversion with various inputs."""
    assert to_slug(input_str) == expected
```

### Exception Tests

Test error handling:

```python
def test_invalid_input() -> None:
    """Test handling of invalid input."""
    with pytest.raises(ValueError, match="Invalid input"):
        function("invalid")

def test_type_error() -> None:
    """Test type checking."""
    with pytest.raises(TypeError):
        function(None)
```

## Fixtures

### Built-in Fixtures

```python
def test_temp_file(tmp_path: Path) -> None:
    """Test with temporary directory."""
    test_file = tmp_path / "test.txt"
    test_file.write_text("content")
    assert test_file.read_text() == "content"

def test_with_monkeypatch(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test with environment variable."""
    monkeypatch.setenv("TEST_VAR", "value")
    assert os.getenv("TEST_VAR") == "value"
```

### Custom Fixtures

Create in `conftest.py`:

```python
# tst/conftest.py
import pytest


@pytest.fixture
def sample_data() -> dict[str, Any]:
    """Provide sample test data."""
    return {
        "name": "test",
        "value": 42,
        "active": True,
    }


@pytest.fixture
def temp_file(tmp_path: Path) -> Path:
    """Create a temporary test file."""
    file_path = tmp_path / "test.txt"
    file_path.write_text("test content")
    return file_path


# Use in tests
def test_with_fixture(sample_data: dict[str, Any]) -> None:
    """Test using custom fixture."""
    assert sample_data["name"] == "test"
```

## Code Coverage

### Measuring Coverage

```bash
# Run tests with coverage
poetry run pytest --cov=rite --cov-report=html --cov-report=term

# Open HTML report
open htmlcov/index.html

# Generate XML report (for CI)
poetry run pytest --cov=rite --cov-report=xml
```

### Coverage Goals

-   **Overall**: >80% coverage
-   **New code**: >90% coverage
-   **Critical modules**: 100% coverage

### Excluding from Coverage

In code:

```python
def debug_function():  # pragma: no cover
    """This function is only for debugging."""
    pass
```

In `.coveragerc`:

```ini
[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplementedError
    if __name__ == .__main__.:
```

## Mocking

### Using unittest.mock

```python
from unittest.mock import Mock, patch, MagicMock


def test_with_mock() -> None:
    """Test with mocked dependency."""
    mock_service = Mock()
    mock_service.get_data.return_value = {"key": "value"}

    result = function_using_service(mock_service)

    mock_service.get_data.assert_called_once()
    assert result["key"] == "value"


@patch("rite.module.external_function")
def test_with_patch(mock_external: Mock) -> None:
    """Test with patched function."""
    mock_external.return_value = "mocked"

    result = function()

    assert result == "mocked"
    mock_external.assert_called()
```

## Test Markers

Defined in `pytest.ini`:

```ini
[pytest]
markers =
    unit: Unit tests (fast, isolated)
    integration: Integration tests (multiple components)
    slow: Slow tests (skip in development)
    smoke: Smoke tests (quick sanity check)
    regression: Regression tests (known bugs)
    security: Security tests
```

Usage:

```python
@pytest.mark.unit
def test_fast() -> None:
    pass

@pytest.mark.integration
@pytest.mark.slow
def test_complex() -> None:
    pass
```

## Best Practices

### Test Names

```python
# ✅ Good: Descriptive test names
def test_empty_string_returns_empty_slug() -> None:
    pass

def test_uppercase_letters_converted_to_lowercase() -> None:
    pass

# ❌ Bad: Vague test names
def test_function() -> None:
    pass

def test_1() -> None:
    pass
```

### Arrange-Act-Assert

```python
def test_user_creation() -> None:
    """Test user creation."""
    # Arrange
    name = "John Doe"
    email = "john@example.com"

    # Act
    user = create_user(name, email)

    # Assert
    assert user.name == name
    assert user.email == email
    assert user.is_active is True
```

### One Assertion Per Test

```python
# ✅ Good: Focused tests
def test_user_name() -> None:
    user = create_user("John")
    assert user.name == "John"

def test_user_email() -> None:
    user = create_user("John", "john@example.com")
    assert user.email == "john@example.com"

# ❌ Bad: Multiple unrelated assertions
def test_user() -> None:
    user = create_user("John", "john@example.com")
    assert user.name == "John"
    assert user.email == "john@example.com"
    assert user.is_active is True
    assert len(user.id) > 0
```

### Test Independence

```python
# ✅ Good: Tests don't depend on each other
class TestCounter:
    def test_increment(self) -> None:
        counter = Counter()
        counter.increment()
        assert counter.value == 1

    def test_decrement(self) -> None:
        counter = Counter()
        counter.decrement()
        assert counter.value == -1

# ❌ Bad: Tests depend on execution order
class TestCounter:
    counter = Counter()

    def test_increment(self) -> None:
        self.counter.increment()
        assert self.counter.value == 1

    def test_another_increment(self) -> None:
        # Assumes previous test ran first
        self.counter.increment()
        assert self.counter.value == 2
```

## Continuous Integration

Tests run automatically in CI:

```yaml
# .github/workflows/ci-cd.yml
- name: Run tests with coverage
  run: poetry run pytest --cov=rite --cov-report=xml

- name: Upload coverage
  uses: codecov/codecov-action@v4
```

## Multi-Environment Testing

Test across Python versions:

```bash
# Using tox
make tox

# Or directly
poetry run tox -e py310,py311,py312
```

## Performance Testing

### Benchmark Tests

```python
@pytest.mark.benchmark
def test_performance(benchmark):
    """Benchmark function performance."""
    result = benchmark(expensive_function, "input")
    assert result is not None
```

### Profiling

```bash
# Profile tests
poetry run pytest --profile

# With detailed output
poetry run pytest --profile-svg
```

## Debugging Tests

### Print Debugging

```bash
# Show print output
poetry run pytest -s

# Show local variables on failure
poetry run pytest -l
```

### Using pdb

```python
def test_debug() -> None:
    """Test with debugger."""
    result = function("input")
    import pdb; pdb.set_trace()  # Breakpoint
    assert result == "expected"
```

Run with:

```bash
poetry run pytest --pdb
```

## Common Patterns

### Testing Files

```python
def test_file_operations(tmp_path: Path) -> None:
    """Test file operations."""
    # Create test file
    test_file = tmp_path / "test.txt"
    test_file.write_text("content")

    # Test
    result = read_file(test_file)
    assert result == "content"
```

### Testing Exceptions

```python
def test_exception_message() -> None:
    """Test exception details."""
    with pytest.raises(ValueError) as exc_info:
        function("invalid")

    assert "invalid" in str(exc_info.value)
```

### Testing Async Code

```python
@pytest.mark.asyncio
async def test_async_function() -> None:
    """Test async function."""
    result = await async_function()
    assert result is not None
```

## Resources

-   [Pytest Documentation](https://docs.pytest.org/)
-   [Coverage.py Documentation](https://coverage.readthedocs.io/)
-   [Python Testing with pytest](https://pythontest.com/pytest-book/)
-   [Effective Python Testing](https://realpython.com/python-testing/)

## See Also

-   [Code Style Guide](code-style.md)
-   [Development Setup](setup.md)
-   [Contributing Guide](https://github.com/scape-agency/rite/blob/main/CONTRIBUTING.md)

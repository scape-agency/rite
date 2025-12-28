# Benchmark Tests

Performance benchmarks for the Rite library using `pytest-benchmark`.

## Running Benchmarks

### Run all benchmarks

```bash
poetry run pytest tst/benchmarks/ --benchmark-only
```

### Run specific benchmark module

```bash
poetry run pytest tst/benchmarks/test_benchmark_text.py --benchmark-only
```

### Generate JSON output

```bash
poetry run pytest tst/benchmarks/ --benchmark-only --benchmark-json=output.json
```

### Compare with baseline

```bash
# Save baseline
poetry run pytest tst/benchmarks/ --benchmark-only --benchmark-save=baseline

# Compare with baseline
poetry run pytest tst/benchmarks/ --benchmark-only --benchmark-compare=baseline
```

## Benchmark Modules

### Text Operations (`test_benchmark_text.py`)
- `slugify` - URL slug generation
- Case conversions (snake_case, camelCase, PascalCase, kebab-case)
- Character frequency analysis
- Email validation
- Text truncation
- Text sanitization

### Crypto Operations (`test_benchmark_crypto.py`)
- SHA-256 hashing
- MD5 hashing
- BLAKE2b hashing
- UUID generation
- UUID hex conversion
- UUID validation

### Filesystem Operations (`test_benchmark_filesystem.py`)
- File reading (text and binary)
- File writing (text and binary)
- Path cleaning
- Path security checks
- Safe path joining
- Path leaf extraction

### Collections Operations (`test_benchmark_collections.py`)
- List unique operation
- List flattening
- List chunking
- List partitioning
- Deep dictionary get/set
- Dictionary merging

### Conversion Operations (`test_benchmark_conversion.py`)
- Boolean conversion
- Integer conversion
- Float conversion
- String conversion
- Batch conversions

## Benchmark Configuration

Benchmarks are configured in `pytest.ini`:

```ini
[pytest]
benchmark_disable_gc = true
benchmark_warmup = true
benchmark_min_rounds = 5
```

## CI/CD Integration

Benchmarks run automatically on:
- Push to `main` or `dev` branches
- Pull requests
- Manual workflow dispatch

Results are stored and compared using GitHub Actions `benchmark-action/github-action-benchmark`.

## Performance Targets

Target performance goals:
- Text operations: < 1ms for typical inputs
- Crypto operations: < 10ms for SHA-256 on 1KB data
- File operations: < 10ms for 100KB files
- Collection operations: < 1ms for 1000 items

## Adding New Benchmarks

Follow the existing patterns:

```python
def test_benchmark_your_function(benchmark):
    """Benchmark description."""
    result = benchmark(your_function, arg1, arg2)
    assert result is not None  # Verify correctness
```

For setup-heavy benchmarks:

```python
def test_benchmark_with_setup(benchmark, tmp_path):
    """Benchmark with setup."""
    # Setup
    data = prepare_test_data()
    
    # Define function to benchmark
    def run():
        return process_data(data)
    
    # Benchmark
    result = benchmark(run)
    assert result is not None
```

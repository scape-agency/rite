# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive CI/CD workflow with GitHub Actions
- Pre-commit hooks for code quality (Black, isort, flake8, mypy)
- pytest configuration with coverage reporting
- mypy type checking configuration
- Enhanced .gitignore for Python projects
- CONTRIBUTING.md with development guidelines
- Enhanced README with usage examples

### Changed
- Updated pyproject.toml with missing dependencies (Pillow, geojson, python-gnupg, xmltodict)
- Fixed license classifier to match actual MIT License
- Improved Python .gitignore entries

### Fixed
- Fixed pkg_resources import to use importlib.metadata
- Fixed Python 2 xrange to range in colour.py
- Added missing colorsys import

## [0.1.1] - Previous Release

### Added
- Initial release with core utilities
- Time utilities (timestamp, duration, timezone)
- String manipulation utilities
- UUID generation and validation
- File and directory operations
- Cryptography utilities
- Format conversion (JSON, CSV, GeoJSON, etc.)

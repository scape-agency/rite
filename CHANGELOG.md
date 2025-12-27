# Changelog

All notable changes to this project will be documented in this file.

## [0.1.2-beta.4](https://github.com/scape-agency/rite/compare/v0.1.2-beta.3...v0.1.2-beta.4) (2025-12-27)

### 🐛 Bug Fixes

* **lint:** Fix E704 protocol method signatures with proper implementation ([ccc0a6d](https://github.com/scape-agency/rite/commit/ccc0a6ddc43b36c4baaa93ea9fd806acdc7c8eed))

## [0.1.2-beta.3](https://github.com/scape-agency/rite/compare/v0.1.2-beta.2...v0.1.2-beta.3) (2025-12-27)

### 🐛 Bug Fixes

* **lint:** Fix E704 protocol method signatures ([a75d561](https://github.com/scape-agency/rite/commit/a75d561e9248b3b54f6298fe8247e68467f21687))

## [0.1.2-beta.2](https://github.com/scape-agency/rite/compare/v0.1.2-beta.1...v0.1.2-beta.2) (2025-12-27)

### 🐛 Bug Fixes

* **ci:** Replace types-all with specific type stubs ([24ed8b1](https://github.com/scape-agency/rite/commit/24ed8b14846db725b72c7844b69c8c738a332024))
* **docs:** Register myst_parser extension for Sphinx markdown support ([1c6df53](https://github.com/scape-agency/rite/commit/1c6df53d05d98fa0660a71929284908592dab3ac))
* **lint:** Fix E704 protocol method signatures ([0fdaa79](https://github.com/scape-agency/rite/commit/0fdaa7917c9fd8a897c1e40dce20a5c4a35c6f6c))
* **test:** Resolve Black parsing errors in test files ([6b7b91c](https://github.com/scape-agency/rite/commit/6b7b91c53b3e2f1903518db2f3697ecbbdc45549))

### 📚 Documentation

* Document trailing newline enforcement across linting tools ([fa8b0a2](https://github.com/scape-agency/rite/commit/fa8b0a2fb3c77023849c78cc38065c501ee55c44))

## [0.1.2-beta.1](https://github.com/scape-agency/rite/compare/v0.1.1...v0.1.2-beta.1) (2025-12-27)

### 🐛 Bug Fixes

* **lint:** Resolve flake8 E704 and C901 violations ([4811f29](https://github.com/scape-agency/rite/commit/4811f29a84cfb0f4764083543ee8b0969250ceb8))

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

## [0.1.2] - Previous Release

### Added
- Initial release with core utilities
- Time utilities (timestamp, duration, timezone)
- String manipulation utilities
- UUID generation and validation
- File and directory operations
- Cryptography utilities
- Format conversion (JSON, CSV, GeoJSON, etc.)

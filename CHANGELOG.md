# Changelog

All notable changes to this project will be documented in this file.

## [0.2.0-beta.4](https://github.com/scape-agency/rite/compare/v0.2.0-beta.3...v0.2.0-beta.4) (2025-12-27)

### ✨ Features

* Implement system path and functional composition tests ([ceefef0](https://github.com/scape-agency/rite/commit/ceefef0002872831d74ea333cb75a811b00f4b0d))

## [0.2.0-beta.3](https://github.com/scape-agency/rite/compare/v0.2.0-beta.2...v0.2.0-beta.3) (2025-12-27)

### ✨ Features

* Implement numeric conversion and JSON serialization tests ([efd6509](https://github.com/scape-agency/rite/commit/efd65096f5b8da83625ee00c5c96dfe02a8e3155))
* Implement reflection attribute and collection list tests ([a4c4f37](https://github.com/scape-agency/rite/commit/a4c4f37f78d40195e49895c127e38f0d22d771c8))
* Implement text converter tests (int, float, bool, binary, decimal, datetime) ([d5c1b3a](https://github.com/scape-agency/rite/commit/d5c1b3ab6cbdac17918efd7d5825ed724d384bbe))

## [0.2.0-beta.2](https://github.com/scape-agency/rite/compare/v0.2.0-beta.1...v0.2.0-beta.2) (2025-12-27)

### ✨ Features

* Implement temporal calendar, numeric math, and text validation/search tests ([01f69c8](https://github.com/scape-agency/rite/commit/01f69c84457e817141fcacd813415716dda80074))

## [0.2.0-beta.1](https://github.com/scape-agency/rite/compare/v0.1.3-beta.1...v0.2.0-beta.1) (2025-12-27)

### ✨ Features

* Implement conversion formats, filesystem path, text analysis, and platform tests ([912341e](https://github.com/scape-agency/rite/commit/912341ed49343510f17fa11f5388b08aad140f01))
* Implement crypto hash tests ([c60099d](https://github.com/scape-agency/rite/commit/c60099db10ac738099703464a9a5a630b66346cf))
* Implement crypto random and UUID tests ([d982a58](https://github.com/scape-agency/rite/commit/d982a58de5351a0bb4b995fbe4694e44f916d7a4))
* Implement numeric rounding and system environment tests ([e65394b](https://github.com/scape-agency/rite/commit/e65394bc747e4bd9b2dad25119a385cbbb84f5eb))

### 🐛 Bug Fixes

* Logger clear_log and test fixes ([53681d3](https://github.com/scape-agency/rite/commit/53681d35b2a52d9bebda4f017ea18bbfe3730d85))

## [0.1.3-beta.1](https://github.com/scape-agency/rite/compare/v0.1.2...v0.1.3-beta.1) (2025-12-27)

### 🐛 Bug Fixes

* Remove broken imports and nonexistent module references ([e8770b3](https://github.com/scape-agency/rite/commit/e8770b3254a228d2533229f1686ae0f903ef8bc5))

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

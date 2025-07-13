# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive GitHub Actions CI/CD workflows
- Automated testing across multiple Python versions and platforms
- Automated publishing to PyPI and Test PyPI
- Development guide and workflow documentation

### Changed
- Package rebranded from "Error Monitor" to "Errica by EaseCloud"
- Version changed to 0.1.0-beta (first beta release)
- Improved .gitignore with comprehensive exclusions
- Removed noisy import message for cleaner experience

### Removed
- Build artifacts and cache files from git tracking

## [0.1.0-beta] - 2025-07-13

### Added
- Multi-channel error monitoring and notification system
- Support for Console, Telegram, Slack, and Webhook channels
- Global exception handling for unhandled exceptions
- Task and batch monitoring with context managers
- Rate limiting and message deduplication
- Rich message formatting per channel type
- Health checks for all channels
- Comprehensive configuration system with YAML support
- Environment variable configuration support
- Example scripts for basic, advanced, and multi-channel usage

### Features
- **Console Channel**: Colored terminal output with detailed formatting
- **Telegram Channel**: Rich Markdown formatting with file attachments
- **Slack Channel**: Rich message blocks with threading support
- **Webhook Channel**: JSON/form-encoded payloads with custom headers
- **Rate Limiting**: Configurable limits per channel (messages/minute, messages/hour)
- **Deduplication**: Prevent duplicate messages within time windows
- **Context Management**: Task monitoring with automatic timing
- **Error Context**: Capture additional context with errors
- **Statistics**: Comprehensive monitoring statistics and health metrics

### Technical
- Python 3.8+ support
- Async-safe exception handling
- Thread-safe operations
- Comprehensive test coverage
- Development tooling (linting, formatting, type checking)
- Automated CI/CD pipeline

---

## Release Types

- **Stable releases** (1.0.0) - Production ready, published to PyPI
- **Beta releases** (1.0.0-beta.1) - Feature complete, published to Test PyPI  
- **Alpha releases** (1.0.0-alpha.1) - Early testing, published to Test PyPI
- **Dev builds** (1.0.0-dev.123+sha) - Continuous builds from main branch

## Links

- [GitHub Repository](https://github.com/easecloudio/easecloud-errica)
- [PyPI Package](https://pypi.org/project/easecloud-errica/)
- [Documentation](docs/)
- [Issue Tracker](https://github.com/easecloudio/easecloud-errica/issues)
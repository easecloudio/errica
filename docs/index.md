# Errica Documentation

## Available Documentation

- [Main README](../README.md) - Quick start and overview
- [Development Guide](development.md) - Local setup and testing
- [GitHub Actions Workflows](workflows.md) - CI/CD pipeline

## Quick Start

```bash
# Install
pip install easecloud-errica

# Basic usage
python examples/basic_usage.py
```

## Development

```bash
# Setup
pip install -e .[dev]

# Run tests
pytest tests/

# Build package
python -m build
```
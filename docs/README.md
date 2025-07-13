# Errica Documentation

Welcome to the Errica by EaseCloud documentation! This directory contains comprehensive guides for using, developing, and contributing to the Errica error monitoring package.

## 📖 Available Documentation

### 🚀 Getting Started
- **[Main README](../README.md)** - Quick start and overview
- **[Installation Guide](installation.md)** - Installation options and requirements *(coming soon)*

### 🔧 Development & Contributing  
- **[Development Guide](development.md)** - Local setup, testing, and contribution workflow
- **[GitHub Actions Workflows](workflows.md)** - CI/CD pipeline and automated publishing

### 📚 Usage & Configuration
- **[Configuration Reference](configuration.md)** - Complete configuration options *(coming soon)*
- **[Channel Setup Guides](channels/)** - Setting up different notification channels *(coming soon)*
- **[API Documentation](api.md)** - Complete API reference *(coming soon)*

### 🏗️ Architecture & Internals
- **[Architecture Overview](architecture.md)** - System design and components *(coming soon)*
- **[Plugin Development](plugins.md)** - Creating custom channels and formatters *(coming soon)*

## 🎯 Quick Navigation

### For Users
If you're using Errica in your project:
1. Start with the [Main README](../README.md) for installation
2. Check [Configuration Reference](configuration.md) for setup options
3. See [Channel Setup Guides](channels/) for specific integrations

### For Contributors  
If you're contributing to Errica:
1. Read the [Development Guide](development.md) for local setup
2. Understand [GitHub Actions Workflows](workflows.md) for CI/CD
3. Check [Architecture Overview](architecture.md) for system design

### For Maintainers
If you're maintaining releases:
1. Use [GitHub Actions Workflows](workflows.md) for automated publishing
2. Follow the release process in [Development Guide](development.md)
3. Update documentation as needed

## 🚀 CI/CD Quick Reference

### Automated Publishing
- **Dev builds**: Push to `main` → `0.1.0-dev.123+sha` → Test PyPI
- **Beta releases**: Push to `release/v*` → `0.1.0-beta.1` → Test PyPI  
- **Stable releases**: GitHub release → `1.0.0` → PyPI

### Manual Release Process
```bash
# 1. Go to GitHub Actions → "Create Release"
# 2. Enter version: 1.0.0
# 3. Select: stable
# 4. Workflow handles everything automatically
```

### Local Testing
```bash
# Setup development environment
pip install -e .[dev]

# Run tests
pytest tests/

# Test functionality
python examples/basic_usage.py

# Build package
python -m build
```

## 📝 Documentation Status

| Document | Status | Description |
|----------|--------|-------------|
| [Development Guide](development.md) | ✅ Complete | Local setup and contribution workflow |
| [Workflows Guide](workflows.md) | ✅ Complete | CI/CD and automated publishing |
| Configuration Reference | 🚧 Planned | Complete configuration options |
| Channel Setup Guides | 🚧 Planned | Setup guides for each channel type |
| API Documentation | 🚧 Planned | Complete API reference |
| Architecture Overview | 🚧 Planned | System design and components |
| Plugin Development | 🚧 Planned | Creating custom extensions |

## 🤝 Contributing to Documentation

Documentation improvements are welcome! To contribute:

1. **For existing docs**: Edit files directly and submit a PR
2. **For new docs**: Create new files following the existing structure
3. **For major changes**: Open an issue first to discuss

### Documentation Standards
- Use clear, concise language
- Include code examples where helpful
- Follow the existing structure and formatting
- Update this index when adding new documents

## 🔗 External Resources

- **GitHub Repository**: https://github.com/easecloudio/easecloud-errica
- **PyPI Package**: https://pypi.org/project/easecloud-errica/
- **Issue Tracker**: https://github.com/easecloudio/easecloud-errica/issues

## 📞 Getting Help

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and community support
- **Documentation Issues**: Use the issue tracker with "documentation" label
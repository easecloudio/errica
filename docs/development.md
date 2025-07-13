# Development Guide

## Development Setup

### Prerequisites
- Python 3.8+ 
- Git
- pip

### Local Development

1. **Clone and setup:**
```bash
git clone https://github.com/easecloudio/easecloud-errica.git
cd easecloud-errica
pip install -e .[dev]
```

2. **Test your changes:**
```bash
# Run tests
pytest tests/

# Test basic functionality
python -c "
from easecloud_errica import quick_setup, log_info
manager, handler = quick_setup()
log_info('Development test successful')
"

# Run examples
python examples/basic_usage.py
```

3. **Build package:**
```bash
python -m build
pip install dist/*.whl  # Test installation
```

## CI/CD Pipeline

### GitHub Actions Workflows

We use automated workflows for testing and publishing:

#### 1. **Continuous Testing** (`test.yml`)
- **Triggers**: Pull requests, pushes to main
- **Matrix**: Python 3.8-3.12 × Ubuntu/Windows/macOS
- **Tests**: Import, functionality, examples, package building

#### 2. **Automated Publishing** (`publish.yml`)
- **Dev builds**: Push to main → `0.1.0-dev.123+sha` → Test PyPI
- **Beta releases**: Push to `release/v*` → `0.1.0-beta.1` → Test PyPI
- **Stable releases**: GitHub releases → `1.0.0` → PyPI

#### 3. **Manual Releases** (`release.yml`)
- Manual workflow for creating proper releases
- Handles version updates, tagging, and changelog generation

### Release Process

#### **For Stable Release:**
1. Navigate to Actions → "Create Release"
2. Enter version (e.g., `1.0.0`)
3. Select "stable" release type
4. Workflow automatically:
   - Updates version files
   - Creates git tag and GitHub release
   - Publishes to PyPI

#### **For Beta Testing:**
```bash
git checkout -b release/v1.0.0-beta
git push origin release/v1.0.0-beta
# Auto-publishes to Test PyPI as 1.0.0-beta.X
```

#### **For Development:**
```bash
git push origin main
# Auto-publishes to Test PyPI as 0.1.0-dev.X+sha
```

### Version Strategy

**Semantic Versioning:**
- `1.0.0` - Stable release (PyPI)
- `1.0.0-beta.1` - Beta release (Test PyPI)
- `1.0.0-dev.123+a1b2c3d` - Development build (Test PyPI)

## Code Quality

### Linting and Formatting
```bash
# Format code
black src/ --line-length=100

# Check linting
flake8 src/ --max-line-length=100

# Type checking
mypy src/easecloud_errica --ignore-missing-imports
```

### Testing
```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=easecloud_errica --cov-report=html

# Run specific test
pytest tests/test_basic.py::test_quick_setup
```

### Pre-commit Hooks (Optional)
```bash
pip install pre-commit
pre-commit install
```

## Contributing

### Pull Request Process

1. **Fork and branch:**
```bash
git checkout -b feature/your-feature-name
```

2. **Make changes and test:**
```bash
# Add your changes
git add .
git commit -m "feat: add new feature"

# Test locally
pytest tests/
python examples/basic_usage.py
```

3. **Push and create PR:**
```bash
git push origin feature/your-feature-name
# Create PR on GitHub
```

4. **Automated checks:**
- All tests must pass across Python versions
- Code quality checks must pass
- Examples must run successfully

### Commit Message Format
Follow conventional commits:
- `feat:` - New features
- `fix:` - Bug fixes  
- `docs:` - Documentation changes
- `chore:` - Maintenance tasks
- `test:` - Test improvements

## Repository Setup

### Required Secrets
For automated publishing, add these GitHub secrets:

```bash
PYPI_API_TOKEN=pypi-...          # For stable releases
TEST_PYPI_API_TOKEN=pypi-...     # For dev/beta releases
```

**Get tokens from:**
- PyPI: https://pypi.org/manage/account/token/
- Test PyPI: https://test.pypi.org/manage/account/token/

### Branch Protection (Recommended)
Enable branch protection for `main`:
- Require pull request reviews
- Require status checks (test workflow)
- Require up-to-date branches

## Local Testing

### Test Installation from Packages
```bash
# Test from Test PyPI
pip install -i https://test.pypi.org/simple/ easecloud-errica

# Test from PyPI
pip install easecloud-errica
```

### Test Different Scenarios
```bash
# Test with Telegram (if you have credentials)
export TELEGRAM_BOT_TOKEN="your_token"
export TELEGRAM_CHAT_ID="your_chat_id"
python examples/basic_usage.py

# Test error handling
python -c "
from easecloud_errica import quick_setup, log_error
manager, handler = quick_setup()
try:
    raise ValueError('Test error')
except Exception as e:
    log_error('Test error occurred', e)
"
```

## Troubleshooting

### Common Development Issues

1. **Import errors after changes:**
```bash
pip install -e .[dev]  # Reinstall in development mode
```

2. **Test failures:**
```bash
pytest tests/ -v  # Verbose output
pytest tests/ -s   # Show print statements
```

3. **Package build issues:**
```bash
rm -rf dist/ build/ *.egg-info/  # Clean build artifacts
python -m build                  # Rebuild
```

4. **Workflow failures:**
- Check Actions tab for detailed logs
- Ensure all secrets are properly set
- Verify branch naming for automatic releases

### Getting Help

- **Issues**: https://github.com/easecloudio/easecloud-errica/issues
- **Discussions**: Use GitHub Discussions for questions
- **Documentation**: Check docs/ folder for guides
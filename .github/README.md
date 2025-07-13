# GitHub Actions Workflows

This directory contains automated workflows for the easecloud-errica package.

## Workflows

### 1. `test.yml` - Continuous Testing
**Triggers:**
- Pull requests to main
- Pushes to main (code changes only)
- Manual dispatch

**What it does:**
- Tests package across Python 3.8-3.12 and multiple OS
- Verifies import and basic functionality
- Runs example scripts
- Tests package building

### 2. `publish.yml` - Automated Publishing
**Triggers:**
- Pushes to main → Dev releases (`X.Y.Z-dev.N+sha`)
- Pushes to `release/**` branches → Beta releases (`X.Y.Z-beta.N`)
- GitHub releases → Stable releases (`X.Y.Z`)
- Manual dispatch → Any release type

**Publishing Strategy:**
- **Dev/Alpha/Beta/RC** → Test PyPI
- **Stable releases** → PyPI
- Automatic version calculation based on commits
- GitHub release creation for stable versions

### 3. `release.yml` - Manual Release Creation
**Triggers:**
- Manual dispatch only

**What it does:**
- Validates version format
- Updates version in `pyproject.toml` and `__init__.py`
- Creates git tag
- Generates changelog
- Creates GitHub release
- Triggers publish workflow

## Setup Required

### 1. PyPI API Tokens
Add these secrets to your GitHub repository:

```bash
# For stable releases
PYPI_API_TOKEN=pypi-...

# For dev/beta releases  
TEST_PYPI_API_TOKEN=pypi-...
```

### 2. GitHub Environments (Optional)
Create environments in repository settings:
- `production` - for stable releases (requires approval)
- `development` - for dev/beta releases

## Release Process

### Stable Release (Recommended)
1. Go to Actions → "Create Release"
2. Enter version (e.g., `1.0.0`)
3. Select "stable" release type
4. Run workflow
5. Workflow will:
   - Update version files
   - Create git tag
   - Create GitHub release
   - Trigger automatic PyPI publish

### Pre-release
1. Create branch: `release/v1.0.0-beta`
2. Push changes
3. Workflow automatically publishes to Test PyPI

### Development Builds
- Automatic on every push to main
- Published to Test PyPI as `X.Y.Z-dev.N+sha`

## Version Strategy

### Semantic Versioning
- `MAJOR.MINOR.PATCH` for stable releases
- `MAJOR.MINOR.PATCH-PRERELEASE.BUILD` for pre-releases

### Examples
- `1.0.0` - Stable release
- `1.0.0-beta.1` - Beta release  
- `1.0.0-alpha.5` - Alpha release
- `1.0.0-dev.123+a1b2c3d` - Development build

## Testing Strategy

### Quality Gates
All releases must pass:
- Multi-Python version testing (3.8-3.12)
- Multi-OS testing (Ubuntu, Windows, macOS)
- Import and functionality tests
- Package building verification
- Example script execution

### Test Locally
```bash
# Install in development mode
pip install -e .[dev]

# Run tests
pytest tests/

# Run examples
python examples/basic_usage.py

# Build package
python -m build
```

## Troubleshooting

### Common Issues
1. **PyPI token expired**: Update secrets in repository settings
2. **Version already exists**: Check PyPI/Test PyPI for existing versions
3. **Test failures**: Check the Actions tab for detailed logs
4. **Permission denied**: Ensure tokens have correct permissions

### Manual Override
If workflows fail, you can always publish manually:
```bash
python -m build
twine upload dist/* --repository testpypi  # or pypi
```
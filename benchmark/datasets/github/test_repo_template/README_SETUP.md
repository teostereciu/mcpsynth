# Test Repository Setup Instructions

This directory contains template files for setting up your GitHub test repository.

## Quick Setup

1. Create a new repository on GitHub (or use an existing one)
2. Set the `GITHUB_TEST_REPO` environment variable to your repo (format: `owner/repo`)
3. Copy all files from this directory to your test repository:

```bash
# Clone your test repository
git clone https://github.com/YOUR_OWNER/YOUR_REPO.git
cd YOUR_REPO

# Copy template files (adjust path as needed)
cp -r /path/to/test_repo_template/* .
cp -r /path/to/test_repo_template/.github .

# Commit and push
git add .
git commit -m "Add test files for MCP server scenarios"
git push origin main
```

## Required Files

### Workflow Files
- `.github/workflows/ci.yml` - CI workflow for testing scenarios
- `.github/workflows/deploy.yml` - Deployment workflow with manual inputs

### Source Files
- `README.md` - Repository documentation
- `src/api.py` - API module with intentional TODOs for review comments
- `src/auth.py` - Authentication module with review comment targets
- `tests/test_api.py` - Test file for PR review scenarios

### Asset Files
- `dist/app-linux.tar.gz` - Dummy binary for release testing
- `dist/app-macos.zip` - Dummy binary for release testing

## Repository Requirements

- Must have a `main` branch
- Your GitHub token must have write access
- For org-based scenarios (11, 13), additional setup is needed

## Optional Scenarios

The following scenarios require organization access and can be skipped:
- **Scenario 11:** Team Collaboration Setup (requires GitHub organization)
- **Scenario 13:** Repository Transfer and Archive (requires org or second account)

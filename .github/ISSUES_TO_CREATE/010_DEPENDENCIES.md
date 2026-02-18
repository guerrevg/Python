# 📦 DEPENDENCIES & CONFIGURATION - Priority: MEDIUM

---

## Issue #57: Outdated Dependencies in requirements.txt

### Title
[DEPENDENCIES]: Update outdated package dependencies

### Description

**What:** requirements.txt contains pinned versions that may be outdated.

**Why it matters:** 
- Security vulnerabilities in old versions
- Missing new features
- Compatibility issues

**Where:** `requirements.txt`

**Current state:**
```
fastapi==0.128.0
flask==3.1.2
torch==2.9.1
...
```

**Suggested approach:**

1. Check for outdated packages:
```bash
pip install pip-review
pip-review --local
```

2. Update with care:
```bash
# Update all
pip-review --auto

# Or update interactively
pip-review --interactive
```

3. Use compatible version specifiers:
```txt
# Good - allows patch updates
fastapi>=0.128.0,<1.0.0
flask>=3.1.2,<4.0.0

# Better - uses compatible release
fastapi~=0.128.0
flask~=3.1.2
```

**Acceptance criteria:**
- [ ] Audit all dependencies for security issues
- [ ] Update to latest compatible versions
- [ ] Use ~= for compatible releases
- [ ] Test all functionality after update
- [ ] Set up Dependabot for auto-updates

**Labels:** `dependencies`, `security`, `priority: medium`

---

## Issue #58: No Dependency Separation

### Title
[DEPENDENCIES]: Separate production and development dependencies

### Description

**What:** All dependencies in single requirements.txt file.

**Why it matters:** 
- Production installs unnecessary packages
- Larger Docker images
- Longer install times
- More attack surface

**Where:** `requirements.txt`

**Suggested approach:**

Create `requirements-dev.txt`:
```txt
# Include all production dependencies
-r requirements.txt

# Development tools
pytest>=7.4.0
pytest-cov>=4.1.0
black>=23.0.0
flake8>=6.0.0
isort>=5.12.0
mypy>=1.0.0
pre-commit>=3.0.0

# Documentation
mkdocs>=1.5.0
mkdocs-material>=9.0.0

# Debugging
ipdb>=0.13.0
```

Keep `requirements.txt` minimal:
```txt
# Core dependencies only
fastapi>=0.128.0
uvicorn>=0.23.0
flask>=3.1.2
flask-sqlalchemy>=3.1.0
pydantic>=2.0.0

# Data science
numpy>=1.24.0
pandas>=2.0.0

# ML/LLM
torch>=2.0.0
transformers>=4.30.0
```

**Acceptance criteria:**
- [ ] Create requirements-dev.txt
- [ ] Move dev-only packages
- [ ] Update installation instructions
- [ ] Update CI/CD to use both files
- [ ] Document separation

**Labels:** `dependencies`, `devex`, `priority: medium`

---

## Issue #59: No Dependency Vulnerability Scanning

### Title
[DEPENDENCIES]: Add automated dependency vulnerability scanning

### Description

**What:** No automated scanning for security vulnerabilities in dependencies.

**Why it matters:** 
- Vulnerable dependencies go undetected
- Security breaches possible
- Compliance issues

**Where:** CI/CD workflow

**Suggested approach:**

Add to `.github/workflows/security.yml`:
```yaml
name: Security Scan

on:
  push:
    branches: [main]
  schedule:
    - cron: '0 0 * * 0'  # Weekly

jobs:
  security:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'
    
    - name: Install safety
      run: pip install safety
    
    - name: Check dependencies
      run: safety check -r requirements.txt
    
    - name: Run pip-audit
      run: |
        pip install pip-audit
        pip-audit -r requirements.txt
    
    - name: Upload results
      uses: github/codeql-action/upload-sarif@v2
      if: always()
```

Also enable GitHub Dependabot:
```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
```

**Acceptance criteria:**
- [ ] Add safety scanning to CI/CD
- [ ] Add pip-audit to CI/CD
- [ ] Enable Dependabot
- [ ] Set up weekly scans
- [ ] Configure alerts for vulnerabilities

**Labels:** `dependencies`, `security`, `ci/cd`, `priority: high`

---

## Issue #60: Hardcoded Configuration Values

### Title
[CONFIGURATION]: Move hardcoded values to configuration

### Description

**What:** Configuration values hardcoded in source files.

**Why it matters:** 
- Can't change without code changes
- Different environments need different values
- Security risk if secrets hardcoded

**Where:** Multiple files

**Examples:**
```python
# fastapi/main.py
app = FastAPI(
    title="Campaign Management API",  # Hardcoded
    version="1.0.0"  # Hardcoded
)

# llm_fundamentals/weight_loading/03_gpt_download.py
base_url = "https://openaipublic.blob.core.windows.net/gpt-2/models"  # Hardcoded
```

**Suggested approach:**

Create `config.py`:
```python
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App settings
    APP_TITLE: str = "Campaign Management API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    
    # Database
    DATABASE_URL: str = "sqlite:///./campaigns.db"
    
    # LLM
    OLLAMA_MODEL: str = "llama3.2"
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    
    # Rate limiting
    RATE_LIMIT_PER_MINUTE: int = 100
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
```

Usage:
```python
from config import settings

app = FastAPI(
    title=settings.APP_TITLE,
    version=settings.APP_VERSION,
    debug=settings.DEBUG
)
```

**Acceptance criteria:**
- [ ] Create config.py with Settings class
- [ ] Move all hardcoded values
- [ ] Use environment variables
- [ ] Add .env.example
- [ ] Update all references

**Labels:** `configuration`, `security`, `priority: medium`

---

## Issue #61: No Docker Support

### Title
[CONFIGURATION]: Add Docker support for consistent environments

### Description

**What:** No Docker configuration for containerized deployment.

**Why it matters:** 
- Inconsistent development environments
- "Works on my machine" problems
- Harder deployment

**Where:** Root directory

**Suggested approach:**

Create `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Expose ports
EXPOSE 8000 5000

# Default command
CMD ["uvicorn", "fastapi.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Create `docker-compose.yml`:
```yaml
version: '3.8'

services:
  fastapi:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DEBUG=true
    volumes:
      - ./fastapi:/app/fastapi
    command: uvicorn fastapi.main:app --reload --host 0.0.0.0

  flask:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./rest_api:/app/rest_api
    command: python rest_api/main.py

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
```

Create `.dockerignore`:
```
.git
__pycache__
*.pyc
.venv
.env
*.md
```

**Acceptance criteria:**
- [ ] Create Dockerfile
- [ ] Create docker-compose.yml
- [ ] Create .dockerignore
- [ ] Document Docker usage
- [ ] Test all services run correctly

**Labels:** `configuration`, `devex`, `priority: low`

---

## Issue #62: No Python Version Specification

### Title
[CONFIGURATION]: Add Python version specification

### Description

**What:** No clear specification of required Python version.

**Why it matters:** 
- Developers may use wrong version
- Compatibility issues
- Hard to debug version-specific bugs

**Where:** Multiple locations

**Suggested approach:**

1. Add to `requirements.txt`:
```txt
python_version>="3.10"
python_version<"3.13"
```

2. Create `.python-version`:
```
3.10
3.11
3.12
```

3. Add to `pyproject.toml`:
```toml
[project]
requires-python = ">=3.10,<3.13"
```

4. Add version check to code:
```python
import sys

if sys.version_info < (3, 10):
    print("Error: Python 3.10+ required")
    sys.exit(1)
```

5. Update README:
```markdown
## Prerequisites
- Python 3.10, 3.11, or 3.12
```

**Acceptance criteria:**
- [ ] Add .python-version file
- [ ] Update pyproject.toml
- [ ] Add version check
- [ ] Update README
- [ ] Add to CI/CD matrix

**Labels:** `configuration`, `documentation`, `good first issue`

---

## Issue #63: No Unused Dependency Detection

### Title
[DEPENDENCIES]: Add automated unused dependency detection

### Description

**What:** No tooling to detect and remove unused dependencies.

**Why it matters:** 
- Bloats installation size
- Increases attack surface
- Longer install times
- Potential conflicts

**Where:** requirements.txt

**Suggested approach:**

Install and run deptry:
```bash
pip install deptry
deptry .
```

Add to CI/CD:
```yaml
- name: Check for unused dependencies
  run: |
    pip install deptry
    deptry . --exit-code 1
```

Or use pipreqs to generate minimal requirements:
```bash
pip install pipreqs
pipreqs /path/to/project --force
```

**Acceptance criteria:**
- [ ] Install deptry
- [ ] Run analysis
- [ ] Remove unused dependencies
- [ ] Add to CI/CD
- [ ] Document process

**Labels:** `dependencies`, `devex`, `priority: low`

---

# 🛠️ DEVELOPER EXPERIENCE - Priority: MEDIUM

---

## Issue #50: No Linting Configuration

### Title
[DEVEX]: Add comprehensive linting configuration

### Description

**What:** No linting configuration (flake8, pylint, black) in repository.

**Why it matters:** 
- Inconsistent code style
- Easy bugs go undetected
- Wastes code review time

**Where:** Root directory

**Suggested approach:**

Create `.flake8`:
```ini
[flake8]
max-line-length = 88
extend-ignore = E203, W503
exclude = .git,__pycache__,.venv,build,dist
max-complexity = 10
```

Create `pyproject.toml`:
```toml
[tool.black]
line-length = 88
target-version = ['py310', 'py311', 'py312']
include = '\.pyi?$'
exclude = '''
/(
    \.git
  | \.venv
  | build
  | dist
)/
'''

[tool.isort]
profile = "black"
line_length = 88
```

Add to requirements-dev.txt:
```
flake8>=6.0.0
black>=23.0.0
isort>=5.12.0
pylint>=2.17.0
mypy>=1.0.0
```

**Acceptance criteria:**
- [ ] Create .flake8 configuration
- [ ] Create pyproject.toml with black/isort
- [ ] Add pre-commit hooks
- [ ] Add lint scripts to package.json or Makefile
- [ ] Configure CI to run linters
- [ ] Add lint status badge

**Labels:** `devex`, `code quality`, `priority: medium`

---

## Issue #51: No Pre-commit Hooks

### Title
[DEVEX]: Set up pre-commit hooks for automated checks

### Description

**What:** No pre-commit hooks to catch issues before commit.

**Why it matters:** 
- Broken code gets committed
- Inconsistent formatting
- Wastes CI/CD resources

**Where:** Root directory

**Suggested approach:**

Create `.pre-commit-config.yaml`:
```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files

  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black
        language_version: python3.10

  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort

  - repo: https://github.com/pycqa/flake8
    rev: 7.0.0
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
```

Setup instructions:
```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

**Acceptance criteria:**
- [ ] Create .pre-commit-config.yaml
- [ ] Add to requirements-dev.txt
- [ ] Document setup in CONTRIBUTING.md
- [ ] Test all hooks run correctly
- [ ] Add pre-commit badge

**Labels:** `devex`, `automation`, `priority: medium`

---

## Issue #52: No Makefile for Common Tasks

### Title
[DEVEX]: Create Makefile for common development tasks

### Description

**What:** No Makefile to simplify common development commands.

**Why it matters:** 
- Developers must remember complex commands
- Inconsistent workflows
- Onboarding takes longer

**Where:** Root directory (Makefile)

**Suggested approach:**

Create `Makefile`:
```makefile
.PHONY: help install dev test lint format clean run-api

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	pip install -r requirements.txt

dev: ## Install development dependencies
	pip install -r requirements.txt -r requirements-dev.txt

test: ## Run tests
	pytest --cov=basics --cov=fastapi --cov=rest_api

lint: ## Run linters
	flake8 basics fastapi rest_api
	black --check basics fastapi rest_api
	isort --check-only basics fastapi rest_api

format: ## Format code
	black basics fastapi rest_api
	isort basics fastapi rest_api

clean: ## Clean build artifacts
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	rm -rf build/ dist/ *.egg-info/ .pytest_cache/ .coverage htmlcov/

run-fastapi: ## Run FastAPI server
	cd fastapi && uvicorn main:app --reload

run-flask: ## Run Flask server
	cd rest_api && python main.py

setup-env: ## Set up development environment
	python3 -m venv .venv
	source .venv/bin/activate
	make dev
	pre-commit install
```

**Acceptance criteria:**
- [ ] Create Makefile with common targets
- [ ] Add help command
- [ ] Document in README
- [ ] Test all targets work
- [ ] Add to CONTRIBUTING.md

**Labels:** `devex`, `automation`, `good first issue`

---

## Issue #53: No Development Environment Setup Guide

### Title
[DEVEX]: Add comprehensive development environment setup guide

### Description

**What:** No detailed guide for setting up development environment.

**Why it matters:** 
- Onboarding takes longer
- Developers miss important steps
- Inconsistent environments

**Where:** CONTRIBUTING.md or separate DEVELOPMENT.md

**Suggested approach:**

Add to CONTRIBUTING.md:
```markdown
## Development Setup

### Prerequisites
- Python 3.10, 3.11, or 3.12
- pip (Python package manager)
- Git

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/python-learning.git
cd python-learning
```

### Step 2: Create Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
# Basic dependencies
pip install -r requirements.txt

# Development dependencies
pip install -r requirements-dev.txt
```

### Step 4: Install Pre-commit Hooks
```bash
pre-commit install
```

### Step 5: Verify Setup
```bash
# Run tests
make test

# Run linters
make lint

# Start FastAPI
make run-fastapi
```

### Troubleshooting
[Link to TROUBLESHOOTING.md]
```

**Acceptance criteria:**
- [ ] Add detailed setup steps
- [ ] Include verification commands
- [ ] Add troubleshooting section
- [ ] Test on fresh machine
- [ ] Include Windows instructions

**Labels:** `devex`, `documentation`, `priority: high`

---

## Issue #54: No Environment Variable Template

### Title
[DEVEX]: Add .env.example template file

### Description

**What:** No template for required environment variables.

**Why it matters:** 
- Developers don't know what env vars needed
- Secrets accidentally committed
- Configuration confusion

**Where:** `.env.example` (new file)

**Suggested approach:**

Create `.env.example`:
```bash
# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here

# Database
DATABASE_URL=sqlite:///./travel.db

# FastAPI
API_VERSION=v1
API_PREFIX=/api

# LLM Configuration
OLLAMA_MODEL=llama3.2
OLLAMA_BASE_URL=http://localhost:11434

# Optional: Redis for caching
REDIS_URL=redis://localhost:6379/0

# Optional: API Keys (for advanced features)
OPENAI_API_KEY=
HUGGINGFACE_TOKEN=
```

Add to .gitignore:
```
.env
.env.local
.env.*.local
```

**Acceptance criteria:**
- [ ] Create .env.example
- [ ] Document all variables
- [ ] Mark required vs optional
- [ ] Add to .gitignore
- [ ] Reference in README

**Labels:** `devex`, `security`, `good first issue`

---

## Issue #55: CI/CD Workflow References Non-Existent File

### Title
[DEVEX]: Fix CI/CD workflow referencing missing environment.yml

### Description

**What:** GitHub Actions workflow references `environment.yml` which doesn't exist.

**Why it matters:** 
- CI/CD fails on every push
- Wastes CI minutes
- Blocks deployments

**Where:** `.github/workflows/python-package-conda.yml`

**Current behavior:**
```yaml
- name: Install dependencies
  run: |
    conda env update --file environment.yml --name base
    # environment.yml doesn't exist!
```

**Suggested approach:**

Option 1: Convert to pip-based workflow
```yaml
- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install -r requirements.txt
```

Option 2: Create environment.yml
```yaml
name: python-learning
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.10
  - pip
  - pip:
    - -r requirements.txt
```

**Acceptance criteria:**
- [ ] Either create environment.yml OR convert to pip
- [ ] Test workflow runs successfully
- [ ] Remove conda if not needed
- [ ] Add workflow status badge

**Labels:** `devex`, `ci/cd`, `bug`, `priority: high`

---

## Issue #56: No Error Logging

### Title
[DEVEX]: Add structured logging instead of print statements

### Description

**What:** Code uses print() instead of proper logging.

**Why it matters:** 
- Can't control log levels
- No timestamps
- Hard to debug production issues
- Can't filter by severity

**Where:** Throughout codebase

**Current behavior:**
```python
print("Error: File not found")
print("Campaign created")
```

**Suggested approach:**
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Usage
logger.error("File not found: %s", filename)
logger.info("Campaign created: %s", campaign_id)
logger.debug("Debug info: %s", data)
```

For APIs:
```python
from fastapi import HTTPException, status
import logging

logger = logging.getLogger(__name__)

@app.get("/campaigns/{id}")
async def get_campaign(id: int):
    logger.info("Fetching campaign: %d", id)
    campaign = get_from_db(id)
    if not campaign:
        logger.warning("Campaign not found: %d", id)
        raise HTTPException(status_code=404)
    logger.info("Campaign found: %d", id)
    return campaign
```

**Acceptance criteria:**
- [ ] Replace print() with logging
- [ ] Configure log levels
- [ ] Add structured logging
- [ ] Include request IDs in APIs
- [ ] Document logging configuration

**Labels:** `devex`, `enhancement`, `priority: medium`

---

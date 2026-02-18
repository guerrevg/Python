---
title: "BUG: requirement.txt has typos and issues"
labels: ["bug", "good first issue"]
---

## Issue

The requirements file has naming issues:

1. File is named `requirement.txt` (singular) - should be `requirements.txt` (plural)
2. Many commented out packages that may confuse learners
3. No organization by category

## Problems

```
#contourpy==1.3.0     # Commented with typo (# instead of # )
#ipython==9.9.0       # Why commented?
#keras==3.13.0        # Why commented?
#networkx==3.6.1      # Why commented?
```

## Fix

### 1. Rename file
```bash
git mv requirement.txt requirements.txt
```

### 2. Organize into sections
```txt
# Core Dependencies
fastapi==0.128.0
uvicorn==0.40.0
flask==3.1.2
flask-sqlalchemy==3.1.1

# Data Science
numpy==1.26.4
pandas==2.3.3
matplotlib==3.10.8

# ML/LLM
torch==2.9.1
transformers==4.57.3
tiktoken==0.12.0

# Utilities
python-dotenv==1.2.1
pydantic==2.12.5
```

### 3. Create optional requirements
```txt
# requirements-llm.txt
litgpt==0.5.12
langchain==1.2.3
llama-index==0.14.12

# requirements-dev.txt
pytest>=7.0.0
black>=24.0.0
ruff>=0.1.0
```

## Files to Update
- `requirement.txt` → `requirements.txt`
- Create `requirements-llm.txt`
- Create `requirements-dev.txt`
- Update README.md references

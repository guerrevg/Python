---
title: "CI: Add GitHub Actions workflow to run examples"
labels: ["ci/cd", "enhancement"]
---

## Issue

No CI/CD pipeline to verify examples work when code changes.

## Goal

Add GitHub Actions workflow that:
1. Installs dependencies
2. Runs basic examples
3. Validates APIs start correctly

## Workflow File

```yaml
# .github/workflows/test-examples.yml
name: Test Examples

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      
      - name: Install dependencies
        run: |
          pip install -r requirement.txt
          pip install pytest
      
      - name: Run basic examples
        run: |
          cd basics/01_introduction
          python 01_hello_world.py
          python 02_user_input_addition.py
      
      - name: Test FastAPI
        run: |
          timeout 10 uvicorn fastapi.main:app --host 0.0.0.0 &
          sleep 3
          curl http://localhost:8000/
      
      - name: Test Flask
        run: |
          timeout 10 python rest_api/main.py &
          sleep 3
          curl http://localhost:5000/
```

## Files to Create

- `.github/workflows/test-examples.yml`

## Benefits

- Catches breaking changes
- Ensures examples always work
- Builds confidence in code quality

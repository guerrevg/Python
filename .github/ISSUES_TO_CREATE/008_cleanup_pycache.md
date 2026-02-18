---
title: "CLEANUP: Remove __pycache__ folders and .pyc files"
labels: ["cleanup", "good first issue"]
---

## Issue

Repository contains `__pycache__` folders and `.pyc` files that should be in `.gitignore`.

## Problem

These are auto-generated Python bytecode files:
- Not needed in repository
- Increase repo size
- Can cause confusion

## Fix

1. Delete all `__pycache__/` folders
2. Delete all `*.pyc` files
3. Verify `.gitignore` includes:
   ```
   __pycache__/
   *.pyc
   *.pyo
   .venv/
   ```

## Command to Clean

```bash
# Find and remove all __pycache__ folders
find . -type d -name "__pycache__" -exec rm -rf {} +

# Find and remove all .pyc files
find . -name "*.pyc" -delete
```

## Prevention

Update `.gitignore` if not already present.

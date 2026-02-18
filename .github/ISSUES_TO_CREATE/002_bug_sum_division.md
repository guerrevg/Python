---
title: "BUG: Function named 'sum()' performs division instead of addition"
labels: ["bug", "good first issue"]
---

## Bug Description

The function `sum()` in `basics/09_error_handling/01_try_except.py` performs division instead of addition, which is confusing and incorrect.

## Problem

```python
def sum(a: int, b: int) -> int:
    result = a / b  # This is division, not addition!
    return result
```

Issues:
1. Function named `sum` but divides
2. Type hint says `-> int` but division returns `float`
3. Misleading for learners

## Fix

Rename function to `divide()` and fix the type hint:

```python
def divide(a: int, b: int) -> float:
    result = a / b
    return result
```

## Files
- `basics/09_error_handling/01_try_except.py`

## Testing
```bash
cd basics/09_error_handling
python 01_try_except.py
# Enter 10 and 2 → should show 5.0 (division makes sense here)
```

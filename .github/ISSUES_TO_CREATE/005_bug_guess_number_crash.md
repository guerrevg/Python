---
title: "BUG: Guess number game crashes on non-integer input"
labels: ["bug", "good first issue"]
---

## Bug Description

The guess number game crashes when user enters non-integer input.

## Problem

In `basics/11_projects/01_guess_number.py`:
```python
user_input = int(input(f"Guess the Number: "))  # Crashes on "abc"
```

## Error

```
ValueError: invalid literal for int() with base 10: 'abc'
```

## Fix

Add input validation:

```python
while True:
    try:
        user_input = int(input(f"Guess the Number: "))
        break
    except ValueError:
        print("Please enter a valid number!")
```

## Files
- `basics/11_projects/01_guess_number.py`

## Testing
```bash
cd basics/11_projects
python 01_guess_number.py
# Enter "abc" → should show error, not crash
# Enter "50" → should work normally
```

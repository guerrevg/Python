---
title: "ENHANCEMENT: Add type hints to function examples"
labels: ["enhancement", "good first issue"]
---

## Issue

Many function examples lack type hints, making it harder for learners to understand expected types.

## Current State

```python
# basics/04_functions/01_functions_basics.py
def add(a, b):
    return a + b
```

## Expected

```python
def add(a: int, b: int) -> int:
    return a + b
```

## Files to Update

Priority order:
1. `basics/04_functions/` - All function files
2. `basics/08_oop/` - Class methods
3. `basics/10_advanced/` - Lambda and modules

## Guidelines

- Add parameter types: `def func(name: str, age: int)`
- Add return types: `-> str`
- Use `Optional[str]` for values that can be None
- Use `list[int]` for lists of integers

## Example Changes

```python
# Before
def greet(name):
    return f"Hello, {name}"

# After
def greet(name: str) -> str:
    return f"Hello, {name}"
```

## Testing
Run mypy to verify:
```bash
pip install mypy
mypy basics/04_functions/*.py
```

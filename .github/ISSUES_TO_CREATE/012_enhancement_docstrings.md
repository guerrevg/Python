---
title: "ENHANCEMENT: Add docstrings to functions and classes"
labels: ["enhancement", "documentation", "good first issue"]
---

## Issue

Most functions and classes lack docstrings explaining what they do.

## Current State

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

## Expected

```python
def factorial(n: int) -> int:
    """
    Calculate factorial of a number.
    
    Args:
        n: Non-negative integer
        
    Returns:
        Factorial of n (n!)
        
    Example:
        >>> factorial(5)
        120
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

## Files to Update

1. `basics/04_functions/` - All functions
2. `basics/08_oop/` - All classes and methods
3. `fastapi/main.py` - API endpoints
4. `rest_api/main.py` - Route handlers

## Docstring Format

Use this format:
```python
def function(param: type) -> return_type:
    """One line description."""
    # Code
```

## Testing
Verify docstrings are accessible:
```python
>>> from basics.04_functions import factorial
>>> help(factorial)
```

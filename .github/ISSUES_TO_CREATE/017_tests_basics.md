---
title: "TESTING: Add basic tests for basics examples"
labels: ["testing", "enhancement", "help wanted"]
---

## Issue

No automated tests exist for basics examples. Bugs can be introduced without detection.

## Goal

Add simple tests to verify examples work correctly.

## Test Structure

```
tests/
├── __init__.py
├── test_basics/
│   ├── test_control_flow.py
│   ├── test_functions.py
│   └── test_data_structures.py
└── test_apis/
    ├── test_fastapi.py
    └── test_flask.py
```

## Example Tests

### test_control_flow.py
```python
import pytest

def test_prime_checker():
    """Test prime number checker returns correct results."""
    # Import the logic from the example
    from basics.03_control_flow.02_check_prime import is_prime
    
    assert is_prime(7) == True
    assert is_prime(10) == False
    assert is_prime(2) == True
    assert is_prime(1) == False
```

### test_functions.py
```python
def test_factorial():
    from basics.04_functions.10_factorial_loop import factorial
    
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
```

## Setup

1. Add pytest to requirements:
   ```
   pytest>=7.0.0
   ```

2. Create `tests/conftest.py`:
   ```python
   import sys
   from pathlib import Path
   
   # Add basics to path
   sys.path.insert(0, str(Path(__file__).parent.parent / 'basics'))
   ```

3. Run tests:
   ```bash
   pytest tests/ -v
   ```

## Priority Files to Test

1. `basics/03_control_flow/02_check_prime.py`
2. `basics/04_functions/10_factorial_loop.py`
3. `basics/05_data_structures/` - List operations
4. `basics/11_projects/` - Game logic

## Getting Started

Start with 2-3 simple test files, then expand.

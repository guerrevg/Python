---
name: ✨ Add Type Hints
about: Add comprehensive type hints to all Python code
title: '[ENHANCEMENT] Add type hints to all Python files'
labels: ['enhancement', 'refactor', 'intermediate']
assignees: ''
---

## 📋 Issue Description

Most Python files lack type hints, missing out on:
- IDE autocomplete
- Type checking with mypy
- Better documentation
- Early bug detection

## 🔍 Current State

```python
# Current (no types)
def add(a, b):
    return a + b

def greet(name):
    print(f"Hello {name}")
```

## ✅ Expected State

```python
# With type hints
def add(a: int | float, b: int | float) -> int | float:
    """Add two numbers"""
    return a + b

def greet(name: str) -> None:
    """Greet a person"""
    print(f"Hello {name}")
```

## 📝 Tasks

### Phase 1: Basics (Beginner-Friendly)

- [ ] Add type hints to `01_introduction/`
- [ ] Add type hints to `02_variables_types/`
- [ ] Add type hints to `03_control_flow/`
- [ ] Add type hints to `04_functions/`

### Phase 2: Intermediate Topics

- [ ] Add type hints to `05_data_structures/`
- [ ] Add type hints to `06_strings/`
- [ ] Add type hints to `07_file_handling/`
- [ ] Add type hints to `08_oop/`

### Phase 3: Advanced Topics

- [ ] Add type hints to `09_error_handling/`
- [ ] Add type hints to `10_advanced/`
- [ ] Add type hints to `11_projects/`
- [ ] Add type hints to `12_web/`

### Phase 4: APIs & LLM

- [ ] Add type hints to `fastapi/`
- [ ] Add type hints to `rest_api/`
- [ ] Add type hints to `llm_fundamentals/`

## 🎯 Type Hint Standards

### Basic Types
```python
def greet(name: str) -> str:
    return f"Hello {name}"

def add(a: int, b: int) -> int:
    return a + b

def divide(a: float, b: float) -> float:
    return a / b
```

### Collections
```python
from typing import List, Dict, Tuple, Set

def process_items(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}

def get_coordinates() -> Tuple[int, int, int]:
    return (x, y, z)
```

### Optional & Union
```python
from typing import Optional, Union

def greet(name: Optional[str] = None) -> str:
    if name is None:
        return "Hello stranger"
    return f"Hello {name}"

def process(value: Union[int, str, float]) -> str:
    return str(value)
```

### Classes
```python
class Calculator:
    def __init__(self, initial_value: float = 0) -> None:
        self.value: float = initial_value
    
    def add(self, amount: float) -> None:
        self.value += amount
    
    def get_value(self) -> float:
        return self.value
```

## 💡 Tools

### mypy Configuration
```ini
# mypy.ini
[mypy]
python_version = 3.10
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = False  # Start lenient
```

### Run Type Checking
```bash
# Install mypy
pip install mypy

# Check types
mypy basics/
mypy fastapi/
mypy rest_api/

# With configuration
mypy --config-file mypy.ini .
```

## 🎯 Why This Matters

- **IDE Support**: Better autocomplete
- **Bug Prevention**: Catch type errors early
- **Documentation**: Self-documenting code
- **Professionalism**: Industry standard
- **Learning**: Teach modern Python

## ⚠️ Risk Assessment

**Low Risk:**
- Type hints don't change runtime
- Can be added incrementally
- Backward compatible

## 📝 Difficulty

**Intermediate** - Requires type hint knowledge

## 🔗 Related

- Docstrings: #21
- Code quality: #23
- Testing: #20

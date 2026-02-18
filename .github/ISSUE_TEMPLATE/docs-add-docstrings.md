---
name: 📚 Add Missing Docstrings
about: Add comprehensive docstrings to all functions and classes
title: '[DOCS] Add docstrings to all Python files'
labels: ['documentation', 'enhancement', 'good first issue']
assignees: ''
---

## 📋 Issue Description

Many Python files lack proper docstrings, making them harder to understand and learn from.

## 🔍 Current State

### Files Without Docstrings

**High Priority (Functions/Classes):**
- `basics/04_functions/*.py` - Function examples need docs
- `basics/08_oop/*.py` - Class examples need docs
- `basics/10_advanced/*.py` - Advanced concepts need explanation

**Medium Priority:**
- `basics/11_projects/*.py` - Project files need docs
- `basics/12_web/*.py` - Web examples need docs

### Example of Missing Docs

```python
# Current
def sum(a, b):
    sum = a + b
    return sum

# Should be
def sum(a, b):
    """
    Calculate the sum of two numbers.
    
    Args:
        a (int|float): First number
        b (int|float): Second number
    
    Returns:
        int|float: Sum of a and b
    
    Example:
        >>> sum(2, 3)
        5
    """
    return a + b
```

## ✅ Tasks

### Priority 1: Functions & Classes
- [ ] Add docstrings to all functions
- [ ] Add docstrings to all classes
- [ ] Include Args, Returns, Examples

### Priority 2: Modules
- [ ] Add module-level docstrings
- [ ] Explain file purpose
- [ ] Link to related concepts

### Priority 3: Complex Code
- [ ] Add inline comments
- [ ] Explain algorithms
- [ ] Document edge cases

## 📝 Docstring Standard

Use Google-style docstrings:

```python
def function_name(param1, param2):
    """Short description.
    
    Longer description if needed.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    
    Raises:
        ValueError: When something goes wrong
    
    Example:
        >>> function_name(1, 2)
        3
    """
```

## 🎯 Why This Matters

- **Learning**: Clearer explanations
- **IDE Support**: Better autocomplete
- **Documentation**: Auto-generate docs
- **Professionalism**: Industry standard

## 💡 Tools

- Use `pydocstyle` to check: `pydocstyle basics/`
- Use `black` for formatting
- Use `mypy` for type checking

## ⚠️ Risk Assessment

**No Risk:**
- Adding documentation only
- No code logic changes
- Improves code quality

## 📝 Difficulty

**Beginner** - Add comments and docstrings

## 🔗 Related

- Type hints: #22
- Code quality: #23

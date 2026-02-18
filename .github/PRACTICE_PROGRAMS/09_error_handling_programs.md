# Practice Programs: Error Handling (09_error_handling)

**Total Programs:** 12 | **Easy:** 6 | **Medium:** 4 | **Hard:** 2

---

## Easy Programs (1-6)

### 001 - Basic Try-Except
**Difficulty:** Easy  
**Description:** Handle division by zero error.  
**Learning:** `try-except` block  
**Expected:** Graceful error message

### 002 - Handle ValueError
**Difficulty:** Easy  
**Description:** Handle invalid number input.  
**Learning:** `ValueError` exception  
**Expected:** `Please enter a valid number`

### 003 - Multiple Except Blocks
**Difficulty:** Easy  
**Description:** Handle different errors differently.  
**Learning:** Multiple `except` clauses  
**Expected:** Specific error messages

### 004 - Else Clause
**Difficulty:** Easy  
**Description:** Use `else` when no exception occurs.  
**Learning:** `try-except-else`  
**Expected:** Success message on no error

### 005 - Finally Clause
**Difficulty:** Easy  
**Description:** Use `finally` for cleanup code.  
**Learning:** `try-finally`  
**Expected:** Always executes

### 006 - Raise Exception
**Difficulty:** Easy  
**Description:** Raise custom exception manually.  
**Learning:** `raise` statement  
**Expected:** Custom error thrown

---

## Medium Programs (7-10)

### 007 - Custom Exception Class
**Difficulty:** Medium  
**Description:** Create custom exception type.  
**Learning:** Inherit from `Exception`  
**Expected:** `InvalidAgeError`

### 008 - Validate Email Function
**Difficulty:** Medium  
**Description:** Raise error for invalid email format.  
**Learning:** Validation with exceptions  
**Expected:** `InvalidEmailError`

### 009 - Safe File Reader
**Difficulty:** Medium  
**Description:** Read file with comprehensive error handling.  
**Learning:** Multiple error types  
**Expected:** Handle all file errors

### 010 - ATM with Error Handling
**Difficulty:** Medium  
**Description:** ATM simulation with validation.  
**Learning:** Business logic exceptions  
**Expected:** `InsufficientFundsError`

---

## Hard Programs (11-12)

### 011 - Robust Calculator
**Difficulty:** Hard  
**Description:** Calculator handling all edge cases.  
**Learning:** Comprehensive validation  
**Expected:** Never crashes, always helpful error

### 012 - Data Validation Framework
**Difficulty:** Hard  
**Description:** Generic validator with custom exceptions.  
**Learning:** Exception hierarchy  
**Expected:** Reusable validation system

---

## Files to Create

```
basics/09_error_handling/
├── easy/
│   ├── 01_basic_try_except.py
│   ├── 02_handle_value_error.py
│   ├── 03_multiple_excepts.py
│   ├── 04_else_clause.py
│   ├── 05_finally_clause.py
│   └── 06_raise_exception.py
├── medium/
│   ├── 07_custom_exception_class.py
│   ├── 08_validate_email.py
│   ├── 09_safe_file_reader.py
│   └── 10_atm_simulation.py
└── hard/
    ├── 11_robust_calculator.py
    └── 12_validation_framework.py
```

## Custom Exceptions to Define

```python
class InvalidAgeError(Exception):
    """Raised when age is invalid"""
    pass

class InvalidEmailError(Exception):
    """Raised when email format is invalid"""
    pass

class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds"""
    pass

class ValidationError(Exception):
    """Base class for validation errors"""
    pass
```

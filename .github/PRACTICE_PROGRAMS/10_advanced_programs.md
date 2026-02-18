# Practice Programs: Advanced Topics (10_advanced)

**Total Programs:** 18 | **Easy:** 8 | **Medium:** 7 | **Hard:** 3

---

## Easy Programs (1-8)

### 001 - Lambda: Add Two Numbers
**Difficulty:** Easy  
**Description:** Create lambda to add two numbers.  
**Learning:** Lambda syntax  
**Expected:** `add = lambda a, b: a + b`

### 002 - Lambda: Square Number
**Difficulty:** Easy  
**Description:** Lambda to calculate square.  
**Learning:** Single expression lambda  
**Expected:** `square = lambda x: x**2`

### 003 - Map: Square All Numbers
**Difficulty:** Easy  
**Description:** Use map to square all numbers in list.  
**Learning:** `map()` function  
**Expected:** `[1, 4, 9, 16, 25]`

### 004 - Filter: Even Numbers
**Difficulty:** Easy  
**Description:** Filter even numbers from list.  
**Learning:** `filter()` function  
**Expected:** `[2, 4, 6, 8, 10]`

### 005 - Reduce: Sum of List
**Difficulty:** Easy  
**Description:** Use reduce to sum all elements.  
**Learning:** `functools.reduce()`  
**Expected:** `15` for `[1,2,3,4,5]`

### 006 - Import Custom Module
**Difficulty:** Easy  
**Description:** Create and import custom module.  
**Learning:** Module creation, `import`  
**Expected:** Functions from module work

### 007 - Use Built-in Module
**Difficulty:** Easy  
**Description:** Use `math` or `random` module.  
**Learning:** Standard library  
**Expected:** `math.sqrt(16)` → `4.0`

### 008 - Match-Case: Day Name
**Difficulty:** Easy  
**Description:** Convert day number to name using match.  
**Learning:** `match-case` statement  
**Expected:** `1` → `Monday`

---

## Medium Programs (9-15)

### 009 - Lambda with Sort
**Difficulty:** Medium  
**Description:** Sort list of tuples by second element.  
**Learning:** Lambda as key function  
**Expected:** Sorted by custom criteria

### 010 - Map with Multiple Iterables
**Difficulty:** Medium  
**Description:** Map function over two lists.  
**Learning:** `map(func, list1, list2)`  
**Expected:** Element-wise operation

### 011 - Filter and Map Combined
**Difficulty:** Medium  
**Description:** Filter then map in chain.  
**Learning:** Function composition  
**Expected:** Transformed filtered data

### 012 - Reduce: Find Maximum
**Difficulty:** Medium  
**Description:** Use reduce to find max in list.  
**Learning:** Reduce with comparison  
**Expected:** Maximum value

### 013 - Decorator: Timing Function
**Difficulty:** Medium  
**Description:** Create decorator to measure execution time.  
**Learning:** Function decorators  
**Expected:** Prints execution time

### 014 - Decorator: Logging
**Difficulty:** Medium  
**Description:** Create decorator to log function calls.  
**Learning:** Decorator with arguments  
**Expected:** Logs function name and args

### 015 - Generator: Number Sequence
**Difficulty:** Medium  
**Description:** Create generator for number sequence.  
**Learning:** `yield` keyword  
**Expected:** Lazy sequence generation

---

## Hard Programs (16-18)

### 016 - Decorator: Retry Mechanism
**Difficulty:** Hard  
**Description:** Retry function on failure N times.  
**Learning:** Decorator with parameters  
**Expected:** Automatic retry on error

### 017 - Generator: Fibonacci Infinite
**Difficulty:** Hard  
**Description:** Infinite Fibonacci generator.  
**Learning:** Infinite generators  
**Expected:** Yields forever until stopped

### 018 - Context Manager: Timer
**Difficulty:** Hard  
**Description:** Create context manager for timing code.  
**Learning:** `__enter__`, `__exit__`  
**Expected:** `with Timer():` prints duration

---

## Files to Create

```
basics/10_advanced/
├── lambda/
│   ├── 01_lambda_add.py
│   ├── 02_lambda_square.py
│   └── 09_lambda_sort.py
├── map_filter_reduce/
│   ├── 03_map_squares.py
│   ├── 04_filter_even.py
│   ├── 05_reduce_sum.py
│   ├── 10_map_multiple.py
│   ├── 11_filter_map_combined.py
│   └── 12_reduce_maximum.py
├── modules/
│   ├── 06_import_custom.py
│   ├── mymodule.py
│   └── 07_use_builtin.py
├── match_case/
│   └── 08_day_name.py
├── decorators/
│   ├── 13_decorator_timing.py
│   ├── 14_decorator_logging.py
│   └── 16_decorator_retry.py
└── generators/
    ├── 15_generator_sequence.py
    ├── 17_generator_fibonacci.py
    └── 18_context_manager_timer.py
```

# Practice Programs: Functions (04_functions)

**Total Programs:** 20 | **Easy:** 10 | **Medium:** 7 | **Hard:** 3

---

## Easy Programs (1-10)

### 001 - Greet Function
**Difficulty:** Easy  
**Description:** Create function that greets a person by name.  
**Learning:** Function definition, parameters  
**Expected:** `greet("Alice")` → `Hello, Alice!`

### 002 - Add Function
**Difficulty:** Easy  
**Description:** Function to add two numbers.  
**Learning:** Parameters, return statement  
**Expected:** `add(5, 3)` → `8`

### 003 - Is Even Function
**Difficulty:** Easy  
**Description:** Function that returns True if number is even.  
**Learning:** Boolean return values  
**Expected:** `is_even(4)` → `True`

### 004 - Max of Two
**Difficulty:** Easy  
**Description:** Function returning larger of two numbers.  
**Learning:** Conditional return  
**Expected:** `max_of_two(10, 20)` → `20`

### 005 - Square Function
**Difficulty:** Easy  
**Description:** Function to calculate square of a number.  
**Learning:** Single parameter, return  
**Expected:** `square(7)` → `49`

### 006 - Area of Circle
**Difficulty:** Easy  
**Description:** Function to calculate circle area from radius.  
**Learning:** Using math constants  
**Expected:** `area_circle(5)` → `78.54`

### 007 - Convert to Uppercase
**Difficulty:** Easy  
**Description:** Function to convert string to uppercase.  
**Learning:** String methods in functions  
**Expected:** `to_upper("hello")` → `"HELLO"`

### 008 - Calculate Discount
**Difficulty:** Easy  
**Description:** Function to calculate discounted price.  
**Learning:** Percentage calculations  
**Expected:** `discount(100, 20)` → `80`

### 009 - Concatenate Strings
**Difficulty:** Easy  
**Description:** Function to join two strings with space.  
**Learning:** String concatenation  
**Expected:** `join_strings("Hello", "World")` → `"Hello World"`

### 010 - Is Positive
**Difficulty:** Easy  
**Description:** Function checking if number is positive.  
**Learning:** Boolean logic  
**Expected:** `is_positive(5)` → `True`

---

## Medium Programs (11-17)

### 011 - Factorial Function
**Difficulty:** Medium  
**Description:** Recursive function to calculate factorial.  
**Learning:** Recursion, base case  
**Expected:** `factorial(5)` → `120`

### 012 - Fibonacci Function
**Difficulty:** Medium  
**Description:** Recursive function for nth Fibonacci number.  
**Learning:** Recursive calls  
**Expected:** `fibonacci(7)` → `13`

### 013 - Sum of Natural Numbers
**Difficulty:** Medium  
**Description:** Recursive sum from 1 to n.  
**Learning:** Recursive accumulation  
**Expected:** `sum_natural(10)` → `55`

### 014 - Is Prime Function
**Difficulty:** Medium  
**Description:** Function to check if number is prime.  
**Learning:** Helper functions, optimization  
**Expected:** `is_prime(17)` → `True`

### 015 - Power Function
**Difficulty:** Medium  
**Description:** Calculate base^exponent without `**` operator.  
**Learning:** Loop in function  
**Expected:** `power(2, 5)` → `32`

### 016 - Find LCM
**Difficulty:** Medium  
**Description:** Function to find LCM of two numbers.  
**Learning:** Multiple functions, GCD usage  
**Expected:** `lcm(12, 18)` → `36`

### 017 - Celsius to Fahrenheit
**Difficulty:** Medium  
**Description:** Function with formula implementation.  
**Learning:** Mathematical functions  
**Expected:** `c_to_f(0)` → `32.0`

---

## Hard Programs (18-20)

### 018 - Quick Sort Implementation
**Difficulty:** Hard  
**Description:** Implement quicksort algorithm as function.  
**Learning:** Recursion, list manipulation  
**Expected:** `quicksort([3,1,4,1,5])` → `[1,1,3,4,5]`

### 019 - Binary Search
**Difficulty:** Hard  
**Description:** Implement binary search recursively.  
**Learning:** Divide and conquer recursion  
**Expected:** `binary_search([1,3,5,7], 5)` → `2`

### 020 - Memoized Fibonacci
**Difficulty:** Hard  
**Description:** Optimized Fibonacci with memoization.  
**Learning:** Decorators, caching  
**Expected:** `fib_memo(100)` → Fast calculation

---

## Files to Create

```
basics/04_functions/
├── easy/
│   ├── 01_greet.py
│   ├── 02_add.py
│   ├── 03_is_even.py
│   ├── 04_max_of_two.py
│   ├── 05_square.py
│   ├── 06_area_circle.py
│   ├── 07_to_uppercase.py
│   ├── 08_calculate_discount.py
│   ├── 09_concatenate.py
│   └── 10_is_positive.py
├── medium/
│   ├── 11_factorial_recursive.py
│   ├── 12_fibonacci_recursive.py
│   ├── 13_sum_natural_recursive.py
│   ├── 14_is_prime.py
│   ├── 15_power_function.py
│   ├── 16_find_lcm.py
│   └── 17_celsius_to_fahrenheit.py
└── hard/
    ├── 18_quicksort.py
    ├── 19_binary_search.py
    └── 20_memoized_fibonacci.py
```

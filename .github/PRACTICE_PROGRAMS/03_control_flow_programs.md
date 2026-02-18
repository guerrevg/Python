# Practice Programs: Control Flow (03_control_flow)

**Total Programs:** 25 | **Easy:** 15 | **Medium:** 7 | **Hard:** 3

---

## Easy Programs (1-15)

### 001 - Largest of Two Numbers
**Difficulty:** Easy  
**Description:** Find the larger of two numbers using if-else.  
**Learning:** `if-else` statements  
**Expected:** `Larger number is 15`

### 002 - Vote Eligibility Checker
**Difficulty:** Easy  
**Description:** Check if person is eligible to vote (age >= 18).  
**Learning:** Comparison with if  
**Expected:** `Eligible to vote` or `Not eligible`

### 003 - Pass or Fail
**Difficulty:** Easy  
**Description:** Check if student passed (marks >= 35).  
**Learning:** Simple conditionals  
**Expected:** `Result: Pass`

### 004 - Absolute Value
**Difficulty:** Easy  
**Description:** Convert negative number to positive.  
**Learning:** Conditional negation  
**Expected:** `Absolute value: 5`

### 005 - Leap Year Checker
**Difficulty:** Easy  
**Description:** Check if year is a leap year.  
**Learning:** Divisibility rules, nested if  
**Expected:** `2024 is a leap year`

### 006 - Day of Week
**Difficulty:** Easy  
**Description:** Print day name from number (1-7).  
**Learning:** `if-elif-else` chain  
**Expected:** `Day: Monday`

### 007 - Grade Calculator
**Difficulty:** Easy  
**Description:** Assign grade based on marks (A, B, C, D, F).  
**Learning:** Multiple elif conditions  
**Expected:** `Grade: B`

### 008 - Count from 1 to N
**Difficulty:** Easy  
**Description:** Print numbers from 1 to N using for loop.  
**Learning:** `for` loop, `range()`  
**Expected:** `1 2 3 4 5`

### 009 - Print Even Numbers
**Difficulty:** Easy  
**Description:** Print even numbers from 1 to N.  
**Learning:** Loop with condition  
**Expected:** `2 4 6 8 10`

### 010 - Multiplication Table
**Difficulty:** Easy  
**Description:** Print multiplication table of a number.  
**Learning:** Loop with multiplication  
**Expected:** `5 x 1 = 5, 5 x 2 = 10...`

### 011 - Sum of First N Numbers
**Difficulty:** Easy  
**Description:** Calculate sum using loop.  
**Learning:** Accumulator pattern  
**Expected:** `Sum of 1-10: 55`

### 012 - Factorial Using Loop
**Difficulty:** Easy  
**Description:** Calculate factorial iteratively.  
**Learning:** Loop multiplication  
**Expected:** `5! = 120`

### 013 - Reverse a Number
**Difficulty:** Easy  
**Description:** Reverse digits of a number.  
**Learning:** While loop, modulus  
**Expected:** `Reverse of 123 is 321`

### 014 - Count Digits
**Difficulty:** Easy  
**Description:** Count number of digits in an integer.  
**Learning:** While loop, division  
**Expected:** `Digits: 3`

### 015 - Sum of Digits
**Difficulty:** Easy  
**Description:** Add all digits of a number.  
**Learning:** Modulus, accumulation  
**Expected:** `Sum of digits: 6`

---

## Medium Programs (16-22)

### 016 - Fibonacci Sequence
**Difficulty:** Medium  
**Description:** Print first N Fibonacci numbers.  
**Learning:** Sequence generation, variables swap  
**Expected:** `0 1 1 2 3 5 8 13`

### 017 - Prime Number Checker
**Difficulty:** Medium  
**Description:** Check if a number is prime.  
**Learning:** Loop with flag, optimization  
**Expected:** `17 is prime`

### 018 - Armstrong Number
**Difficulty:** Medium  
**Description:** Check if number equals sum of cubes of digits.  
**Learning:** Digit extraction, powers  
**Expected:** `153 is an Armstrong number`

### 019 - Palindrome Number
**Difficulty:** Medium  
**Description:** Check if number reads same forwards/backwards.  
**Learning:** Reverse and compare  
**Expected:** `121 is a palindrome`

### 020 - Pattern: Right Triangle
**Difficulty:** Medium  
**Description:** Print right triangle star pattern.  
**Learning:** Nested loops  
**Expected:**
```
*
**
***
****
```

### 021 - Pattern: Pyramid
**Difficulty:** Medium  
**Description:** Print pyramid star pattern.  
**Learning:** Complex nested loops  
**Expected:**
```
   *
  ***
 *****
*******
```

### 022 - GCD of Two Numbers
**Difficulty:** Medium  
**Description:** Find greatest common divisor.  
**Learning:** Euclidean algorithm  
**Expected:** `GCD of 48 and 18 is 6`

---

## Hard Programs (23-25)

### 023 - Pattern: Hollow Square
**Difficulty:** Hard  
**Description:** Print hollow square pattern.  
**Learning:** Complex conditionals in loops  
**Expected:**
```
*****
*   *
*   *
*****
```

### 024 - Number Pattern
**Difficulty:** Hard  
**Description:** Print number pyramid pattern.  
**Learning:** Complex nested loops  
**Expected:**
```
    1
   121
  12321
 1234321
```

### 025 - Prime Numbers in Range
**Difficulty:** Hard  
**Description:** Find all primes between two numbers.  
**Learning:** Nested loops, optimization  
**Expected:** `Primes between 1-50: 2, 3, 5, 7, 11...`

---

## Files to Create

```
basics/03_control_flow/
├── if_else/
│   ├── 01_largest_two.py
│   ├── 02_vote_eligibility.py
│   ├── 03_pass_fail.py
│   ├── 04_absolute_value.py
│   ├── 05_leap_year.py
│   ├── 06_day_of_week.py
│   └── 07_grade_calculator.py
├── for_loops/
│   ├── 08_count_1_to_n.py
│   ├── 09_print_even.py
│   ├── 10_multiplication_table.py
│   └── 11_sum_first_n.py
├── while_loops/
│   ├── 12_factorial.py
│   ├── 13_reverse_number.py
│   ├── 14_count_digits.py
│   └── 15_sum_of_digits.py
├── medium/
│   ├── 16_fibonacci.py
│   ├── 17_prime_checker.py
│   ├── 18_armstrong.py
│   ├── 19_palindrome.py
│   ├── 20_pattern_triangle.py
│   ├── 21_pattern_pyramid.py
│   └── 22_gcd.py
└── hard/
    ├── 23_pattern_hollow_square.py
    ├── 24_pattern_number.py
    └── 25_primes_in_range.py
```

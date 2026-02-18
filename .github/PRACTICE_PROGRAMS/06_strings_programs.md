# Practice Programs: Strings (06_strings)

**Total Programs:** 20 | **Easy:** 12 | **Medium:** 5 | **Hard:** 3

---

## Easy Programs (1-12)

### 001 - String Length
**Difficulty:** Easy  
**Description:** Find length of input string.  
**Learning:** `len()` function  
**Expected:** `Length: 13` for "Hello, World!"

### 002 - Uppercase Conversion
**Difficulty:** Easy  
**Description:** Convert string to uppercase.  
**Learning:** `.upper()` method  
**Expected:** `HELLO WORLD`

### 003 - Lowercase Conversion
**Difficulty:** Easy  
**Description:** Convert string to lowercase.  
**Learning:** `.lower()` method  
**Expected:** `hello world`

### 004 - String Concatenation
**Difficulty:** Easy  
**Description:** Join two strings together.  
**Learning:** `+` operator  
**Expected:** `HelloWorld`

### 005 - String Slicing
**Difficulty:** Easy  
**Description:** Extract first 5 characters.  
**Learning:** `[start:end]` syntax  
**Expected:** `Hello` from "Hello World"

### 006 - Reverse String
**Difficulty:** Easy  
**Description:** Reverse a string using slicing.  
**Learning:** `[::-1]` slice  
**Expected:** `dlroW olleH`

### 007 - Count Vowels
**Difficulty:** Easy  
**Description:** Count vowels in a string.  
**Learning:** Loop, conditionals  
**Expected:** `Vowels: 3`

### 008 - Count Consonants
**Difficulty:** Easy  
**Description:** Count consonants in a string.  
**Learning:** Character classification  
**Expected:** `Consonants: 7`

### 009 - Replace Character
**Difficulty:** Easy  
**Description:** Replace all spaces with hyphens.  
**Learning:** `.replace()` method  
**Expected:** `Hello-World`

### 010 - Check Substring
**Difficulty:** Easy  
**Description:** Check if word exists in sentence.  
**Learning:** `in` operator  
**Expected:** `True` or `False`

### 011 - String Comparison
**Difficulty:** Easy  
**Description:** Compare two strings ignoring case.  
**Learning:** `.lower()`, `==`  
**Expected:** `Strings are equal`

### 012 - Split String
**Difficulty:** Easy  
**Description:** Split sentence into words.  
**Learning:** `.split()` method  
**Expected:** `['Hello', 'World']`

---

## Medium Programs (13-17)

### 013 - Palindrome Checker
**Difficulty:** Medium  
**Description:** Check if string is palindrome.  
**Learning:** Reverse and compare  
**Expected:** `madam is a palindrome`

### 014 - Anagram Checker
**Difficulty:** Medium  
**Description:** Check if two strings are anagrams.  
**Learning:** Sorting, comparison  
**Expected:** `listen and silent are anagrams`

### 015 - Title Case Converter
**Difficulty:** Medium  
**Description:** Convert string to title case without `.title()`.  
**Learning:** Character manipulation  
**Expected:** `Hello World How Are You`

### 016 - Remove Duplicates from String
**Difficulty:** Medium  
**Description:** Remove duplicate characters preserving order.  
**Learning:** Set with order  
**Expected:** `hello` → `helo`

### 017 - Character Frequency
**Difficulty:** Medium  
**Description:** Count frequency of each character.  
**Learning:** Dictionary counting  
**Expected:** `{'h': 1, 'e': 1, 'l': 2, 'o': 1}`

---

## Hard Programs (18-20)

### 018 - Run-Length Encoding
**Difficulty:** Hard  
**Description:** Compress string using run-length encoding.  
**Learning:** String compression algorithm  
**Expected:** `aaabbcccc` → `a3b2c4`

### 019 - Longest Word in Sentence
**Difficulty:** Hard  
**Description:** Find longest word and its length.  
**Learning:** String parsing, tracking  
**Expected:** `Longest: programming (11 chars)`

### 020 - String Permutation Checker
**Difficulty:** Hard  
**Description:** Check if one string is permutation of another.  
**Learning:** Character counting  
**Expected:** `abc and bca are permutations`

---

## Files to Create

```
basics/06_strings/
├── easy/
│   ├── 01_string_length.py
│   ├── 02_uppercase.py
│   ├── 03_lowercase.py
│   ├── 04_concatenation.py
│   ├── 05_slicing.py
│   ├── 06_reverse.py
│   ├── 07_count_vowels.py
│   ├── 08_count_consonants.py
│   ├── 09_replace_char.py
│   ├── 10_check_substring.py
│   ├── 11_compare_strings.py
│   └── 12_split_string.py
├── medium/
│   ├── 13_palindrome.py
│   ├── 14_anagram_checker.py
│   ├── 15_title_case.py
│   ├── 16_remove_duplicates.py
│   └── 17_char_frequency.py
└── hard/
    ├── 18_run_length_encoding.py
    ├── 19_longest_word.py
    └── 20_permutation_checker.py
```

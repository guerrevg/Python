# Practice Programs: Data Structures (05_data_structures)

**Total Programs:** 25 | **Easy:** 15 | **Medium:** 7 | **Hard:** 3

---

## Easy Programs (1-15)

### 001 - Create and Print List
**Difficulty:** Easy  
**Description:** Create a list of 5 fruits and print it.  
**Learning:** List creation, printing  
**Expected:** `['apple', 'banana', 'cherry', 'date', 'elderberry']`

### 002 - Access List Elements
**Difficulty:** Easy  
**Description:** Access first, middle, and last elements.  
**Learning:** Indexing, negative indexing  
**Expected:** `First: apple, Last: elderberry`

### 003 - Append to List
**Difficulty:** Easy  
**Description:** Add new item to end of list.  
**Learning:** `append()` method  
**Expected:** List with new item added

### 004 - Insert in List
**Difficulty:** Easy  
**Description:** Insert item at specific position.  
**Learning:** `insert()` method  
**Expected:** Item at specified index

### 005 - Remove from List
**Difficulty:** Easy  
**Description:** Remove item by value.  
**Learning:** `remove()` method  
**Expected:** List without the item

### 006 - List Slicing
**Difficulty:** Easy  
**Description:** Extract sublist using slicing.  
**Learning:** `[start:end:step]` syntax  
**Expected:** Sublist with selected elements

### 007 - List Length
**Difficulty:** Easy  
**Description:** Find number of elements in list.  
**Learning:** `len()` function  
**Expected:** `Length: 5`

### 008 - List Sum and Average
**Difficulty:** Easy  
**Description:** Calculate sum and average of number list.  
**Learning:** `sum()`, division  
**Expected:** `Sum: 50, Average: 10.0`

### 009 - Find Maximum and Minimum
**Difficulty:** Easy  
**Description:** Find max and min in list without built-ins.  
**Learning:** Loop comparison  
**Expected:** `Max: 100, Min: 5`

### 010 - List Reversal
**Difficulty:** Easy  
**Description:** Reverse a list without using reverse().  
**Learning:** Slicing `[::-1]`, or loop  
**Expected:** Reversed list

### 011 - Create Tuple
**Difficulty:** Easy  
**Description:** Create tuple of coordinates (x, y).  
**Learning:** Tuple creation, immutability  
**Expected:** `(5, 10)`

### 012 - Tuple Unpacking
**Difficulty:** Easy  
**Description:** Unpack tuple into variables.  
**Learning:** `x, y = tuple`  
**Expected:** `x=5, y=10`

### 013 - Create Set
**Difficulty:** Easy  
**Description:** Create set from list with duplicates.  
**Learning:** Set removes duplicates  
**Expected:** `{1, 2, 3, 4, 5}`

### 014 - Set Operations
**Difficulty:** Easy  
**Description:** Perform union and intersection.  
**Learning:** `|`, `&` operators  
**Expected:** Union and intersection results

### 015 - Create Dictionary
**Difficulty:** Easy  
**Description:** Create dictionary of student names and grades.  
**Learning:** Dict creation, key-value pairs  
**Expected:** `{'Alice': 95, 'Bob': 87}`

---

## Medium Programs (16-22)

### 016 - List Comprehension: Squares
**Difficulty:** Medium  
**Description:** Create list of squares using comprehension.  
**Learning:** `[x**2 for x in range(10)]`  
**Expected:** `[0, 1, 4, 9, 16, ...]`

### 017 - Filter Even Numbers
**Difficulty:** Medium  
**Description:** Filter even numbers from list using comprehension.  
**Learning:** Conditional comprehension  
**Expected:** `[2, 4, 6, 8, 10]`

### 018 - Flatten Nested List
**Difficulty:** Medium  
**Description:** Convert 2D list to 1D list.  
**Learning:** Nested comprehension  
**Expected:** `[[1,2],[3,4]]` → `[1,2,3,4]`

### 019 - Count Word Frequency
**Difficulty:** Medium  
**Description:** Count occurrences of each word in sentence.  
**Learning:** Dictionary for counting  
**Expected:** `{'hello': 2, 'world': 1}`

### 020 - Remove Duplicates
**Difficulty:** Medium  
**Description:** Remove duplicates while preserving order.  
**Learning:** Set with order preservation  
**Expected:** `[1,2,3,4,5]` from `[1,2,2,3,3,3,4,5]`

### 021 - Merge Two Dictionaries
**Difficulty:** Medium  
**Description:** Merge two dictionaries into one.  
**Learning:** `update()`, `**` unpacking  
**Expected:** Merged dictionary

### 022 - Dictionary from Two Lists
**Difficulty:** Medium  
**Description:** Create dict from keys and values lists.  
**Learning:** `zip()`, `dict()`  
**Expected:** `{'a': 1, 'b': 2, 'c': 3}`

---

## Hard Programs (23-25)

### 023 - Matrix Operations
**Difficulty:** Hard  
**Description:** Add, multiply two matrices.  
**Learning:** Nested lists, nested loops  
**Expected:** Result matrix

### 024 - Group Anagrams
**Difficulty:** Hard  
**Description:** Group words that are anagrams.  
**Learning:** Dict with list values, sorting  
**Expected:** `[['eat', 'tea', 'ate'], ['tan', 'nat']]`

### 025 - Implement Stack Using List
**Difficulty:** Hard  
**Description:** Create stack with push, pop, peek operations.  
**Learning:** Class with list methods  
**Expected:** Working stack implementation

---

## Files to Create

```
basics/05_data_structures/
├── lists_easy/
│   ├── 01_create_list.py
│   ├── 02_access_elements.py
│   ├── 03_append.py
│   ├── 04_insert.py
│   ├── 05_remove.py
│   ├── 06_slicing.py
│   ├── 07_length.py
│   ├── 08_sum_average.py
│   ├── 09_max_min.py
│   └── 10_reverse.py
├── tuples_sets/
│   ├── 11_create_tuple.py
│   ├── 12_tuple_unpacking.py
│   ├── 13_create_set.py
│   └── 14_set_operations.py
├── dictionaries/
│   ├── 15_create_dict.py
│   ├── 19_word_frequency.py
│   ├── 21_merge_dicts.py
│   └── 22_dict_from_lists.py
├── medium/
│   ├── 16_comprehension_squares.py
│   ├── 17_filter_even.py
│   ├── 18_flatten_list.py
│   └── 20_remove_duplicates.py
└── hard/
    ├── 23_matrix_operations.py
    ├── 24_group_anagrams.py
    └── 25_stack_implementation.py
```

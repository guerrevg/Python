# Practice Programs: File Handling (07_file_handling)

**Total Programs:** 15 | **Easy:** 8 | **Medium:** 5 | **Hard:** 2

---

## Easy Programs (1-8)

### 001 - Create and Write File
**Difficulty:** Easy  
**Description:** Create a file and write text to it.  
**Learning:** `open()`, `write()`, `'w'` mode  
**Expected:** File created with content

### 002 - Read Entire File
**Difficulty:** Easy  
**Description:** Read and display entire file content.  
**Learning:** `read()` method  
**Expected:** Display file contents

### 003 - Read File Line by Line
**Difficulty:** Easy  
**Description:** Read file one line at a time.  
**Learning:** `readline()`, iteration  
**Expected:** Each line printed separately

### 004 - Read All Lines to List
**Difficulty:** Easy  
**Description:** Read all lines into a list.  
**Learning:** `readlines()` method  
**Expected:** `['line1\n', 'line2\n', ...]`

### 005 - Append to File
**Difficulty:** Easy  
**Description:** Add new content to existing file.  
**Learning:** `'a'` mode, `write()`  
**Expected:** Content added to end

### 006 - Copy File Content
**Difficulty:** Easy  
**Description:** Copy content from one file to another.  
**Learning:** Read and write combination  
**Expected:** Duplicate file created

### 007 - Count Lines in File
**Difficulty:** Easy  
**Description:** Count total number of lines.  
**Learning:** Iteration, counting  
**Expected:** `Total lines: 10`

### 008 - Count Words in File
**Difficulty:** Easy  
**Description:** Count total words in file.  
**Learning:** `split()`, counting  
**Expected:** `Total words: 50`

---

## Medium Programs (9-13)

### 009 - Count Characters in File
**Difficulty:** Medium  
**Description:** Count occurrences of each character.  
**Learning:** Dictionary, file reading  
**Expected:** `{'a': 15, 'b': 8, ...}`

### 010 - Find and Replace in File
**Difficulty:** Medium  
**Description:** Replace all occurrences of a word.  
**Learning:** Read, modify, write  
**Expected:** File with replaced text

### 011 - Filter Lines by Keyword
**Difficulty:** Medium  
**Description:** Extract lines containing specific word.  
**Learning:** Conditional filtering  
**Expected:** New file with filtered lines

### 012 - Merge Two Files
**Difficulty:** Medium  
**Description:** Combine content of two files.  
**Learning:** Multiple file operations  
**Expected:** Third file with merged content

### 013 - Create File with Numbers
**Difficulty:** Medium  
**Description:** Create file with numbers 1-100, one per line.  
**Learning:** Loop with file writing  
**Expected:** File with 100 lines

---

## Hard Programs (14-15)

### 014 - Log File Analyzer
**Difficulty:** Hard  
**Description:** Parse log file and extract errors/warnings.  
**Learning:** Pattern matching, parsing  
**Expected:** Summary report of errors

### 015 - CSV File Processor
**Difficulty:** Hard  
**Description:** Read CSV and calculate statistics.  
**Learning:** CSV parsing, calculations  
**Expected:** Average, min, max values

---

## Files to Create

```
basics/07_file_handling/
├── easy/
│   ├── 01_create_write.py
│   ├── 02_read_entire.py
│   ├── 03_read_line_by_line.py
│   ├── 04_readlines_to_list.py
│   ├── 05_append_content.py
│   ├── 06_copy_file.py
│   ├── 07_count_lines.py
│   └── 08_count_words.py
├── medium/
│   ├── 09_count_characters.py
│   ├── 10_find_replace.py
│   ├── 11_filter_lines.py
│   ├── 12_merge_files.py
│   └── 13_create_number_file.py
└── hard/
    ├── 14_log_analyzer.py
    └── 15_csv_processor.py
```

## Sample Data Files to Create

```
basics/07_file_handling/data/
├── sample.txt          # General text
├── numbers.txt         # Numbers 1-100
├── log.txt             # Sample log entries
├── data.csv            # Sample CSV data
├── file1.txt           # For merge exercises
└── file2.txt           # For merge exercises
```

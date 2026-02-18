---
title: "BUG: File handling examples need sample data files"
labels: ["bug", "good first issue"]
---

## Issue

File handling examples reference data files that don't exist, causing errors.

## Problem

Examples try to read files like:
- `newfile.txt`
- `even_numbers_data.txt`
- `sample.txt`

These files are created by the scripts themselves, but examples that read first fail.

## Fix

### Option 1: Create sample files
Add sample data files to `basics/07_file_handling/`:
- `sample.txt` with example content
- `data.txt` with numbers
- `log.txt` with sample logs

### Option 2: Reorder code
Write file first, then read it in the same script.

### Option 3: Add error handling
```python
try:
    with open("sample.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Sample file not found. Creating it...")
    # Create the file
```

## Files Affected
- `basics/07_file_handling/01_file_handling_basics.py`
- `basics/07_file_handling/02_file_readlines.py`
- Other file handling examples

## Testing
```bash
cd basics/07_file_handling
python 01_file_handling_basics.py  # Should not crash
```

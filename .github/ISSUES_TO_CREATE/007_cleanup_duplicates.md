---
title: "CLEANUP: Remove duplicate Python files in basics/"
labels: ["cleanup", "good first issue"]
---

## Issue

Many directories have duplicate files - same code exists twice with different names.

## Example

In `basics/01_introduction/`:
- `01_hello_world.py` 
- `hello_world_first.py` ← Duplicate

This pattern exists across all basics folders (~110 duplicate files total).

## Problem

- Confusing for learners (which file to run?)
- Harder to maintain
- Bloated repository

## Fix

Keep only numbered files (e.g., `01_*.py`), delete descriptive names.

## Files to Check

| Directory | Duplicates |
|-----------|------------|
| 01_introduction | 2 |
| 02_variables_types | 13 |
| 03_control_flow | 10 |
| 04_functions | 11 |
| 05_data_structures | 21 |
| 06_strings | 8 |
| 07_file_handling | 13 |
| 08_oop | 15 |
| 10_advanced | 11 |
| 11_projects | 6 |

## Testing
After cleanup, verify README examples still work:
```bash
cd basics/01_introduction
python 01_hello_world.py  # Should still work
```

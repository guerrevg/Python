---
title: "BUG: Debug output in first hello world example"
labels: ["bug", "good first issue"]
---

## Bug Description

The very first file beginners run (`basics/01_introduction/01_hello_world.py`) has debug output that should be removed.

## Problem

```python
print("ram")         # Debug output - should be removed
print("Hello World")
```

## Expected

Only print "Hello World"

## Fix

Remove line 1:
```python
print("Hello World")
```

## Files
- `basics/01_introduction/01_hello_world.py`

## Why Important

This is the first program beginners run. Extra output is confusing and looks like a mistake.

## Testing
```bash
cd basics/01_introduction
python 01_hello_world.py
# Should only output: Hello World
```

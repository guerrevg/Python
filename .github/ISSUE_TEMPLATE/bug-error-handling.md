---
name: 🐛 Fix Missing Error Handling
about: Add proper error handling to file operations
title: '[BUG] Add error handling to file handling examples'
labels: ['bug', 'enhancement', 'good first issue']
assignees: ''
---

## 📋 Issue Description

Many file handling examples lack proper error handling. If a file doesn't exist or can't be read, the program crashes with unhelpful errors.

## 🔍 Affected Files

### High Priority (User Input)
- `basics/07_file_handling/10_file_rename.py` - No file existence check
- `basics/07_file_handling/file_rename_function.py` - Same issue
- `basics/07_file_handling/03_file_multiple.py` - Generic error message

### Medium Priority (Educational)
- `basics/07_file_handling/07_file_find_word.py` - No FileNotFoundError handling
- `basics/07_file_handling/08_file_search_log.py` - Same issue
- `basics/07_file_handling/file_find_word.py` - Same issue

## 🐛 Current Behavior

```python
# Current code
with open("nonexistent.txt", "r") as f:
    data = f.read()  # Crashes: FileNotFoundError
```

## ✅ Expected Behavior

```python
# Improved code
try:
    with open("nonexistent.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("Error: File 'nonexistent.txt' not found!")
    print("Please create the file or check the path.")
except PermissionError:
    print("Error: Permission denied!")
```

## 📝 Tasks

- [ ] Add try-except blocks to all file operations
- [ ] Handle common exceptions:
  - `FileNotFoundError`
  - `PermissionError`
  - `IsADirectoryError`
- [ ] Add helpful error messages
- [ ] Test with missing files
- [ ] Update README with error handling examples

## 🎯 Why This Matters

- **Learning**: Teaches best practices
- **UX**: Better error messages
- **Debugging**: Easier to fix issues
- **Professionalism**: Production-ready code

## 💡 Implementation Hints

```python
# Example for file_rename.py
def rename_file(source, destination):
    try:
        with open(source, "r") as src:
            data = src.read()
        with open(destination, "w") as dst:
            dst.write(data)
        print("File renamed successfully!")
    except FileNotFoundError:
        print(f"Error: File '{source}' not found!")
    except PermissionError:
        print(f"Error: Permission denied for '{source}'!")
```

## ⚠️ Risk Assessment

**Low Risk:**
- Adding error handling only
- No logic changes
- Backward compatible

## 📝 Difficulty

**Beginner to Intermediate** - Basic try-except with educational value

## 🔗 Related

- Input validation: #15
- Security improvements: #16

---
name: 🐛 Fix Hardcoded Sample Data Files
about: Create sample data files for examples that need them
title: '[BUG] Add sample data files for file handling examples'
labels: ['bug', 'enhancement', 'good first issue']
assignees: ''
---

## 📋 Issue Description

Many file handling examples reference data files that don't exist in the repository:
- `this.txt`
- `pcopy.txt`
- `donkey.txt`
- `censored.txt`
- `logfile.txt`
- `poems.txt`
- `newfile.txt`
- `1.txt`, `2.txt`, `3.txt`

Users must create these manually before running examples.

## 🔍 Affected Files

| File | Requires | Purpose |
|------|----------|---------|
| `01_file_handling_basics.py` | `newfile.txt` | Read/write demo |
| `03_file_multiple.py` | `1.txt`, `2.txt`, `3.txt` | Multiple files |
| `07_file_find_word.py` | `poems.txt` | Word search |
| `08_file_search_log.py` | `logfile.txt` | Log parsing |
| `11_file_copy.py` | `this.txt` | Copy demo |
| `12_file_replace.py` | `donkey.txt` | Replace demo |
| `13_file_censor.py` | `censored.txt` | Censor demo |
| `14_file_compare.py` | `this.txt`, `pcopy.txt` | Compare demo |

## ✅ Tasks

### Option 1: Create Sample Files (Recommended)

- [ ] Create `basics/07_file_handling/samples/` folder
- [ ] Create each sample file with meaningful content:

```txt
# samples/this.txt
Hello World!
This is a sample file for testing.
Python is awesome!

# samples/poems.txt
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

# samples/logfile.txt
[INFO] System started successfully
[WARNING] Low memory detected
[INFO] User logged in
[ERROR] python module failed to load
[INFO] System shutting down

# samples/donkey.txt
The donkey is a hardworking animal.
The donkey carries heavy loads.
People often underestimate the donkey.
```

- [ ] Update examples to use `samples/` prefix
- [ ] Add `.gitkeep` to keep folder in git

### Option 2: Auto-Generate Files

- [ ] Create `setup_samples.py` script
- [ ] Generate files on first run
- [ ] Document in README

## 🎯 Why This Matters

- **UX**: Examples work out of the box
- **Learning**: No confusion about missing files
- **Testing**: Consistent test data
- **Professionalism**: Complete examples

## 💡 Implementation Example

```python
# Updated file path
with open("samples/poems.txt") as f:
    data = f.read()
```

## ⚠️ Risk Assessment

**No Risk:**
- Adding sample data only
- No code logic changes
- Improves user experience

## 📝 Difficulty

**Beginner** - Create text files with sample content

## 🔗 Related

- Error handling: #14
- Documentation: #10

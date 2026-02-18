---
name: 🔒 Security: Add Input Validation
about: Prevent security issues in file operations
title: '[SECURITY] Add input validation to prevent path traversal attacks'
labels: ['security', 'bug', 'enhancement', 'advanced']
assignees: ''
---

## 📋 Issue Description

File handling examples accept user input without validation, making them vulnerable to:
- **Path Traversal Attacks**: `../../../etc/passwd`
- **Arbitrary File Access**: Reading sensitive files
- **File Overwrite**: Overwriting important files

## 🔍 Vulnerable Code

### High Risk (User Input → File Operations)

```python
# basics/07_file_handling/10_file_rename.py
rename(
    source=input("Enter the File Name: "),      # ⚠️ No validation
    destination=input("Enter the New Name: ")    # ⚠️ No validation
)
```

```python
# basics/07_file_handling/file_rename_function.py
with open(f"{source_file}", "r") as src:  # ⚠️ Direct user input
    data = src.read()
```

## 🐛 Attack Scenarios

### Scenario 1: Path Traversal
```
Enter the File Name: ../../../etc/passwd
Enter the New Name: password_copy.txt
# Attacker reads system password file!
```

### Scenario 2: Overwrite Important Files
```
Enter the New Name: ../../requirements.txt
# Attacker overwrites project dependencies!
```

### Scenario 3: Read Sensitive Data
```
Enter the File Name: .env
Enter the New Name: leaked.txt
# Attacker reads environment secrets!
```

## ✅ Tasks

### Immediate (High Priority)

- [ ] Add path validation function:
  ```python
  import os
  
  def is_safe_path(base_path, user_path):
      """Prevent path traversal attacks"""
      # Resolve to absolute paths
      base = os.path.abspath(base_path)
      user = os.path.abspath(user_path)
      # Check if user path is within base
      return os.path.commonpath([base]) == os.path.commonpath([base, user])
  ```

- [ ] Validate all user inputs:
  ```python
  source = input("Enter filename: ")
  
  # Reject dangerous patterns
  if ".." in source or source.startswith("/"):
      print("Error: Invalid filename!")
      return
  
  # Ensure file is in allowed directory
  if not is_safe_path("./basics/07_file_handling/", source):
      print("Error: Access denied!")
      return
  ```

- [ ] Add filename validation:
  ```python
  import re
  
  def is_valid_filename(name):
      """Only allow safe characters"""
      return bool(re.match(r'^[a-zA-Z0-9._-]+$', name))
  ```

### Educational (Medium Priority)

- [ ] Add security notes to README
- [ ] Create security best practices document
- [ ] Add comments explaining the validation

## 🎯 Why This Matters

- **Security**: Prevents real attacks
- **Education**: Teaches secure coding
- **Professionalism**: Production-ready examples
- **Responsibility**: Don't teach bad habits

## 💡 Implementation Example

```python
import os
import re

def safe_rename(source, destination):
    """Safely rename files with validation"""
    
    # Validate filename format
    if not re.match(r'^[a-zA-Z0-9._-]+$', source):
        print("Error: Invalid filename characters!")
        return False
    
    # Prevent path traversal
    if ".." in source or ".." in destination:
        print("Error: Path traversal not allowed!")
        return False
    
    # Ensure files are in current directory
    base = os.getcwd()
    src_path = os.path.abspath(source)
    dst_path = os.path.abspath(destination)
    
    if not src_path.startswith(base) or not dst_path.startswith(base):
        print("Error: Access denied!")
        return False
    
    # Safe to proceed
    try:
        with open(src_path, "r") as src:
            data = src.read()
        with open(dst_path, "w") as dst:
            dst.write(data)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
```

## ⚠️ Risk Assessment

**Medium Risk:**
- Security vulnerability in educational code
- Could be exploited if users run examples
- Teaches bad practices

## 📝 Difficulty

**Advanced** - Security concepts with educational value

## 🔗 Related

- Error handling: #14
- Input validation: #15
- Security audit: #20

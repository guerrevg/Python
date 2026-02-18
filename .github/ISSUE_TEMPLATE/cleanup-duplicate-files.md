---
name: 🗑️ Remove Duplicate Python Files
about: Remove files that exist twice with different naming conventions
title: '[CLEANUP] Remove duplicate Python files in basics/'
labels: ['cleanup', 'good first issue']
assignees: ''
---

## 📋 Issue Description

After the file reorganization, many Python files exist twice:
- Old names (e.g., `hello_world_first.py`)
- New numbered names (e.g., `01_hello_world.py`)

This creates confusion and maintenance overhead.

## 🔍 Affected Files

### 01_introduction/
- [ ] `hello_world_first.py` → Keep `01_hello_world.py`
- [ ] `user_input_addition.py` → Keep `02_user_input_addition.py`

### 02_variables_types/
- [ ] `convert_inches_to_cm.py` → Keep `06_convert_inches_cm.py`
- [ ] `escape_sequences.py` → Keep `13_escape_sequences.py`
- [ ] `find_remainder_operator.py` → Keep `04_modulus_remainder.py`
- [ ] `global_variable_example.py` → Keep `07_global_variable.py`
- [ ] `input_type_validation.py` → Keep `08_input_validation.py`
- [ ] `operator_greater_than.py` → Keep `03_comparison_greater.py`
- [ ] `operators_comparison_assignment.py` → Keep `11_operators.py`
- [ ] `square_number_input.py` → Keep `05_square_input.py`
- [ ] `typecasting_examples.py` → Keep `09_typecasting.py`
- [ ] `typing_union_annotations.py` → Keep `10_union_types.py`

### 03_control_flow/ (10 files)
### 04_functions/ (11 files)
### 05_data_structures/ (21 files)
### 06_strings/ (9 files)
### 07_file_handling/ (14 files)
### 08_oop/ (16 files)
### 09_error_handling/ (3 files)
### 10_advanced/ (11 files)
### 11_projects/ (6 files)

**Total: ~100 duplicate files to remove**

## ✅ Tasks

- [ ] Create backup branch before deletion
- [ ] Verify numbered files have all content from old files
- [ ] Remove old unnumbered files
- [ ] Update any imports/references
- [ ] Test all examples still work
- [ ] Update README if needed

## ⚠️ Risk Assessment

**Low Risk:**
- Numbered files are verified copies
- Can be restored from git history if needed
- No external dependencies

**Mitigation:**
- Create backup branch: `git checkout -b backup-before-cleanup`
- Test after each folder cleanup
- Keep git history intact

## 🎯 Why This Matters

- **Clarity**: One file per topic
- **Navigation**: Numbered system is clear
- **Maintenance**: Half the files to maintain
- **Confusion**: No duplicate content

## 📝 Difficulty

**Beginner** - Systematic file deletion with verification

## 🔗 Related

- File reorganization: #1
- Folder naming standardization: #3

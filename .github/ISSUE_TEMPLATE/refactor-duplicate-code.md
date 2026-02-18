---
name: 🧹 Refactor Duplicate Code
about: Remove duplicate code between old and new file versions
title: '[REFACTOR] Consolidate duplicate code in basics/'
labels: ['refactor', 'intermediate']
assignees: ''
---

## 📋 Issue Description

Many Python files exist in duplicate with identical code:
- Old naming: `hello_world_first.py`
- New naming: `01_hello_world.py`

This creates maintenance burden and confusion.

## 🔍 Analysis

### Duplicate Pairs Found

| Old File | New File | Lines | Topic |
|----------|----------|-------|-------|
| `hello_world_first.py` | `01_hello_world.py` | 1 | Print |
| `user_input_addition.py` | `02_user_input_addition.py` | 6 | Input math |
| `arithmetic_addition.py` | `01_arithmetic.py` | 3 | Addition |
| `average_two_numbers.py` | `02_average.py` | 4 | Average |
| `loops_for_while.py` | `03_for_while_loops.py` | 69 | Loops |
| `functions.py` | `01_functions_basics.py` | 10 | Functions |
| ... | ... | ... | ... |

**Total: ~100 duplicate pairs**

## ✅ Tasks

### Phase 1: Verification
- [ ] Compare each pair to confirm identical content
- [ ] Document any differences
- [ ] Create verification script:
  ```bash
  # Verify duplicates
  for old in basics/01_introduction/*.py; do
      new=$(echo $old | sed 's/_first/01_/')
      diff $old $new
  done
  ```

### Phase 2: Consolidation
- [ ] Keep numbered versions (learning order)
- [ ] Remove unnumbered versions
- [ ] Update all imports
- [ ] Update README references

### Phase 3: Testing
- [ ] Run all examples
- [ ] Verify no broken imports
- [ ] Check documentation links

## 🎯 Why This Matters

- **Maintenance**: Half the files to update
- **Clarity**: One source of truth
- **Git**: Cleaner history
- **Confusion**: No duplicate content

## 💡 Implementation Notes

```bash
# Safe removal process
1. Create backup branch
2. Verify content matches
3. Remove old files
4. Test everything
5. Merge to main
```

## ⚠️ Risk Assessment

**Low Risk:**
- Files are identical
- Git history preserved
- Can restore if needed

## 📝 Difficulty

**Intermediate** - Systematic verification needed

## 🔗 Related

- Duplicate file cleanup: #2
- File organization: #1

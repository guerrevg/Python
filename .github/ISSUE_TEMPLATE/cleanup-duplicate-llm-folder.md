---
name: 🗑️ Remove Duplicate LLM Folder (WEIGHT-LOADING)
about: Clean up duplicate folder from reorganization
title: '[CLEANUP] Remove duplicate llm_fundamentals/WEIGHT-LOADING folder'
labels: ['cleanup', 'good first issue']
assignees: ''
---

## 📋 Issue Description

During the recent project reorganization, a duplicate folder was created:
- `llm_fundamentals/weight_loading/` (correct, lowercase)
- `llm_fundamentals/WEIGHT-LOADING/` (duplicate, uppercase)

The uppercase folder contains only one file and should be removed.

## 🔍 Affected Files

```
llm_fundamentals/
├── weight_loading/      ✓ Keep this (complete)
│   ├── 01_weight_loading.py
│   ├── 02_run_inference.py
│   ├── 03_gpt_download.py
│   ├── 04_weight_helpers.py
│   └── README.md
└── WEIGHT-LOADING/      ✗ Remove this (duplicate)
    └── supplementary.py
```

## ✅ Tasks

- [ ] Verify `WEIGHT-LOADING/supplementary.py` content is already in `weight_loading/04_weight_helpers.py`
- [ ] Remove `llm_fundamentals/WEIGHT-LOADING/` folder
- [ ] Update `.gitignore` if needed
- [ ] Test that all LLM imports still work

## 🎯 Why This Matters

- **Consistency**: All other folders use lowercase naming
- **Confusion**: Having both folders confuses contributors
- **Maintenance**: Duplicate code is hard to maintain
- **Git**: Prevents merge conflicts

## 📝 Difficulty

**Beginner** - Simple file deletion with verification

## 🔗 Related

- Project reorganization: #1
- Folder structure cleanup: #2

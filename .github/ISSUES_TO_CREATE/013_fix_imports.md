---
title: "BUG: Fix broken imports in LLM fundamentals examples"
labels: ["bug", "llm"]
---

## Issue

LLM fundamentals examples have import errors and missing dependencies.

## Problems Found

1. `llm_fundamentals/architecture/01_transformer_architecture.py`
   - Imports from `supplementary.py` but file structure unclear
   - May fail on missing dependencies

2. `llm_fundamentals/pre_training/01_pretraining.py`
   - Uses relative imports that may break

3. `llm_fundamentals/fine_tuning/01_fine_tuning.py`
   - Requires `litgpt` but not clearly documented

## Fix

1. Verify all imports work:
   ```bash
   cd llm_fundamentals/architecture
   python 01_transformer_architecture.py
   ```

2. Add requirements file:
   ```
   # llm_fundamentals/requirements.txt
   torch>=2.0.0
   tiktoken>=0.5.0
   transformers>=4.30.0
   ```

3. Update README with setup instructions

## Files to Check
- `llm_fundamentals/architecture/*.py`
- `llm_fundamentals/pre_training/*.py`
- `llm_fundamentals/fine_tuning/*.py`
- `llm_fundamentals/weight_loading/*.py`

## Testing
```bash
cd llm_fundamentals
pip install -r requirements.txt
python architecture/01_transformer_architecture.py
```

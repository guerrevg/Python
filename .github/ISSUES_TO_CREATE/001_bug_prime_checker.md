---
title: "BUG: Prime number checker returns incorrect results"
labels: ["bug", "good first issue", "priority: high"]
---

## Bug Description

The prime number checker in `basics/03_control_flow/02_check_prime.py` has inverted logic that returns wrong results.

## Problem

In the final if-else block (lines 13-16):
```python
if(prime):
    prime = False  # Wrong! Should be True
else:
    prime = True   # Wrong! Should be False
```

## Expected Behavior

| Input | Expected | Actual |
|-------|----------|--------|
| 7     | True     | False  |
| 10    | False    | True   |
| 2     | True     | False  |

## Fix

Remove lines 13-16 entirely. The logic before this block already sets `prime` correctly.

## Files
- `basics/03_control_flow/02_check_prime.py`

## Testing
```bash
cd basics/03_control_flow
python 02_check_prime.py
# Enter 7 → should show True
# Enter 10 → should show False
```

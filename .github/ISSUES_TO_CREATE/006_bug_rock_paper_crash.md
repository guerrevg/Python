---
title: "BUG: Rock paper scissors crashes on invalid input"
labels: ["bug", "good first issue"]
---

## Bug Description

The rock paper scissors game crashes or behaves unexpectedly on invalid input.

## Problem

In `basics/11_projects/03_rock_paper_scissors.py`:
- No input validation
- Assumes user enters "rock", "paper", or "scissors"

## Expected

Should handle invalid input gracefully:
```
Enter your choice (rock/paper/scissors): dragon
Invalid choice! Please enter rock, paper, or scissors.
```

## Fix

Add input validation loop:

```python
while True:
    user = input("Enter your choice (rock/paper/scissors): ").lower()
    if user in ["rock", "paper", "scissors"]:
        break
    print("Invalid choice! Try again.")
```

## Files
- `basics/11_projects/03_rock_paper_scissors.py`

## Testing
```bash
cd basics/11_projects
python 03_rock_paper_scissors.py
# Enter "dragon" → should show error message
# Enter "rock" → should work normally
```

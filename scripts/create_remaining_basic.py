#!/usr/bin/env python3
import subprocess
import time

remaining = [
    "Create Shopping List Program",
    "Build Basic Expense Tracker",
    "Create BMI Calculator",
    "Build Age Calculator",
    "Create Tip Calculator",
    "Build Basic Unit Converter",
    "Create Countdown Timer",
    "Build Simple Stopwatch",
    "Create Number to Words Converter",
    "Build Word Scramble Game",
    "Create Simple Hangman Game",
    "Build Tic Tac Toe Game",
    "Create Memory Card Game",
    "Build Flashcard Program",
    "Create Recipe Storage Program",
    "Build Book Library Tracker",
    "Create Movie Watchlist",
    "Build Habit Tracker",
    "Create Weather Display Program",
    "Build Simple Note Taker",
]

created = 0
for title in remaining:
    body = f"""## Description
Build a Python program: {title}

## Requirements
- Program runs without errors
- Includes user interaction
- Has error handling
- Includes comments
- Follows PEP 8

## File Location
exercises/basic_coding/{title.lower().replace(' ', '_')}.py

---
Part of 150 Basic Coding Issues
"""
    cmd = ['gh', 'issue', 'create', '--title', f'[BEGINNER] {title}', '--body', body, '--label', 'beginner,exercise,good first issue']
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✅ {title}")
        created += 1
    else:
        print(f"❌ {title}")
    time.sleep(0.5)

print(f"\nCreated {created}/{len(remaining)} issues")

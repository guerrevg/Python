# Practice Programs: Projects (11_projects)

**Total Programs:** 10 | **Easy:** 2 | **Medium:** 4 | **Hard:** 4

---

## Easy Projects (1-2)

### 001 - Number Guessing Game
**Difficulty:** Easy  
**Description:** Computer picks random number, user guesses it.  
**Learning:** `random`, loops, conditionals  
**Features:**
- Generate random number 1-100
- Give higher/lower hints
- Count attempts
- Ask to play again

### 002 - Rock Paper Scissors
**Difficulty:** Easy  
**Description:** Play against computer.  
**Learning:** `random`, game logic  
**Features:**
- User input validation
- Computer random choice
- Win/lose/draw logic
- Score tracking

---

## Medium Projects (3-6)

### 003 - Password Generator
**Difficulty:** Medium  
**Description:** Generate secure random passwords.  
**Learning:** `random`, `string` modules  
**Features:**
- Customizable length
- Include letters, numbers, symbols
- Ensure complexity requirements
- Generate multiple passwords

### 004 - Quiz Application
**Difficulty:** Medium  
**Description:** Multiple choice quiz with scoring.  
**Learning:** Data structures, file I/O  
**Features:**
- Question bank (dict/list)
- Track score
- Display results
- Save high scores

### 005 - Contact Book
**Difficulty:** Medium  
**Description:** Store and manage contacts.  
**Learning:** CRUD operations, file storage  
**Features:**
- Add contact
- View all contacts
- Search contact
- Delete contact
- Save to file

### 006 - Expense Tracker
**Difficulty:** Medium  
**Description:** Track daily expenses.  
**Learning:** Data management, calculations  
**Features:**
- Add expense with category
- View all expenses
- Calculate totals
- Filter by category
- Monthly summary

---

## Hard Projects (7-10)

### 007 - To-Do List Manager
**Difficulty:** Hard  
**Description:** Full-featured task manager.  
**Learning:** File I/O, data structures, dates  
**Features:**
- Add task with priority/due date
- Mark complete
- Edit tasks
- Delete tasks
- Filter by status/priority
- Save/load from file
- Due date reminders

### 008 - Hangman Game
**Difficulty:** Hard  
**Description:** Classic word guessing game.  
**Learning:** String manipulation, game state  
**Features:**
- Word bank
- Display hangman stages
- Track guessed letters
- Win/lose conditions
- Score tracking
- Hint system

### 009 - Tic-Tac-Toe
**Difficulty:** Hard  
**Description:** Two player or vs computer.  
**Learning:** 2D lists, game AI  
**Features:**
- 3x3 game board
- Two player mode
- Basic AI opponent
- Win detection
- Draw detection
- Score tracking

### 010 - Text-Based Adventure Game
**Difficulty:** Hard  
**Description:** Interactive story with choices.  
**Learning:** Complex state management  
**Features:**
- Multiple rooms/locations
- Inventory system
- Puzzles/challenges
- Multiple endings
- Save/load game
- Help system

---

## Files to Create

```
basics/11_projects/
├── easy/
│   ├── 01_guess_number.py
│   └── 02_rock_paper_scissors.py
├── medium/
│   ├── 03_password_generator.py
│   ├── 04_quiz_application.py
│   ├── 05_contact_book.py
│   └── 06_expense_tracker.py
└── hard/
    ├── 07_todo_manager.py
    ├── 08_hangman.py
    ├── 09_tic_tac_toe.py
    └── 10_adventure_game.py
```

## Project Structure Template

```python
"""
Project: Project Name
Difficulty: easy/medium/hard
Features:
  - Feature 1
  - Feature 2
"""

# Imports
import module

# Constants
CONSTANT = value

# Functions
def function_name():
    """Docstring"""
    pass

# Main game loop
def main():
    while True:
        # Game logic
        pass

if __name__ == "__main__":
    main()
```

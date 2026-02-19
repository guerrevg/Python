#!/usr/bin/env python3
"""
Create 150 NEW simple coding issues (no duplicates)
"""

import subprocess
import time

# 150 Simple Coding Issues - Basic Python Programming
new_issues = [
    # Basic Print & Variables (1-20)
    ("Print Your Name and Age", "beginner", "Create a program that prints your name and age in a formatted sentence"),
    ("Add Two Numbers Together", "beginner", "Write a program that adds two numbers and displays the result"),
    ("Calculate Rectangle Perimeter", "beginner", "Create a program to calculate rectangle perimeter from length and width"),
    ("Convert Minutes to Seconds", "beginner", "Write a program that converts minutes to seconds"),
    ("Find Square of a Number", "beginner", "Create a program that calculates the square of any number"),
    ("Check if Number is Positive", "beginner", "Write a program that checks if a number is positive or negative"),
    ("Print Numbers 1 to 10", "beginner", "Create a program that prints numbers from 1 to 10 using a loop"),
    ("Calculate Circle Area", "beginner", "Write a program to calculate the area of a circle given radius"),
    ("Find Maximum of Two Numbers", "beginner", "Create a program that finds the larger of two numbers"),
    ("Convert KM to Meters", "beginner", "Write a program that converts kilometers to meters"),
    ("Print Even Numbers 1 to 20", "beginner", "Create a program that prints even numbers from 1 to 20"),
    ("Calculate Simple Discount", "beginner", "Write a program that calculates 10% discount on a price"),
    ("Find Cube of a Number", "beginner", "Create a program that calculates the cube of any number"),
    ("Check Voting Eligibility", "beginner", "Write a program that checks if someone can vote based on age"),
    ("Print Multiplication Table of 5", "beginner", "Create a program that prints the 5 times table"),
    ("Calculate Average of 3 Numbers", "beginner", "Write a program that finds the average of three numbers"),
    ("Convert Hours to Minutes", "beginner", "Create a program that converts hours to minutes"),
    ("Find Remainder of Division", "beginner", "Write a program that finds the remainder when dividing two numbers"),
    ("Print Odd Numbers 1 to 19", "beginner", "Create a program that prints odd numbers from 1 to 19"),
    ("Calculate Triangle Area", "beginner", "Write a program to calculate triangle area from base and height"),
    
    # String Basics (21-40)
    ("Reverse a String", "beginner", "Create a program that reverses any input string"),
    ("Count Vowels in Word", "beginner", "Write a program that counts vowels in a word"),
    ("Check Palindrome Word", "beginner", "Create a program that checks if a word is a palindrome"),
    ("Convert to Uppercase", "beginner", "Write a program that converts text to uppercase"),
    ("Count Characters in String", "beginner", "Create a program that counts characters in a string"),
    ("Extract First Letter", "beginner", "Write a program that extracts the first letter of each word"),
    ("Check String Contains Word", "beginner", "Create a program that checks if a string contains a specific word"),
    ("Replace Spaces with Underscore", "beginner", "Write a program that replaces all spaces with underscores"),
    ("Count Words in Sentence", "beginner", "Create a program that counts words in a sentence"),
    ("Extract Numbers from String", "beginner", "Write a program that extracts all numbers from a string"),
    ("Check String Starts With", "beginner", "Create a program that checks if string starts with specific letter"),
    ("Convert to Title Case", "beginner", "Write a program that converts text to title case"),
    ("Remove Vowels from String", "beginner", "Create a program that removes all vowels from a string"),
    ("Find Longest Word", "beginner", "Write a program that finds the longest word in a sentence"),
    ("Count Capital Letters", "beginner", "Create a program that counts capital letters in a string"),
    ("Check Anagrams", "beginner", "Write a program that checks if two words are anagrams"),
    ("Duplicate String N Times", "beginner", "Create a program that duplicates a string N times"),
    ("Find Middle Character", "beginner", "Write a program that finds the middle character of a string"),
    ("Check String is Numeric", "beginner", "Create a program that checks if a string contains only numbers"),
    ("Split String into List", "beginner", "Write a program that splits a string into a list of words"),
    
    # List Basics (41-60)
    ("Create List of Fruits", "beginner", "Create a program that creates and displays a list of fruits"),
    ("Find List Length", "beginner", "Write a program that finds the length of a list"),
    ("Add Item to List", "beginner", "Create a program that adds an item to a list"),
    ("Remove Item from List", "beginner", "Write a program that removes an item from a list"),
    ("Find Maximum in List", "beginner", "Create a program that finds the maximum value in a list"),
    ("Find Minimum in List", "beginner", "Write a program that finds the minimum value in a list"),
    ("Sum All List Elements", "beginner", "Create a program that sums all elements in a list"),
    ("Reverse a List", "beginner", "Write a program that reverses a list"),
    ("Sort List in Order", "beginner", "Create a program that sorts a list in ascending order"),
    ("Count Item Occurrences", "beginner", "Write a program that counts how many times an item appears in a list"),
    ("Find Item Index", "beginner", "Create a program that finds the index of an item in a list"),
    ("Merge Two Lists", "beginner", "Write a program that merges two lists into one"),
    ("Filter Even Numbers", "beginner", "Create a program that filters even numbers from a list"),
    ("Remove Duplicates from List", "beginner", "Write a program that removes duplicate items from a list"),
    ("Find Common Elements", "beginner", "Create a program that finds common elements in two lists"),
    ("Rotate List Elements", "beginner", "Write a program that rotates list elements by one position"),
    ("Find Second Largest", "beginner", "Create a program that finds the second largest number in a list"),
    ("Count Positive Numbers", "beginner", "Write a program that counts positive numbers in a list"),
    ("Calculate List Average", "beginner", "Create a program that calculates the average of list elements"),
    ("Check if List is Empty", "beginner", "Write a program that checks if a list is empty"),
    
    # Dictionary Basics (61-80)
    ("Create Student Dictionary", "beginner", "Create a program that creates a dictionary of student information"),
    ("Add Key to Dictionary", "beginner", "Write a program that adds a new key to a dictionary"),
    ("Remove Key from Dictionary", "beginner", "Create a program that removes a key from a dictionary"),
    ("Get Dictionary Value", "beginner", "Write a program that retrieves a value from a dictionary"),
    ("Count Dictionary Keys", "beginner", "Create a program that counts the number of keys in a dictionary"),
    ("Check Key Exists", "beginner", "Write a program that checks if a key exists in a dictionary"),
    ("Merge Two Dictionaries", "beginner", "Create a program that merges two dictionaries"),
    ("Get All Keys", "beginner", "Write a program that gets all keys from a dictionary"),
    ("Get All Values", "beginner", "Create a program that gets all values from a dictionary"),
    ("Update Dictionary Value", "beginner", "Write a program that updates a value in a dictionary"),
    ("Find Maximum Value", "beginner", "Create a program that finds the key with maximum value"),
    ("Find Minimum Value", "beginner", "Write a program that finds the key with minimum value"),
    ("Invert Dictionary", "beginner", "Create a program that swaps keys and values in a dictionary"),
    ("Count Word Frequency", "beginner", "Write a program that counts word frequency in a sentence"),
    ("Create Phonebook", "beginner", "Create a program that creates a phonebook dictionary"),
    ("Lookup Phone Number", "beginner", "Write a program that looks up a phone number by name"),
    ("Add Contact to Phonebook", "beginner", "Create a program that adds a contact to phonebook"),
    ("Delete Contact from Phonebook", "beginner", "Write a program that deletes a contact from phonebook"),
    ("Search Contact by Name", "beginner", "Create a program that searches for a contact by name"),
    ("Display All Contacts", "beginner", "Write a program that displays all contacts in phonebook"),
    
    # Function Basics (81-100)
    ("Create Greeting Function", "beginner", "Create a function that greets a person by name"),
    ("Function to Add Numbers", "beginner", "Write a function that adds two numbers and returns result"),
    ("Function to Check Even", "beginner", "Create a function that checks if a number is even"),
    ("Function to Find Maximum", "beginner", "Write a function that returns the maximum of two numbers"),
    ("Function to Calculate Area", "beginner", "Create a function that calculates rectangle area"),
    ("Function to Convert Temperature", "beginner", "Write a function that converts Celsius to Fahrenheit"),
    ("Function to Check Positive", "beginner", "Create a function that checks if number is positive"),
    ("Function to Reverse String", "beginner", "Write a function that reverses a string"),
    ("Function to Count Vowels", "beginner", "Create a function that counts vowels in a string"),
    ("Function to Check Palindrome", "beginner", "Write a function that checks if string is palindrome"),
    ("Function with Default Parameter", "beginner", "Create a function with a default parameter value"),
    ("Function Returning Multiple Values", "beginner", "Write a function that returns multiple values"),
    ("Function with Variable Arguments", "beginner", "Create a function that accepts variable number of arguments"),
    ("Recursive Factorial Function", "beginner", "Write a recursive function to calculate factorial"),
    ("Recursive Sum Function", "beginner", "Create a recursive function to sum numbers from 1 to N"),
    ("Function to Find GCD", "beginner", "Write a function that finds GCD of two numbers"),
    ("Function to Find LCM", "beginner", "Create a function that finds LCM of two numbers"),
    ("Function to Check Prime", "beginner", "Write a function that checks if a number is prime"),
    ("Function to Generate Fibonacci", "beginner", "Create a function that generates Fibonacci sequence"),
    ("Function to Calculate Power", "beginner", "Write a function that calculates base raised to power"),
    
    # File Basics (101-120)
    ("Create Text File", "beginner", "Create a program that creates a new text file"),
    ("Write to Text File", "beginner", "Write a program that writes text to a file"),
    ("Read Text File", "beginner", "Create a program that reads and displays file contents"),
    ("Count Lines in File", "beginner", "Write a program that counts lines in a file"),
    ("Count Words in File", "beginner", "Create a program that counts words in a file"),
    ("Copy File Content", "beginner", "Write a program that copies content from one file to another"),
    ("Append to File", "beginner", "Create a program that appends text to an existing file"),
    ("Find Word in File", "beginner", "Write a program that searches for a word in a file"),
    ("Delete a File", "beginner", "Create a program that deletes a file"),
    ("Check if File Exists", "beginner", "Write a program that checks if a file exists"),
    ("Get File Size", "beginner", "Create a program that gets the size of a file"),
    ("Read File Line by Line", "beginner", "Write a program that reads a file line by line"),
    ("Write Numbers to File", "beginner", "Create a program that writes numbers 1-100 to a file"),
    ("Read Numbers from File", "beginner", "Write a program that reads numbers from a file"),
    ("Find Longest Line", "beginner", "Create a program that finds the longest line in a file"),
    ("Count Characters in File", "beginner", "Write a program that counts characters in a file"),
    ("Replace Word in File", "beginner", "Create a program that replaces a word in a file"),
    ("Create Log File", "beginner", "Write a program that creates a simple log file"),
    ("Backup a File", "beginner", "Create a program that creates a backup of a file"),
    ("List Files in Directory", "beginner", "Write a program that lists all files in a directory"),
    
    # Simple Games & Projects (121-150)
    ("Hello World Program", "beginner", "Create the classic Hello World program"),
    ("Simple Calculator", "beginner", "Create a basic calculator that does addition, subtraction, multiplication, division"),
    ("Number Guessing Game", "beginner", "Create a game where user guesses a number between 1-10"),
    ("Rock Paper Scissors Game", "beginner", "Create a simple rock paper scissors game"),
    ("Dice Roll Simulator", "beginner", "Create a program that simulates rolling a dice"),
    ("Coin Flip Simulator", "beginner", "Create a program that simulates flipping a coin"),
    ("Random Password Generator", "beginner", "Create a program that generates random passwords"),
    ("Mad Libs Game", "beginner", "Create a simple Mad Libs style game"),
    ("Quiz Game Basic", "beginner", "Create a simple quiz game with 5 questions"),
    ("To-Do List Basic", "beginner", "Create a basic to-do list program"),
    ("Contact List Basic", "beginner", "Create a basic contact list program"),
    ("Shopping List Program", "beginner", "Create a simple shopping list program"),
    ("Expense Tracker Basic", "beginner", "Create a basic expense tracking program"),
    ("BMI Calculator", "beginner", "Create a BMI calculator program"),
    ("Age Calculator", "beginner", "Create a program that calculates age from birth year"),
    ("Tip Calculator", "beginner", "Create a program that calculates tip amount"),
    ("Unit Converter Basic", "beginner", "Create a basic unit converter program"),
    ("Countdown Timer", "beginner", "Create a simple countdown timer program"),
    ("Stopwatch Program", "beginner", "Create a basic stopwatch program"),
    ("Number to Words", "beginner", "Create a program that converts numbers to words"),
    ("Word Scramble Game", "beginner", "Create a simple word scramble game"),
    ("Hangman Game Basic", "beginner", "Create a basic hangman game"),
    ("Tic Tac Toe Game", "beginner", "Create a simple tic tac toe game"),
    ("Memory Card Game", "beginner", "Create a basic memory card matching game"),
    ("Flashcard Program", "beginner", "Create a simple flashcard study program"),
    ("Recipe Storage Program", "beginner", "Create a basic recipe storage program"),
    ("Book Library Basic", "beginner", "Create a basic book library tracker"),
    ("Movie Watchlist", "beginner", "Create a simple movie watchlist program"),
    ("Habit Tracker Basic", "beginner", "Create a basic habit tracking program"),
    ("Weather Info Display", "beginner", "Create a program that displays weather information"),
]

def create_issue(title, difficulty, description):
    """Create a GitHub issue"""
    body = f"""## 📝 Description
{description}

## 🎯 Difficulty
{difficulty.capitalize()}

## ✅ Requirements
- [ ] Program runs without errors
- [ ] Includes user input/output
- [ ] Has proper error handling
- [ ] Includes comments explaining code
- [ ] Follows PEP 8 style guidelines

## 📁 File Location
`exercises/150_basic_coding/{title.lower().replace(' ', '_')}.py`

## 💡 Implementation Hints
- Start with pseudocode
- Break down into small steps
- Test with different inputs
- Add comments as you code

## 📋 Example
```python
# Add your example input/output here
```

---
*Part of 150 Basic Coding Issues Initiative*
"""
    
    cmd = [
        'gh', 'issue', 'create',
        '--title', f"[BEGINNER] {title}",
        '--body', body,
        '--label', 'beginner,exercise,good first issue'
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print(f"✅ {title}")
            time.sleep(0.3)
            return True
        else:
            print(f"❌ {title}")
            return False
    except Exception as e:
        print(f"❌ {title} - {str(e)}")
        return False

def main():
    print("="*60)
    print("🚀 Creating 150 NEW Simple Coding Issues")
    print("="*60)
    print()
    
    created = 0
    failed = 0
    
    for title, difficulty, description in new_issues:
        if create_issue(title, difficulty, description):
            created += 1
        else:
            failed += 1
    
    print()
    print("="*60)
    print("📊 Summary")
    print("="*60)
    print(f"✅ Created: {created}")
    print(f"❌ Failed: {failed}")
    print(f"📍 View at: https://github.com/hackdartstorm/Python/issues")
    print("="*60)

if __name__ == "__main__":
    main()

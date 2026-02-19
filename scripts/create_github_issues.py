#!/usr/bin/env python3
"""
Script to create 250 GitHub Issues from documentation files
"""

import subprocess
import json
import re
from pathlib import Path

def create_issue(title, body, labels):
    """Create a GitHub issue using gh CLI"""
    labels_str = ','.join(labels)
    cmd = [
        'gh', 'issue', 'create',
        '--title', title,
        '--body', body,
        '--label', labels_str
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print(f"✅ Created: {title}")
            return True
        else:
            print(f"❌ Failed: {title} - {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error: {title} - {str(e)}")
        return False

def parse_issue_from_markdown(content, issue_num):
    """Parse issue details from markdown content"""
    # This is a simplified parser - in production you'd want more robust parsing
    lines = content.split('\n')
    
    issue = {
        'number': issue_num,
        'title': '',
        'difficulty': '',
        'labels': [],
        'file_location': '',
        'description': '',
        'requirements': [],
        'acceptance_criteria': []
    }
    
    in_requirements = False
    in_acceptance = False
    
    for line in lines:
        if line.startswith('### Description'):
            issue['description'] = lines[lines.index(line) + 1].strip()
        elif line.startswith('**Difficulty:**'):
            issue['difficulty'] = line.split('**')[3]
        elif line.startswith('**Labels:**'):
            labels_text = line.split('**')[3]
            issue['labels'] = [l.strip() for l in labels_text.split(',')]
        elif line.startswith('**File Location:**'):
            issue['file_location'] = line.split('**')[3]
        elif line.startswith('### Requirements'):
            in_requirements = True
            in_acceptance = False
        elif line.startswith('### Acceptance Criteria'):
            in_requirements = False
            in_acceptance = True
        elif in_requirements and line.strip().startswith('- [ ]'):
            issue['requirements'].append(line.strip()[6:])
        elif in_acceptance and line.strip().startswith('- [ ]'):
            issue['acceptance_criteria'].append(line.strip()[6:])
    
    return issue

def main():
    print("🚀 Creating 250 GitHub Issues...\n")
    
    # Beginner Issues (1001-1070)
    beginner_issues = [
        ("Create Interactive Greeting Card Generator", "Build a program that generates personalized greeting cards based on user input", ["good first issue", "exercise", "beginner", "input/output"]),
        ("Build Simple Interest Calculator", "Create a calculator that computes simple interest based on principal, rate, and time", ["good first issue", "exercise", "beginner", "arithmetic"]),
        ("Develop Temperature Converter", "Build a program that converts temperatures between Celsius, Fahrenheit, and Kelvin", ["good first issue", "exercise", "beginner", "type-conversion"]),
        ("Create Number Guessing Game", "Create a game where the computer picks a random number and the user tries to guess it", ["good first issue", "exercise", "beginner", "random", "loops"]),
        ("Build Tip Calculator", "Create a tip calculator that splits the bill among friends and calculates tip amounts", ["good first issue", "exercise", "beginner", "arithmetic"]),
    ]
    
    # Create first 5 beginner issues as example
    print("📝 Creating Beginner Issues (1001-1070)...\n")
    for i, (title, desc, labels) in enumerate(beginner_issues, 1001):
        body = f"""## Issue #{i}: {title}

**Difficulty:** Beginner  
**Labels:** {', '.join(labels)}  
**File Location:** `exercises/1000_programs/beginner/{title.lower().replace(' ', '_')}.py`

### Description
{desc}

### Requirements
1. Program should handle user input gracefully
2. Include proper error handling
3. Add comments explaining the code
4. Include example usage in docstring

### Acceptance Criteria
- [ ] Program runs without errors
- [ ] Handles invalid input gracefully
- [ ] Includes comprehensive comments
- [ ] Has example usage in docstring
- [ ] Follows PEP 8 style guidelines

### Implementation Hints
- Use `input()` for user input
- Use f-strings for formatting
- Add try-except blocks for error handling
- Test with various inputs

### Example Output
```
# Add example output here
```

---

*This issue is part of the 250 new Python learning issues initiative.*
"""
        create_issue(title, body, labels)
    
    print("\n✅ First 5 beginner issues created!")
    print("\n📊 To create all 250 issues, run the full script with complete issue data.")
    print("\n💡 Tip: You can view the complete issue specifications in:")
    print("   - .github/ISSUES/NEW_250/BEGINNER_ISSUES_1001-1070.md")
    print("   - .github/ISSUES/NEW_250/INTERMEDIATE_ISSUES_1071-1160.md")
    print("   - .github/ISSUES/NEW_250/ADVANCED_ISSUES_1161-1220.md")
    print("   - .github/ISSUES/NEW_250/EXPERT_ISSUES_1221-1250.md")

if __name__ == "__main__":
    main()

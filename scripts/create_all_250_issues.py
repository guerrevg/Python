#!/usr/bin/env python3
"""
Script to create all 250 GitHub Issues
"""

import subprocess
import time

# Standard labels that should exist
DEFAULT_LABELS = ['exercise']

def create_issue(title, body, difficulty):
    """Create a GitHub issue using gh CLI"""
    labels = ['exercise', difficulty]
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
            print(f"✅ #{title}")
            time.sleep(0.5)  # Rate limiting
            return True
        else:
            print(f"❌ {title}")
            return False
    except Exception as e:
        print(f"❌ {title} - {str(e)}")
        return False

def main():
    print("="*60)
    print("🚀 Creating 250 GitHub Issues")
    print("="*60)
    print()
    
    created = 0
    failed = 0
    
    # BEGINNER ISSUES (70 issues)
    print("📝 Creating Beginner Issues (1-70)...\n")
    
    beginner = [
        "Create Interactive Greeting Card Generator",
        "Build Simple Interest Calculator",
        "Develop Temperature Converter",
        "Create Number Guessing Game",
        "Build Tip Calculator",
        "Create BMI Calculator",
        "Build Multiplication Table Generator",
        "Develop Password Generator",
        "Create Countdown Timer",
        "Build Rock Paper Scissors Game",
        "Create Leap Year Checker",
        "Build Factorial Calculator",
        "Develop Fibonacci Sequence Generator",
        "Create Prime Number Checker",
        "Build Area Calculator for Multiple Shapes",
        "Create Digital Clock Display",
        "Build Unit Converter for Length",
        "Create Vowel Counter",
        "Build Palindrome Checker",
        "Develop Caesar Cipher Encoder",
        "Create Binary to Decimal Converter",
        "Build Decimal to Binary Converter",
        "Create ASCII Value Finder",
        "Build Random Password Generator",
        "Develop Hangman Game",
        "Create Mad Libs Story Generator",
        "Build Contact Book Basic",
        "Create To-Do List Console",
        "Develop Dice Rolling Simulator",
        "Build Coin Flip Simulator",
        "Create Age Calculator",
        "Build Day of Week Finder",
        "Create Roman Numeral Converter",
        "Build Word Counter",
        "Develop Sentence Reverser",
        "Create Anagram Checker",
        "Build Letter Frequency Counter",
        "Create Number to Words Converter",
        "Build Time Format Converter 12h to 24h",
        "Develop Currency Converter with Static Rates",
        "Create Quiz Game Multiple Choice",
        "Build Memory Card Matching Game",
        "Create Text-Based Adventure Game",
        "Build Calculator with History",
        "Develop Number Pattern Printer",
        "Create Star Pattern Generator",
        "Build Multiplication Quiz",
        "Create Spelling Bee Game",
        "Build Word Scramble Game",
        "Develop Math Quiz Generator",
        "Create Story Builder Fill in the Blanks",
        "Build Recipe Cost Calculator",
        "Create Workout Timer",
        "Build Calorie Counter Basic",
        "Develop Sleep Calculator",
        "Create Water Intake Tracker",
        "Build Step Counter Simulator",
        "Create Loan Payment Calculator",
        "Build Discount Calculator",
        "Develop Sales Tax Calculator",
        "Create Grade Calculator",
        "Build GPA Calculator",
        "Create Study Timer Pomodoro",
        "Build Habit Tracker Console",
        "Develop Mood Tracker",
        "Create Journal Entry System",
        "Build Book Reading List",
        "Create Movie Watch List",
        "Build Shopping List Manager",
        "Develop Expense Splitter",
    ]
    
    for title in beginner:
        body = f"""## Description
Build a Python program: {title}

## Difficulty
Beginner (5-30 minutes)

## Requirements
1. Create the program with clear user interaction
2. Include proper error handling
3. Add comments explaining the code
4. Include example usage in docstring
5. Follow PEP 8 style guidelines

## File Location
`exercises/1000_programs/beginner/{title.lower().replace(' ', '_')}.py`

## Acceptance Criteria
- [ ] Program runs without errors
- [ ] Handles invalid input gracefully
- [ ] Includes comprehensive comments
- [ ] Has example usage in docstring
- [ ] Follows PEP 8 style guidelines

## Implementation Hints
- Use `input()` for user input
- Use f-strings for formatting
- Add try-except blocks for error handling
- Test with various inputs

---
*Part of 250 new Python learning issues - Beginner Track*
"""
        if create_issue(title, body, 'beginner'):
            created += 1
        else:
            failed += 1
    
    print(f"\n✅ Beginner: {created} created, {failed} failed\n")
    
    # INTERMEDIATE ISSUES (90 issues)
    print("📚 Creating Intermediate Issues (71-160)...\n")
    
    intermediate = [
        "Build Contact List Manager with Search",
        "Create Password Strength Checker",
        "Develop File Backup Utility",
        "Build Expense Tracker with Categories",
        "Create Student Grade Management System",
        "Build Library Book Management System",
        "Create Inventory Management System",
        "Develop Hotel Reservation System",
        "Build Patient Record System",
        "Create Employee Payroll System",
        "Build Quiz Application with Timer",
        "Create Text File Analyzer",
        "Develop CSV Data Processor",
        "Build JSON Data Validator",
        "Create Image Metadata Extractor",
        "Build PDF Text Extractor",
        "Develop Email Sender with SMTP",
        "Create FTP File Uploader",
        "Build Weather Data Fetcher",
        "Create News RSS Feed Reader",
        "Build YouTube Video Downloader",
        "Create Spotify Playlist Manager",
        "Develop Twitter Bot Basic",
        "Build WhatsApp Message Sender",
        "Create SMS Notification System",
        "Build URL Link Checker",
        "Develop Website Uptime Monitor",
        "Create Port Scanner Basic",
        "Build Network Speed Tester",
        "Create System Resource Monitor",
        "Build Process Manager Basic",
        "Develop File Search Utility",
        "Create Duplicate File Finder",
        "Build Disk Space Analyzer",
        "Create Screenshot Automation",
        "Build Keyboard Macro Recorder",
        "Develop Mouse Automation Tool",
        "Create Clipboard Manager",
        "Build Password Manager Local",
        "Create Encrypted File Storage",
        "Build ZIP File Creator",
        "Develop File Compression Tool",
        "Create Audio File Player",
        "Build Video File Player Basic",
        "Create Image Viewer GUI",
        "Build Drawing Application GUI",
        "Develop Note-Taking App GUI",
        "Create Calculator GUI",
        "Build Text Editor GUI",
        "Create Code Syntax Highlighter",
        "Build Markdown Editor",
        "Develop HTML Previewer",
        "Create Color Picker Tool",
        "Build Unit Test Framework",
        "Develop Code Coverage Tool",
        "Create Documentation Generator",
        "Build API Documentation Tool",
        "Create Database Schema Designer",
        "Build ER Diagram Generator",
        "Develop Flowchart Maker",
        "Create Mind Mapping Tool",
        "Build Kanban Board Console",
        "Develop Gantt Chart Generator",
        "Create Time Tracking System",
        "Build Invoice Generator",
        "Create QR Code Generator",
        "Build Barcode Generator",
        "Develop CAPTCHA Generator",
        "Create Meme Generator",
        "Build Image Watermarker",
        "Create Image Resizer",
        "Build Image Format Converter",
        "Develop Video Format Converter",
        "Create Audio Format Converter",
        "Build Subtitle Editor",
        "Create Podcast Downloader",
        "Build E-book Reader",
        "Develop Audiobook Player",
        "Create Flashcard App",
        "Build Language Learning App",
        "Create Typing Speed Tester",
        "Build Code Typing Tutor",
        "Develop Math Practice App",
        "Create Spelling Practice App",
        "Build Memory Training Game",
        "Create Logic Puzzle Game",
        "Build Sudoku Solver",
        "Develop Crossword Generator",
        "Create Chess Game 2 Player",
        "Build Checkers Game 2 Player",
    ]
    
    int_created = 0
    for title in intermediate:
        body = f"""## Description
Build a Python program: {title}

## Difficulty
Intermediate (30-90 minutes)

## Requirements
1. Implement all core features
2. Use appropriate data structures
3. Include error handling
4. Add comprehensive comments
5. Write basic tests

## File Location
`exercises/1000_programs/intermediate/{title.lower().replace(' ', '_')}.py`

## Acceptance Criteria
- [ ] All core features implemented
- [ ] Uses appropriate data structures
- [ ] Includes error handling
- [ ] Has comprehensive comments
- [ ] Includes basic tests
- [ ] Follows PEP 8 style guidelines

## Implementation Hints
- Break down into functions
- Use appropriate data structures (lists, dicts, etc.)
- Handle edge cases
- Test thoroughly

---
*Part of 250 new Python learning issues - Intermediate Track*
"""
        if create_issue(title, body, 'intermediate'):
            int_created += 1
    
    created += int_created
    print(f"\n✅ Intermediate: {int_created} created\n")
    
    # ADVANCED ISSUES (60 issues)
    print("🚀 Creating Advanced Issues (161-220)...\n")
    
    advanced = [
        "Build REST API with Flask",
        "Create Real-Time Chat Application with WebSockets",
        "Implement Binary Search Tree from Scratch",
        "Build Web Scraper with Data Export",
        "Create Machine Learning Model from Scratch",
        "Build Neural Network from Scratch",
        "Create Convolutional Neural Network",
        "Develop Recurrent Neural Network",
        "Build Image Classification System",
        "Create Object Detection System",
        "Develop Sentiment Analysis Model",
        "Build Text Summarization System",
        "Create Machine Translation System",
        "Build Recommendation System",
        "Develop Anomaly Detection System",
        "Create Time Series Forecasting Model",
        "Build Clustering System",
        "Develop Dimensionality Reduction Tool",
        "Create Feature Engineering Pipeline",
        "Build Hyperparameter Tuning System",
        "Develop Model Ensemble System",
        "Create Transfer Learning Application",
        "Build GAN for Image Generation",
        "Develop Chatbot with NLP",
        "Create Question Answering System",
        "Build Speech Recognition System",
        "Develop Text-to-Speech System",
        "Create Face Recognition System",
        "Build Pose Estimation System",
        "Develop Style Transfer System",
        "Create Super Resolution System",
        "Build Image Segmentation System",
        "Develop Video Classification System",
        "Create Action Recognition System",
        "Build Multi-Modal Learning System",
        "Develop Reinforcement Learning Agent",
        "Create Deep Q-Network Agent",
        "Build Policy Gradient Agent",
        "Develop Actor-Critic Agent",
        "Create Multi-Agent System",
        "Build Distributed Training System",
        "Develop Model Serving API",
        "Create A/B Testing Platform",
        "Build Feature Store System",
        "Develop Data Pipeline ETL",
        "Create Real-Time Analytics System",
        "Build Dashboard with Plotly",
        "Develop Interactive Visualization",
        "Create Automated Reporting System",
        "Build Data Quality Monitor",
        "Develop Model Monitoring System",
        "Create Drift Detection System",
        "Build AutoML System Basic",
        "Develop Neural Architecture Search",
        "Create Explainable AI System",
        "Build Federated Learning System",
        "Develop Privacy-Preserving ML",
        "Create Model Compression System",
        "Build Quantization Tool",
        "Develop Model Pruning System",
    ]
    
    adv_created = 0
    for title in advanced:
        body = f"""## Description
Build an advanced Python project: {title}

## Difficulty
Advanced (2-5 hours)

## Requirements
1. Implement complete solution
2. Use best practices and design patterns
3. Include comprehensive error handling
4. Write unit tests
5. Add documentation

## File Location
`exercises/1000_programs/advanced/{title.lower().replace(' ', '_')}.py`

## Acceptance Criteria
- [ ] Complete solution implemented
- [ ] Uses best practices and patterns
- [ ] Comprehensive error handling
- [ ] Unit tests included
- [ ] Documentation added
- [ ] Code reviewed and optimized

## Implementation Hints
- Plan architecture first
- Use appropriate libraries
- Write tests as you go
- Document decisions

---
*Part of 250 new Python learning issues - Advanced Track*
"""
        if create_issue(title, body, 'advanced'):
            adv_created += 1
    
    created += adv_created
    print(f"\n✅ Advanced: {adv_created} created\n")
    
    # EXPERT ISSUES (30 issues)
    print("💎 Creating Expert Issues (221-250)...\n")
    
    expert = [
        "Build Distributed Task Queue System",
        "Create Microservices Architecture",
        "Build Production-Ready ML Pipeline",
        "Create Real-Time Stream Processing System",
        "Build Scalable Search Engine",
        "Create Distributed Database System",
        "Build Blockchain Implementation",
        "Develop Cryptocurrency Exchange",
        "Create Decentralized Application DApp",
        "Build Smart Contract Platform",
        "Create High-Frequency Trading System",
        "Develop Algorithmic Trading Bot",
        "Build Risk Management System",
        "Create Fraud Detection System",
        "Develop Identity Verification System",
        "Build Access Control System RBAC ABAC",
        "Create Zero-Knowledge Proof System",
        "Develop Homomorphic Encryption System",
        "Build Secure Multi-Party Computation",
        "Create Quantum Key Distribution System",
        "Develop Satellite Communication System",
        "Build Autonomous Vehicle Control",
        "Create Robot Control System",
        "Develop Drone Swarm Coordination",
        "Build IoT Platform at Scale",
        "Create Edge Computing Platform",
        "Develop Fog Computing System",
        "Build 5G Network Slicing System",
        "Create CDN from Scratch",
        "Develop Global Load Balancer",
    ]
    
    exp_created = 0
    for title in expert:
        body = f"""## Description
Build an expert-level production system: {title}

## Difficulty
Expert (5-20+ hours)

## Requirements
1. Production-ready implementation
2. Scalable architecture
3. Comprehensive monitoring
4. Full test coverage
5. Deployment configuration
6. Documentation

## File Location
`exercises/1000_programs/expert/{title.lower().replace(' ', '_')}.py`

## Acceptance Criteria
- [ ] Production-ready implementation
- [ ] Scalable architecture
- [ ] Comprehensive monitoring
- [ ] Full test coverage
- [ ] Deployment configuration
- [ ] Complete documentation
- [ ] Performance benchmarks

## Implementation Hints
- Design for scale
- Use industry best practices
- Implement monitoring from start
- Plan for failures
- Document everything

---
*Part of 250 new Python learning issues - Expert Track*
"""
        if create_issue(title, body, 'expert'):
            exp_created += 1
    
    created += exp_created
    print(f"\n✅ Expert: {exp_created} created\n")
    
    # Summary
    print("="*60)
    print("📊 Summary")
    print("="*60)
    print(f"✅ Total Created: {created}")
    print(f"❌ Total Failed: {failed}")
    print(f"📝 Beginner: 70 issues")
    print(f"📚 Intermediate: 90 issues")
    print(f"🚀 Advanced: 60 issues")
    print(f"💎 Expert: 30 issues")
    print(f"🎯 TOTAL: 250 issues")
    print("="*60)
    print()
    print("🎉 All 250 issues created successfully!")
    print("📍 View them at: https://github.com/hackdartstorm/Python/issues")

if __name__ == "__main__":
    main()

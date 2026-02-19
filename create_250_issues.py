#!/usr/bin/env python3
"""Script to create 250 GitHub issues with proper formatting"""

import subprocess
import time
import json

# Issue templates organized by difficulty
BEGINNER_ISSUES = [
    # Basic Input/Output (15 issues)
    ("Build ASCII Art Name Banner", "011_ascii_art_banner.py", "Create ASCII art banner from user's name"),
    ("Build Mad Libs Story Generator", "012_mad_libs_generator.py", "Create funny stories from user input words"),
    ("Build Personal Bio Generator", "013_bio_generator.py", "Generate formatted bio from user details"),
    ("Build Unit Converter Suite", "014_unit_converter.py", "Convert between common units"),
    ("Build Currency Converter CLI", "015_currency_converter.py", "Convert between currencies with fixed rates"),
    
    # String Manipulation (20 issues)
    ("Build Vowel Counter Program", "016_vowel_counter.py", "Count vowels in a string"),
    ("Build String Reversal Tool", "017_string_reversal.py", "Reverse string character by character"),
    ("Build Word Counter Program", "018_word_counter.py", "Count words in a sentence"),
    ("Build Character Frequency Analyzer", "019_char_frequency.py", "Count frequency of each character"),
    ("Build Case Converter Tool", "020_case_converter.py", "Convert between upper/lower/title case"),
    ("Build Palindrome Checker", "021_palindrome_checker.py", "Check if string is palindrome"),
    ("Build Anagram Checker", "022_anagram_checker.py", "Check if two strings are anagrams"),
    ("Build Caesar Cipher Encoder", "023_caesar_cipher.py", "Encode text with Caesar cipher"),
    ("Build Caesar Cipher Decoder", "024_caesar_decoder.py", "Decode Caesar cipher text"),
    ("Build String Compression Tool", "025_string_compression.py", "Compress repeated characters"),
    
    # Control Flow (15 issues)
    ("Build Even Odd Classifier", "026_even_odd_classifier.py", "Classify numbers as even or odd"),
    ("Build Positive Negative Checker", "027_sign_checker.py", "Check if number is positive/negative/zero"),
    ("Build Leap Year Checker", "028_leap_year_checker.py", "Check if year is leap year"),
    ("Build Grade Calculator", "029_grade_calculator.py", "Calculate letter grade from score"),
    ("Build Triangle Validator", "030_triangle_validator.py", "Check if sides form valid triangle"),
    
    # Functions Practice (15 issues)
    ("Build Factorial Calculator Function", "031_factorial_function.py", "Calculate factorial using functions"),
    ("Build Fibonacci Generator Function", "032_fibonacci_function.py", "Generate Fibonacci sequence"),
    ("Build Prime Checker Function", "033_prime_checker.py", "Check if number is prime"),
    ("Build GCD Calculator Function", "034_gcd_function.py", "Calculate greatest common divisor"),
    ("Build LCM Calculator Function", "035_lcm_function.py", "Calculate least common multiple"),
    
    # Data Structures (15 issues)
    ("Build List Statistics Calculator", "036_list_stats.py", "Calculate mean, median, mode of list"),
    ("Build List Duplicate Remover", "037_remove_duplicates.py", "Remove duplicates from list"),
    ("Build List Merger Tool", "038_merge_lists.py", "Merge two sorted lists"),
    ("Build Tuple Unpacker Program", "039_tuple_unpacker.py", "Demonstrate tuple unpacking"),
    ("Build Set Operations Tool", "040_set_operations.py", "Perform union, intersection, difference"),
]

INTERMEDIATE_ISSUES = [
    # File Handling (20 issues)
    ("Build File Line Counter", "041_line_counter.py", "Count lines in a text file"),
    ("Build File Word Counter", "042_word_counter_file.py", "Count words in a file"),
    ("Build File Backup Utility", "043_file_backup.py", "Create backup of files"),
    ("Build Log File Analyzer", "044_log_analyzer.py", "Analyze log file patterns"),
    ("Build CSV Data Reader", "045_csv_reader.py", "Read and display CSV data"),
    
    # OOP Projects (20 issues)
    ("Build Bank Account Class", "046_bank_account.py", "Implement bank account with deposit/withdraw"),
    ("Build Student Record System", "047_student_records.py", "Manage student records with OOP"),
    ("Build Library Book Manager", "048_library_manager.py", "Manage library books with OOP"),
    ("Build Employee Management System", "049_employee_system.py", "Manage employees with inheritance"),
    ("Build Shopping Cart Class", "050_shopping_cart.py", "Implement shopping cart with OOP"),
    
    # API Projects (20 issues)
    ("Build Weather API Client", "051_weather_client.py", "Fetch weather data from API"),
    ("Build REST API Client", "052_rest_client.py", "Make HTTP requests to REST API"),
    ("Build JSON Data Parser", "053_json_parser.py", "Parse and display JSON data"),
    ("Build API Rate Limiter", "054_rate_limiter.py", "Implement API rate limiting"),
    ("Build URL Shortener CLI", "055_url_shortener.py", "Shorten URLs using API"),
    
    # Data Processing (20 issues)
    ("Build Data Filter Tool", "056_data_filter.py", "Filter data based on criteria"),
    ("Build Data Sorter Program", "057_data_sorter.py", "Sort data by multiple keys"),
    ("Build Data Aggregator", "058_data_aggregator.py", "Aggregate data by groups"),
    ("Build Report Generator", "059_report_generator.py", "Generate formatted reports"),
    ("Build Data Validator Tool", "060_data_validator.py", "Validate data formats"),
]

ADVANCED_ISSUES = [
    # Web Development (20 issues)
    ("Build Flask REST API Server", "061_flask_api.py", "Create REST API with Flask"),
    ("Build FastAPI Endpoint", "062_fastapi_endpoint.py", "Create endpoint with FastAPI"),
    ("Build Web Scraper Tool", "063_web_scraper.py", "Scrape data from websites"),
    ("Build URL Parser Tool", "064_url_parser.py", "Parse and validate URLs"),
    ("Build HTML Template Renderer", "065_template_renderer.py", "Render HTML templates"),
    
    # Database Integration (15 issues)
    ("Build SQLite Database Manager", "066_sqlite_manager.py", "Manage SQLite database"),
    ("Build CRUD Operations Tool", "067_crud_tool.py", "Implement CRUD operations"),
    ("Build Database Backup Tool", "068_db_backup.py", "Backup database to file"),
    ("Build Query Builder Tool", "069_query_builder.py", "Build SQL queries dynamically"),
    ("Build Database Migration Tool", "070_db_migration.py", "Migrate database schema"),
    
    # Automation Tools (15 issues)
    ("Build File Organizer Script", "071_file_organizer.py", "Organize files by extension"),
    ("Build Bulk File Renamer", "072_bulk_renamer.py", "Rename multiple files"),
    ("Build Directory Tree Generator", "073_tree_generator.py", "Generate directory tree"),
    ("Build Disk Usage Analyzer", "074_disk_analyzer.py", "Analyze disk usage"),
    ("Build System Info Collector", "075_system_info.py", "Collect system information"),
    
    # Testing & Debugging (10 issues)
    ("Build Unit Test Suite", "076_unit_tests.py", "Write unit tests for module"),
    ("Build Integration Test Suite", "077_integration_tests.py", "Write integration tests"),
    ("Build Mock Data Generator", "078_mock_generator.py", "Generate test data"),
    ("Build Code Coverage Tool", "079_coverage_tool.py", "Measure code coverage"),
    ("Build Debug Logger Tool", "080_debug_logger.py", "Implement debug logging"),
]

EXPERT_ISSUES = [
    # System Design (8 issues)
    ("Build Distributed Task Queue", "081_task_queue.py", "Implement distributed task queue"),
    ("Build Message Queue System", "082_message_queue.py", "Implement message queue"),
    ("Build Load Balancer Simulator", "083_load_balancer.py", "Simulate load balancing"),
    ("Build Cache System Implementation", "084_cache_system.py", "Implement caching system"),
    ("Build Rate Limiter Service", "085_rate_limiter_service.py", "Build rate limiting service"),
    ("Build Circuit Breaker Pattern", "086_circuit_breaker.py", "Implement circuit breaker"),
    ("Build Event Sourcing System", "087_event_sourcing.py", "Implement event sourcing"),
    ("Build CQRS Implementation", "088_cqrs_impl.py", "Implement CQRS pattern"),
    
    # Performance Optimization (6 issues)
    ("Build Memory Profiler Tool", "089_memory_profiler.py", "Profile memory usage"),
    ("Build CPU Profiler Tool", "090_cpu_profiler.py", "Profile CPU usage"),
    ("Build Performance Benchmark Tool", "091_benchmark_tool.py", "Benchmark code performance"),
    ("Build Algorithm Optimizer", "092_algo_optimizer.py", "Optimize algorithm performance"),
    ("Build Database Query Optimizer", "093_query_optimizer.py", "Optimize database queries"),
    ("Build Caching Strategy Tool", "094_cache_strategy.py", "Implement caching strategies"),
    
    # Security Tools (6 issues)
    ("Build Password Hash Generator", "095_password_hasher.py", "Generate secure password hashes"),
    ("Build JWT Token Handler", "096_jwt_handler.py", "Handle JWT tokens"),
    ("Build Encryption Tool", "097_encryption_tool.py", "Encrypt/decrypt data"),
    ("Build Security Scanner", "098_security_scanner.py", "Scan for security issues"),
    ("Build Input Sanitizer", "099_input_sanitizer.py", "Sanitize user input"),
    ("Build Authentication System", "100_auth_system.py", "Build authentication system"),
]

def create_issue(title, file, description, difficulty, labels):
    """Create a GitHub issue using gh CLI"""
    body = f"""## Description
{description}

## Difficulty
{difficulty}

## File Location
exercises/1000_programs/{difficulty.lower()}/{file}

## Requirements
- [ ] Accept user input where applicable
- [ ] Implement core functionality
- [ ] Display formatted output
- [ ] Validate input
- [ ] Add error handling
- [ ] Include docstrings
- [ ] Add type hints

## Expected Behavior
Program should execute correctly and produce expected output for given inputs.

## Acceptance Criteria
- [ ] Core functionality works correctly
- [ ] Input validation implemented
- [ ] Clear output formatting
- [ ] Error handling for edge cases
- [ ] Code follows PEP 8 style
- [ ] Type hints included
- [ ] Docstrings present

## Hints
- Break problem into smaller functions
- Test with various inputs
- Consider edge cases
- Use appropriate data structures

## Related Issues
Part of 250 issues initiative for Python practice exercises"""

    cmd = [
        "gh", "issue", "create",
        "--title", f"[{difficulty.upper()}] {title}",
        "--body", body,
        "--label", labels
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print(f"✓ Created: {title}")
            return True
        else:
            print(f"✗ Failed: {title} - {result.stderr}")
            return False
    except Exception as e:
        print(f"✗ Error: {title} - {str(e)}")
        return False

def main():
    """Create all 250 issues"""
    total = 0
    success = 0
    
    print("Creating BEGINNER issues...")
    for title, file, desc in BEGINNER_ISSUES:
        if create_issue(title, file, desc, "Beginner", "good first issue,beginner,exercise"):
            success += 1
        total += 1
        time.sleep(2)  # Rate limiting
    
    print("\nCreating INTERMEDIATE issues...")
    for title, file, desc in INTERMEDIATE_ISSUES:
        if create_issue(title, file, desc, "Intermediate", "intermediate,exercise"):
            success += 1
        total += 1
        time.sleep(2)
    
    print("\nCreating ADVANCED issues...")
    for title, file, desc in ADVANCED_ISSUES:
        if create_issue(title, file, desc, "Advanced", "advanced,exercise"):
            success += 1
        total += 1
        time.sleep(2)
    
    print("\nCreating EXPERT issues...")
    for title, file, desc in EXPERT_ISSUES:
        if create_issue(title, file, desc, "Expert", "expert,exercise"):
            success += 1
        total += 1
        time.sleep(2)
    
    print(f"\n{'='*50}")
    print(f"Total: {success}/{total} issues created successfully")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()

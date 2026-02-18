# ⭐⭐ Medium Python Programs (301-600)

**Time:** 30 min - 2 hours each | **Difficulty:** ⭐⭐ Medium

---

## File Handling (301-350)

### #301 - Read File and Count Lines
**File:** `basics/07_file_handling/301_count_lines.py`
**Task:** Count total lines in a file
**Skills:** open(), readlines(), len()

### #302 - Read File and Count Words
**File:** `basics/07_file_handling/302_count_words.py`
**Task:** Count total words in a file
**Skills:** read(), split(), len()

### #303 - Read File and Count Characters
**File:** `basics/07_file_handling/303_count_characters.py`
**Task:** Count total characters in a file
**Skills:** read(), len()

### #304 - Copy Content from One File to Another
**File:** `basics/07_file_handling/304_copy_file.py`
**Task:** Copy contents of file1 to file2
**Skills:** read(), write()

### #305 - Merge Two Files into Third File
**File:** `basics/07_file_handling/305_merge_files.py`
**Task:** Merge file1 and file2 into file3
**Skills:** read(), write(), append

### #306 - Find and Replace Word in File
**File:** `basics/07_file_handling/306_find_replace.py`
**Task:** Replace all occurrences of a word
**Skills:** read(), replace(), write()

### #307 - Remove Duplicate Lines from File
**File:** `basics/07_file_handling/307_remove_duplicate_lines.py`
**Task:** Remove duplicate lines from file
**Skills:** set(), readlines()

### #308 - Sort Lines in File Alphabetically
**File:** `basics/07_file_handling/308_sort_lines.py`
**Task:** Sort all lines in file
**Skills:** readlines(), sorted()

### #309 - Split File into Multiple Files
**File:** `basics/07_file_handling/309_split_file.py`
**Task:** Split file by line count
**Skills:** readlines(), write()

### #310 - Combine Multiple Files into One
**File:** `basics/07_file_handling/310_combine_files.py`
**Task:** Combine multiple files
**Skills:** glob, write()

### #311 - Find Longest Word in File
**File:** `basics/07_file_handling/311_longest_word.py`
**Task:** Find longest word in file
**Skills:** read(), split(), max()

### #312 - Find Most Frequent Word in File
**File:** `basics/07_file_handling/312_frequent_word.py`
**Task:** Find most frequent word
**Skills:** dictionary, count

### #313 - Count Occurrences of a Word in File
**File:** `basics/07_file_handling/313_count_word.py`
**Task:** Count how many times word appears
**Skills:** read(), count()

### #314 - Extract Emails from File
**File:** `basics/07_file_handling/314_extract_emails.py`
**Task:** Extract all email addresses
**Skills:** regex, findall()

### #315 - Extract Phone Numbers from File
**File:** `basics/07_file_handling/315_extract_phones.py`
**Task:** Extract all phone numbers
**Skills:** regex, findall()

### #316 - Extract URLs from File
**File:** `basics/07_file_handling/316_extract_urls.py`
**Task:** Extract all URLs from file
**Skills:** regex, findall()

### #317 - Create Log File Analyzer
**File:** `basics/07_file_handling/317_log_analyzer.py`
**Task:** Analyze log file for errors
**Skills:** read(), pattern matching

### #318 - Find Errors in Log File
**File:** `basics/07_file_handling/318_find_errors.py`
**Task:** Find all ERROR entries
**Skills:** grep-like search

### #319 - Generate Report from CSV File
**File:** `basics/07_file_handling/319_csv_report.py`
**Task:** Generate summary from CSV
**Skills:** csv module

### #320 - Write Student Data to CSV
**File:** `basics/07_file_handling/320_write_csv.py`
**Task:** Write student records to CSV
**Skills:** csv.writer()

### #321 - Read Student Data from CSV
**File:** `basics/07_file_handling/321_read_csv.py`
**Task:** Read and parse CSV file
**Skills:** csv.reader()

### #322 - Calculate Average from CSV
**File:** `basics/07_file_handling/322_csv_average.py`
**Task:** Calculate average of column
**Skills:** csv, statistics

### #323 - Filter CSV by Condition
**File:** `basics/07_file_handling/323_filter_csv.py`
**Task:** Filter rows by condition
**Skills:** csv, conditionals

### #324 - Sort CSV by Column
**File:** `basics/07_file_handling/324_sort_csv.py`
**Task:** Sort CSV by specific column
**Skills:** csv, sorted()

### #325 - Add Column to CSV
**File:** `basics/07_file_handling/325_add_csv_column.py`
**Task:** Add new column to CSV
**Skills:** csv, write

### #326 - Remove Column from CSV
**File:** `basics/07_file_handling/326_remove_csv_column.py`
**Task:** Remove column from CSV
**Skills:** csv, filtering

### #327 - Merge Two CSV Files
**File:** `basics/07_file_handling/327_merge_csv.py`
**Task:** Merge CSV files by key
**Skills:** csv, join

### #328 - Split CSV into Multiple Files
**File:** `basics/07_file_handling/328_split_csv.py`
**Task:** Split CSV by column value
**Skills:** csv, groupby

### #329 - Convert CSV to JSON
**File:** `basics/07_file_handling/329_csv_to_json.py`
**Task:** Convert CSV file to JSON
**Skills:** csv, json

### #330 - Convert JSON to CSV
**File:** `basics/07_file_handling/330_json_to_csv.py`
**Task:** Convert JSON file to CSV
**Skills:** json, csv

### #331 - Read JSON Configuration File
**File:** `basics/07_file_handling/331_read_json_config.py`
**Task:** Read and parse JSON config
**Skills:** json.load()

### #332 - Write Settings to JSON File
**File:** `basics/07_file_handling/332_write_json.py`
**Task:** Write settings to JSON
**Skills:** json.dump()

### #333 - Update JSON Configuration
**File:** `basics/07_file_handling/333_update_json.py`
**Task:** Update specific key in JSON
**Skills:** json, update

### #334 - Validate JSON File
**File:** `basics/07_file_handling/334_validate_json.py`
**Task:** Check if file is valid JSON
**Skills:** json, try/except

### #335 - Pretty Print JSON File
**File:** `basics/07_file_handling/335_pretty_print_json.py`
**Task:** Format JSON with indentation
**Skills:** json.dumps(indent=)

### #336 - Create Backup of File
**File:** `basics/07_file_handling/336_backup_file.py`
**Task:** Create timestamped backup
**Skills:** shutil, datetime

### #337 - Compress File Using gzip
**File:** `basics/07_file_handling/337_compress_gzip.py`
**Task:** Compress file with gzip
**Skills:** gzip module

### #338 - Decompress gzip File
**File:** `basics/07_file_handling/338_decompress_gzip.py`
**Task:** Decompress gzip file
**Skills:** gzip module

### #339 - Find File Size
**File:** `basics/07_file_handling/339_file_size.py`
**Task:** Find size of file in bytes
**Skills:** os.path.getsize()

### #340 - Find File Creation Date
**File:** `basics/07_file_handling/340_file_creation_date.py`
**Task:** Get file creation timestamp
**Skills:** os.path.getctime()

### #341 - Find File Modification Date
**File:** `basics/07_file_handling/341_file_modification_date.py`
**Task:** Get file modification timestamp
**Skills:** os.path.getmtime()

### #342 - List All Files in Directory
**File:** `basics/07_file_handling/342_list_files.py`
**Task:** List all files in directory
**Skills:** os.listdir()

### #343 - List All Python Files in Directory
**File:** `basics/07_file_handling/343_list_python_files.py`
**Task:** List only .py files
**Skills:** glob, filter

### #344 - Find Largest File in Directory
**File:** `basics/07_file_handling/344_largest_file.py`
**Task:** Find file with largest size
**Skills:** os.path.getsize(), max()

### #345 - Find Smallest File in Directory
**File:** `basics/07_file_handling/345_smallest_file.py`
**Task:** Find file with smallest size
**Skills:** os.path.getsize(), min()

### #346 - Find Duplicate Files
**File:** `basics/07_file_handling/346_find_duplicate_files.py`
**Task:** Find files with same content
**Skills:** hashlib, comparison

### #347 - Rename All Files in Directory
**File:** `basics/07_file_handling/347_rename_files.py`
**Task:** Batch rename files
**Skills:** os.rename()

### #348 - Delete All Temporary Files
**File:** `basics/07_file_handling/348_delete_temp_files.py`
**Task:** Delete .tmp, .bak files
**Skills:** glob, os.remove()

### #349 - Organize Files by Extension
**File:** `basics/07_file_handling/349_organize_by_extension.py`
**Task:** Sort files into folders by ext
**Skills:** os, shutil

### #350 - Create File Directory Tree
**File:** `basics/07_file_handling/350_directory_tree.py`
**Task:** Print directory tree structure
**Skills:** os.walk()

---

## OOP Programs (351-400)

### #351 - Create a Class for Book
**File:** `basics/08_oop/351_book_class.py`
**Task:** Create Book class with attributes
**Skills:** class, __init__

### #352 - Create a Class for Student
**File:** `basics/08_oop/352_student_class.py`
**Task:** Create Student class
**Skills:** class, methods

### #353 - Create a Class for Employee
**File:** `basics/08_oop/353_employee_class.py`
**Task:** Create Employee class
**Skills:** class, attributes

### #354 - Create a Class for Bank Account
**File:** `basics/08_oop/354_bank_account_class.py`
**Task:** Create BankAccount class
**Skills:** class, methods, state

### #355 - Create a Class for Rectangle
**File:** `basics/08_oop/355_rectangle_class.py`
**Task:** Create Rectangle with area method
**Skills:** class, methods

### #356 - Create a Class for Circle
**File:** `basics/08_oop/356_circle_class.py`
**Task:** Create Circle with area method
**Skills:** class, math

### #357 - Create a Class for Triangle
**File:** `basics/08_oop/357_triangle_class.py`
**Task:** Create Triangle class
**Skills:** class, geometry

### #358 - Create a Class for Complex Number
**File:** `basics/08_oop/358_complex_number_class.py`
**Task:** Create ComplexNumber class
**Skills:** class, operations

### #359 - Create a Class for Fraction
**File:** `basics/08_oop/359_fraction_class.py`
**Task:** Create Fraction class
**Skills:** class, arithmetic

### #360 - Create a Class for Vector
**File:** `basics/08_oop/360_vector_class.py`
**Task:** Create Vector class
**Skills:** class, vector ops

### #361 - Create a Class for Date
**File:** `basics/08_oop/361_date_class.py`
**Task:** Create Date class
**Skills:** class, date ops

### #362 - Create a Class for Time
**File:** `basics/08_oop/362_time_class.py`
**Task:** Create Time class
**Skills:** class, time ops

### #363 - Create a Class for PhoneNumber
**File:** `basics/08_oop/363_phone_class.py`
**Task:** Create PhoneNumber class
**Skills:** class, validation

### #364 - Create a Class for Email
**File:** `basics/08_oop/364_email_class.py`
**Task:** Create Email class
**Skills:** class, validation

### #365 - Create a Class for Address
**File:** `basics/08_oop/365_address_class.py`
**Task:** Create Address class
**Skills:** class, formatting

### #366 - Create a Class for Product
**File:** `basics/08_oop/366_product_class.py`
**Task:** Create Product class
**Skills:** class, pricing

### #367 - Create a Class for ShoppingCart
**File:** `basics/08_oop/367_cart_class.py`
**Task:** Create ShoppingCart class
**Skills:** class, list ops

### #368 - Create a Class for Order
**File:** `basics/08_oop/368_order_class.py`
**Task:** Create Order class
**Skills:** class, status

### #369 - Create a Class for Customer
**File:** `basics/08_oop/369_customer_class.py`
**Task:** Create Customer class
**Skills:** class, attributes

### #370 - Create a Class for Movie
**File:** `basics/08_oop/370_movie_class.py`
**Task:** Create Movie class
**Skills:** class, media

### #371 - Create a Class for Song
**File:** `basics/08_oop/371_song_class.py`
**Task:** Create Song class
**Skills:** class, music

### #372 - Create a Class for Playlist
**File:** `basics/08_oop/372_playlist_class.py`
**Task:** Create Playlist class
**Skills:** class, list ops

### #373 - Create a Class for Library
**File:** `basics/08_oop/373_library_class.py`
**Task:** Create Library class
**Skills:** class, collection

### #374 - Create a Class for University
**File:** `basics/08_oop/374_university_class.py`
**Task:** Create University class
**Skills:** class, composition

### #375 - Create a Class for Hospital
**File:** `basics/08_oop/375_hospital_class.py`
**Task:** Create Hospital class
**Skills:** class, management

### #376 - Create a Class for Patient
**File:** `basics/08_oop/376_patient_class.py`
**Task:** Create Patient class
**Skills:** class, medical

### #377 - Create a Class for Doctor
**File:** `basics/08_oop/377_doctor_class.py`
**Task:** Create Doctor class
**Skills:** class, specialization

### #378 - Create a Class for Vehicle
**File:** `basics/08_oop/378_vehicle_class.py`
**Task:** Create Vehicle base class
**Skills:** class, inheritance

### #379 - Create a Class for Car
**File:** `basics/08_oop/379_car_class.py`
**Task:** Create Car class (inherits Vehicle)
**Skills:** inheritance

### #380 - Create a Class for Bike
**File:** `basics/08_oop/380_bike_class.py`
**Task:** Create Bike class
**Skills:** inheritance

### #381 - Create a Class for Airplane
**File:** `basics/08_oop/381_airplane_class.py`
**Task:** Create Airplane class
**Skills:** inheritance

### #382 - Create a Class for Ship
**File:** `basics/08_oop/382_ship_class.py`
**Task:** Create Ship class
**Skills:** inheritance

### #383 - Implement Inheritance for Animals
**File:** `basics/08_oop/383_animal_inheritance.py`
**Task:** Create Animal hierarchy
**Skills:** inheritance hierarchy

### #384 - Implement Inheritance for Shapes
**File:** `basics/08_oop/384_shape_inheritance.py`
**Task:** Create Shape hierarchy
**Skills:** inheritance, polymorphism

### #385 - Implement Inheritance for Employees
**File:** `basics/08_oop/385_employee_inheritance.py`
**Task:** Create Employee hierarchy
**Skills:** inheritance

### #386 - Implement Inheritance for Students
**File:** `basics/08_oop/386_student_inheritance.py`
**Task:** Create Student hierarchy
**Skills:** inheritance

### #387 - Implement Multiple Inheritance
**File:** `basics/08_oop/387_multiple_inheritance.py`
**Task:** Class with multiple parents
**Skills:** multiple inheritance

### #388 - Implement Multilevel Inheritance
**File:** `basics/08_oop/388_multilevel_inheritance.py`
**Task:** Grandparent-Parent-Child
**Skills:** multilevel inheritance

### #389 - Implement Hierarchical Inheritance
**File:** `basics/08_oop/389_hierarchical_inheritance.py`
**Task:** One parent, multiple children
**Skills:** hierarchical inheritance

### #390 - Implement Hybrid Inheritance
**File:** `basics/08_oop/390_hybrid_inheritance.py`
**Task:** Combination of inheritances
**Skills:** hybrid inheritance

### #391 - Create Abstract Class for Payment
**File:** `basics/08_oop/391_abstract_payment.py`
**Task:** Create abstract Payment class
**Skills:** abc, abstractmethod

### #392 - Create Abstract Class for Database
**File:** `basics/08_oop/392_abstract_database.py`
**Task:** Create abstract Database class
**Skills:** abc, abstractmethod

### #393 - Implement Operator Overloading
**File:** `basics/08_oop/393_operator_overloading.py`
**Task:** Overload +, -, *, etc.
**Skills:** __add__, __sub__

### #394 - Implement Method Overloading
**File:** `basics/08_oop/394_method_overloading.py`
**Task:** Same method, different params
**Skills:** *args, **kwargs

### #395 - Implement Method Overriding
**File:** `basics/08_oop/395_method_overriding.py`
**Task:** Override parent method
**Skills:** inheritance, override

### #396 - Create Class with Properties
**File:** `basics/08_oop/396_properties.py`
**Task:** Use @property decorator
**Skills:** @property, getters/setters

### #397 - Implement Encapsulation
**File:** `basics/08_oop/397_encapsulation.py`
**Task:** Private and public members
**Skills:** __private, _protected

### #398 - Implement Data Hiding
**File:** `basics/08_oop/398_data_hiding.py`
**Task:** Hide sensitive data
**Skills:** name mangling

### #399 - Create Singleton Class
**File:** `basics/08_oop/399_singleton.py`
**Task:** Ensure only one instance
**Skills:** __new__, singleton

### #400 - Create Factory Class
**File:** `basics/08_oop/400_factory.py`
**Task:** Factory pattern implementation
**Skills:** factory pattern

---

**Total Medium Programs: 100 (301-400 shown)**
**Remaining:** 401-600 (Database, API, Web Scraping, Data Analysis)

---

## Progress Tracking

- [x] Programs 301-350 completed (File Handling)
- [x] Programs 351-400 completed (OOP)
- [ ] Programs 401-450 completed (Database)
- [ ] Programs 451-500 completed (API)
- [ ] Programs 501-550 completed (Web Scraping)
- [ ] Programs 551-600 completed (Data Analysis)

---

**Previous:** [Easy Programs 201-300](./EASY_PROGRAMS_201-300.md)  
**Next:** [Medium Programs 401-600](./MEDIUM_PROGRAMS_401-600.md)

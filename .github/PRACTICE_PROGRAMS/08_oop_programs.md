# Practice Programs: Object-Oriented Programming (08_oop)

**Total Programs:** 20 | **Easy:** 10 | **Medium:** 7 | **Hard:** 3

---

## Easy Programs (1-10)

### 001 - Create Simple Class
**Difficulty:** Easy  
**Description:** Create a Person class with name and age attributes.  
**Learning:** Class definition, `__init__`, attributes  
**Expected:** `Person("Alice", 25)`

### 002 - Add Method to Class
**Difficulty:** Easy  
**Description:** Add greet method to Person class.  
**Learning:** Instance methods, `self`  
**Expected:** `person.greet()` → `Hello, I'm Alice`

### 003 - Class with Calculator
**Difficulty:** Easy  
**Description:** Create Calculator class with add, subtract methods.  
**Learning:** Multiple methods  
**Expected:** `calc.add(5, 3)` → `8`

### 004 - Class Attributes
**Difficulty:** Easy  
**Description:** Create class with class-level attributes.  
**Learning:** Class vs instance attributes  
**Expected:** Shared attributes across instances

### 005 - Constructor with Default Values
**Difficulty:** Easy  
**Description:** Create class with optional parameters.  
**Learning:** Default parameter values  
**Expected:** `Student("Bob", grade=10)`

### 006 - String Representation
**Difficulty:** Easy  
**Description:** Implement `__str__` method for custom output.  
**Learning:** Magic methods, string representation  
**Expected:** `print(obj)` shows custom format

### 007 - Bank Account Class
**Difficulty:** Easy  
**Description:** Create account with deposit/withdraw methods.  
**Learning:** State management  
**Expected:** `account.deposit(100)`

### 008 - Rectangle Class
**Difficulty:** Easy  
**Description:** Create rectangle with area and perimeter methods.  
**Learning:** Geometric calculations  
**Expected:** `rect.area()` → `50`

### 009 - Student Class
**Difficulty:** Easy  
**Description:** Create student with marks and average method.  
**Learning:** List attribute, calculations  
**Expected:** `student.average()` → `85.5`

### 010 - Book Class
**Difficulty:** Easy  
**Description:** Create book with title, author, pages.  
**Learning:** Multiple attributes  
**Expected:** `book.info()` displays details

---

## Medium Programs (11-17)

### 011 - Inheritance: Employee
**Difficulty:** Medium  
**Description:** Create Employee class inheriting from Person.  
**Learning:** Single inheritance, `super()`  
**Expected:** `Employee` extends `Person`

### 012 - Method Overriding
**Difficulty:** Medium  
**Description:** Override parent method in child class.  
**Learning:** Polymorphism  
**Expected:** Child has custom behavior

### 013 - Multiple Inheritance
**Difficulty:** Medium  
**Description:** Create class inheriting from two parents.  
**Learning:** Multiple inheritance  
**Expected:** Combined functionality

### 014 - Class with Private Attributes
**Difficulty:** Medium  
**Description:** Implement encapsulation with private variables.  
**Learning:** `_variable`, name mangling  
**Expected:** Protected data access

### 015 - Property Decorator
**Difficulty:** Medium  
**Description:** Use `@property` for getter/setter.  
**Learning:** Property decorators  
**Expected:** `obj.value` with validation

### 016 - Static and Class Methods
**Difficulty:** Medium  
**Description:** Implement `@staticmethod` and `@classmethod`.  
**Learning:** Method types  
**Expected:** Both method types working

### 017 - Operator Overloading
**Difficulty:** Medium  
**Description:** Overload `+`, `-`, `==` operators.  
**Learning:** `__add__`, `__sub__`, `__eq__`  
**Expected:** `obj1 + obj2` works

---

## Hard Programs (18-20)

### 018 - Library Management System
**Difficulty:** Hard  
**Description:** Complete system with Book, Member, Library classes.  
**Learning:** Multiple classes, relationships  
**Expected:** Full working system

### 019 - Shape Hierarchy
**Difficulty:** Hard  
**Description:** Create Shape base class with Circle, Rectangle, Triangle.  
**Learning:** Abstract base classes, polymorphism  
**Expected:** `shape.area()` works for all

### 020 - Card Game Framework
**Difficulty:** Hard  
**Description:** Create Card, Deck, Player classes for card games.  
**Learning:** Complex OOP design  
**Expected:** Working deck shuffling, dealing

---

## Files to Create

```
basics/08_oop/
├── easy/
│   ├── 01_person_class.py
│   ├── 02_greet_method.py
│   ├── 03_calculator_class.py
│   ├── 04_class_attributes.py
│   ├── 05_default_constructor.py
│   ├── 06_str_method.py
│   ├── 07_bank_account.py
│   ├── 08_rectangle_class.py
│   ├── 09_student_class.py
│   └── 10_book_class.py
├── medium/
│   ├── 11_inheritance_employee.py
│   ├── 12_method_overriding.py
│   ├── 13_multiple_inheritance.py
│   ├── 14_private_attributes.py
│   ├── 15_property_decorator.py
│   ├── 16_static_class_methods.py
│   └── 17_operator_overloading.py
└── hard/
    ├── 18_library_system.py
    ├── 19_shape_hierarchy.py
    └── 20_card_game_framework.py
```

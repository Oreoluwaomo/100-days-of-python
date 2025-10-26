# Day 16 - Coffee Machine in OOP

## Overview
Day 16 was all about **refactoring the Coffee Machine project** from Day 15 into an **object-oriented program (OOP)**.  
This version focuses on organizing the logic into **classes and objects**, showing how OOP makes complex programs cleaner, more scalable, and easier to maintain.

By applying OOP principles, I transformed a procedural coffee machine simulation into a structured, modular system with clear responsibilities.

---

## Concepts Learned
- **Object-Oriented Programming (OOP)** fundamentals:
  - Classes and objects  
  - Methods and attributes  
  - Composition (using objects within other objects)
- How to refactor procedural code into a **class-based structure**
- Importing and working with **multiple class files**
- Understanding **encapsulation** and **responsibility separation**
- How to make classes **interact** to achieve a shared goal

---

## Project Description
The **OOP Coffee Machine** simulates the same functionality as before but with improved organization.  
It uses multiple classes to handle different tasks:  

### Components
- **`CoffeeMaker`** — manages ingredients and makes the drinks  
- **`Menu`** — stores available drinks and their ingredients  
- **`MenuItem`** — represents each drink as an object  
- **`MoneyMachine`** — handles payments and transactions  
- **`main.py`** — runs the overall coffee machine loop  

### How It Works
1. The program displays available menu options.  
2. The user selects a drink or types `report`/`off`.  
3. The system checks:
   - If resources are sufficient (`CoffeeMaker`)  
   - If payment is successful (`MoneyMachine`)  
4. If both pass, the drink is made.  

---

## Code Files
- `main.py` — coordinates interactions between objects  
- `menu.py` — defines `Menu` and `MenuItem` classes  
- `coffee_maker.py` — defines the `CoffeeMaker` class  
- `money_machine.py` — defines the `MoneyMachine` class  

---

## Reflection
This project showed me the **power of OOP** in simplifying large programs.  
Instead of long procedural code, I worked with **modular, reusable classes** that each handled one part of the system.  

It also helped me think like a software engineer — designing systems where each component has a clear purpose and interacts with others predictably.

---

## Summary of What I Learned
- How to refactor procedural code into an OOP model  
- How to create and use multiple classes in one project  
- How to organize code using encapsulation and composition  
- How objects communicate and work together  
- How OOP makes programs easier to read, maintain, and extend

# Day 15 - Coffee Machine Project

## Overview
On Day 15, I built a **Coffee Machine simulation program** using Python.  
The goal was to simulate how a real coffee machine operates — taking orders, checking resources, processing coins, and serving coffee.  

This project was my first deeper introduction to **code logic that models real-world systems**, where multiple functions interact and manage shared data.

---

## Concepts Learned
- How to use **functions** to break a larger program into smaller tasks  
- Working with **nested dictionaries** to represent data (menu, ingredients, and prices)  
- How to manage and update a **resource inventory**  
- Using **loops and conditionals** to control program flow  
- Implementing **user input handling** and validation  
- Simulating **a transaction system** — calculating payments and giving change  
- Practicing **procedural programming** to organize code clearly  

---

## Project Description
The **Coffee Machine Program** lets the user choose between drinks like **espresso**, **latte**, or **cappuccino**.  
The program checks if there are enough ingredients, processes inserted coins, and then “makes” the drink if all conditions are met.

### How It Works
1. The user selects a drink (espresso/latte/cappuccino).  
2. The program checks if there are enough ingredients in the machine.  
3. The user is asked to “insert coins”.  
4. The total amount is compared to the drink cost:
   - If sufficient, the drink is made, and resources are updated.  
   - If not, the money is refunded.  
5. The user can also type:
   - **`report`** → to display the remaining ingredients and profit.  
   - **`off`** → to turn off the machine (end program).  

---

## Code Files
- `main.py` — runs the main loop and handles input/output  
- `menu` (dictionary) — contains all drink types, ingredients, and costs  
- `resources` (dictionary) — stores available milk, coffee, and water quantities  

---

## Reflection
This project taught me how to manage **data flow** between functions and how to think step-by-step like a machine.  
It strengthened my understanding of:
- **Procedural thinking**  
- **Data structures (dictionaries)**  
- **Code logic for system design**

I also got to experience debugging real world logic issues, like handling insufficient funds or missing ingredients.

---

## Summary of What I Learned
- How to simulate a real-world process using code  
- How to use nested dictionaries for structured data  
- How to manage state and update data dynamically  
- How to organize code with functions for better readability  
- How to design a user-interactive program with clear logic

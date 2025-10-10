# 🐍 Day 3 – Control Flow and Logical Operators

## 📘 Overview
Day 3 of the **100 Days of Python** challenge focused on **control flow** — how programs make decisions using conditions.  
I learned how to use:
- `if`, `elif`, and `else` statements  
- **Comparison operators** (`>`, `<`, `>=`, `<=`, `==`, `!=`)  
- **Logical operators** (`and`, `or`, `not`)  
- **Nested conditionals** (if statements inside other if statements)  
- **Code indentation and scope** — why alignment matters in Python  

These concepts allow a program to make decisions based on user input or conditions.

---

## 🍕 Project 1: Pizza Order Calculator

### 🎯 Goal
Build a small program that calculates the final bill for a pizza order based on user choices.

### 🧠 What I Learned
- How to take user input using `input()`
- How to use multiple conditions to control program flow
- How to incrementally add to a variable (`bill += value`)
- Importance of order in condition checks

### 💻 Example Code
```python
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")

🧾 Example Output
Welcome to Python Pizza Deliveries!
What size pizza do you want? M
Do you want pepperoni? Y
Do you want extra cheese? Y
Your final bill is: $24

🗺️ Project 2: Treasure Island Game
🎯 Goal

Create an interactive text-based adventure game where the user must make choices to find hidden treasure.

🧠 What I Learned

How to combine if/else statements to create story-based decisions

Importance of string comparison and input validation

How to structure text-based games logically

How to use nested conditionals effectively
💻 Example Code
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right": ').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle. Type "wait" to wait for a boat or "swim" to swim across: ').lower()
    if choice2 == "wait":
        choice3 = input('You arrive safely on the island. There is a house with 3 doors: one red, one yellow, and one blue. Which do you choose? ').lower()
        if choice3 == "yellow":
            print("You found the treasure! You win! 🏆")
        elif choice3 == "red":
            print("Burned by fire. Game Over 🔥")
        elif choice3 == "blue":
            print("Eaten by beasts. Game Over 🐉")
        else:
            print("You chose a door that doesn’t exist. Game Over.")
    else:
        print("You got attacked by a trout. Game Over 🐟")
else:
    print("You fell into a hole. Game Over 💀")

🧾 Example Output
Welcome to Treasure Island.
Your mission is to find the treasure.
You're at a cross road. Where do you want to go? left
You've come to a lake. Type "wait" to wait for a boat or "swim" to swim across: wait
You arrive at the island unharmed. There is a house with 3 doors: one red, one yellow, and one blue. Which one do you choose? yellow
You found the treasure! You Win! 🏆

🗓️ My Reflection

This day was really fun and practical!
I learned how logic can make programs respond differently to different user inputs.
The Treasure Island game showed me how even simple conditions can create engaging storylines.

📅 Day 3 Summary

Topics Learned: Control Flow, Comparison & Logical Operators
Projects Completed: Pizza Order Calculator 🍕 and Treasure Island 🏝️
Difficulty Level: ⭐⭐☆☆☆ (Medium)
Main Skill Gained: Decision-making in programs
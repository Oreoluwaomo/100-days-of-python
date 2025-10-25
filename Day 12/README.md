# Day 12 - Number Guessing Game

## Overview
On Day 12, I built a **Number Guessing Game** using Python.  
This project focused on using **conditionals**, **loops**, and **variable scope** to create an interactive program where the user guesses a randomly generated number.  
It also introduced the concept of **global vs local scope**, helping me understand how variable accessibility works within functions.

---

## Concepts Learned
- **Local and Global Scope** in Python  
- Using the **`random`** module to generate random numbers  
- **While loops** and conditionals for game flow control  
- Tracking user lives and limiting attempts  
- Breaking large problems into smaller logical pieces  
- Writing clear and structured game logic

---

## Project Description
The game picks a random number between 1 and 100.  
The user must guess the number within a limited number of attempts based on the selected difficulty level (“easy” or “hard”).

Example interaction:
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts remaining to guess the number.
Make a guess: 45
Too high.
Guess again.
Make a guess: 32
Too low.
Guess again.
Make a guess: 37
You got it! The answer was 37.


If the user runs out of attempts before guessing correctly, the game ends with a message showing the correct number.

---

## Code Files
- `main.py`
- `art.py` (for the logo)

---

## Reflection
This project helped me understand how **scope** affects variable accessibility and how to manage data between functions.  
I learned to design a clear **game flow**, keep track of attempts, and provide instant feedback to the user.  
It was a great step toward mastering function structure and control logic.

---

## Summary of What I Learned
- The difference between **local and global scope**  
- How to use the **`random`** module for random number generation  
- How to control **game flow** using loops and conditionals  
- How to implement **difficulty levels** with dynamic attempts  
- How to give user feedback and manage program termination gracefully

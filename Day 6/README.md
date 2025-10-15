# Day 6 - Functions, Code Blocks, and While Loops

## Overview
On Day 6, I learned about defining and using **functions** in Python, understanding **code blocks**, and working with **while loops**.  
The main focus was learning how to write reusable code and control program flow effectively.  
I practiced these concepts using the **Reeborg’s World** environment to help a robot navigate hurdles.
You can explore Reeborg’s World here: [https://reeborg.ca/reeborg.html](https://reeborg.ca/reeborg.html)

---

## Concepts Learned
- Defining and calling functions using `def`
- Writing reusable and modular code
- Using **parameters** and **arguments** in functions
- Understanding **indentation** and **scope**
- Implementing **while loops** for repetitive actions
- Combining **loops and conditionals** to control logic
- Thinking algorithmically to solve step-by-step problems

---

## Project Description
The project involved solving challenges in **Reeborg’s World**, where the goal was to make the robot reach its destination by jumping over hurdles.  

I wrote functions such as:
```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
Then used them in loops like:
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
Code Files

main.py

Reflection

Day 6 helped me understand how functions make code more organized and reusable.
I learned how to break down complex tasks into smaller, logical steps and how loops can automate repeated patterns.
Practicing with Reeborg’s World made the logic behind conditionals and loops much clearer.

Summary of What I Learned

How to define and call custom functions in Python

The difference between functions with and without parameters

How to use while loops for continuous execution until a condition is met

The importance of code readability and indentation

How to combine loops, functions, and conditionals to solve logical problems

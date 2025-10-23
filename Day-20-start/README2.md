# Day 21 - Snake Game (Part 2)

## Overview
On Day 21, I continued building the **Snake Game** project using **Object-Oriented Programming (OOP)** in Python.  
This stage focused on improving the game logic adding collision detection, scoring, and refining gameplay behavior.  
By the end of this stage, the Snake Game was fully functional and interactive.

---

## Concepts Learned
- **Class Inheritance**: Understanding how one class can inherit attributes and methods from another to reduce repetition and improve organization.  
- **Collision Detection**: Detecting when the snake collides with food, walls, or its own tail.  
- **Scoreboard Management**: Creating a scoreboard class to display and update the player's score dynamically.  
- **List & Tuple Slicing**: Using slicing techniques to handle snake segments and prevent self-collision.  
- **Modular Design**: Dividing code into multiple files (`main.py`, `snake.py`, `food.py`, `scoreboard.py`) for better readability and maintenance.

---

## Features Implemented
1. **Collision with Food**
   - The snake detects when it touches the food.
   - When this happens, the food moves to a new random position and the snake grows in length.
   - The score increases each time food is eaten.

2. **Scoreboard**
   - A `Scoreboard` class displays and updates the score in real time.
   - The game resets the score and snake position when a collision occurs.

3. **Collision with Walls**
   - The game ends when the snake’s head moves beyond the screen boundary.

4. **Collision with Tail**
   - The program detects when the snake runs into its own body.
   - The game resets automatically, maintaining a seamless restart experience.

---

## Code Files
- `main.py` — runs the game loop and handles collision logic  
- `snake.py` — defines the Snake class and movement logic  
- `food.py` — defines the Food class  
- `scoreboard.py` — defines the Scoreboard class  

---

## Reflection
This stage reinforced my understanding of **object-oriented design** and how multiple classes interact in a game.  
I learned how to manage complex interactions (like collisions) while keeping the code clean and organized.  
The debugging process also helped me better understand **turtle graphics coordinates**, **list slicing**, and **real-time updates**.

---

## Summary of What I Learned
- How to use **inheritance** to build on existing classes efficiently.  
- How to implement **collision detection** using coordinates and distance.  
- How to update and display a **dynamic scoreboard** using the Turtle module.  
- How to use **list slicing** to manage and check parts of data efficiently.  
- The importance of separating code into logical modules for readability and maintenance.

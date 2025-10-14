# Day 20 - Snake Game: Setup, Animation, and OOP Implementation

## Overview
On Day 20, I began developing the classic Snake Game using Python’s `turtle` module.  
The project started with a simple procedural setup and gradually transitioned into an Object-Oriented Programming (OOP) structure.  
By the end of this stage, I had a functional snake that moves smoothly and responds to keyboard input.

---

## Concepts Learned
- Working with the `turtle` module for game graphics
- Setting up a game window using `turtle.Screen()`
- Creating and positioning multiple turtle objects
- Using loops for animation
- Implementing Object-Oriented Programming (OOP) principles:
  - Classes and objects
  - Instance methods and attributes
- Handling keyboard events with `onkey()` and `listen()`
- Using keypresses to control movement

---

## Project Description

### 1. Setting Up the Screen
- Created a game window using `Screen()`
- Set background color, size, and title
- Used `screen.update()` to manage manual screen refreshes

### 2. Creating the Snake Body
- Generated three square-shaped segments using the `Turtle` class
- Positioned them in a straight horizontal line
- Stored all segments in a list for easy management

### 3. Animating the Snake
- Used a loop to move the snake continuously across the screen
- Updated segment positions so each segment follows the one before it
- Controlled movement speed using `time.sleep()`

### 4. Moving to OOP and Adding Key Controls
- Created a `Snake` class to encapsulate behavior and structure
- Defined methods for:
  - Creating the snake body
  - Moving the snake
  - Changing direction (`up()`, `down()`, `left()`, `right()`)
- Added key bindings with `screen.listen()` and `screen.onkey()` for movement control

---

## Code Files
- `main.py` — Initializes the game screen and controls
- `snake.py` — Contains the `Snake` class and movement logic

---

## Reflection
Transitioning from procedural code to an OOP structure made the project more organized and scalable.  
Implementing keyboard controls brought the game to life, allowing interaction through directional keys.  
This stage provided valuable experience in structuring code for larger projects and handling user input effectively.

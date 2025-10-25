# Day 22 - Pong Game Project

## Overview
On Day 22, I built a **Pong Game** using Python and the `turtle` module.  
This project was my first experience creating a **classic arcade-style game**, combining graphics, movement, collision detection, and scorekeeping.  
It introduced me to more advanced **object-oriented programming** concepts and game logic.

---

## Concepts Learned
- **Object-Oriented Programming (OOP)** with classes for Ball, Paddle, and Scoreboard  
- Moving objects on screen with the `turtle` module  
- Handling **keyboard input** to control paddles  
- Detecting **collisions** with walls and paddles  
- Implementing a **scoreboard** and updating scores dynamically  
- Controlling **game loop timing** with `time.sleep()` for smooth animation  
- Using **incremental speed changes** to make gameplay more challenging  

---

## Project Description
The Pong Game simulates a two-player game:  

- Each player controls a paddle (left or right) using the keyboard.  
- A ball moves across the screen and bounces off walls and paddles.  
- If a player misses the ball, the other player scores a point.  
- The game continues indefinitely or until a player reaches a set score.  

### Example Controls
- Right paddle: `Up` and `Down` arrow keys  
- Left paddle: `w` (up) and `s` (down)  

---

## Code Files
- `main.py` — runs the game loop and manages collisions and scoring  
- `ball.py` — defines the Ball class and movement logic  
- `paddle.py` — defines the Paddle class and movement controls  
- `scoreboard.py` — defines the Scoreboard class and score updating  

---

## Reflection
This project helped me understand **game mechanics** and how multiple objects interact in real time.  
I strengthened my understanding of OOP by creating reusable classes and learned how to **structure a game loop** efficiently.  
Debugging collisions and paddle movement taught me to carefully consider coordinates and object positions in a graphical environment.

---

## Summary of What I Learned
- How to build a simple **arcade game** using Python  
- How to use **classes and OOP** to manage game objects  
- How to **control user input** for interactive gameplay  
- How to implement **collision detection** for dynamic objects  
- How to track and display scores dynamically with a scoreboard  
- How to structure a **real-time game loop** for smooth animation

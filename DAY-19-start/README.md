# 🐢 Day 19 – Instances, State, and Higher Order Functions

## 📘 Overview
Day 19 of the **100 Days of Python** challenge was all about learning how to make Python programs *interactive* using **event listeners** and **function arguments**.  
I learned how to control objects like the **Turtle** with keyboard inputs and how functions can be passed as arguments to other functions — a key idea behind event-driven programming.

By the end of the day, I built two fun and interactive projects:
1. 🎨 **Etch-A-Sketch** – draw with your keyboard  
2. 🏁 **Turtle Race Game** – simulate a race between colorful turtles

---

## 🧠 Key Concepts Learned
- **Event Listeners**: Making the turtle respond to user actions like key presses  
- **Function Arguments**: Passing functions into other functions (`onkey(fun, key)`)  
- **State and Instances**: Managing multiple objects of the same class independently  
- **Higher Order Functions**: Functions that accept other functions as input  
- **Object Movement**: Controlling direction and rotation in a graphical window  

---

## 🎨 Project 1: Etch-A-Sketch App

### 🎯 Goal
Create an Etch-A-Sketch drawing app where I can move the turtle with the keyboard:
- `W` → Move forward  
- `S` → Move backward  
- `A` → Turn left  
- `D` → Turn right  
- `C` → Clear the screen and reset position  

### 💻 Example Code
```python
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_drawing, "c")

screen.exitonclick()

🧾 How It Works

The screen.listen() method tells the program to listen for key presses.

Each key press triggers its corresponding function.

The turtle moves in the direction of your key input, letting you draw freely on the screen.
🏁 Project 2: Turtle Race Game
🎯 Goal

Simulate a race between multiple turtles of different colors.
The user guesses which turtle will win before the race starts.
🧾 How It Works

The user inputs their bet (color) using a popup dialog.

Each turtle moves forward by a random amount every loop cycle.

The race continues until one turtle crosses the finish line.

The program prints whether your chosen turtle won or lost.

🧩 Concepts Reinforced
| Concept                | Description                                  |
| ---------------------- | -------------------------------------------- |
| `screen.listen()`      | Enables keyboard input detection             |
| `onkey(function, key)` | Assigns a function to a key press            |
| Instances              | Multiple turtles can exist independently     |
| State                  | Each turtle keeps its own position and color |
| Randomization          | Adds unpredictability and fun to the race    |

🗓️ Reflection

This day was super fun and interactive!
It was amazing to see how I could control the turtle with just my keyboard and simulate real movement on screen.
I now understand how event driven programming works — a foundation for GUI applications and games.
📅 Day 19 Summary

Topic: Instances, State, and Higher Order Functions
Projects: Etch-A-Sketch 🎨, Turtle Race 🐢
Skills Gained: Event listeners, multiple instances, keyboard control
Difficulty Level: ⭐⭐⭐☆☆
Main Takeaway: Functions can be used as inputs, and user interaction can bring programs to life.
# 🐢 Day 18 — Turtle Graphics & GUI | #100DaysOfCode  

Welcome to **Day 18** of my #100DaysOfCode challenge!  
Today’s focus was on the **Turtle Graphics module** — a fun and visual way to understand how graphics, loops, and color handling work in Python.  

---

## 🎯 Learning Goals
- Understand how **Turtle Graphics** works in Python  
- Learn how to use **loops** to automate drawing  
- Practice **modular programming** and **code reusability**  
- Explore **RGB color mode** and random color generation  
- Build creative drawings step by step using code  

---

## 🧩 What I Built
During this day, I worked on several small projects that built upon one another:  

1. ✏️ **Draw a Square**  
   - Used `for` loops and the `forward()` / `right()` methods.  
   - Learned how to make the turtle move and draw simple shapes.

2. 🟢 **Dashed Line**  
   - Practiced creating patterns with loops and conditional movement.  
   - Used `penup()` and `pendown()` to make gaps in the line.  

3. 🔺 **Drawing Different Shapes**  
   - Used loops to draw multiple polygons — triangles, squares, pentagons, hexagons, etc.  
   - Calculated turning angles using `360 / number_of_sides`.  

4. 🎨 **Random Walk**  
   - Learned about randomness and colors.  
   - Generated random RGB values using `random.randint(0, 255)`.  
   - Used `turtle.colormode(255)` to enable RGB color settings.  
   - Made the turtle wander in random directions, creating colorful paths.  

5. 🌈 **Spirograph Pattern**  
   - Combined loops and random colors to make circular spirograph designs.  
   - Practiced setting headings, color cycling, and smooth looping.

---

## 💡 Key Concepts I Learned
### 🐍 The Turtle Module
The `turtle` module allows you to create graphics by controlling a virtual “turtle” that moves on the screen.  
You can control its direction, color, and drawing behavior using simple commands.

### ⚙️ Common Turtle Methods
```python
from turtle import Turtle, Screen, colormode
import random

colormode(255)
timmy = Turtle()
timmy.shape("turtle")
timmy.speed("fastest")

Movement and Drawing:
timmy.forward(100)
timmy.right(90)
timmy.penup()
timmy.pendown()

Colors and Randomization:
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

timmy.color(random_color())

Finishing the Drawing:
screen = Screen()
screen.exitonclick()


🧠 Important Note

If you get this error:
AttributeError: 'Turtle' object has no attribute 'colormode'
✅ It means colormode() should be called from the turtle module, not the Turtle instance.
So the correct way is:from turtle import colormode
colormode(255)

🪄 Lessons & Insights

Turtle graphics are a fun introduction to event-driven GUI programming.

Using for loops makes it easy to draw complex, repeating shapes.

Working with colors and randomness helped strengthen my understanding of RGB systems.

Python can be both creative and mathematical — you’re coding and designing at once!
Day 27 – Tkinter, GUI Programming & Mile to KM Converter
#100DaysOfPython Challenge

Today I started learning GUI (Graphical User Interface) development in Python using the Tkinter library. Tkinter is Python’s standard GUI toolkit, and it allows you to build windows, buttons, input boxes, labels, and more.

This was my first introduction to designing desktop applications visually instead of just using print() and the console.

 What I Learned Today
1. History of GUI & Introduction to Tkinter

GUIs make programs easier for users by providing buttons, windows, and inputs.

Tkinter comes built-in with Python—no installation needed.

The main structure of a Tkinter app:

```python
from tkinter import *

window = Tk()
window.mainloop()
```
mainloop() keeps the window open and listens for user actions.

2. Creating Windows and Labels

I learned how to create a label and add it to the screen:
```python
from tkinter import *

window = Tk()
window.title("My First GUI App")
window.minsize(width=300, height=200)

label = Label(text="Hello World!", font=("Arial", 24, "bold"))
label.pack()

window.mainloop()
```

Key points:

Label displays text.

.pack() is a layout manager.

Fonts can be customized.

3. Setting Default Values for Optional Arguments

Optional parameters in function headers:
```python
def greet(name="User"):
    print(f"Hello {name}")
```

This helps Tkinter because many widget parameters are optional.

*4. args – Many Positional Arguments

I learned that:
```python
def add(*args):
    return sum(args)
```

Using *args lets you pass many positional values.

**5. kwargs – Many Keyword Arguments

Tkinter uses kwargs heavily:
```python
def create_button(**kwargs):
    print(kwargs)

create_button(text="Click me", width=10, color="red")
```

You can pass unlimited keyword arguments like a dictionary.

Tkinter widgets internally behave the same way:
```python
Label(text="Hello", font=("Arial", 12), padx=20)
```

6. Buttons, Entry Widgets & Updating Labels

I learned how to:

add buttons

collect user input

update labels dynamically

Example:
```python
from tkinter import *

def button_clicked():
    new_text = input_box.get()
    label.config(text=new_text)

window = Tk()

label = Label(text="Old Text")
label.pack()

input_box = Entry(width=20)
input_box.pack()

button = Button(text="Click Me", command=button_clicked)
button.pack()

window.mainloop()
```

7. Other Tkinter Widgets

Today I also learned about:

Radiobutton

Scale

Checkbutton

Spinbox

Text widget

Listbox

These make GUI apps more interactive.

8. The 3 Layout Managers

Tkinter provides:

✔️ pack()

Places widgets one after another (top/bottom/left/right).

✔️ grid()

Places widgets using row & column structure (like a table).

✔️ place()

Absolute positioning (x, y coordinates).

 Final Project: Mile → Kilometer Converter

I built a simple GUI converter that:

takes a number in miles

converts it to kilometers

displays the result instantly when the button is pressed

✔️ Conversion Formula
1 mile = 1.609 km

 Reflection

This was my first real GUI project, and I learned:

how to create interactive windows

how to collect user input

how to use functions to update the interface

and how powerful Tkinter is for desktop apps

I now understand GUI events, widget configuration, and layout structure.
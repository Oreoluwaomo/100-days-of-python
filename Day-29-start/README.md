Day 29 – Password Manager App (Tkinter UI + Password Generator)
Part of my #100DaysOfPython challenge

Day 29 introduced a major multi-concept project:
A Password Manager Application built using Tkinter, Python’s built in GUI library.
This project challenged my understanding of UI layout, user input validation, randomization, clipboard functionality, and file handling.

Full Breakdown of Everything I Learned Today
## 1. Tkinter GUI: How a Python Window Is Created

Tkinter uses a main window object (Tk()) where all widgets (labels, buttons, entries, etc.) live.
```python
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
```

✔ Concepts Practiced

Creating the main application window

Adding padding around the layout

Setting a window title

Understanding the Tkinter event loop (window.mainloop())

Why this matters

Every GUI application needs a container to hold and manage user interface components.

2. Using Canvas to Display Images

I learned how to load and center an image (logo.png) using Tkinter’s Canvas.
```python
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
```
✔ What I learned:

PNG images must be stored in the same directory

PhotoImage is required to load images

Canvas helps position images precisely

3. Understanding Tkinter Widgets (Labels, Entries, Buttons)

Widgets used today:
Label :	Text displayed on the screen

Entry :	Input fields for website/email/password

Button :	Triggers functions (Generate Password, Add)

Example:
```python
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
```
✔ Concepts practiced

Using .grid(row, column) to structure the UI

Adding spacing with Entry widths

Autofocusing an Entry using .focus()

Automatically populating fields using .insert()

4. Password Generator Logic (Random Letters, Numbers, Symbols)

This is one of the most important parts of the project.

Steps:

Create lists of letters, numbers, and symbols

Randomly choose characters

Shuffle the characters

Join them into a password

Insert into the Entry field

Copy to clipboard

✔ What I learned:

List comprehensions

Dynamic password lengths

Shuffling for unpredictability

Using pyperclip to copy automatically

5. Input Validation Using Message Boxes

Before saving data, I learned to check:

Website field cannot be empty

Password cannot be empty
```
if website == "" or password == "":
    messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
```

Then a confirmation pop-up:
```python
is_ok = messagebox.askokcancel(title=website, message=f"...")
```
✔ Why this is important

Real applications must prevent incomplete or invalid data from being stored.

6. Saving the User Data into a File

I implemented a simple saving mechanism that appends the data into data.txt.
```python
with open("data.txt", "a") as data_file:
    data_file.write(f"{website} | {email} | {password}\n")
```
✔ Concepts learned:

Writing files in append mode

Concatenating multiple fields into a structured line

Clearing fields after saving

7. Final User Interface Layout (Grid System)

The UI uses the grid() layout manager.
Below is an ASCII map of the UI:

            [Logo.png]

Website:   [_________________________] [Generate Password]
Email:     [_________________________]
Password:  [______________]           [Generate Password]
           [Add Button - Full Width]


This helped me understand how rows and columns organize GUI elements.

📁 Project Structure
Day29/
│
├── main.py
├── logo.png
└── data.txt   (created automatically after saving)

By the end of Day 29, I built a functional password manager that can:

✔ Generate secure passwords
✔ Copy passwords to clipboard
✔ Accept user website/email/password inputs
✔ Validate empty fields
✔ Save login data to a file
✔ Display a polished GUI using Tkinter

This project ties together Tkinter, randomization, file handling, and user flows, forming the foundation for tomorrow’s upgraded version using JSON + Search functionality.
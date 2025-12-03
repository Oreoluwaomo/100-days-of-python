# Day 31 – Flash Card App (French–English Learning Tool)

Day 31 of the #100DaysOfPython challenge focused on building a complete, data-driven **Flash Card App** using Tkinter and Pandas.  
This project combines GUI programming, file handling, exception handling, timers, and persistent data storage into one functional learning tool.

---

##  Project Description

The goal of this project was to build a **smart flashcard application** that helps users memorize French to English vocabulary.  
The app displays a French word on the front of a card. After 3 seconds, the card automatically flips to reveal the English translation.  
Users can click:

- **✔ Yes / I knew the word**  
- **✘ No / I didn't know the word**

If the user selects **✔**, the word is removed from the learning dataset. This progress is saved to a CSV file so the app remembers the user’s learning history between sessions.  
This turns the app into a real spaced-repetition-style study tool.

---

##  What I Learned Today

###  1. Tkinter GUI Design (Advanced)
- Building a window with custom background colors & padding  
- Using `Canvas` to layer:
  - Images (`card_front.png`, `card_back.png`)
  - Text (title + word)
  - Dynamic content updates  
- Using `PhotoImage` to load PNG assets  
- Setting up buttons with transparent backgrounds & PNG icons  
- Switching card images when the card flips  
- Proper layout management using `grid()` instead of `pack()`

###  2. Timers with Tkinter (`after()` method)
- Running delayed functions (e.g., flip after 3 seconds)  
- Canceling existing timers with `after_cancel()` to avoid overlapping flips  
- Resetting timers when generating new cards  

###  3. Working with CSV using Pandas
- Reading CSVs with `read_csv()`  
- Converting DataFrames to dictionaries using:
 ```python
  data.to_dict(orient="records")
```
• Writing progress back to CSV with to_csv()

• Ensuring persistent learning progress across app restarts

### 4. Exception Handling in Real Applications

Used try / except to detect whether the user has an existing progress file:
```python
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
```
This prevents the app from crashing and lets new users start fresh while returning users continue where they stopped.

### 5. Stateful User Interaction

The app remembers:

• current card

• words remaining to learn

• which words are known

• progress during the session

### How the Flashcard System Works (Behind the Scenes)
### 1. Load the Words

The app first tries to load previously saved progress:
```python
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
```
### 2. Convert DataFrame to a List of Dictionaries

This makes it easier to select random words:
```python
to_learn = data.to_dict(orient="records")
```

Each record looks like:

{"French": "partir", "English": "to leave"}

### 3. Display a Random French Word

The app chooses a random card and starts the flip timer:
```python
flip_timer = window.after(3000, flip_card)
```

### 4. Flip the Card After 3 Seconds

Front → Back
```python
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
```
### 5. Handle Known Words

If the user knew the word:

• Remove the card from to_learn

• Save the remaining cards to words_to_learn.csv

### Move to the next card
```python
def is_known():
    to_learn.remove(current_card)
    pd.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)
    next_card()
```

### Complete Code (Core Sections)
### ✔ Main Logic Snippet
```python
import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
```

### Load data
```python
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")
current_card = {}
flip_timer = None
```

### ✔ Generating Next Card
```python
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)

    flip_timer = window.after(3000, flip_card)
```

### ✔ Flipping to Translation
```python
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
```

### ✔ Saving Known Words
```python
def is_known():
    to_learn.remove(current_card)
    pd.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)
    next_card()
```
### Buttons & UI Assets

Two image buttons for marking words:

right.png → “I knew this”

wrong.png → “I didn’t know this”


### Card images:

card_front.png → French word (white card)

card_back.png  → English translation (green card)

### Final Thoughts

Day 31 was one of the most hands-on days so far.
This project combined:

• GUI development

• Data storage

• Timers

• Exception handling

• Real learning mechanics

• State persistence

• Randomization

It’s a practical app that I can actually use to study languages  and a big step toward building full applications with Python.
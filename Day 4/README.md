# Day 4 — Randomisation and Python Lists 🎲✂️🪨

**Today’s Focus:** Randomisation and Lists in Python (Angela Yu’s #100DaysOfCode)

---

## 💡 What I Learned

Today I explored how to make my programs more fun and unpredictable using **randomisation**, and how to store and manage collections of data using **lists**.

### 🔢 Randomisation

I learned how to use Python’s `random` module to generate random numbers and make random choices. This helps in games or situations where you need an element of chance.

```python
import random

# Generate random integer between 1 and 10
random_number = random.randint(1, 10)
print(random_number)

# Generate random floating-point number between 0 and 1
random_float = random.random()
print(random_float)
```

`randint()` gives a whole number, while `random()` gives a decimal between 0 and 1. You can combine them to scale random numbers into a specific range.

### 🧺 Lists in Python

Lists are used to store multiple pieces of data in a single variable. I learned how to create, modify, and access items in a list.

```python
fruits = ["Apple", "Banana", "Cherry"]
print(fruits[0])   # Apple
fruits.append("Mango")
print(fruits)      # ['Apple', 'Banana', 'Cherry', 'Mango']
```

I also learned how to use `random.choice()` to pick a random item from a list — super useful in games!

```python
import random
friends = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
payer = random.choice(friends)
print(payer + " is going to buy the meal today!")
```

---

## 🏦 Project 1: Banker Roulette

A fun mini-project to randomly select who pays the bill!

### 🧠 Concept

1. Get a list of names.
2. Randomly select one person to pay the bill.

### 💻 Code Example

```python
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

payer = random.choice(names)
print(payer + " is going to buy the meal today!")
```

### ✅ What I Practiced

* Using `split()` to convert user input into a list.
* Using `random.choice()` for random selection.
* String formatting and user input.

---

## 🪨📄✂️ Project 2: Rock Paper Scissors Game

A simple game against the computer!

### 🧠 Concept

You choose rock, paper, or scissors. The computer randomly chooses too — then we compare choices to decide who wins.

### 💻 Code Example

```python
import random

options = ["Rock", "Paper", "Scissors"]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

print(f"You chose: {options[user_choice]}")
print(f"Computer chose: {options[computer_choice]}")

if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")
```

### ✅ What I Practiced

* Random integer generation with `randint()`.
* Comparing player and computer choices.
* Writing multiple condition statements.
* Handling lists and indexes.

---

## 🧭 Key Takeaways

* `random` module makes your code less predictable and more fun.
* Lists let you manage groups of data efficiently.
* Combining both creates the foundation for interactive games.
* Pay attention to **index errors** — always check list lengths!

---

## 🧰 Concepts Learned

* `import random`
* `random.randint()` & `random.choice()`
* `split()` for converting strings to lists
* List indexing and appending
* `if/elif/else` conditions for decision-making

---

## 💬 Reflection

Today was really engaging — mixing logic and randomness made Python feel more creative. Building games like *Banker Roulette* and *Rock Paper Scissors* helped me understand lists and conditionals better.

I’m beginning to see how even small programs can become fun projects with a few lines of code!

---


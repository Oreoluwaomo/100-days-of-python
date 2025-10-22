# Day 7 - Hangman Game Project

## Overview
On Day 7, I built a **Hangman Game** using Python.  
This project combined everything I had learned from previous days, including conditionals, loops, functions, and working with lists and strings.  
The goal was to create a word-guessing game where the player tries to guess a hidden word one letter at a time.

---

## Concepts Learned
- Using **lists**, **strings**, and **loops** together  
- Applying **if/else** logic for conditional checks  
- Updating data within lists dynamically  
- Working with **ASCII art** for simple game visuals  
- Importing modules and splitting code into multiple files  
- Understanding the concept of **game states** and **lives**  
- Testing and debugging small logic errors

---

## Project Description
The Hangman Game randomly selects a word from a list and displays blanks for each letter.  
The player guesses one letter at a time:
- If the guess is correct, the letter appears in the word.  
- If incorrect, the player loses a life and part of the hangman image is drawn.  
The game ends when the player guesses all letters or runs out of lives.

Example interaction:
Guess a letter: a
_ a _ _ _
Guess a letter: z
You guessed z, that's not in the word. You lose a life.

The game uses multiple Python files for better structure:
- `main.py` — main game logic  
- `hangman_art.py` — contains ASCII art for the hangman  
- `hangman_words.py` — contains the list of possible words  

---

## Code Files
- `main.py`
- `hangman_art.py`
- `hangman_words.py`

---

## Reflection
This project helped me understand how to combine different programming concepts into a complete working game.  
I also learned how to structure code across multiple files for better organization.  
Debugging logical errors and managing game states strengthened my problem-solving skills.

---

## Summary of What I Learned
- How to manage and update lists dynamically  
- How to use nested conditionals and loops for game logic  
- How to import data or functions from other Python files  
- How to use ASCII art to display visual feedback in text-based games  
- How to handle user input and update the display in real time  
- The importance of planning logic before coding to avoid errors

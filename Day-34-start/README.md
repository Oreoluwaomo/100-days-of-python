# Day 34 – API Practice: Building a GUI Quiz Application

## Project Overview
Day 34 of the **100 Days of Python** challenge focused on consuming real world APIs and integrating external data into a graphical user interface. The main project was a **Quiz Application** that retrieves questions from an online trivia API and presents them interactively using **Tkinter**.

This day was important because it brought together multiple skills:
- API communication
- JSON data handling
- Object-Oriented Programming (OOP)
- GUI development
- Application logic and user feedback

---

## Learning Objectives
By the end of Day 34, the goal was to:
- Understand how APIs work and how to consume them using Python
- Practice extracting and processing JSON data
- Apply OOP principles to structure a larger project
- Build a responsive GUI that updates based on user interaction
- Combine backend logic with frontend presentation

---

## Key Concepts Covered

### 1. API Requests with `requests`
- Learned how to send HTTP GET requests using the `requests` library.
- Passed query parameters to customize API responses such as:
  - Number of questions
  - Question type (True/False)
- Handled potential errors using `raise_for_status()` to ensure reliable responses.

Example:
```python
import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
```
This code fetches quiz questions from an online trivia API and converts the response into usable Python data.

### What I Learned

- How to connect Python applications to real-world APIs.

- How to safely handle API responses and errors.

- How to combine backend logic with a frontend GUI.

- How OOP improves readability and scalability in larger projects.

- How Python can be used to build interactive applications, not just scripts.
---
 ### Project Outcome

By the end of Day 34, I successfully built a functional GUI Quiz App that:

- Fetches live questions from an API

- Displays them in a clean interface

- Tracks user progress and score

- Responds dynamically to user input

### Tools & Libraries Used

- Python

- Tkinter

- requests

- JSON

- Object Oriented Programming
---
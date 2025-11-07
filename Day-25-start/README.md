Day 25 – CSV Data, Pandas Library, and the U.S. States Game

Day 25 was all about learning how to work with CSV files (Comma-Separated Values) and exploring the Pandas library to handle, analyze, and manipulate structured data efficiently. I also completed two major mini-projects:

The Great Squirrel Census Data Analysis

The U.S. States Game (built with turtle and pandas)

This day combined data analysis, file handling, and game development, which made it both fun and insightful.
What I Learned:
- Reading CSV Data in Python

I started by learning how to manually open and read CSV files using Python’s built-in csv module.
Key takeaways:

How to open and read CSV files using open() and csv.reader.

How to split and extract individual columns from a dataset.

Understanding that each line in a CSV file can be processed as a list in Python.

Example:
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

- Using the Pandas Library

After the manual approach, I learned how to use Pandas to simplify data handling. Pandas introduces DataFrames and Series, which allow you to access and manipulate large datasets more efficiently.

Key takeaways:

Reading CSV files with pandas.read_csv()

Accessing columns and rows using attributes and indexes

Performing operations like mean, max, and filtering

Converting data between lists, dictionaries, and DataFrames

Example:
import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"].mean())  # Find average temperature
print(data[data.day == "Monday"])  # Access specific row

-The Great Squirrel Census Data Analysis 

This project involved analyzing real-world data from the 2018 Central Park Squirrel Census. The dataset included thousands of entries with different squirrel colors and behaviors.

Tasks completed:

Loaded the dataset using Pandas

Counted how many squirrels of each fur color were observed

Created a new CSV file summarizing the results
Example:
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])

squirrel_count = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray, black, cinnamon]
}

df = pandas.DataFrame(squirrel_count)
df.to_csv("squirrel_count.csv")
This project taught me how to apply data filtering and export new data summaries using Pandas.

- U.S. States Game (with Turtle and Pandas) 

Next, I began the U.S. States Game, a project combining graphical interaction (turtle) and data handling (pandas).

How it works:

The program displays a blank map of the United States.

The player types the name of a state.

If the state exists in the CSV file, its name appears at the correct location on the map.

The game continues until all 50 states are guessed or the player exits.

Key learning points:

Using Pandas to read and access data from a CSV file of state names and coordinates.

Integrating data-driven logic with graphics using the turtle module.

Storing missing states in a new CSV file to track which ones weren’t guessed.

Example snippet:

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

 Concepts Strengthened

File handling (open, read, write)

Data analysis using Pandas

Filtering and exporting structured data

Combining data science with interactive Python graphics

Writing clean, modular code using loops, lists, and conditionals

 Summary

By the end of Day 25, I had learned how to manage and analyze datasets with Pandas, create visual projects that use real data, and export results dynamically. This day bridged the gap between automation, data science, and game logic  showing how powerful Python can be when combining libraries creatively.



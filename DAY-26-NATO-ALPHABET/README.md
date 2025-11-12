Day 26 – List & Dictionary Comprehension, Pandas Iteration, and the NATO Alphabet Project

Today’s lessons focused on list and dictionary comprehensions in Python 
a more concise and elegant way to create and manipulate collections. 
I also learned how to iterate through Pandas DataFrames efficiently, 
and wrapped up the day with the NATO Alphabet Project, which applied all these concepts together.

🧠 Concepts Learned

List Comprehension

Creating lists in a single line using expressions and loops.

Applying conditions (if statements) to filter items.

Dictionary Comprehension

Building dictionaries dynamically using for-loops in one line.

Applying transformations and filters to dictionary data.

Iterating Over Pandas DataFrames

Accessing rows efficiently using .iterrows().

Working with Pandas Series and applying dictionary mappings.

🧩 Coding Exercises
🔹 Squaring Numbers
```python
Created a new list with each element squared.
numbers = [1, 2, 3, 4, 5]
squared_numbers = [n ** 2 for n in numbers]
print(squared_numbers)
# Output: [1, 4, 9, 16, 25]
```
🔹 Filtering Even Numbers

Filtered out only even numbers from a list.
```python
numbers = [10, 13, 20, 25, 30, 33]
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)
# Output: [10, 20, 30]
```
🔹 Data Overlap

Compared numbers in two files and found common values using list comprehension.
```python
with open("file1.txt") as file1:
    list1 = file1.readlines()
with open("file2.txt") as file2:
    list2 = file2.readlines()

result = [int(num) for num in list1 if num in list2]
print(result)
```
🗺️ Applying List Comprehension to the U.S. States Game

Improved the U.S. States Game from Day 25 by using list comprehension to handle missing states more efficiently.
```python
missing_states = [state for state in all_states if state not in guessed_states]
new_data = pandas.DataFrame(missing_states)
new_data.to_csv("states_to_learn.csv")
```

🧮 Dictionary Comprehension
🔹 Basic Example
```python
names = ["Alice", "Bob", "Charlie", "David"]
import random
student_scores = {name: random.randint(60, 100) for name in names}
print(student_scores)
```

🔹 Conditional Dictionary
passed_students = {name: score for (name, score) in student_scores.items() if score >= 70}
print(passed_students)

🧠 Iterating Over a Pandas DataFrame

Learned how to loop through rows in a DataFrame and access individual columns.
```python
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    print(row.student, row.score)
  ```

🔤 NATO Alphabet Project

The final project of the day was the NATO Alphabet Project,
which reads the NATO phonetic alphabet data from a CSV file and 
converts any user-inputted word into its phonetic code equivalents.

Project Code:
```python
import pandas

# Read the CSV file
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Convert the DataFrame into a dictionary
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Get input from user and generate the phonetic code words
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
```

✅ Key Concepts Practiced:

Reading data from CSV files using Pandas

Iterating through DataFrames with .iterrows()

Building dictionaries dynamically

Applying list comprehension to process user input

📘 Summary

By the end of Day 26, I mastered comprehensions (both lists and dictionaries),
learned how to iterate through DataFrames, and applied these ideas in a real-world mini-project 
the NATO Alphabet Converter. This day helped solidify how to make Python code cleaner, faster, and more expressive.

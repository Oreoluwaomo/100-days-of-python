# Day 30 – Exception Handling + JSON in the Password Manager  

Day 30 focused on **making programs safer, more reliable, and more professional** by handling errors properly. I learned how to catch exceptions, raise my own custom errors, handle specific Python exceptions like `IndexError` and `KeyError`, and finally apply all of this to upgrade my Password Manager from Day 29 using **JSON storage** and **search functionality**.

---

## 🎯 What I Learned Today
### 1. The `try / except / else / finally` pattern  
I practiced how Python handles errors:
- **try**: code that might cause an error  
- **except**: runs only if an error happens  
- **else**: runs only if NO error happens  
- **finally**: always runs, no matter what  

This makes programs robust and prevents crashes.

### 2. Raising my own exceptions  
I used `raise` to manually trigger errors when input is invalid.  
Example concept:
```python
height = int(input("Height: "))
if height > 300:
    raise ValueError("Height too large to be realistic.")
```
### 3.Working with specific errors

I practiced:

● IndexError Handling (accessing list items safely)

● KeyError Handling (looking up dictionary keys safely)

These linked directly into the NATO Alphabet and Password Manager tasks later.

● Coding Exercises Completed

✔ Coding Exercise  – IndexError Handling

Goal: Prevent the program from crashing when the user enters an index that doesn’t exist.
Concept example:
```python
try:
    print(list_values[user_index])
except IndexError:
    print("Index is out of range.")
```

✔ Coding Exercise  – KeyError Handling

Goal: Safely handle dictionary lookups.
Concept example:
```python
try:
    print(dictionary[user_key])
except KeyError:
    print("Key not found.")
```

✔ Exception Handling in the NATO Phonetic Alphabet Project

I improved the user input validation so the program:

● Rejects numbers

● Rejects characters not in A–Z

● Keeps asking for valid input instead of crashing

Example:
```python
try:
    result = [alphabet[char] for char in user_input]
except KeyError:
    print("Only letters A–Z allowed. Try again.")
```
 Major Project: Password Manager (Improved)

This was the biggest part of Day 30.
I transformed the Day 29 password manager using everything learned today.

 New Features Added:

● Save passwords as JSON instead of plain text

● Search for a website and automatically retrieve credentials

● Handle missing JSON file

● Handle corrupted JSON file

● Confirm before overwriting existing entries

● Use exceptions to prevent crashes

JSON Structure Used:

Each website becomes a dictionary key:
```python
{
    "youtube.com": {
        "email": "example@gmail.com",
        "password": "xAjs3#Ks!"
    }
}
```
Core Code Implemented Today:

✔ Saving to JSON (with exception handling)
```python
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        data = {}
    except json.JSONDecodeError:
        messagebox.showerror("Error", "data.json is corrupted.")
        return

    data.update(new_data)

    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

    website_entry.delete(0, END)
    password_entry.delete(0, END)
```
✔ Searching the JSON file:
```python
def find_password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo("Error", "No data file found.")
        return
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Data file corrupted.")
        return

    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(website, f"Email: {email}\nPassword: {password}")
    else:
        messagebox.showinfo("Not found", f"No details for {website} found.")
```

NOTE:

try/except: Prevented crashes when JSON file is missing or corrupted

KeyError handling :	Used when searching for websites in the JSON data

Raising exceptions: Used to validate user inputs

JSON reading/writing:Made the password manager scalable and structured

Finally block:Ensured certain UI actions always run (e.g., clearing fields)

 What I Understand Now:

Programs shouldn’t crash — they should guide the user.

JSON is much better than text files: structured, readable, and easy to update.

Exception handling is one of the most important skills for building reliable applications.

The password manager is now a fully functional real-world mini-app.

Summary:

Day 30 was all about professional-level exception handling and turning the basic password manager into a polished tool using:

JSON storage

Search feature

Robust error handling

Cleaner UI behavior

It was one of the biggest upgrades so far, and now I can build apps that:

✔ don’t crash,

✔ handle real user mistakes,

✔ save and read structured data,

✔ and behave like real applications.
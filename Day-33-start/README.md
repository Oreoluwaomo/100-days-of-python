## Day 32 : Email Automation with Python (SMTP + Datetime + Automation Projects)

Today I built two real-world automation tools using Python:

#### A Monday Motivational Email Sender

#### An Automated Birthday Wishing System

I also learned how to securely send emails, work with dates, and structure reusable automation code.

##  Lessons Covered Today
### 1️⃣ Understanding SMTP (Simple Mail Transfer Protocol)

SMTP is the protocol responsible for sending emails between servers.

Key Things I Learned:

• How email travels from a device → SMTP server → destination inbox.

• Gmail’s SMTP server details:
````
Server: smtp.gmail.com  
Port: 587 (supports TLS encryption)
````
• Why we MUST use App Passwords instead of normal passwords (security & blocking by Google).

• How to create a secure connection using:

   •starttls() → upgrades connection to encrypted

   •login() → authenticates the sender

   •sendmail() → delivers email
   
### Core Pattern:
```python
import smtplib

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()        # Secure connection
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=receiver_email,
        msg="Subject:Test\n\nHello world!"
    )
```
This pattern becomes the foundation of all automation projects today.

### 2️⃣ Working with the datetime Module

The datetime module helps Python interact with real-world time.

Skills I Practiced:

•Getting the current date & time:
```python
now = datetime.datetime.now()
```

• Extracting specific components:

  .weekday() → Monday = 0

  .month, .day, .year

• Using dates to trigger conditional automation:

   • "If today is Monday, do X"

   • "If today matches a birthday, do Y"

This becomes especially useful in automation scripts.

##  Exercises & Coding Challenges
## Coding Exercise : IndexError Handling

•Focused on preventing the program from crashing when:

•Accessing list items out of range

•Handling user errors gracefully

##  Coding Exercise : KeyError Handling

•Learned to handle situations where:

•A dictionary key does not exist

•The program should inform the user instead of crashing

This was important for the NATO Alphabet Project (handling inputs safely).

# MAIN PROJECTS COMPLETED
##  Project 1: Monday Motivational Quote Email Sender
Goal:

Send a random motivational quote every Monday automatically.

Steps I Completed:
1. Read All Quotes from a Text File
```python
with open("quotes.txt") as file:
    all_quotes = file.readlines()
```
2. Pick a Random Quote
```python
quote = random.choice(all_quotes)
```
3. Check If Today Is Monday
```python
if datetime.datetime.now().weekday() == 0:
   # send email
 ```

4. Send the Email Using SMTP

•Email subject: “Monday Motivation”

•Body: randomly chosen quote

•Triggered only on Mondays

### Skills Reinforced

•File handling

•Randomization

•Date based automation

•Secure emailing

•Maintaining consistent weekly tasks

##  Project 2: Automated Birthday Wisher

This was the more advanced and realistic automation system.

Goal:

Check every day if it’s someone’s birthday → automatically send them a personalized birthday message.

Components Used
✔ birthdays.csv

Contains:

•Name

•Email

•Birth year

•Birth month

•Birth day

✔ Template letters:

letter_1.txt, letter_2.txt, letter_3.txt
Each has the placeholder [NAME] which must be replaced.

Steps I Completed
### 1. Read the Birthday CSV
```python
import pandas as pd
data = pd.read_csv("birthdays.csv")
```

### 2. Convert CSV to a Dictionary

So I can search easily by month & day.
```python
birthday_dict = {
    (row.month, row.day): row
    for (index, row) in data.iterrows()
}
```

### 3. Match Today’s Date
```python
today = (now.month, now.day)
```

If today exists in birthday_dict, then someone has a birthday.

### 4. Choose a Letter Template
```python
file = f"letter_templates/letter_{random.randint(1,3)}.txt"
with open(file) as letter_file:
    contents = letter_file.read()
    personalized_letter = contents.replace("[NAME]", birthday_person.name)
```
### 5. Send the Email Automatically

Using the same SMTP pattern but with custom message.

Why This Project Is Powerful

I learned how to:

•Automate real-life reminders

•Use templates dynamically

•Work with CSV data

•Use conditional logic based on date

•Write reusable automation scripts

This is the kind of automation companies use in:

CRM systems

Customer support

Marketing birthday messages

Scheduled outreach tools

##  Key Concepts Reinforced Today
✔ Email delivery fundamentals

✔ Secure authentication via App Passwords

✔ Using context managers (with) to manage connections

✔ Working with file systems

✔ Using randomness for dynamic messages

✔ Handling CSVs with pandas

✔ Time-based automation

✔ Template-based message personalization
## Tools & Libraries Used

smtplib

datetime

random

pandas

Python file handling

##  End of Day Summary

Today’s session strengthened my understanding of automation, scheduled tasks, and real world Python applications.
I built two complete systems that can run weekly or daily and perform tasks without human involvement.

I can now:

Send automatic emails

Personalize email content

Trigger code based on specific days

Work with CSV and templates efficiently


Build real-world automation systems

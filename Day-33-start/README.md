## Day 33 – Working with APIs, JSON Data & the ISS Overhead Notifier

This project is part of the 100 Days of Python course by Angela Yu.
Day 33 introduced real world API usage, teaching how Python programs can interact with live data from the internet and make decisions based on that data.

Overview

On Day 33, I learned how to:

• Communicate with external APIs using HTTP requests

• Understand API endpoints, parameters, and responses

• Work with JSON formatted data

• Handle errors when making requests

• Combine multiple APIs in a single automation project

• Trigger actions (email notifications) based on real-time conditions

The main project for this day was the ISS Overhead Notifier, a script that checks if the International Space Station is close to my location at night and sends an email alert when it is.

## Concepts Learned in Detail
### 1. What an API Is

An API (Application Programming Interface) allows different software systems to communicate. Instead of scraping websites or manually checking information, APIs provide structured data in formats like JSON.

Key ideas:

• APIs respond to requests

• Requests are sent to endpoints

• Responses include data and status codes
### 2. API Endpoints & HTTP Requests

An endpoint is a specific URL that provides data.

Example:
```python
response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
```

What happens here:

• A GET request is sent to the API

• The API responds with ISS position data

• raise_for_status() ensures the program stops if the request fails
### 3. Understanding API Responses & Status Codes

• 200 → Success

• 400–499 → Client errors

• 500+ → Server errors

Using raise_for_status() prevents silent failures and improves reliability.

### 4. Working with JSON Data

API responses are usually in JSON format, which converts naturally into Python dictionaries.

Example:
```python
data = response.json()
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
```
Skills practiced:

• Navigating nested dictionaries

• Converting string values to floats

• Extracting only the data needed

## ISS Overhead Notifier Project
### Project Goal

Create a Python script that:

1.Retrieves the current position of the ISS

2.Checks if the ISS is close to the user’s location

3.Determines if it is currently nighttime

4.Sends an email alert if all conditions are met

Project Breakdown
### Step 1: Get ISS Position

Used the Open Notify ISS API to retrieve real-time coordinates.

Data retrieved:

• Latitude

• Longitude

### Step 2: Check If ISS Is Overhead

Compared the ISS position with the user’s latitude and longitude.

Logic:

• ISS is considered “overhead” if it is within ±5 degrees of the user’s location
```python
def is_iss_overhead():
    return (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and
        MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    )
```
### Step 3: Check If It Is Nighttime

Used the Sunrise–Sunset API to determine:

• Sunrise time

• Sunset time

Compared those times to the current hour using the datetime module.
```python
def is_night():
    return current_hour >= sunset or current_hour <= sunrise
```
### Step 4: Send Email Alert

When both conditions are met:

• ISS is overhead

• It is nighttime

An email notification is sent using smtplib.

This ensures alerts are meaningful (ISS visibility is best at night).

### Step 5: Continuous Monitoring

The script runs in a loop using:
```python
time.sleep(60)
```

This allows the program to:

• Check conditions every minute

• Act automatically without user interaction

### Libraries & Tools Used

.```requests``` – for making API calls

.```datetime``` – for working with time and dates

.```smtplib``` – for sending emails

.```time``` – for scheduling repeated checks

Public APIs:

  .Open Notify (ISS position)

  .Sunrise–Sunset API

### Error Handling & Best Practices

• Used raise_for_status() to catch failed API calls

• Converted API data into usable Python types

• Avoided hardcoding values where possible

• structured logic into functions for clarity

### Key Takeaways

• APIs are the bridge between Python and real-world data

• JSON is the most common data format used by APIs

• Multiple APIs can be combined to solve one problem

• Automation becomes powerful when driven by live data

• Small scripts can behave like background services

### Skills Gained by the End of Day 33

• Confident use of APIs

• JSON parsing and data extraction

• Conditional automation

• Writing long-running Python scripts

• Combining networking, time logic, and email automation

### Final Thoughts

Day 33 marked a shift from basic scripting to data-driven automation.

This project showed how Python can monitor real world events and respond automatically  a key concept behind modern software systems.

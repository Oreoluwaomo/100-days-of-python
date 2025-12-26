# Day 35 – API Authentication, Weather Forecasting & Automated Alerts

## Overview
Day 35 of the **100 Days of Python** challenge focused on working with **authenticated APIs**, handling **sensitive credentials securely**, and building a **fully automated notification system**. The core project was a weather alert application that checks upcoming weather conditions and sends alerts via messaging services when rain is expected.

This day introduced concepts that are essential in real world software development, including API security, environment variables, third party service integration, and cloud automation.

---

## Learning Objectives
By completing Day 35, I aimed to:
- Understand why most APIs require authentication
- Learn how API keys are generated and used
- Secure sensitive credentials using environment variables
- Fetch and analyze real time weather data
- Build logic that reacts to real-world conditions
- Send automated notifications using external services
- Deploy and automate Python scripts in the cloud

---

## Core Topics Covered

### 1. API Authentication Fundamentals
- Learned what API authentication is and why it exists.
- Understood how APIs use keys to:
  - Identify users
  - Track usage
  - Prevent abuse
- Learned the risks of exposing API keys in public repositories.

This reinforced why security is not optional when working with external services.

---

### 2. Using OpenWeatherMap with API Keys
- Registered for the OpenWeatherMap service and generated a unique API key.
- Passed the API key as a parameter in HTTP requests.
- Requested forecast data based on geographic coordinates.

Example:
```python
import os
import requests

API_KEY = os.environ.get("OWM_API_KEY")

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast",
    params=parameters
)
response.raise_for_status()
weather_data = response.json()
```
This ensured secure authentication while retrieving live weather data.

### 3. Forecast Data Analysis

- Explored the structure of the JSON response returned by the API.

- Extracted weather condition codes for each forecast period.

- Implemented logic to detect rain or storm conditions.

- Checked weather conditions for the next 12 hours.

- This step turned raw data into meaningful information
### 4. Conditional Logic for Alerts

- Used boolean flags to track whether rain was detected.

- Ensured alerts were only sent when necessary.

- Prevented unnecessary notifications when conditions were clear.

- This improved both efficiency and user experience.

### 5. Sending Alerts with Twilio (SMS)

- Learned how to integrate the Twilio API into a Python project.

- Used Twilio credentials to authenticate requests.

- Sent SMS alerts when rain was detected.

Example:
```python
from twilio.rest import Client

client = Client(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
    body="Rain expected today. Remember to carry an umbrella.",
    from_=TWILIO_NUMBER,
    to=MY_PHONE_NUMBER
)
```
This demonstrated how Python can interact with communication platforms.
### 6. WhatsApp Messaging Alternative

- Explored sending alerts via WhatsApp using Twilio.

- Understood use cases where WhatsApp is more reliable than SMS.

- Learned how message formatting differs for WhatsApp delivery.

- This added flexibility to the notification system.

### 7. Automation with PythonAnywhere

- Uploaded the project to PythonAnywhere.

- Scheduled the script to run automatically at set intervals.

- Learned how cloud execution removes the need for manual script execution.

This step transformed the project from a script into a service.

### 8. Environment Variables & Credential Security

- Learned why sensitive data should never be hard-coded.

- Stored credentials using environment variables:

- API keys

- Authentication tokens

- Account IDs

Made the project safe for version control and public repositories.

Example:
```python
import os

OWM_API_KEY = os.environ.get("OWM_API_KEY")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

```
This mirrors best practices used in production systems.

# Final Project Outcome

### By the end of Day 35, I built an automated weather alert system that:

- Retrieves live weather forecast data

- Analyzes upcoming conditions

- Detects rain within the next 12 hours

- Sends alerts via SMS or WhatsApp

- Runs automatically on a cloud platform

- This project combined data analysis, automation, and real-world communication.

### Key Skills Gained

- API authentication and secure access

- Handling sensitive credentials safely

- Parsing and analyzing JSON data

- Integrating multiple third-party APIs

- Automating Python scripts in the cloud

- Writing production aware Python code

### Tools & Technologies Used

- Python

- requests

- OpenWeatherMap API

- Twilio API

- PythonAnywhere

- Environment Variables

- JSON
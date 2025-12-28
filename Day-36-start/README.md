# Day 36 – Stock Trading News Alert Project

## Overview
Day 36 of the **100 Days of Python** challenge focused on building a **real world automation project** that combines multiple APIs to monitor stock price movements and send news alerts when significant changes occur.

The main project for the day was a **Stock Trading News Alert System** that:
- Checks daily stock price changes
- Determines if the price movement is significant
- Fetches relevant news articles
- Sends alerts via SMS when conditions are met

This project reinforced API integration, conditional logic, and automation workflows.

---

## Day Goals
By the end of Day 36, the objectives were to:
- Work with multiple APIs in a single project
- Analyze stock market data programmatically
- Apply conditional logic to detect significant price changes
- Fetch related news articles dynamically
- Send automated alerts via SMS
- Combine data sources into a single automated pipeline

---

## Core Concepts Covered

### 1. Understanding the Problem: “Choose Your Destiny”
- Defined a threshold for what counts as a “significant” stock price change.
- Used percentage calculations to determine whether alerts should be triggered.
- Designed logic that only runs additional API calls when needed.

This ensured efficiency and avoided unnecessary API requests.

---

### 2. Checking Stock Price Movements
- Used a stock market API to retrieve daily stock prices.
- Compared the closing prices of the most recent trading days.
- Calculated the percentage difference between days.

Example:
```python
difference = yesterday_close - day_before_close
percentage_change = (difference / yesterday_close) * 100
```
- Used conditional statements to check if the percentage change exceeded a set threshold.
### 3. Fetching Relevant News Articles

- Integrated a news API to retrieve recent articles related to the selected company.

- Parsed JSON responses to extract:

- Article headlines

- Brief summaries

- Limited the number of articles to avoid information overload.

Example:
```python
articles = news_data["articles"][:3]
```
### 4. Combining Stock Data with News Context

- Linked stock price movements with real-world news events.

- Ensured that alerts included meaningful context instead of raw numbers.

- Improved alert usefulness by attaching headlines and summaries.

### 5. Sending Alerts via SMS

- Used the Twilio API to send SMS notifications.

- Formatted messages to include:

- Stock symbol

- Price movement direction

- Percentage change

- Related news headlines

Example:
```python
client.messages.create(
    body=message,
    from_=TWILIO_NUMBER,
    to=MY_PHONE_NUMBER
)
```
### 6. Automation Logic

- Ensured the script:

- Checks stock prices first

- Fetches news only when price movement is significant

- Sends messages only when conditions are met

- This approach reduced unnecessary API usage and improved efficiency.

### Final Project Outcome

 By the end of Day 36, I successfully built a Stock News Alert System that:

- Monitors daily stock price changes

- Calculates percentage movement automatically

- Fetches relevant news when prices fluctuate significantly

- Sends timely SMS alerts with actionable information

- This project demonstrated how Python can automate financial monitoring and information delivery.

### Key Skills Gained

- Working with multiple APIs in a single project

- Parsing and combining JSON data from different sources

- Implementing real-world conditional logic

- Automating alert systems

- Writing cleaner, modular automation scripts

### Tools & Technologies Used

- Python

- requests

- Stock Market API

- News API

- Twilio API

- JSON

- Environment Variables
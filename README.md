# Day 2 – Selenium Basics

This branch contains my first hands-on practice with Selenium WebDriver using Python.

## What I Practiced

### 1️⃣ Opening a Browser
- Launching Chrome using Selenium
- Navigating to a URL
- Keeping the browser open using input()
- Closing the browser with driver.quit()

File:
- selenium_open_server.py

---

### 2️⃣ Finding Elements & Interacting
- Locating elements using By.NAME
- Using send_keys()
- Submitting a form
- Understanding how Selenium interacts with the DOM

File:
- selenium_finding_elements.py

---

### 3️⃣ Real Login Test (Automation Scenario)
- Navigating to a real test site:
  https://the-internet.herokuapp.com/login
- Filling username and password
- Clicking login
- Using WebDriverWait (Explicit Wait)
- Validating success message using assert
- Handling cleanup with try/finally

File:
- Selenium_first_practice.py

---

## Concepts Learned

- What is Selenium WebDriver
- What is a browser driver
- Locating elements (By.ID, By.NAME, CSS_SELECTOR)
- DOM understanding
- Explicit waits (WebDriverWait + Expected Conditions)
- Basic test validation using assert

---

## How to Run

Make sure Selenium is installed:

```bash
pip install selenium

python selenium_open_server.py
python selenium_finding_elements.py
python Selenium_first_practice.py

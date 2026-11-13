"""
api_caller.py
=============

A beginner-friendly demo of talking to a public REST API with the
`requests` library and reading the JSON data that comes back.

No API key is required, so you can run it immediately:

    python api_caller.py

What is an HTTP request?
    It is a message your program sends to a web server. The server
    replies with a response that has:
      - a status code (a number such as 200 for success), and
      - a body (often JSON text, which Python can turn into a dict/list).

The script has two parts:
    Part 1 - current weather (the JSON is a dictionary)
    Part 2 - a list of todo items (the JSON is a list)
"""

import sys

# requests is a third-party library that makes HTTP calls readable.
# Install it with:  pip install requests   or   uv pip install requests
import requests

# Windows terminals sometimes default to an older text encoding. Asking
# Python to write UTF-8 keeps symbols such as the degree sign (C) readable.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass  # Older Python versions do not have reconfigure; output still works.


def print_header(title):
    """Print a clear separator so each part is easy to find."""
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ================================================================
# Part 1: Current weather in Berlin (JSON object -> dictionary)
# ================================================================
print_header("=== Part 1: Current Weather in Berlin ===")

# An API endpoint is a URL that returns data instead of a web page.
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

# Query parameters tell the API exactly what we want. requests turns
# this dictionary into the "?latitude=...&longitude=..." part of the URL.
weather_params = {
    "latitude": 52.52,
    "longitude": 13.41,
    "current": "temperature_2m,wind_speed_10m",
    "timezone": "auto",
}

# --- Step 1: Send the HTTP GET request --------------------------
print("Step 1: Send a GET request")
print(f"  URL:        {WEATHER_URL}")
print(f"  Parameters: {weather_params}")

try:
    # requests.get() performs the request. The timeout makes the program
    # give up after 10 seconds instead of waiting forever.
    response = requests.get(WEATHER_URL, params=weather_params, timeout=10)
except requests.exceptions.RequestException as error:
    # This catches connection failures, timeouts, DNS errors, and more.
    print("  Could not reach the API. Check your internet connection.")
    print(f"  Details: {error}")
    raise SystemExit(1)

# --- Step 2: Check the status code ------------------------------
print()
print("Step 2: Check the HTTP status code")

# Status codes are grouped by meaning:
#   2xx = success (200 means OK)
#   4xx = the request was wrong (404 means not found)
#   5xx = the server itself had a problem
print(f"  Status code: {response.status_code}")

if response.status_code != 200:
    print("  The API did not return success, so we stop here.")
    raise SystemExit(1)

print("  200 means success, so there is data to read.")

# --- Step 3: Turn the JSON text into Python data ----------------
print()
print("Step 3: Convert the JSON text into Python data")

try:
    # .json() reads the response body and converts JSON text into
    # normal Python objects: {...} becomes a dict, [...] becomes a list.
    weather = response.json()
except requests.exceptions.JSONDecodeError:
    print("  The response was not valid JSON, so we stop here.")
    raise SystemExit(1)

print(f"  Type of weather: {type(weather).__name__}")
print(f"  Top-level keys:  {list(weather.keys())}")

# --- Step 4: Extract and print the fields we want ---------------
print()
print("Step 4: Extract the fields we want")

# weather["current"] is a nested dictionary inside the main one.
current = weather["current"]

# The units live in a separate dictionary, so we read them from there.
units = weather["current_units"]

temperature = current["temperature_2m"]
wind_speed = current["wind_speed_10m"]
observed_at = current["time"]

print(f"  Temperature: {temperature} {units['temperature_2m']}")
print(f"  Wind speed:  {wind_speed} {units['wind_speed_10m']}")
print(f"  Observed at: {observed_at}")


# ================================================================
# Part 2: A list of todo items (JSON array -> list of dictionaries)
# ================================================================
print_header("=== Part 2: A List of Todo Items ===")

# JSONPlaceholder is a free fake API used for practice.
TODO_URL = "https://jsonplaceholder.typicode.com/todos"

# _limit asks the API to return only the first few items.
todo_params = {"_limit": 5}

print("Send a GET request, then let raise_for_status() check the code.")
print(f"  URL:        {TODO_URL}")
print(f"  Parameters: {todo_params}")

try:
    todo_response = requests.get(TODO_URL, params=todo_params, timeout=10)

    # raise_for_status() is a shortcut: it raises an exception for any
    # 4xx or 5xx status, so we do not need an explicit if statement.
    todo_response.raise_for_status()
except requests.exceptions.RequestException as error:
    print("  Could not load the todos.")
    print(f"  Details: {error}")
    raise SystemExit(1)

print(f"  Status code: {todo_response.status_code}")

# Here the JSON is a list, so .json() returns a Python list.
todos = todo_response.json()
print(f"  Type of todos: {type(todos).__name__}")
print(f"  Number of items: {len(todos)}")
print()

# Each item in the list is a dictionary with its own fields.
for todo in todos:
    # A dictionary lookup gives the value for a key.
    if todo["completed"]:
        mark = "x"
    else:
        mark = " "

    print(f"  [{mark}] {todo['id']}: {todo['title']}")


# ================================================================
# Summary
# ================================================================
print_header("=== Summary ===")
print("Every API call in this script follows the same four steps:")
print("  1. requests.get(url, params=...) sends the request")
print("  2. check response.status_code (or use raise_for_status())")
print("  3. response.json() turns JSON text into dicts and lists")
print("  4. read the fields you need with [] and print them")

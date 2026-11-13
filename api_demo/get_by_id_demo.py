"""
get_by_id_demo.py
=================

A small follow-up to api_caller.py: how to GET one specific resource by
putting its id in the URL path.

Example endpoints (JSONPlaceholder, no API key required):
    https://jsonplaceholder.typicode.com/users/1
    https://jsonplaceholder.typicode.com/users/3
    https://jsonplaceholder.typicode.com/users/9999   <- does not exist

Run it with the default ids:
    python get_by_id_demo.py

Or look up your own id:
    python get_by_id_demo.py 5

The main lesson: the id is just part of the URL, and a missing id comes
back as status code 404 rather than raising an error by itself.
"""

import sys

import requests

# Windows terminals sometimes use an older text encoding; force UTF-8.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass

# The base URL is the part that stays the same for every user.
BASE_URL = "https://jsonplaceholder.typicode.com"


def print_header(title):
    """Print a clear separator so each part is easy to find."""
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


def fetch_user(user_id):
    """GET one user by id.

    Returns the user as a dictionary, or None when it cannot be read.
    """
    # An f-string builds the full URL: /users/ + the id.
    url = f"{BASE_URL}/users/{user_id}"
    print(f"  Request: GET {url}")

    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.RequestException as error:
        print(f"  Network problem: {error}")
        return None

    # A 404 is not an exception by default; it is just a status code.
    print(f"  Status code: {response.status_code}")

    if response.status_code == 404:
        print(f"  No user exists with id={user_id}.")
        return None

    if response.status_code != 200:
        print("  Unexpected status code, so we skip this user.")
        return None

    try:
        # Turn the JSON object into a Python dictionary.
        return response.json()
    except requests.exceptions.JSONDecodeError:
        print("  The response was not valid JSON.")
        return None


def show_user(user):
    """Print a few fields from one user dictionary."""
    # Nested data needs two sets of brackets: user -> address -> city.
    city = user["address"]["city"]
    company = user["company"]["name"]

    print(f"  Name:     {user['name']}")
    print(f"  Username: {user['username']}")
    print(f"  Email:    {user['email']}")
    print(f"  City:     {city}")
    print(f"  Company:  {company}")


# Decide which ids to look up. Use the command-line value if given.
ids_to_try = [1, 3, 9999]

if len(sys.argv) > 1:
    try:
        ids_to_try = [int(sys.argv[1])]
    except ValueError:
        print(f"'{sys.argv[1]}' is not a whole number. Using the default ids.")

print_header("=== GET by ID Demo ===")
print("The id is part of the URL path: /users/<id>")
print(f"Looking up ids: {ids_to_try}")

for user_id in ids_to_try:
    print()
    print(f"--- User id {user_id} ---")
    user = fetch_user(user_id)

    if user is None:
        # No data for this id, so move on to the next one.
        continue

    show_user(user)

print_header("=== Summary ===")
print("GET /users/1    -> 200 OK, plus JSON for that one user")
print("GET /users/9999 -> 404 Not Found")
print("requests does NOT raise for 404; check the status code yourself")
print("response.json() turns the JSON object into a Python dict")
print("Call response.raise_for_status() if you prefer 4xx/5xx to raise")

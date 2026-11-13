"""
http_methods_demo.py
====================

A beginner-friendly demo of the four HTTP methods that CHANGE data:

    POST   -> create a new resource
    PUT    -> replace a whole resource
    PATCH  -> update part of a resource
    DELETE -> remove a resource

GET (reading data) is covered in api_caller.py and get_by_id_demo.py.

The demo uses JSONPlaceholder, a free fake API. It replies like a real
server but does not really save anything, which makes it safe to practice.

Run it with:

    python http_methods_demo.py
"""

import json
import sys

import requests

# Windows terminals sometimes use an older text encoding; force UTF-8.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass

BASE_URL = "https://jsonplaceholder.typicode.com"
POSTS_URL = f"{BASE_URL}/posts"


def print_header(title):
    """Print a clear separator so each method is easy to find."""
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


def show_response(response):
    """Print the status code and pretty-print the JSON body."""
    print(f"  Status code: {response.status_code}")

    try:
        # .json() turns the response body into a Python dict or list.
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        print("  Body: (the response was not JSON)")
        return

    # json.dumps(..., indent=2) prints nested data in a readable layout.
    # Each line is indented to sit neatly under the label above.
    print("  Body returned by the server:")
    pretty = json.dumps(data, indent=2)
    for line in pretty.splitlines():
        print(f"    {line}")


print_header("=== HTTP Methods Demo: POST, PUT, PATCH, DELETE ===")
print("GET reads data. The four methods below change data:")
print("  POST   -> create a new resource")
print("  PUT    -> replace a whole resource")
print("  PATCH  -> update part of a resource")
print("  DELETE -> remove a resource")
print()
print("JSONPlaceholder is a fake API: it answers like a real server but")
print("does not actually save changes, so it is safe to experiment.")


# ================================================================
# 1. POST: create a new post
# ================================================================
print_header("=== 1. POST: create a new post ===")

# The payload is the data we want to create, written as a dictionary.
new_post = {
    "title": "My first post",
    "body": "Hello from requests!",
    "userId": 1,
}

print(f"  Sending POST {POSTS_URL}")
print(f"  Payload: {new_post}")

try:
    # json=new_post tells requests to:
    #   1. convert the dictionary into JSON text, and
    #   2. set the header Content-Type: application/json
    post_response = requests.post(POSTS_URL, json=new_post, timeout=10)
except requests.exceptions.RequestException as error:
    print(f"  Network problem: {error}")
    raise SystemExit(1)

show_response(post_response)

# 201 means "Created", the usual success code for POST.
if post_response.status_code == 201:
    created = post_response.json()
    print(f"  Success: the server assigned id={created.get('id')}.")


# ================================================================
# 2. PUT: replace a whole resource
# ================================================================
print_header("=== 2. PUT: replace post 1 completely ===")

# PUT sends the entire object. Any field you leave out is treated as
# removed, which is why people often prefer PATCH for small edits.
replacement = {
    "id": 1,
    "title": "Replaced title",
    "body": "Replaced body",
    "userId": 1,
}

print(f"  Sending PUT {POSTS_URL}/1")
print(f"  Payload: {replacement}")

try:
    put_response = requests.put(f"{POSTS_URL}/1", json=replacement, timeout=10)
except requests.exceptions.RequestException as error:
    print(f"  Network problem: {error}")
    raise SystemExit(1)

show_response(put_response)
print("  Notice the server echoes back the whole replaced object.")


# ================================================================
# 3. PATCH: update part of a resource
# ================================================================
print_header("=== 3. PATCH: update only the title of post 1 ===")

# PATCH sends only the fields that change. Everything else stays as is.
changes = {"title": "Only the title changed"}

print(f"  Sending PATCH {POSTS_URL}/1")
print(f"  Payload: {changes}")

try:
    patch_response = requests.patch(f"{POSTS_URL}/1", json=changes, timeout=10)
except requests.exceptions.RequestException as error:
    print(f"  Network problem: {error}")
    raise SystemExit(1)

show_response(patch_response)
print("  The title changed, but the original body is still there.")


# ================================================================
# 4. DELETE: remove a resource
# ================================================================
print_header("=== 4. DELETE: remove post 1 ===")

print(f"  Sending DELETE {POSTS_URL}/1")

try:
    # DELETE needs no payload: the id in the URL says what to remove.
    delete_response = requests.delete(f"{POSTS_URL}/1", timeout=10)
except requests.exceptions.RequestException as error:
    print(f"  Network problem: {error}")
    raise SystemExit(1)

show_response(delete_response)
print("  JSONPlaceholder answers 200 and an empty object {}.")


# ================================================================
# Summary
# ================================================================
print_header("=== Summary ===")
print("Method  URL          Payload          Typical success code")
print("POST    /posts       full object      201 Created")
print("PUT     /posts/1     full object      200 OK")
print("PATCH   /posts/1     changed fields   200 OK")
print("DELETE  /posts/1     none             200 OK")
print()
print("Use json=payload so requests serializes the dict and sets the header.")
print("Always pass a timeout, and check the status code before trusting the body.")

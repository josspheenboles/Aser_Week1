"""
network_error_demo.py
=====================

A beginner-friendly demo of robust error handling around network calls.

Why this matters:
    Network calls are inherently unreliable. The server may be down,
    the internet may drop, the reply may be slow, or the URL may be
    wrong. Without error handling, any of those stops the whole program
    with a long stack trace. With error handling, the program prints a
    friendly message and keeps running.

The demo covers four scenarios:
    1. ConnectionError    - the domain cannot be reached
    2. Timeout            - the server is too slow to answer
    3. HTTPError          - the server answers with 404 or 500
    4. RequestException   - the catch-all safety net

Run it with:

    python network_error_demo.py
"""

import sys

import requests

# Windows terminals sometimes use an older text encoding; force UTF-8.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass


def print_header(title):
    """Print a clear separator so each scenario is easy to find."""
    print()
    print("=" * 64)
    print(title)
    print("=" * 64)


def safe_get(url, timeout=5.0):
    """GET a URL without letting network problems crash the program.

    Returns the response object on success, or None if anything failed.
    The try / except / else / finally layout shows exactly where each
    part runs:

        try     -> the code that might fail (the network call)
        except  -> the specific errors we know how to explain
        else    -> runs only when no error happened
        finally -> always runs, error or not (cleanup goes here)
    """
    print(f"  Requesting: {url}")
    print(f"  Timeout: {timeout} seconds")

    try:
        # --- The network call happens here ---
        # timeout stops the program from waiting forever for an answer.
        response = requests.get(url, timeout=timeout)

        # Turn a 4xx or 5xx status code into a catchable HTTPError.
        # Without this line, a 404 would look like a success.
        response.raise_for_status()

    except requests.exceptions.ConnectionError:
        # The domain could not be reached: no internet, wrong name, or
        # the server is offline. requests raises ConnectionError.
        print("  [ConnectionError] Network connection failed.")
        print("  Please check your internet connection and the URL.")
        return None

    except requests.exceptions.Timeout:
        # Timeout covers both ConnectTimeout and ReadTimeout. The server
        # simply did not answer within the number of seconds we allowed.
        print(f"  [Timeout] The server did not reply within {timeout} seconds.")
        print("  Try again later, or allow a longer timeout.")
        return None

    except requests.exceptions.HTTPError as error:
        # raise_for_status() sends us here when the server answers with
        # an error status such as 404 Not Found or 500 Server Error.
        status = error.response.status_code
        print(f"  [HTTPError] The server answered with status {status}.")
        if 400 <= status < 500:
            print("  That usually means the request or URL was wrong.")
        else:
            print("  That usually means the server itself had a problem.")
        return None

    except requests.exceptions.RequestException as error:
        # Safety net for every other requests problem: bad URL, too many
        # redirects, SSL failures, and anything added in future versions.
        # Catching this guarantees the program never crashes here.
        print(f"  [RequestException] Something else went wrong: {error}")
        return None

    else:
        # Runs only when the try block finished with no exception.
        print(f"  [Success] Status {response.status_code}. Data received.")
        return response

    finally:
        # Runs whether the request succeeded or failed. Real programs use
        # this spot to close files, stop timers, or write a log entry.
        print("  [finally] Done handling this request.")


# ================================================================
# Intro
# ================================================================
print_header("=== Network Error Handling Demo ===")
print("Every scenario below fails safely instead of crashing.")
print("Read the [tag] on each line to see which except block ran.")


# ================================================================
# Scenario 1: ConnectionError (bad domain / server down)
# ================================================================
print_header("=== Scenario 1: Connection Error (bad domain) ===")
print("The .invalid domain never resolves, so the connection fails.")
safe_get("https://this-domain-should-not-exist-abc123.invalid", timeout=5.0)


# ================================================================
# Scenario 2: Timeout (slow server)
# ================================================================
print_header("=== Scenario 2: Timeout (slow server) ===")
print("httpbin.org/delay/5 waits 5 seconds, but we only allow 2.")
safe_get("https://httpbin.org/delay/5", timeout=2.0)


# ================================================================
# Scenario 3: HTTPError (404 and 500)
# ================================================================
print_header("=== Scenario 3: HTTP Status Errors ===")

print("3a. A missing resource answers 404 Not Found:")
safe_get("https://httpbin.org/status/404", timeout=5.0)

print()
print("3b. A broken endpoint answers 500 Server Error:")
safe_get("https://httpbin.org/status/500", timeout=5.0)


# ================================================================
# Scenario 4: Catch-all RequestException (malformed URL)
# ================================================================
print_header("=== Scenario 4: Catch-All RequestException ===")
print("This URL has no http:// or https:// scheme, so requests raises")
print("MissingSchema, which is caught by the RequestException safety net.")
safe_get("not-a-real-url", timeout=5.0)


# ================================================================
# Bonus: a request that actually works
# ================================================================
print_header("=== Bonus: A Request That Works ===")
response = safe_get("https://httpbin.org/json", timeout=5.0)

if response is not None:
    # Only reached when the request succeeded, so .json() is safe to use.
    slideshow = response.json()["slideshow"]
    print(f"  Slideshow title:  {slideshow['title']}")
    print(f"  Slideshow author: {slideshow['author']}")


# ================================================================
# Summary
# ================================================================
print_header("=== Summary: Exceptions to Know ===")
print("requests.exceptions.ConnectionError   -> cannot reach the server")
print("requests.exceptions.Timeout           -> server too slow (set timeout=!)")
print("requests.exceptions.HTTPError         -> 4xx/5xx from raise_for_status()")
print("requests.exceptions.RequestException  -> base class; catches everything")
print()
print("Catch the specific errors first, then RequestException as a net.")
print("Always pass a timeout, and keep the user-facing message friendly.")

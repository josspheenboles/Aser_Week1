"""
main.py
=======

A beginner-friendly demo of keeping secrets out of source code.

Why this matters:
    Hardcoded API keys and passwords end up in your Git history forever.
    Once pushed, anyone who can read the repository can read the secret,
    even if you delete the line later. Real breaches start this way.

How this script stays safe:
    1. Real values live in a local .env file, not in this file.
    2. .gitignore keeps .env out of Git.
    3. .env.example documents the required keys with placeholder values.
    4. This code loads the values at runtime with python-dotenv and
       os.getenv(), and prints only a masked version of each secret.

Run it with:

    python main.py
"""

import os
import sys

# python-dotenv is a small third-party package. If it is missing, show a
# friendly install message instead of a raw ModuleNotFoundError traceback.
try:
    from dotenv import load_dotenv
except ImportError:
    print("This demo needs the python-dotenv package.")
    print("Install it with one of these commands:")
    print("    pip install python-dotenv")
    print("    uv pip install python-dotenv")
    raise SystemExit(1)


def mask(secret):
    """Return a masked copy of a secret that is safe to print.

    It keeps the first three and last two characters so you can tell
    which key is loaded, while hiding everything in the middle.
    """
    if len(secret) <= 5:
        # Too short to reveal anything at all.
        return "*" * len(secret)

    hidden = len(secret) - 5
    return f"{secret[:3]}{'*' * hidden}{secret[-2:]}"


def simulate_api_call(api_key):
    """Pretend to call a remote API using the secret key.

    A real program would send the key in a header, for example:
        requests.get(url, headers={"Authorization": f"Bearer {api_key}"})
    The key is used here but never printed in full.
    """
    print("  Calling https://api.example.com/v1/data ...")
    print(f"  Using key: {mask(api_key)}")
    return {"status": "ok", "message": "Simulated data received safely."}


# ================================================================
# Step 1: Load the .env file
# ================================================================
print("=" * 60)
print("=== Secure Secrets Demo ===")
print("=" * 60)

# load_dotenv() reads the .env file and copies its values into the
# process environment. By default it does NOT overwrite variables that
# already exist in the operating system, which is the safe behavior.
if load_dotenv():
    print("Loaded settings from .env (kept out of source control).")
else:
    print("No .env file found; checking system environment variables.")

# ================================================================
# Step 2: Read the values with os.getenv()
# ================================================================
# os.getenv() looks up an environment variable by name.
# It returns None when the variable is missing, so we can check for it.
api_key = os.getenv("API_KEY")
app_env = os.getenv("APP_ENV", "development")  # second value is the default
database_url = os.getenv("DATABASE_URL")

# ================================================================
# Step 3: Fail clearly when something required is missing
# ================================================================
required = {"API_KEY": api_key, "DATABASE_URL": database_url}
missing = [name for name, value in required.items() if not value]

if missing:
    print()
    print(f"Missing required setting(s): {', '.join(missing)}")
    print("Fix it by creating your own .env file from the template:")
    print("    Windows:     copy .env.example .env")
    print("    macOS/Linux: cp .env.example .env")
    print("Then replace the placeholder values with your own.")
    # Exit with code 1 so scripts and CI systems know it failed.
    raise SystemExit(1)

# ================================================================
# Step 4: Use the secrets without exposing them
# ================================================================
print()
print(f"Environment: {app_env}")
print(f"API key:     {mask(api_key)}  (length {len(api_key)})")
print(f"Database:    {mask(database_url)}")
print()
print("Notice that the real values are never printed or written in main.py.")
print()

print("Simulating a secure API request:")
result = simulate_api_call(api_key)
print(f"  Result: {result['message']}")

# ================================================================
# Summary
# ================================================================
print()
print("=" * 60)
print("=== Why This Pattern Matters ===")
print("=" * 60)
print("1. Secrets live in .env, which stays on your machine.")
print("2. .gitignore stops .env from ever reaching GitHub.")
print("3. .env.example shows which keys are needed, without values.")
print("4. Code reads secrets at runtime with os.getenv().")
print("5. Printing a masked value proves the key loaded without leaking it.")

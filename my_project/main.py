"""
main.py
=======

The entry point of this demo. It shows how to import code that lives in
another file (a module) and another folder (a package).

Run it from inside the my_project folder:

    python main.py
"""

# --- Two ways to import from the same package ---

# Style 1: import the package, then reach inside it with a dot.
# We use this to read the package version.
import calculator

# Style 2: pull specific functions straight into this file by name.
# After this line, add() can be called directly.
from calculator import add, power, square_root, subtract

print("=== Calculator Demo ===")
print(f"calculator package version: {calculator.__version__}")
print()

print("Basic functions from calculator.basic:")
print(f"  2 + 3 = {add(2, 3)}")
print(f"  10 - 4 = {subtract(10, 4)}")
print()

print("Advanced functions from calculator.advanced:")
print(f"  2 ** 10 = {power(2, 10)}")
print(f"  square root of 81 = {square_root(81)}")
print()

# --- Optional third-party package demo ---
# This block works with or without colorama installed.
# To install it inside your virtual environment, run:
#     uv pip install colorama
try:
    from colorama import Fore, Style, init

    # init() sets up colored text; autoreset clears the color after each print.
    init(autoreset=True)
    success = Fore.GREEN
    reset = Style.RESET_ALL
    colorama_ready = True
except ImportError:
    # colorama is not installed, so use empty strings (no color).
    success = ""
    reset = ""
    colorama_ready = False

print(f"{success}All calculations finished successfully.{reset}")

if colorama_ready:
    print("colorama is installed, so the line above was printed in green.")
else:
    print("(Optional) Install colorama to make that line green:")
    print("    uv pip install colorama")

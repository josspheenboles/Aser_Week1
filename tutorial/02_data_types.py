"""
02 - DATA TYPES
===============

Every value in Python has a *type*. The type decides:
  - what the value means,
  - which operators work on it,
  - which methods it has.

The big four for beginners:

    str    text           "hello", 'hi', triple-quoted text
    int    whole numbers  42, -7, 0
    float  decimals       3.14, 2.0, 1e6
    bool   truth values   True, False

Use type(value) to inspect. Use isinstance(value, SomeType) to test safely.
"""

# ---------------------------------------------------------------------
# 1. STRINGS - text
# ---------------------------------------------------------------------
# Strings are immutable sequences of characters.

name = "Ada"
empty = ""
multi = """This spans
multiple lines."""

# Concatenation and repetition create NEW strings (immutability):
print("Hello, " + name)     # Hello, Ada
print("-" * 10)             # ----------

# f-strings: the modern, readable way to build text.
age = 36
print(f"{name} is {age} years old.")
print(f"2 + 2 = {2 + 2}, and pi is about {3.14159:.2f}")

# Indexing and slicing: 0-based, end-exclusive, negatives count from the end
s = "python"
print(s[0], s[-1])          # p n
print(s[0:3], s[:3], s[3:]) # pyt pyt hon
print(s[::-1])              # nohtyp  (a common reverse trick)

# Common methods (all return new strings; none mutate):
messy = "  Hello World  "
print(messy.strip())                 # "Hello World"
print(messy.strip().lower())         # "hello world"
print("a,b,c".split(","))            # ['a', 'b', 'c']
print("-".join(["a", "b", "c"]))     # a-b-c
print("hello".startswith("he"))      # True
print("hello".replace("l", "L"))     # heLLo

# A frequent bug: strings are NOT numbers.
# "3" + 3  -> TypeError. Convert explicitly:
print(int("3") + 3)                  # 6
print(str(3) + "3")                  # "33"
print(float("2.5") * 2)              # 5.0

# ---------------------------------------------------------------------
# 2. INTEGERS - whole numbers
# ---------------------------------------------------------------------
# Python ints have arbitrary precision: they grow as large as memory allows.

count = 42
negative = -7
big = 10 ** 20            # no overflow, unlike many languages

print(count + 8)          # 50
print(count // 5)         # 8   floor division (integer result)
print(count % 5)          # 2   remainder / modulo
print(count ** 2)         # 1764 exponentiation
print(divmod(42, 5))      # (8, 2)  quotient and remainder together

# Underscores improve readability of long literals:
population = 8_000_000_000
print(f"{population:,}")  # 8,000,000,000

# ---------------------------------------------------------------------
# 3. FLOATS - decimals (IEEE-754 double precision)
# ---------------------------------------------------------------------
# Floats are approximations. This is not a Python quirk; it is how
# binary floating point works in every mainstream language.

print(0.1 + 0.2)                 # 0.30000000000000004
print(0.1 + 0.2 == 0.3)          # False (!)  never compare floats with ==

# Compare with a tolerance instead:
import math
print(math.isclose(0.1 + 0.2, 0.3))   # True

# For money, prefer integers (cents) or the `decimal` module:
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))  # 0.3  (exact)
print(Decimal("19.99") * 3)             # 59.97

# Useful float tools
print(round(3.14159, 2))    # 3.14
print(math.floor(3.9))      # 3  (int)
print(math.ceil(3.1))       # 4  (int)
print(float("inf") > 10**100)  # True

# ---------------------------------------------------------------------
# 4. BOOLEANS - True / False
# ---------------------------------------------------------------------
# bool is a subclass of int: True == 1 and False == 0.
# That is occasionally handy, but prefer explicit bools for clarity.

is_ready = True
is_empty = False
print(is_ready, is_empty)
print(True + True)          # 2  (True behaves as 1)
print(isinstance(True, int))  # True

# Comparison operators produce booleans:
print(5 > 3, 5 == 3, 5 != 3, 3 <= 3)

# Logical operators: and, or, not (short-circuiting)
print(True and False)       # False
print(True or False)        # True
print(not True)             # False

# `and` / `or` return one of their OPERANDS, not necessarily a bool.
# This enables the common "default value" idiom:
username = "" or "guest"
print(username)             # guest   ("" is falsy)

# Truthiness: every object is either truthy or falsy in a condition.
# Falsy values: False, None, 0, 0.0, "", [], (), {}, set()
for value in [0, 1, "", "x", [], [0], None]:
    print(f"{value!r:8} -> {'truthy' if value else 'falsy'}")

# ---------------------------------------------------------------------
# 5. TYPE CONVERSION AND INSPECTION
# ---------------------------------------------------------------------
print(type(42))             # <class 'int'>
print(type(42.0))           # <class 'float'>
print(type("42"))           # <class 'str'>
print(type(True))           # <class 'bool'>

# int <-> float <-> str conversions
print(int(3.99))            # 3   (truncates toward zero, does NOT round)
print(float(3))             # 3.0
print(str(3.0))             # "3.0"

# Careful: int("3.5") raises ValueError. Go through float first:
print(int(float("3.5")))    # 3

# isinstance handles inheritance and is preferred over type() == ...
print(isinstance(True, bool))   # True
print(type(True) == bool)       # True
print(isinstance(5, (int, float)))  # True

# ---------------------------------------------------------------------
# 6. WHY TYPES MATTER: the same operator, different behaviour
# ---------------------------------------------------------------------
print("3" * 3)    # "333"     string repetition
print(3 * 3)      # 9         arithmetic
print([0] * 3)    # [0, 0, 0] list repetition
# print("3" + 3)  # TypeError: can only concatenate str to str
# This is why knowing the type tells you what an operator will do.

# ---------------------------------------------------------------------
# HANDS-ON CHALLENGES
# ---------------------------------------------------------------------
def challenge_1():
    """Given a full name "  ada lovelace  ", produce "Ada Lovelace".

    TODO: strip whitespace, title-case each word, join with spaces.
    """
    pass


def challenge_2():
    """Ask for a price as text, add 8% tax, print with 2 decimals.

    Note: input() always returns str, so you must convert.
    """
    pass


def challenge_3():
    """Predict each result, then run:
       1) 7 / 2
       2) 7 // 2
       3) 7 % 2
       4) bool("0")
       5) 0.1 * 3 == 0.3
    """
    pass


# ---------------------------------------------------------------------
# SOLUTIONS
# ---------------------------------------------------------------------
def solution_1():
    raw = "  ada lovelace  "
    cleaned = " ".join(raw.split()).title()
    print(repr(cleaned))   # 'Ada Lovelace'


def solution_2():
    raw = "19.99"                       # imagine this came from input()
    price = float(raw)
    total = price * 1.08
    print(f"Total: {total:.2f}")        # Total: 21.59


def solution_3():
    print(7 / 2)                 # 3.5    true division -> float
    print(7 // 2)                # 3      floor division
    print(7 % 2)                 # 1      remainder
    print(bool("0"))             # True   non-empty string is truthy
    print(0.1 * 3 == 0.3)        # False  float precision


if __name__ == "__main__":
    print("\n--- Solutions ---")
    solution_1()
    solution_2()
    solution_3()

# KEY TAKEAWAYS
# --------------
# 1. type() tells you what operations are legal.
# 2. Strings are immutable; every "modifying" method returns a new string.
# 3. int is exact; float is approximate. Never compare floats with ==.
# 4. bool is an int subclass, and every object has a truthiness.
# 5. Convert explicitly (int(), float(), str()) when types must match.

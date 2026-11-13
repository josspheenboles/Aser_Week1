"""
01 - VARIABLES
==============

A variable is a *name* that refers to a value stored in memory.

The key mental model (and the one that trips people up):

    name  ----->  object (value)  in memory

The name is NOT the box. The name is a label pointing at a box.
Python keeps a table of names -> memory addresses. Assigning a value
makes the name point at an object; it does not copy the object into
a fixed slot like C or Java primitives do.

Try the examples in order. Run with:  python 01_variables.py
"""

# ---------------------------------------------------------------------
# 1. Creating a variable
# ---------------------------------------------------------------------
# The syntax is:   name = expression
# "=" is the ASSIGNMENT operator, not "equals". It means:
# "evaluate the right side, then make the left-side name point at it."

age = 30            # create an int object, bind the name `age` to it
greeting = "Hello"  # create a str object, bind `greeting` to it

print(age)          # 30      -> reading a variable looks up its object
print(greeting)     # Hello

# ---------------------------------------------------------------------
# 2. Assignment in memory: identity vs equality
# ---------------------------------------------------------------------
# id(obj) gives the object's identity (its address in CPython).
# "is" compares identity; "==" compares value.

a = [1, 2, 3]
b = a               # b points at the SAME list object, no copy happens
c = [1, 2, 3]       # a brand-new list that happens to look equal

print(a is b)       # True   -> one object, two names (aliasing)
print(a is c)       # False  -> two different objects
print(a == c)       # True   -> same contents, different identity
print(id(a) == id(b))  # True

# Because b is an alias, mutating through b is visible through a:
b.append(4)
print(a)            # [1, 2, 3, 4]  <-- a "changed" too
print(c)            # [1, 2, 3]     <-- c untouched

# ---------------------------------------------------------------------
# 3. Rebinding vs mutating
# ---------------------------------------------------------------------
x = 10
x = x + 1           # right side builds 11, then `x` is REBOUND to 11.
                    # The old 10 object is simply no longer referenced.
print(x)            # 11

# Integers are immutable: you never change a 10 into an 11.
# Strings are immutable too, so this makes a NEW string:
word = "cat"
word = word + "s"   # "cats" is a new object; `word` now points at it
print(word)

# Lists are mutable, so this changes the object in place:
numbers = [1, 2]
numbers.append(3)   # no rebinding! same list object, new contents
print(numbers)

# ---------------------------------------------------------------------
# 4. Multiple assignment and swapping
# ---------------------------------------------------------------------
first, second = "Ada", "Lovelace"   # unpacking: two names, two values
print(first, second)

first, second = second, first       # classic swap, no temp variable needed
print(first, second)

a = b = 0                           # both names point at the same int 0
print(a, b)

# ---------------------------------------------------------------------
# 5. Naming rules and style (PEP 8)
# ---------------------------------------------------------------------
# - Letters, digits, underscores; cannot start with a digit.
# - Case-sensitive: `total` and `Total` are different names.
# - snake_case for variables and functions.
# - UPPER_CASE for constants (a convention, not enforced by Python).
# - Names should describe intent: `elapsed_seconds`, not `t`.

MAX_RETRIES = 3
user_name = "ada"
is_logged_in = False

# ---------------------------------------------------------------------
# 6. A small worked example: using variables to avoid repetition
# ---------------------------------------------------------------------
price = 19.99
quantity = 3
tax_rate = 0.08

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Subtotal: {subtotal:.2f}")
print(f"Tax:      {tax:.2f}")
print(f"Total:    {total:.2f}")

# ---------------------------------------------------------------------
# HANDS-ON CHALLENGES
# ---------------------------------------------------------------------
# Try these yourself before reading the solutions at the bottom.


def challenge_1():
    """Create variables describing yourself and print one sentence.

    TODO:
      - Create `name` (str), `age` (int), and `favourite_language` (str).
      - Print: "My name is <name>, I am <age>, and I like <lang>."
    """
    pass


def challenge_2():
    """Predict the output, then verify.

    TODO:
      - Set a = [1, 2], b = a
      - append 3 through b
      - print a and b. Are they the same object? Prove it with `is`.
    """
    pass


def challenge_3():
    """Swap two variables in one line, then print them."""
    pass


# ---------------------------------------------------------------------
# SOLUTIONS  (run this file to see them)
# ---------------------------------------------------------------------
def solution_1():
    name = "Maya"
    age = 28
    favourite_language = "Python"
    print(f"My name is {name}, I am {age}, and I like {favourite_language}.")


def solution_2():
    a = [1, 2]
    b = a
    b.append(3)
    print(a, b)          # [1, 2, 3] [1, 2, 3]
    print(a is b)        # True
    # Lesson: assignment aliases; it does not copy.


def solution_3():
    left, right = "left", "right"
    left, right = right, left
    print(left, right)   # right left


if __name__ == "__main__":
    print("\n--- Solutions ---")
    solution_1()
    solution_2()
    solution_3()

# KEY TAKEAWAYS
# --------------
# 1. `name = value` makes a name refer to an object.
# 2. `is` asks "same object?"; `==` asks "same value?".
# 3. Rebinding (`x = ...`) changes what a name points at.
#    Mutating (`.append(...)`) changes the object itself.
# 4. Two names can point at one object (aliasing). Copy explicitly if
#    you need independence:  b = a.copy()  (shallow)  or  copy.deepcopy(a).

"""
functions_basics.py
===================

A beginner-friendly tour of Python functions:

    Part 1 - Define and call your first function
    Part 2 - Parameters and arguments (inputs)
    Part 3 - The return statement (outputs)
    Part 4 - Default parameters and keyword arguments
    Part 5 - Local vs. global scope

Run it with:

    python functions_basics.py

Read the comments next to each block, then compare them with what
appears in the terminal. Only the Python standard library is used,
so there is nothing to install.
"""

# ============================================================
# Part 1: Your First Function
# ============================================================
# A function is a named block of code that you can reuse.
# Defining a function does not run it. It only teaches Python the
# steps, ready for when you call the function by name.
print()
print("=" * 55)
print("=== Part 1: Your First Function ===")
print("=" * 55)


def say_hello():
    """Print a friendly greeting.

    This function takes no parameters and returns nothing.
    Its only job is to print one line of text.
    """
    print("Hello! Welcome to the functions demo.")


# Nothing above was printed yet: we only defined the function.
# Calling it by name runs its indented block. One definition can
# be used as many times as we like.
say_hello()
say_hello()
say_hello()


# ============================================================
# Part 2: Parameters and Arguments
# ============================================================
# Parameters are placeholders listed in the function definition.
# Arguments are the real values passed in when the function is called.
print()
print("=" * 55)
print("=== Part 2: Parameters and Arguments ===")
print("=" * 55)


def rectangle_area(width, height):
    """Print the area of a rectangle.

    width and height are parameters. They let the same function
    work for many different rectangles instead of one fixed size.
    """
    area = width * height
    print(f"A {width} x {height} rectangle has an area of {area}.")


# Here 4 and 5 are arguments. They fill width and height in order:
# width gets 4, height gets 5. Order matters when using positions.
rectangle_area(4, 5)
rectangle_area(10, 3)
rectangle_area(7, 7)


# ============================================================
# Part 3: The return Statement
# ============================================================
# print() displays a value, but it hands nothing back to your code.
# return sends a value back to the caller so it can be stored,
# printed later, or used in more calculations.
print()
print("=" * 55)
print("=== Part 3: The return Statement ===")
print("=" * 55)


def calculate_discount(price, discount_percent):
    """Return the final price after a percentage discount.

    The returned number belongs to the code that called the function.
    """
    discount_amount = price * discount_percent / 100
    final_price = price - discount_amount
    return final_price


original_price = 80

# sale_price receives the value returned by the function. We could
# not do this if calculate_discount only printed its answer.
sale_price = calculate_discount(original_price, 25)

print(f"Original price: ${original_price:.2f}")
print(f"Sale price:     ${sale_price:.2f}")
print(f"You save:       ${original_price - sale_price:.2f}")

# Because sale_price is a normal number, we can keep calculating.
print(f"Two items on sale: ${sale_price * 2:.2f}")


# ============================================================
# Part 4: Default Parameters and Keyword Arguments
# ============================================================
# A default value is used when the caller does not provide that
# argument. Keyword arguments name each value at the call site,
# which can make longer calls easier to read.
print()
print("=" * 55)
print("=== Part 4: Default Parameters and Keyword Arguments ===")
print("=" * 55)


def format_price(amount, currency="USD"):
    """Return a price formatted with a currency label.

    currency is optional because it has a default value of "USD".
    amount has no default, so it must always be provided.
    """
    return f"{currency} {amount:.2f}"


# No currency argument: the default "USD" is used.
print(f"Default currency:      {format_price(19.99)}")

# A second positional argument replaces the default.
print(f"Positional override:   {format_price(19.99, 'EUR')}")

# Keyword arguments state the parameter names. Order no longer matters.
print(f"Keyword arguments:     {format_price(currency='GBP', amount=25)}")

# Only amount is named, so currency still uses its default value.
print(f"Keyword plus default:  {format_price(amount=5)}")


# ============================================================
# Part 5: Local vs. Global Scope
# ============================================================
# Scope describes where a variable can be used.
#   - A global variable is created outside any function.
#   - A local variable is created inside a function and belongs
#     to that function only.
print()
print("=" * 55)
print("=== Part 5: Local vs. Global Scope ===")
print("=" * 55)

shop_name = "Corner Cafe"  # global: available in the whole file


def show_scope():
    """Show the difference between a local and a global variable."""
    order = "latte"  # local: created inside this function

    # The function can read the global variable.
    print(f"Inside the function, shop_name is: {shop_name}")
    print(f"Inside the function, order is: {order}")


show_scope()

# The global variable is still available after the function runs.
print(f"Outside the function, shop_name is: {shop_name}")

print("Outside the function, trying to read order...")

# The try/except block is here only so the demo can catch the
# expected NameError and keep running. Without it, Python would
# stop the whole script at the next line.
try:
    print(order)
except NameError:
    print("  NameError: 'order' only exists inside show_scope().")


# ============================================================
# Summary
# ============================================================
print()
print("=" * 55)
print("=== Summary ===")
print("=" * 55)
print("def          -> define a reusable block of code")
print("parameters   -> placeholder names in the definition")
print("arguments    -> real values passed in when calling")
print("return       -> send a result back to the caller")
print("default      -> fallback value for an optional parameter")
print("keyword args -> name=value at the call site")
print("local scope  -> variables inside a function stay there")

# Practice ideas:
#   1. Call say_hello() one more time.
#   2. Change rectangle_area(4, 5) to different sizes.
#   3. Change the discount from 25 to 50 and compare the savings.
#   4. Call format_price(12.5, currency="AUD").
#   5. Add a local variable inside show_scope() and try to print it
#      outside. Predict the error before running the script.

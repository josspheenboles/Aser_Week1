"""
control_flow_basics.py
======================

A beginner-friendly tour of Python control flow:

    Part 1 - if / elif / else   (make a decision)
    Part 2 - for loops          (repeat over a collection)
    Part 3 - while loops        (repeat until something changes)
    Part 4 - break / continue   (stop early or skip one item)

Run it with:

    python control_flow_basics.py

Read the comments next to each block, then compare them with what
appears in the terminal. Only the Python standard library is used,
so there is nothing to install.
"""

# ============================================================
# Part 1: if / elif / else
# ============================================================
# An if statement asks a yes/no question. Python runs the first
# branch whose condition is True, then skips the other branches.
print()
print("=" * 55)
print("=== Part 1: If / Else ===")
print("=" * 55)

age = 15

if age < 13:
    # This branch runs only when age is less than 13.
    ticket_price = 5
    ticket_type = "child"
elif age < 65:
    # elif means "else if": it is checked only when the first
    # condition was False.
    ticket_price = 10
    ticket_type = "adult"
else:
    # else is the fallback. It runs when every condition above
    # was False, so no condition has to be written here.
    ticket_price = 7
    ticket_type = "senior"

# These lines run after the decision above, using whichever values
# the chosen branch stored in ticket_type and ticket_price.
print(f"Age: {age}")
print(f"Ticket type: {ticket_type}")
print(f"Price: ${ticket_price}")

# Try changing age on line 31 to 8 or to 70 and run the script again.
# A different branch will run, so the printed result will change too.


# ============================================================
# Part 2: for loops
# ============================================================
# A for loop visits each item in a collection, one at a time,
# in the order the items appear.
print()
print("=" * 55)
print("=== Part 2: For Loops ===")
print("=" * 55)

shopping_list = ["apples", "bread", "milk", "eggs"]

print("Shopping list:")
for item in shopping_list:
    # On each pass, "item" holds the next value from the list.
    print(f"  - {item}")

print()
print("Counting from 1 to 5 with range():")

# range(1, 6) produces 1, 2, 3, 4, 5.
# The stop value (6) is NOT included. Python stops just before it.
for number in range(1, 6):
    print(f"  {number}")

print()
print("Counting the items on the list:")

item_count = 0
for item in shopping_list:
    # Add 1 for every item the loop visits.
    item_count = item_count + 1

# This line is outside the loop (note the indentation), so it runs
# once, after every item has been counted.
print(f"  The list has {item_count} items.")


# ============================================================
# Part 3: while loops
# ============================================================
# A while loop repeats as long as its condition stays True.
# Use it when you do not know the number of repeats in advance.
print()
print("=" * 55)
print("=== Part 3: While Loops ===")
print("=" * 55)

print("Countdown:")
countdown = 5

while countdown > 0:
    # This block repeats while countdown is greater than zero.
    print(f"  {countdown}...")

    # This line is essential: it makes the number smaller, so the
    # condition eventually becomes False and the loop can stop.
    countdown = countdown - 1

# When countdown reaches 0, the condition is False, so Python
# leaves the loop and runs the next line.
print("  Blast off!")

# Warning for beginners: if a while loop never changes anything
# that its condition checks, it will run forever. Press Ctrl+C to
# stop a runaway program if that happens.


# ============================================================
# Part 4: break and continue
# ============================================================
# break    -> leave the loop immediately
# continue -> skip the rest of this pass, then start the next one
print()
print("=" * 55)
print("=== Part 4: Break and Continue ===")
print("=" * 55)

print("Searching for milk in the shopping list:")

for item in shopping_list:
    print(f"  Checking {item}...")

    if item == "milk":
        print("  Found milk! Stopping the search with break.")
        # break ends the whole loop now. "eggs" is never checked.
        break

print()
print("Checking stock before adding items to the cart:")

# A dictionary pairs each item name with how many are in stock.
# A quantity of 0 means the item is unavailable.
stock = {
    "apples": 4,
    "bread": 0,
    "milk": 2,
    "eggs": 0,
}

for item, quantity in stock.items():
    if quantity == 0:
        print(f"  Skipping {item}: out of stock.")
        # continue jumps straight to the next item, so the
        # "Adding ..." line below is skipped for sold-out items.
        continue

    # Only items with stock left reach this line.
    print(f"  Adding {item} to the cart ({quantity} available).")


# ============================================================
# Summary
# ============================================================
print()
print("=" * 55)
print("=== Summary ===")
print("=" * 55)
print("if / elif / else -> choose which branch runs")
print("for              -> visit each item in a collection")
print("while            -> repeat until a condition becomes False")
print("break            -> exit a loop early")
print("continue         -> skip to the next pass of a loop")

# Practice ideas:
#   1. Change age and predict which ticket branch will run.
#   2. Add "butter" to shopping_list and count the items again.
#   3. Change the countdown start value to 3.
#   4. Set "milk" to 0 in stock and see what continue skips.

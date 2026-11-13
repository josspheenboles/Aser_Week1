"""
03 - CONTAINERS
===============

A container holds multiple values in one object.

    tuple   (a, b, c)     ordered, immutable, allows duplicates
    list    [a, b, c]     ordered, mutable,   allows duplicates
    dict    {k: v, ...}   insertion-ordered, mutable, unique keys

Rule of thumb:
  - Fixed record of values that will not change  -> tuple
  - Growing/shrinking collection of items        -> list
  - Look things up by a name/key                 -> dict

"Ordered" here means the position is meaningful and iteration is
predictable. Dicts preserve insertion order (guaranteed since 3.7).
"""

# ---------------------------------------------------------------------
# 1. TUPLES - immutable, ordered records
# ---------------------------------------------------------------------
# Use a tuple when the *shape* is fixed: a point, an RGB colour, a row.

point = (3, 4)
rgb = (255, 128, 0)
single = (42,)      # trailing comma is required for a 1-element tuple
not_a_tuple = (42)  # this is just an int in parentheses!

print(point, rgb, single, type(not_a_tuple))

# Indexing, slicing, unpacking, and iteration all work like lists:
x, y = point
print(x, y)                 # 3 4
print(rgb[0], rgb[-1])      # 255 0
print(len(point))           # 2
print(3 in point)           # True

# A tuple can hold anything, including other containers:
record = ("Ada", 36, ["math", "poetry"])
print(record)

# But the tuple itself cannot be reassigned:
try:
    point[0] = 99
except TypeError as e:
    print("Immutable:", e)      # 'tuple' object does not support item assignment

# Gotcha: immutability is shallow. A mutable element can still change.
record[2].append("computing")
print(record)                   # ('Ada', 36, ['math', 'poetry', 'computing'])

# Tuples are hashable (if their contents are), so they can be dict keys:
distances = {("A", "B"): 5, ("B", "C"): 7}
print(distances[("A", "B")])    # 5

# Returning multiple values from a function is really returning a tuple:
def min_max(values):
    return min(values), max(values)

low, high = min_max([4, 1, 9])
print(low, high)                # 1 9

# ---------------------------------------------------------------------
# 2. LISTS - mutable, ordered sequences
# ---------------------------------------------------------------------
# Use a list for a collection whose size and contents change.

shopping = ["milk", "eggs"]
shopping.append("bread")            # add to the end
shopping.insert(0, "coffee")        # insert at index
shopping.remove("eggs")             # remove first matching value
last = shopping.pop()               # remove and return the last item
print(shopping, last)               # ['coffee', 'milk'] bread

# Ordering and searching
numbers = [5, 2, 9, 1]
numbers.sort()                      # in place, returns None
print(numbers)                      # [1, 2, 5, 9]
print(sorted(numbers, reverse=True))  # new list, original untouched
print(numbers.index(5), numbers.count(2))

# Slicing returns a NEW list (a shallow copy of that range):
print(numbers[1:3])                 # [2, 5]
print(numbers[::-1])                # [9, 5, 2, 1]

# Concatenation and repetition build new lists:
print([1, 2] + [3])                 # [1, 2, 3]
print(["x"] * 3)                    # ['x', 'x', 'x']

# List comprehensions: transform/filter in one readable line
squares = [n * n for n in range(6)]
evens = [n for n in range(10) if n % 2 == 0]
print(squares)                      # [0, 1, 4, 9, 16, 25]
print(evens)                        # [0, 2, 4, 6, 8]

# The classic aliasing bug:
a = [1, 2]
b = a               # alias, NOT a copy
b.append(3)
print(a is b, a)    # True [1, 2, 3]

# Copy explicitly when you want independence:
c = a.copy()        # or list(a) or a[:]
c.append(4)
print(a, c)         # [1, 2, 3] [1, 2, 3, 4]

# Shallow copies share nested objects:
matrix = [[1, 2], [3, 4]]
shallow = matrix.copy()
shallow[0].append(99)
print(matrix)       # [[1, 2, 99], [3, 4]]  <-- inner list shared!

import copy
deep = copy.deepcopy(matrix)
deep[0].append(100)
print(matrix)       # unchanged
print(deep)

# ---------------------------------------------------------------------
# 3. DICTIONARIES - keyed lookups
# ---------------------------------------------------------------------
# Use a dict when you look values up by a meaningful key.

ages = {"ada": 36, "alan": 41}

# Reading: [] raises KeyError if missing; .get() does not.
print(ages["ada"])              # 36
print(ages.get("grace"))        # None
print(ages.get("grace", 0))     # 0  (default)

# Writing: assigning a new key inserts it; existing key updates it.
ages["grace"] = 45
ages["ada"] = 37
print(ages)

# Membership tests check KEYS, not values:
print("ada" in ages)            # True
print(36 in ages)               # False

# Iteration patterns
for name in ages:               # keys
    print(name)
for name, age in ages.items():  # key/value pairs
    print(name, age)
print(list(ages.keys()))
print(list(ages.values()))

# Removing
removed = ages.pop("alan")      # returns the value
print(removed, ages)

# Common building patterns
counts = {}
for word in ["a", "b", "a", "c", "a"]:
    counts[word] = counts.get(word, 0) + 1
print(counts)                   # {'a': 3, 'b': 1, 'c': 1}

# Beginner-friendly equivalent using collections.Counter:
from collections import Counter
print(Counter(["a", "b", "a", "c", "a"]))   # Counter({'a': 3, ...})

# Dict comprehensions
squares = {n: n * n for n in range(5)}
print(squares)                  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Merging (later keys win). `|` needs Python 3.9+.
defaults = {"theme": "dark", "lang": "en"}
user = {"lang": "fr"}
print(defaults | user)          # {'theme': 'dark', 'lang': 'fr'}

# Keys must be hashable: str, int, float, bool, tuple (of hashables).
# Lists and dicts are unhashable because they are mutable.
try:
    bad = {[1, 2]: "no"}
except TypeError as e:
    print("Unhashable:", e)

# Nested data: the shape most real-world JSON has
users = {
    "ada": {"age": 36, "langs": ["python", "math"]},
    "alan": {"age": 41, "langs": ["python"]},
}
print(users["ada"]["langs"][0])         # python
users["grace"] = {"age": 45, "langs": []}
print(len(users))

# ---------------------------------------------------------------------
# 4. CONTRAST: choosing the right container
# ---------------------------------------------------------------------
#                          tuple        list          dict
# mutable?                 no           yes           yes
# ordered?                 yes          yes           yes (insertion)
# duplicates?              yes          yes           keys: no
# access by                index        index         key
# lookup speed             O(n)         O(n)          O(1) average
# can be a dict key?       yes*         no            no
# typical use              fixed record collection    mapping / index
#
# * only if all of its elements are hashable.
#
# Examples:
#   coordinates = (51.5, -0.12)                  -> fixed pair
#   scores = [88, 92, 79]                        -> grows as games are played
#   phone_book = {"ada": "555-0100"}             -> look up by name

# Converting between them:
print(list((1, 2, 3)))              # tuple -> list
print(tuple([1, 2, 3]))             # list -> tuple
print(dict([("a", 1), ("b", 2)]))   # pairs -> dict
print(list({"a": 1, "b": 2}))       # dict -> list of keys

# ---------------------------------------------------------------------
# HANDS-ON CHALLENGES
# ---------------------------------------------------------------------
def challenge_1():
    """Tuples: unpack an RGB tuple and build a CSS colour string.

    Given (255, 128, 0), print "rgb(255, 128, 0)".
    """
    pass


def challenge_2():
    """Lists: given numbers = [4, 8, 1, 9, 3],
    make a NEW list of only the numbers above 3, sorted descending.
    Do not mutate the original.
    """
    pass


def challenge_3():
    """Dicts: count how many times each character appears in "banana"
    and print the result. Then print the most common character.
    """
    pass


def challenge_4():
    """Containers together: represent a small inventory.

    inventory = {"apple": (10, 0.50), "pear": (5, 0.75)}
    Each value is (quantity, unit_price).
    Print each item and its total value, then the grand total.
    """
    pass


# ---------------------------------------------------------------------
# SOLUTIONS
# ---------------------------------------------------------------------
def solution_1():
    rgb = (255, 128, 0)
    r, g, b = rgb
    print(f"rgb({r}, {g}, {b})")


def solution_2():
    numbers = [4, 8, 1, 9, 3]
    result = sorted((n for n in numbers if n > 3), reverse=True)
    print(result)          # [9, 8, 4]
    print(numbers)         # [4, 8, 1, 9, 3]  unchanged


def solution_3():
    text = "banana"
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    print(counts)                              # {'b': 1, 'a': 3, 'n': 2}
    top = max(counts, key=counts.get)
    print(top, counts[top])                    # a 3


def solution_4():
    inventory = {"apple": (10, 0.50), "pear": (5, 0.75)}
    grand_total = 0.0
    for item, (quantity, unit_price) in inventory.items():
        value = quantity * unit_price
        grand_total += value
        print(f"{item:6} {quantity:3} x {unit_price:.2f} = {value:.2f}")
    print(f"Grand total: {grand_total:.2f}")


if __name__ == "__main__":
    print("\n--- Solutions ---")
    solution_1()
    solution_2()
    solution_3()
    solution_4()

# KEY TAKEAWAYS
# --------------
# 1. tuple = fixed shape, list = changing collection, dict = keyed lookup.
# 2. Mutability changes what is legal: lists/dicts change in place and
#    cannot be dict keys; tuples cannot change but can be keys.
# 3. Assignment aliases. Copy with .copy() for a shallow copy and
#    copy.deepcopy() when nested objects must also be independent.
# 4. "in" checks elements for lists/tuples but KEYS for dicts.
# 5. Pick the container that makes your intent obvious.

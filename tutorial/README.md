# Python Foundations: Variables, Data Types, Containers

A short, runnable tutorial. Every file is self-contained, heavily commented,
and ends with hands-on challenges plus solutions.

```
tutorial/
  01_variables.py     names, identity, aliasing, rebinding vs mutating
  02_data_types.py    str, int, float, bool, conversions, truthiness
  03_containers.py    tuple, list, dict, copying, choosing the right one
```

Run any file with:

```powershell
python tutorial/01_variables.py
```

---

## 1. Variables

A variable is a **name bound to an object in memory**:

```
age  --->  [ int object: 30 ]
```

Assignment (`=`) evaluates the right side, then rebinds the name to that
object. It does not copy the value into a fixed slot.

```python
age = 30
alias = age          # both names point at the same object
```

Two consequences worth internalising:

| Concept | Meaning | Test |
| --- | --- | --- |
| identity | same object in memory | `a is b` |
| equality | same value | `a == b` |
| rebinding | name points somewhere new | `a = a + 1` |
| mutation | object changes in place | `a.append(1)` |

```python
a = [1, 2]
b = a          # alias, not a copy
b.append(3)
print(a)       # [1, 2, 3]  -- a and b are one object
```

If you need an independent copy, copy explicitly: `b = a.copy()`
(shallow) or `copy.deepcopy(a)` (nested objects too).

---

## 2. Data Types

The type determines what a value means, which operators work, and which
methods exist.

| Type | Example | Mutable? | Notes |
| --- | --- | --- | --- |
| `str` | `"hello"` | no | sequence of characters, supports slicing |
| `int` | `42` | no | arbitrary precision, `//` `%` `**` |
| `float` | `3.14` | no | IEEE-754 approximation, never use `==` |
| `bool` | `True` | no | subclass of `int`, `True == 1` |

Key points:

- Strings are immutable: `s.upper()` returns a new string.
- Floats are approximate: `0.1 + 0.2 == 0.3` is `False`. Use
  `math.isclose`, or `Decimal` for money.
- Every object has a truthiness. Falsy: `False`, `None`, `0`, `0.0`,
  `""`, `[]`, `()`, `{}`, `set()`.
- Convert explicitly: `int("3")`, `float("2.5")`, `str(3)`.
  `int("3.5")` raises `ValueError`; use `int(float("3.5"))`.

---

## 3. Containers

| | `tuple` | `list` | `dict` |
| --- | --- | --- | --- |
| mutable | no | yes | yes |
| ordered | yes | yes | yes (insertion) |
| duplicates | yes | yes | no (keys) |
| access by | index | index | key |
| lookup | O(n) | O(n) | O(1) avg |
| dict key | yes\* | no | no |
| use for | fixed records | changing collections | keyed lookup |

\* only if every element is hashable.

```python
point = (3, 4)                          # fixed shape
scores = [88, 92, 79]                   # grows and shrinks
phone_book = {"ada": "555-0100"}        # look up by name
```

Gotchas:

- `(42)` is an `int`; `(42,)` is a one-element tuple.
- `in` checks elements for lists/tuples but **keys** for dicts.
- `d["missing"]` raises `KeyError`; `d.get("missing", default)` does not.
- A shallow copy still shares nested objects; use `copy.deepcopy` when
  nested structures must be independent.

---

## Challenges (and answers)

Solutions are at the bottom of each file; try them first.

1. **Variables** — store `name`, `age`, `favourite_language` and print one
   sentence.
2. **Variables** — set `b = a` for a list, append through `b`, explain why
   `a` changed. (`a is b` is `True`: aliasing.)
3. **Data types** — turn `"  ada lovelace  "` into `"Ada Lovelace"`.
   (`" ".join(raw.split()).title()`)
4. **Data types** — add 8% tax to a price read as text, print 2 decimals.
   (`float(raw) * 1.08`)
5. **Lists** — from `[4, 8, 1, 9, 3]`, build a new descending list of values
   above 3 without mutating the original.
6. **Dicts** — count characters in `"banana"` and find the most common.
7. **All three** — model an inventory as
   `{"apple": (quantity, unit_price)}` and total its value.

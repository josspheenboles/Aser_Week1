# Functions Basics

A small Python script for absolute beginners. It explains how to define and call
functions, pass in inputs, return results, use defaults, and understand basic
scope. Only the standard library is used.

## What you will learn

| Part | Topic | Example |
| --- | --- | --- |
| 1 | Defining and calling | `say_hello()` called three times |
| 2 | Parameters and arguments | `rectangle_area(width, height)` |
| 3 | `return` vs. `print` | `calculate_discount(price, percent)` |
| 4 | Defaults and keyword arguments | `format_price(amount, currency="USD")` |
| 5 | Local vs. global scope | A local `order` variable and a global `shop_name` |

## Requirements

- Python 3.8 or newer
- No third-party packages, so there is nothing to install

Check your version with:

```bash
python --version
```

## How to run

1. Open a terminal (PowerShell, Command Prompt, or a terminal on macOS/Linux).
2. Move into this folder:

   ```powershell
   cd C:\Users\M\Desktop\Aser_Demo\functions_demo
   ```

   On macOS or Linux, use the path where you saved the folder, for example:

   ```bash
   cd /path/to/Aser_Demo/functions_demo
   ```

3. Run the script:

   ```bash
   python functions_basics.py
   ```

The program prints five labelled sections and then a summary. It does not ask
for input, so it runs start to finish on its own.

### If `python` is not found

- **Windows:** try `py functions_basics.py` instead.
- **macOS/Linux:** try `python3 functions_basics.py` instead.

## What the output looks like

```text
=======================================================
=== Part 1: Your First Function ===
=======================================================
Hello! Welcome to the functions demo.
Hello! Welcome to the functions demo.
Hello! Welcome to the functions demo.

=======================================================
=== Part 3: The return Statement ===
=======================================================
Original price: $80.00
Sale price:     $60.00
You save:       $20.00
Two items on sale: $120.00
```

## Key takeaways: inputs, logic, output

A function has three useful pieces:

1. **Inputs (parameters):** names in the definition, such as `width` and
   `height`. The real values passed at the call site are called **arguments**.
2. **Logic:** the indented block that does the work, such as multiplying width
   by height.
3. **Output (`return`):** the value sent back to the caller. `print()` only
   displays text; `return` gives your program a value it can store and reuse.

```python
def add(a, b):          # inputs: a and b
    total = a + b       # logic
    return total        # output

result = add(2, 3)      # result is now 5
```

## Try it yourself

Open `functions_basics.py` in any text editor, make one change, save, and run it
again:

1. Call `say_hello()` a fourth time and watch the extra line appear.
2. Change `rectangle_area(4, 5)` to `rectangle_area(12, 8)`.
3. Change the discount from `25` to `50` and compare the sale price and savings.
4. Call `format_price(12.5, currency="AUD")` and see the label change.
5. Add a new local variable inside `show_scope()` and try to print it outside.
   Predict the `NameError` before you run the script.

## A note about scope

A variable created inside a function is **local**: it exists only while that
function runs. A variable created outside a function is **global** and can be
read by functions in the same file. The demo uses a small `try`/`except` block
only to catch the expected `NameError` so the script can keep running.

## Files

| File | Purpose |
| --- | --- |
| `functions_basics.py` | The annotated demo script |
| `README.md` | This guide |

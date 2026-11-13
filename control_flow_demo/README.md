# Control Flow Basics

A small Python script for absolute beginners. It demonstrates how Python makes
decisions and repeats actions, using only the standard library.

## What you will learn

| Part | Topic | Example |
| --- | --- | --- |
| 1 | `if` / `elif` / `else` | Movie-ticket pricing based on age |
| 2 | `for` loops | A shopping list and `range()` counting |
| 3 | `while` loops | A countdown that stops at zero |
| 4 | `break` / `continue` | Searching for an item and skipping sold-out items |

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
   cd C:\Users\M\Desktop\Aser_Demo\control_flow_demo
   ```

   On macOS or Linux, use the path where you saved the folder, for example:

   ```bash
   cd /path/to/Aser_Demo/control_flow_demo
   ```

3. Run the script:

   ```bash
   python control_flow_basics.py
   ```

That is all. The program prints four labelled sections and then a summary.

### If `python` is not found

- **Windows:** try `py control_flow_basics.py` instead.
- **macOS/Linux:** try `python3 control_flow_basics.py` instead.

## What the output looks like

```text
=======================================================
=== Part 1: If / Else ===
=======================================================
Age: 15
Ticket type: adult
Price: $10

=======================================================
=== Part 2: For Loops ===
=======================================================
Shopping list:
  - apples
  - bread
  - milk
  - eggs
...
```

The script does not ask for input, so it runs start to finish on its own.

## Try it yourself

Open `control_flow_basics.py` in any text editor, make one change, save, and run
it again:

1. Change `age = 15` to `age = 8` or `age = 70`. Predict which ticket branch
   will run before you look at the output.
2. Add `"butter"` to `shopping_list` and watch the item count change.
3. Change `countdown = 5` to `countdown = 3`.
4. Set `"milk"` to `0` in the `stock` dictionary. The `continue` example will
   then skip milk instead of adding it.

### A note about `while` loops

A `while` loop repeats until its condition becomes `False`. If nothing inside
the loop changes that condition, the loop runs forever. In this demo, the line
`countdown = countdown - 1` is what allows the loop to finish. If a program ever
gets stuck, press `Ctrl+C` in the terminal to stop it.

## Files

| File | Purpose |
| --- | --- |
| `control_flow_basics.py` | The annotated demo script |
| `README.md` | This guide |

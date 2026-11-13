# My Project: Modules, Packages, Virtual Environments, and `uv`

A tiny, hands-on project for absolute beginners. It answers three common
questions:

1. How does Python organize code across **multiple files and folders**?
2. Why does every project need its own **virtual environment**?
3. How does **`uv`** make installing packages dramatically faster than `pip`?

The example is a small `calculator` package used by `main.py`. No knowledge of
classes or advanced Python is required.

---

## Project structure

```text
my_project/
├── calculator/
│   ├── __init__.py      # Marks the folder as a package and exposes clean imports
│   ├── basic.py         # add() and subtract()
│   └── advanced.py      # power() and square_root()
├── main.py              # Imports the package and runs a short demo
└── README.md            # This guide
```

Every file is small on purpose. Read them in this order: `basic.py`,
`advanced.py`, `__init__.py`, then `main.py`.

---

## Prerequisites

- **Python 3.9 or newer** — check with:

  ```bash
  python --version
  ```

- **`uv` (optional but recommended)** — see Step 3 to install it.

You can complete Steps 1, 2, and 4 with only Python. `uv` is the fast path.

---

## Step 1: Modules and packages, explained

### A module is one `.py` file

Any Python file is a **module**. When you write `basic.py`, you have created a
module named `basic`. Its functions become reusable from other files.

```python
# calculator/basic.py
def add(a, b):
    return a + b
```

### A package is a folder of modules

A **package** is a folder that Python treats as a group of modules. Adding a
special file named `__init__.py` marks the folder as a package:

```text
calculator/          <-- the package
├── __init__.py      <-- the marker file
├── basic.py         <-- module: calculator.basic
└── advanced.py      <-- module: calculator.advanced
```

The full name of a module includes its package, so `basic.py` inside
`calculator/` is imported as `calculator.basic`.

### Four ways to import

```python
# 1. Import a whole module, then use a dot.
import calculator.basic
calculator.basic.add(2, 3)

# 2. Import a module under a shorter name.
import calculator.basic as basic
basic.add(2, 3)

# 3. Import one function by name.
from calculator.basic import add
add(2, 3)

# 4. Import from the package directly (this is why __init__.py matters).
from calculator import add, power
```

### What `__init__.py` does here

`calculator/__init__.py` re-exports the useful functions so consumers can write
the short form:

```python
from calculator import add, power, square_root, subtract
```

The leading dot in `from .basic import add` means **"from this same package"**.
Without the dot, Python would search for a top-level module named `basic`.

### Why `__pycache__` appears

The first time you import a module, Python saves a compiled copy inside a
`__pycache__/` folder. It is a cache for speed. You can safely delete it, and
you should not commit it to Git.

---

## Step 2: Virtual environments

### Why isolate a project?

Without a virtual environment, every package you install goes into your
**system Python**. Over time that creates problems:

- Project A needs `requests==2.28`, project B needs `requests==2.32`.
- A failed upgrade can break unrelated tools on your computer.
- It becomes hard to tell which project uses which package.

A **virtual environment** (venv) is a private folder that holds its own Python
and its own packages. Each project gets a clean, separate set.

### Create one with `uv` (fast)

```bash
cd my_project
uv venv
```

Example output (yours may differ slightly):

```text
Using CPython 3.13.14 interpreter at: C:\Python313\python.exe
Creating virtual environment at: .venv
Activate with: .venv\Scripts\activate
```

### Create one with the standard tool (for comparison)

```bash
python -m venv .venv
```

This does the same job. It is simply slower, because `python -m venv` bootstraps
`pip` and `setuptools` inside the new environment.

### Activate the environment

Activation makes the terminal use the environment's Python and packages.

**Windows PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks the script, allow it for this session only:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

**Windows Command Prompt**

```bat
.venv\Scripts\activate.bat
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

Your prompt usually changes to show `(.venv)`. Confirm the right Python is in
use:

```bash
python -c "import sys; print(sys.executable)"
```

To leave the environment later, run:

```bash
deactivate
```

---

## Step 3: Supercharging with `uv`

`uv` is a single, extremely fast tool that replaces `pip`, `pip-tools`,
`virtualenv`, and more. It is written in Rust and often installs packages 10 to
100 times faster than `pip`.

### Install `uv`

**Windows PowerShell**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS / Linux**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Or with pip / pipx**

```bash
python -m pip install uv
```

Confirm it worked:

```bash
uv --version
```

```text
uv 0.8.0
```

### Install a package with `uv pip`

With your virtual environment activated, install the optional demo package:

```bash
uv pip install colorama
```

Example output:

```text
Resolved 1 package in 120ms
Prepared 1 package in 42ms
Installed 1 package in 9ms
 + colorama==0.4.6
```

Compare that with the traditional command, which uses the same package index but
a slower resolver and installer:

```bash
python -m pip install colorama
```

Useful everyday commands:

```bash
uv pip list                    # show installed packages
uv pip install colorama        # add a package
uv pip uninstall colorama      # remove a package
uv pip install -r requirements.txt
```

### Modern project mode: `uv init` and `uv add`

`uv` can also manage a project for you, recording dependencies in
`pyproject.toml` and locking exact versions in `uv.lock`:

```bash
uv init --bare          # create pyproject.toml in the current folder
uv add colorama         # add a dependency and update the lockfile
uv run main.py          # run inside the managed environment
```

`uv add` is the clean, modern equivalent of installing and then manually writing
the package into a requirements file.

### Run once with a temporary dependency

This is a favorite `uv` trick. It runs your script with a package that is not
permanently installed:

```bash
uv run --with colorama python main.py
```

---

## Step 4: Run the demo

1. Open a terminal and move into the project folder:

   ```powershell
   cd C:\Users\M\Desktop\Aser_Demo\my_project
   ```

2. Create and activate a virtual environment (Step 2):

   ```powershell
   uv venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Run the script:

   ```bash
   python main.py
   ```

You should see (exact numbers are the point — the imports are doing the work):

```text
=== Calculator Demo ===
calculator package version: 1.0.0

Basic functions from calculator.basic:
  2 + 3 = 5
  10 - 4 = 6

Advanced functions from calculator.advanced:
  2 ** 10 = 1024
  square root of 81 = 9.0

All calculations finished successfully.
(Optional) Install colorama to make that line green:
    uv pip install colorama
```

Now install the optional package and run it again:

```bash
uv pip install colorama
python main.py
```

The last lines change to confirm the third-party package is active:

```text
All calculations finished successfully.
colorama is installed, so the line above was printed in green.
```

The script uses `try` / `except ImportError`, so it works with or without
`colorama`. That pattern lets a demo run for everyone while still showing the
benefit of installing a package.

---

## Troubleshooting

| Problem | Cause | Fix |
| --- | --- | --- |
| `ModuleNotFoundError: No module named 'calculator'` | You ran the script from the wrong folder | `cd my_project` first, then `python main.py` |
| `Activate.ps1 cannot be loaded` | PowerShell execution policy | `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` |
| `uv: command not found` | `uv` is not on your PATH | Reinstall `uv`, then open a new terminal |
| Colors do not appear | `colorama` is not installed | `uv pip install colorama` |
| `python` opens the wrong version | System Python is first on PATH | Activate the venv and check `sys.executable` |
| Import works in the editor but not the terminal | The editor added the folder to its own path | Run from the project root, or set `PYTHONPATH` |

---

## Try it yourself

1. **Add a function:** put `multiply(a, b)` in `calculator/basic.py`, export it
   from `__init__.py`, then call it in `main.py`.
2. **Add a module:** create `calculator/stats.py` with an `average(numbers)`
   function and expose it through the package.
3. **Test validation:** call `square_root(-4)` inside a `try` / `except
   ValueError` block and print the error message.
4. **Feel the speed:** time both installers on a fresh environment:
   `uv pip install colorama` versus `python -m pip install colorama`.
5. **Keep Git clean:** add `.venv/` and `__pycache__/` to a `.gitignore` file so
   environments and caches are never committed.

---

## Quick command reference

| Goal | `uv` | Traditional |
| --- | --- | --- |
| Create a venv | `uv venv` | `python -m venv .venv` |
| Activate (PowerShell) | `.\.venv\Scripts\Activate.ps1` | same |
| Install a package | `uv pip install colorama` | `python -m pip install colorama` |
| List packages | `uv pip list` | `python -m pip list` |
| Run a script | `python main.py` | same |
| Run with a temp package | `uv run --with colorama python main.py` | not available |

---

## Files

| File | Purpose |
| --- | --- |
| `calculator/__init__.py` | Marks the folder as a package and exposes clean imports |
| `calculator/basic.py` | `add()` and `subtract()` |
| `calculator/advanced.py` | `power()` and `square_root()` |
| `main.py` | Imports the package and demonstrates it |
| `README.md` | This guide |

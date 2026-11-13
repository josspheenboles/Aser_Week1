# My Secure Project

A beginner-friendly project that shows how to keep API keys, passwords, and
database credentials out of your source code.

The short version:

- **Never** hardcode secrets in `main.py`.
- Put real values in a local `.env` file.
- Add `.env` to `.gitignore` so Git never tracks it.
- Commit a safe `.env.example` so teammates know which keys are needed.
- Read the values at runtime with `python-dotenv` and `os.getenv()`.

## Project structure

```text
my_secure_project/
├── .env              # Real secrets, local only (IGNORED by git)
├── .env.example      # Safe template with placeholders (committed)
├── .gitignore        # Tells Git to ignore .env
├── main.py           # Loads and uses the secrets safely
└── README.md         # This guide
```

## Step 1: Install the dependency

`python-dotenv` is a small library that reads `.env` files.

**With `uv` (fast, recommended):**

```bash
uv pip install python-dotenv
```

**With standard `pip`:**

```bash
python -m pip install python-dotenv
```

Using a virtual environment is recommended:

```powershell
uv venv
.\.venv\Scripts\Activate.ps1
uv pip install python-dotenv
```

On macOS or Linux, activate with `source .venv/bin/activate`.

## Step 2: Create your `.env` from the template

`.env.example` is committed and safe. `.env` holds real values and is ignored.
Copy the template, then edit the copy:

**Windows (PowerShell or Command Prompt):**

```powershell
copy .env.example .env
```

**macOS / Linux:**

```bash
cp .env.example .env
```

Open `.env` and replace the placeholders. For this demo, the included values are
fake and already work:

```dotenv
API_KEY=super_secret_12345
APP_ENV=development
DATABASE_URL=postgres://demo_user:demo_password@localhost:5432/demo_db
```

> The `.env` file is already created in this project with mock values, so you
> can run the demo immediately. The copy step above is what you would do in a
> real project cloned from GitHub, where `.env` is absent.

## Step 3: Run the script

From inside the `my_secure_project` folder:

```bash
cd my_secure_project
python main.py
```

Expected output (the secrets are masked on purpose):

```text
============================================================
=== Secure Secrets Demo ===
============================================================
Loaded settings from .env (kept out of source control).

Environment: development
API key:     sup*************45  (length 18)
Database:    pos****************************************************db

Notice that the real values are never printed or written in main.py.

Simulating a secure API request:
  Calling https://api.example.com/v1/data ...
  Using key: sup*************45
  Result: Simulated data received safely.

============================================================
=== Why This Pattern Matters ===
============================================================
1. Secrets live in .env, which stays on your machine.
2. .gitignore stops .env from ever reaching GitHub.
3. .env.example shows which keys are needed, without values.
4. Code reads secrets at runtime with os.getenv().
5. Printing a masked value proves the key loaded without leaking it.
```

## What happens if `.env` is missing

Rename or delete `.env` and run the script again. Instead of crashing with a
stack trace, it explains exactly what to do:

```text
No .env file found; checking system environment variables.

Missing required setting(s): API_KEY, DATABASE_URL
Fix it by creating your own .env file from the template:
    Windows:     copy .env.example .env
    macOS/Linux: cp .env.example .env
Then replace the placeholder values with your own.
```

The script exits with code `1`, which lets scripts and CI systems detect the
failure.

## How it works

| Piece | Role |
| --- | --- |
| `load_dotenv()` | Reads `.env` and copies its values into the process environment |
| `os.getenv("API_KEY")` | Reads a value by name; returns `None` if missing |
| `os.getenv("APP_ENV", "development")` | Returns a default when the key is absent |
| `mask()` | Shows a few characters so you can verify the key without leaking it |
| `.gitignore` | Prevents `.env` and its variants from being committed |

`load_dotenv()` does **not** overwrite variables that already exist in the
operating system, so real deployment settings always win over the local file.

## Why hardcoding secrets is dangerous

```python
# NEVER do this:
API_KEY = "sk-live-9f8a7b6c5d4e3f2a1b"   # now in your Git history forever
```

- **Git remembers.** Deleting the line later does not remove it from history.
- **Repositories get shared.** Forks, mirrors, laptops, and CI logs all copy it.
- **Bots scan for keys.** Public commits with secrets are found within minutes.
- **Rotation is painful.** A leaked key must be revoked and replaced everywhere.

If a secret does leak, treat it as compromised: revoke it, create a new one, and
remove it from history (for example with `git filter-repo`).

## Verify Git is ignoring `.env`

From the repository root:

```bash
git check-ignore -v my_secure_project/.env
```

It prints the exact rule that protects the file:

```text
my_secure_project/.gitignore:4:.env	my_secure_project/.env
```

To confirm the template is **not** ignored, run the command **without** `-v`; it
should print nothing (exit code `1` means "not ignored"):

```bash
git check-ignore my_secure_project/.env.example
```

A dry-run add is another good check. It lists what Git would stage, and `.env`
must not appear:

```bash
git add -n my_secure_project/
```

```text
add 'my_secure_project/.env.example'
add 'my_secure_project/.gitignore'
add 'my_secure_project/README.md'
add 'my_secure_project/main.py'
```

> Tip: `git check-ignore -v .env.example` also prints the negating rule
> `!.env.example`. That line is what keeps the template tracked, so it is
> expected; the plain command above is the clearer test.

## Best practices checklist

1. Keep every secret in `.env`, never in `.py` files.
2. Add `.env` to `.gitignore` before you create it.
3. Commit `.env.example` with placeholders only.
4. Never print a full secret; mask it or print only its length.
5. Never paste secrets into issues, chats, screenshots, or logs.
6. Use different keys for development and production.
7. In production, prefer a secret manager (AWS Secrets Manager, Azure Key Vault,
   HashiCorp Vault, GitHub Actions secrets) over a `.env` file.
8. Add `.env` to your Docker ignore file too, so it never enters an image.
9. Rotate any key that may have been exposed.
10. Remember that `.env` is convenience, not encryption: anyone with file access
    can read it.

## Troubleshooting

| Problem | Fix |
| --- | --- |
| `ModuleNotFoundError: No module named 'dotenv'` | `uv pip install python-dotenv` or `python -m pip install python-dotenv` |
| `Missing required setting(s): API_KEY` | Create `.env` from `.env.example` and fill in values |
| Values are not loaded | Make sure `.env` sits in the same folder you run `python main.py` from |
| `git status` shows `.env` | Confirm `.gitignore` contains `.env` and you are in the project folder |
| An old value keeps appearing | A system environment variable may override `.env`; check your OS settings |

## Try it yourself

1. **Trigger the error path.** Rename `.env` to `.env.backup`, run the script,
   and read the friendly message. Rename it back afterward.
2. **Add a new setting.** Add `WEATHER_API_KEY=abc123` to both `.env` and
   `.env.example`, then read it in `main.py` with `os.getenv`.
3. **Prove the ignore works.** Run `git check-ignore -v .env` and compare it with
   `git check-ignore .env.example` (the second should print nothing).
4. **Use the key in a request.** Combine this with the `api_demo` project and
   send the key in an `Authorization` header instead of printing it.
5. **Practice rotation.** Change `API_KEY` in `.env`, rerun, and confirm the
   masked output changes.

## Files

| File | Purpose |
| --- | --- |
| `.env` | Real local secrets (ignored by Git) |
| `.env.example` | Safe template committed to Git |
| `.gitignore` | Keeps `.env` and caches out of Git |
| `main.py` | Loads secrets and uses them without exposing them |
| `README.md` | This guide |

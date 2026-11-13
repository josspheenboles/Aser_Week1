# Network Error Demo

A beginner-friendly script that shows how to keep network code from crashing
when servers fail, connections drop, or replies are slow.

It uses the `requests` library and a `try` / `except` / `else` / `finally`
structure to handle four common failure modes gracefully.

## Requirements

- Python 3.9 or newer
- The `requests` library
- An internet connection (the demo deliberately calls some failing endpoints)

## Step 1: Install `requests`

**With `uv` (fast, recommended):**

```bash
uv pip install requests
```

**With standard `pip`:**

```bash
python -m pip install requests
```

If you use a virtual environment (recommended), create and activate it first:

```powershell
uv venv
.\.venv\Scripts\Activate.ps1
uv pip install requests
```

On macOS or Linux, activate with `source .venv/bin/activate`.

## Step 2: Run the demo

From inside the `network_demo` folder:

```bash
cd network_demo
python network_error_demo.py
```

If `python` is not found, try `py network_error_demo.py` on Windows or
`python3 network_error_demo.py` on macOS/Linux.

## Step 3: What the output means

Every request prints a `[tag]` showing which `except` block handled it:

```text
================================================================
=== Scenario 2: Timeout (slow server) ===
================================================================
httpbin.org/delay/5 waits 5 seconds, but we only allow 2.
  Requesting: https://httpbin.org/delay/5
  Timeout: 2.0 seconds
  [Timeout] The server did not reply within 2.0 seconds.
  Try again later, or allow a longer timeout.
  [finally] Done handling this request.

================================================================
=== Scenario 3: HTTP Status Errors ===
================================================================
3a. A missing resource answers 404 Not Found:
  Requesting: https://httpbin.org/status/404
  Timeout: 5.0 seconds
  [HTTPError] The server answered with status 404.
  That usually means the request or URL was wrong.
  [finally] Done handling this request.

3b. A broken endpoint answers 500 Server Error:
  Requesting: https://httpbin.org/status/500
  Timeout: 5.0 seconds
  [HTTPError] The server answered with status 500.
  That usually means the server itself had a problem.
  [finally] Done handling this request.
```

| `[tag]` | Exception caught | When it happens |
| --- | --- | --- |
| `[ConnectionError]` | `requests.exceptions.ConnectionError` | Domain cannot be reached: no internet, wrong host, server offline |
| `[Timeout]` | `requests.exceptions.Timeout` | Server did not answer within `timeout` seconds |
| `[HTTPError]` | `requests.exceptions.HTTPError` | Server answered `4xx` or `5xx` after `raise_for_status()` |
| `[RequestException]` | `requests.exceptions.RequestException` | Any other request problem (bad URL, SSL, redirects, ...) |
| `[Success]` | none | Request worked and returned `200 OK` |

## The four scenarios

| Scenario | Endpoint used | Exception demonstrated |
| --- | --- | --- |
| 1. Connection error | `https://this-domain-should-not-exist-abc123.invalid` | `ConnectionError` |
| 2. Timeout | `https://httpbin.org/delay/5` with `timeout=2.0` | `Timeout` |
| 3a. 404 | `https://httpbin.org/status/404` | `HTTPError` |
| 3b. 500 | `https://httpbin.org/status/500` | `HTTPError` |
| 4. Catch-all | `not-a-real-url` (no scheme) | `RequestException` (`MissingSchema`) |
| Bonus | `https://httpbin.org/json` | no error, `else` branch runs |

## The `try` / `except` / `else` / `finally` pattern

```python
try:
    response = requests.get(url, timeout=5.0)   # the network call
    response.raise_for_status()                 # turn 4xx/5xx into HTTPError
except requests.exceptions.ConnectionError:
    print("Network connection failed.")         # cannot reach the server
except requests.exceptions.Timeout:
    print("The server was too slow.")
except requests.exceptions.HTTPError as error:
    print(f"Server answered {error.response.status_code}.")
except requests.exceptions.RequestException as error:
    print(f"Something else went wrong: {error}")  # safety net
else:
    print("Success!")                           # only when nothing failed
finally:
    print("Request finished.")                  # always runs
```

Why each part exists:

- **`try`** wraps the code that might fail. Network calls always belong here.
- **`except`** blocks catch specific errors first, then the broad
  `RequestException` as a net. Order matters: put specific classes first.
- **`else`** runs only on success, so `.json()` and other "happy path" code
  stays separate from the error handling.
- **`finally`** always runs, error or not. Use it to close files, stop timers,
  or write logs.

## Key exception classes every Python developer should know

All of these live in `requests.exceptions` and inherit from
`RequestException`, which inherits from Python's `OSError` (also called
`IOError`).

| Exception | Meaning |
| --- | --- |
| `RequestException` | Base class for every `requests` error. The catch-all. |
| `ConnectionError` | Could not connect: no internet, DNS failure, server down. |
| `Timeout` | No answer in time. Subclasses: `ConnectTimeout`, `ReadTimeout`. |
| `HTTPError` | A `4xx` or `5xx` status, raised by `response.raise_for_status()`. |
| `TooManyRedirects` | The redirect loop never ended. |
| `MissingSchema` | The URL has no `http://` or `https://`. |
| `InvalidSchema` | The scheme is not supported, such as `htp://`. |
| `InvalidURL` | The URL is malformed. |
| `SSLError` | The secure connection failed (certificate or handshake problem). |
| `JSONDecodeError` | `response.json()` was called on a body that is not JSON. |

> Note: `response.raise_for_status()` only raises `HTTPError`. A `404` by itself
> does **not** raise anything — without that line, a missing page looks like a
> successful request.

## Best practices

1. **Always set a `timeout`.** Without one, a request can hang forever.
2. **Call `raise_for_status()`** so bad status codes become exceptions.
3. **Catch specific errors before the broad one**, so you can give a useful
   message for each case.
4. **Never show a raw stack trace** to a normal user. Print a friendly message.
5. **Keep `else` for success** and `finally` for cleanup.
6. **Add retries with a short delay** for temporary failures in real apps
   (for example, using `urllib3.util.Retry` or a simple loop).
7. **Log the technical detail, show a simple message.** Users see the friendly
   line; your log keeps the exception for debugging.

## Troubleshooting

| Problem | Fix |
| --- | --- |
| `ModuleNotFoundError: No module named 'requests'` | `uv pip install requests` or `python -m pip install requests` |
| Every scenario prints `[ConnectionError]` | You are offline or a firewall blocks the demo endpoints |
| Scenario 2 does not time out | Your network is unusually slow to `httpbin.org`; try again |
| Scenario 3 shows a connection error instead of `[HTTPError]` | The demo host is temporarily unreachable; retry |
| SSL errors in scenario 1 | Some networks intercept unknown domains; the catch-all still handles it |

## Try it yourself

1. **Change the timeout.** Set scenario 2 to `timeout=1.0` and confirm it still
   raises `Timeout`, then try a very large value and watch it succeed.
2. **Add a retry.** Wrap `safe_get` in a `for attempt in range(3)` loop that
   retries after a failure.
3. **Test `raise_for_status()`.** Remove that one line and rerun scenario 3:
   the `404` now looks like a success because the status is not checked.
4. **Add a new scenario.** Call a URL with an unknown scheme such as
   `htp://example.com` and see which exception is raised.
5. **Show the raw error.** Temporarily add `except RequestException as error:
   raise` to see the stack trace that your friendly messages are hiding.

## Files

| File | Purpose |
| --- | --- |
| `network_error_demo.py` | The annotated error-handling demo |
| `README.md` | This guide |

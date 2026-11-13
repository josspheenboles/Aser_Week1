# API Caller

A beginner-friendly script that calls a public REST API and turns the JSON
response into normal Python data.

Two free APIs are used, and **neither needs an API key**:

| Part | API | What comes back |
| --- | --- | --- |
| 1 | [Open-Meteo](https://open-meteo.com/) | Current weather in Berlin (a JSON object → a Python `dict`) |
| 2 | [JSONPlaceholder](https://jsonplaceholder.typicode.com/) | A list of todo items (a JSON array → a Python `list`) |

## Requirements

- Python 3.9 or newer
- The `requests` library (installed in the next step)
- An internet connection

Check your Python version:

```bash
python --version
```

## Step 1: Install `requests`

`requests` is not part of the standard library, so install it once.

**With `uv` (fast, recommended):**

```bash
uv pip install requests
```

**With standard `pip`:**

```bash
python -m pip install requests
```

If you are using a virtual environment (recommended), create and activate it
first, then run one of the commands above:

```powershell
uv venv
.\.venv\Scripts\Activate.ps1
uv pip install requests
```

On macOS or Linux, activate with `source .venv/bin/activate` instead.

## Step 2: Run the script

From inside the `api_demo` folder:

```bash
cd api_demo
python api_caller.py
```

If `python` is not found, try `py api_caller.py` on Windows or
`python3 api_caller.py` on macOS/Linux.

## Step 3: Read the output

The script prints four labelled steps for the weather example, then a second
list example, then a summary. Example run (your numbers and time will differ,
because the weather changes):

```text
==============================================================
=== Part 1: Current Weather in Berlin ===
==============================================================
Step 1: Send a GET request
  URL:        https://api.open-meteo.com/v1/forecast
  Parameters: {'latitude': 52.52, 'longitude': 13.41, 'current': 'temperature_2m,wind_speed_10m', 'timezone': 'auto'}

Step 2: Check the HTTP status code
  Status code: 200
  200 means success, so there is data to read.

Step 3: Convert the JSON text into Python data
  Type of weather: dict
  Top-level keys:  ['latitude', 'longitude', 'generationtime_ms', 'utc_offset_seconds', 'timezone', 'timezone_abbreviation', 'elevation', 'current_units', 'current']

Step 4: Extract the fields we want
  Temperature: 8.4 °C
  Wind speed:  21.6 km/h
  Observed at: 2026-11-13T13:45

==============================================================
=== Part 2: A List of Todo Items ===
==============================================================
Send a GET request, then let raise_for_status() check the code.
  URL:        https://jsonplaceholder.typicode.com/todos
  Parameters: {'_limit': 5}
  Status code: 200
  Type of todos: list
  Number of items: 5

  [ ] 1: delectus aut autem
  [ ] 2: quis ut nam facilis et officia qui
  [ ] 3: fugiat veniam minus
  [x] 4: et porro tempora
  [ ] 5: laboriosam mollitia et enim quasi adipisci quia provident illum
```

### What each part of the output represents

1. **Step 1 — the request.** `requests.get()` sends an **HTTP request** to the
   server. `params` is a dictionary that `requests` turns into the
   `?latitude=52.52&longitude=13.41...` part of the URL.
2. **Step 2 — the status code.** The server answers with a number:
   - `200` means **OK**, the request succeeded.
   - `4xx` means **the request was wrong** (for example, `404` = not found).
   - `5xx` means **the server had a problem**.
   The script stops early if the code is not `200`.
3. **Step 3 — JSON to Python.** The response body is JSON text. `response.json()`
   converts it:
   - JSON `{ "key": "value" }` becomes a Python **dictionary**.
   - JSON `[ ... ]` becomes a Python **list**.
   The printed `Type of weather: dict` and `Type of todos: list` show this.
4. **Step 4 — extract fields.** The script reads nested values with square
   brackets, such as `weather["current"]["temperature_2m"]`, and prints them in
   a readable sentence.

The `[x]` and `[ ]` markers in Part 2 are built from the `completed` boolean on
each todo item.

## How the code handles problems

| Situation | What the script does |
| --- | --- |
| No internet, DNS failure, or timeout | `except requests.exceptions.RequestException` prints a friendly message and exits |
| Server returns `404` or `500` | Part 1 checks `status_code`; Part 2 uses `response.raise_for_status()` |
| Response is not JSON (for example, an HTML error page) | `except requests.exceptions.JSONDecodeError` stops cleanly |

`raise_for_status()` is a shortcut that raises an exception for any `4xx` or
`5xx` code, so you do not have to write an `if` statement yourself.

## Bonus: GET one resource by ID

`get_by_id_demo.py` shows the most common REST pattern: put the id in the URL
path to fetch one specific resource.

```bash
python get_by_id_demo.py       # tries ids 1, 3, and 9999
python get_by_id_demo.py 5     # tries the id you pass in
```

Example output:

```text
==============================================================
=== GET by ID Demo ===
==============================================================
The id is part of the URL path: /users/<id>
Looking up ids: [1, 3, 9999]

--- User id 1 ---
  Request: GET https://jsonplaceholder.typicode.com/users/1
  Status code: 200
  Name:     Leanne Graham
  Username: Bret
  Email:    Sincere@april.biz
  City:     Gwenborough
  Company:  Romaguera-Crona

--- User id 9999 ---
  Request: GET https://jsonplaceholder.typicode.com/users/9999
  Status code: 404
  No user exists with id=9999.
```

Key point: a `404` is **not** an exception. `requests.get()` returns normally,
and you decide what to do by checking `response.status_code`. If you would
rather have `4xx`/`5xx` raise an error, call `response.raise_for_status()`.

The script also reads nested fields such as `user["address"]["city"]` and
accepts an optional command-line id, so `python get_by_id_demo.py 5` looks up
user 5 only.

## Troubleshooting

| Problem | Fix |
| --- | --- |
| `ModuleNotFoundError: No module named 'requests'` | Install it: `uv pip install requests` or `python -m pip install requests` |
| `Could not reach the API` | Check your internet connection, VPN, or firewall |
| The request hangs | The script already sets `timeout=10`; increase it if your connection is slow |
| `SSL: CERTIFICATE_VERIFY_FAILED` | Update `certifi` (`uv pip install --upgrade certifi`) or check your system certificates |
| `429 Too Many Requests` | You are calling the API too often; wait a moment and retry |
| Weird characters instead of `°C` | The script requests UTF-8 output; if your terminal still struggles, the weather value itself is correct |

## Try it yourself

1. **Change the city.** Replace `latitude` and `longitude` in `weather_params`
   with coordinates for your town. Open-Meteo has a free geocoding API at
   `https://geocoding-api.open-meteo.com/v1/search?name=YourCity`.
2. **Ask for more weather.** Add fields to the `current` parameter, such as
   `relative_humidity_2m` or `weather_code`, then print them in Step 4.
3. **Change the list size.** Set `todo_params = {"_limit": 10}` and watch
   `len(todos)` grow.
4. **Filter the list.** Only print items where `todo["completed"]` is `True`.
5. **Try another endpoint.** Call
   `https://jsonplaceholder.typicode.com/users/1` and print the nested
   `address` dictionary.
6. **See a failure on purpose.** Change the weather URL to a path that does not
   exist, or turn off Wi-Fi, and confirm the error handling works.

## Files

| File | Purpose |
| --- | --- |
| `api_caller.py` | The annotated API demo (weather + todo list) |
| `get_by_id_demo.py` | GET one resource by id, including the 404 case |
| `README.md` | This guide |

## Key vocabulary

- **API:** a service your program can talk to over the internet.
- **Endpoint:** the specific URL you call, such as `/v1/forecast`.
- **HTTP GET:** the request type used to read data.
- **Query parameters:** extra `key=value` details added to the URL.
- **Status code:** the server's numeric summary of the result (`200` = OK).
- **JSON:** a text format for data that maps cleanly onto Python dicts and lists.
- **Timeout:** the maximum time to wait before giving up.

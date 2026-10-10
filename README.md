# Python Examples

Topics are learned in the order below.

## 1. Exception Handling

- Errors at runtime crash the program unless handled
- `try` / `except` catches specific errors like `ValueError`
- `else` and `finally` run on success / always

Files: [exception-demo.py](exception-demo.py) → [exception.py](exception.py) → [exception-full.py](exception-full.py)

## 2. File Handling

- `open()` with `read` / `write` modes
- Handle missing files using `try` / `except` / `finally`
- `with` closes files automatically, no `finally` needed

Files: [file-read.py](file-read.py) → [file-except.py](file-except.py) → [file-with.py](file-with.py) → [file-write.py](file-write.py)

## 3. Built-in Modules

- `import` brings ready-made code into your program
- `math` provides `sqrt`, `ceil`, `floor`, `pi`
- `random` provides `randint` and `choice`

Files: [built-in-module.py](built-in-module.py)

## 4. CSV

- `csv` module reads comma-separated rows from files
- `DictReader` gives each row as a dictionary

Files: [csv-read.py](csv-read.py)

## 5. JSON

- `json` module handles JSON data
- `json.load()` turns a JSON file into a dictionary

Files: [json-read.py](json-read.py)

## 6. Virtual Environment (venv)

- Isolated folder holding libraries for one project
- Create once, activate every new terminal session

```bat
python -m venv .venv
.venv\Scripts\activate
deactivate
```

## 7. pip

- `pip` installs third-party libraries, not built into Python
- Activate the venv first, then install

```bat
pip install pypdf openpyxl
```

## 8. PDF

- `pypdf` reads text from PDF files
- `reader.pages[0]` is the first page

Files: [pdf-read.py](pdf-read.py)

## 9. Excel

- `openpyxl` reads Excel files (`.xlsx`)
- `iter_rows()` limits rows and columns read

```bat
pip install openpyxl
```

Files: [excel-read.py](excel-read.py)

## 10. Pandas

- One call reads Excel, CSV, JSON into a DataFrame
- Filter, sort, summarize columns without writing loops
- Handles missing values and large data easily

```bat
pip install pandas openpyxl
```

Files: [pandas-read.py](pandas-read.py)

## 11. Requests (HTTP)

- `requests.get()` fetches data from a web URL
- `status_code` 200 means success
- `response.json()` converts the reply into a dictionary

```bat
pip install requests
```

Files: [http-request.py](http-request.py)

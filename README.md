# Python Web Project

A minimal FastAPI-based Python web project starter.

## Project Structure

```text
.
|-- app/
|   |-- __init__.py
|   |-- main.py
|   `-- routes.py
|-- tests/
|   |-- __init__.py
|   `-- test_main.py
|-- .env.example
|-- .gitignore
`-- requirements.txt
```

## Requirements

- Python 3.10+

## Quick Start

1. Create a virtual environment

```bash
python -m venv .venv
```

2. Activate the virtual environment

PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Start the development server

```bash
uvicorn app.main:app --reload
```

5. Open the API docs

- Swagger UI: <http://127.0.0.1:8000/docs>
- ReDoc: <http://127.0.0.1:8000/redoc>

## Run Tests

```bash
pytest
```

## Next Steps

- Add configuration management
- Connect a database and ORM
- Add logging, auth, and middleware
- Split routes by business domain

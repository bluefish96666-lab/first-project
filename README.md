# Python Web Project

A minimal FastAPI-based Python web project starter.

## Project Structure

```text
.
|-- app/
|   |-- __init__.py
|   |-- config.py
|   |-- logging_config.py
|   |-- main.py
|   |-- middleware.py
|   `-- routes.py
|-- .github/
|   `-- workflows/
|       `-- ci.yml
|-- tests/
|   |-- __init__.py
|   `-- test_main.py
|-- .dockerignore
|-- .env.example
|-- .gitignore
|-- docker-compose.yml
|-- Dockerfile
|-- pyproject.toml
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

## Environment Variables

You can copy `.env.example` to `.env` and adjust values as needed.

- `APP_NAME`: FastAPI app title
- `APP_ENV`: runtime environment such as `development` or `production`
- `APP_HOST`: host for local runs
- `APP_PORT`: port for local runs
- `LOG_LEVEL`: Python log level such as `INFO` or `DEBUG`

If you want to install the app as a local package for development:

```bash
pip install -e .[dev]
```

## Run With Docker

```bash
docker compose up --build
```

The app will be available at <http://127.0.0.1:8000>.

## CI

This project includes a GitHub Actions workflow that runs tests on pushes and pull requests.

## Next Steps

- Add configuration management
- Connect a database and ORM
- Add logging, auth, and middleware
- Split routes by business domain

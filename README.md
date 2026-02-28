# api-flask-sqlalchemy

A small RESTful API built with Flask, Flask-RESTful and SQLAlchemy.

This repository contains a minimal example application demonstrating how to
structure a Flask API that uses SQLAlchemy for data persistence. It is
intended as a learning and reference project for developers who want a simple
starting point for building REST APIs in Python.

**Contents**

- **Features:** REST endpoints, SQLAlchemy models, simple project layout.
- **Tech stack:** Python, Flask, Flask-RESTful, SQLAlchemy.

## Features

- Example CRUD endpoints for a resource using Flask-RESTful.
- SQLAlchemy models with a simple SQLite configuration (development).
- Small, easy-to-read codebase suitable for learning and quick demos.

## Requirements

- Python 3.8+
- The dependencies listed in `dev_flask/requirements.txt`.

Install dependencies using pip (preferably inside a virtual environment):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r dev_flask/requirements.txt
```

## Running the app (development)

From the repository root run:

```bash
export FLASK_APP=dev_flask/app.py
export FLASK_ENV=development
flask run
```

By default the server will be available at `http://127.0.0.1:5000`.

## Project layout

- `dev_flask/app.py` — application entry and route registrations.
- `dev_flask/models.py` — SQLAlchemy model definitions.
- `dev_flask/utils.py` — helper utilities used by the application.
- `dev_flask/requirements.txt` — Python dependencies for the example app.

## Example usage

Assuming the server is running, you can use `curl` or an HTTP client to
interact with the API. Example (replace `/resource` with the actual endpoint
provided by the app):

Create:

```bash
curl -X POST -H "Content-Type: application/json" \
	-d '{"name": "Example"}' http://127.0.0.1:5000/resource
```

Get list:

```bash
curl http://127.0.0.1:5000/resource
```

Get item:

```bash
curl http://127.0.0.1:5000/resource/1
```

Update:

```bash
curl -X PUT -H "Content-Type: application/json" \
	-d '{"name": "Updated"}' http://127.0.0.1:5000/resource/1
```

Delete:

```bash
curl -X DELETE http://127.0.0.1:5000/resource/1
```

## Next steps and customization

- Replace the example SQLite configuration with PostgreSQL or another
  production-grade database.
- Add authentication, input validation and error handling for production use.
- Add automated tests and CI configuration.

## Contributing

Contributions are welcome. Open an issue or submit a pull request with a
description of the change.

## License

See the repository `LICENSE` file for license information.

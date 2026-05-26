# fastapi-mongodb-starter
![Python3.13](https://img.shields.io/badge/Python-3.13-brightgreen.svg?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-latest-brightgreen.svg?style=flat-square)
![Beanie](https://img.shields.io/badge/Beanie-2.x-brightgreen.svg?style=flat-square)

## Introduction
A minimal backend starter for building APIs with [FastAPI](https://fastapi.tiangolo.com/), [Beanie](https://beanie-odm.dev/) (async ODM built on Motor), and [MongoDB](https://www.mongodb.com/).

## Project structure
```
app/
├── conf/       # Configuration and logging setup
├── models/     # Beanie document models
├── routers/    # FastAPI routers
├── schemas/    # Pydantic request/response schemas
├── utils/      # Utility helpers
└── main.py     # App entrypoint
tests/          # Integration tests (require a running server)
```

## Prerequisites
- Python 3.13
- make
- A MongoDB instance (local or [MongoDB Atlas](https://www.mongodb.com/atlas))

## Installation
1. Copy and fill in the environment file:
   ```sh
   cp env.sample .env
   ```
   Set `MONGO_URI`, `MONGO_DB`, `BACKEND_NAME`, and `BACKEND_VERSION`.

2. Create a virtual environment and install dependencies:
   ```sh
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Getting Started

Available make commands:
```sh
make help     # list all commands
make install  # create virtualenv and install dependencies
make dev      # run development server with auto-reload
make test     # run integration tests (requires running server)
make build    # build Docker image
make run      # run app via Docker
```

### Run locally
```sh
make dev
```
API available at `http://localhost:8000` — interactive docs at `http://localhost:8000/docs`.

### Run with Docker
```sh
make build
make run
```

## Tests
Integration tests — require the app to be running first:
```sh
make test
```

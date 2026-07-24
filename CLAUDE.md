# fastapi-mongodb-starter — Claude Code context

Minimal FastAPI + Beanie + MongoDB API starter. Serves on `:8000`, interactive docs
at `/docs`.

## Commands

```bash
make help
make install    # virtualenv + dependencies
make dev        # development server with auto-reload
make test       # integration tests — require the app already running
make build      # Docker image
make run        # run via Docker
```

## Layout

```
app/conf/      configuration and logging setup
app/models/    Beanie document models
app/routers/   FastAPI routers
app/schemas/   Pydantic request/response schemas
app/utils/     helpers
app/main.py    entrypoint
tests/         integration tests
```

## Environment

`MONGO_URI`, `MONGO_DB`, `BACKEND_NAME`, `BACKEND_VERSION` — see `env.sample`.

## Note

Tests are integration tests against a live server, not unit tests: start the app
first, then `make test`.

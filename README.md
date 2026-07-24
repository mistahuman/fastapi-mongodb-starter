# fastapi-mongodb-starter

Minimal backend starter for REST APIs on FastAPI and MongoDB, using Beanie as the
async ODM.

## Stack

Python 3.13 · FastAPI · Beanie 2.x · MongoDB

## Run

```bash
cp env.sample .env
make install     # virtualenv + dependencies
make dev         # -> http://localhost:8000, docs at /docs
```

Or containerised:

```bash
make build
make run
```

## Configuration

| Var | What |
|---|---|
| `MONGO_URI` | Connection string (local or Atlas) |
| `MONGO_DB` | Database name |
| `BACKEND_NAME` | Application name |
| `BACKEND_VERSION` | Application version |

## License

MIT

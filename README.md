# FastAPI + Sapper

This project is an attempt to create a nice DX with Sapper and FastAPI. It is one repo with
a frontend and backend. In `DEBUG` the FastAPI uvicorn development server (port 8000) receives
all requests and proxies directly to Sapper (port 3000) unless there are FastAPI routes
defined.

In non-`DEBUG` mode a static server serves from `__sapper__/export` instead.

Sapper has Tailwind CSS configured.

FastAPI uses SQLite for data.

## Start

```bash
yarn install
poetry install
```

Start dev servers

```bash
yarn run dev  # in tab 1
DEBUG=true poetry run uvicorn api:app --host 0.0.0.0 --reload-dir api  # in tab 2
```

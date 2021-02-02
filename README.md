# FastAPI + Sapper

This project is an attempt to create a nice DX with Sapper and FastAPI. It is
one repo with a frontend and backend. In `DEBUG` the FastAPI uvicorn development
server (port 8000) receives all requests and proxies directly to Sapper (port 3000) unless there are FastAPI routes defined.

In non-`DEBUG` mode a static server serves from `__sapper__/export` instead.

Sapper has Tailwind CSS configured.

FastAPI uses SQLite for data.

## Start

Create an `.env` file like this:

```
FRONTEND_URL=http://localhost:3000
API_HOST=localhost:8000
API_URL=http://localhost:8000/api
DATABASE_URL=sqlite:///./database.db
```

```bash
yarn install
poetry install
```

Start dev servers

```bash
yarn run dev  # in tab 1
DEBUG=true poetry run uvicorn api:app --host 0.0.0.0 --reload-dir api  # in tab 2
```

## Deploying

Have a look at `render.yaml` - it gives you the environment variables, disks and
build/start commands. Again, in production you get a static build with a
minimized Parcel bundle, purged Tailwind etc.

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

from .config import DEBUG
from .database import engine
from .endpoints import app as api_app
from .proxy import frontend_proxy

app = FastAPI()
app.mount("/api", api_app)


@app.get("/_db")
def download_sqlite_db():
    return FileResponse(
        engine.url.database,
        headers={"content-disposition": 'attachment; filename="sqlite.db"'},
        media_type="application/x-sqlite3",
    )


if DEBUG:
    app.mount("/", frontend_proxy)
else:
    app.mount("/", StaticFiles(directory="build", html=True), name="static")

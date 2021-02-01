from typing import List, Optional

from asgiproxy.config import BaseURLProxyConfigMixin, ProxyConfig
from asgiproxy.context import ProxyContext
from asgiproxy.proxies.http import proxy_http
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from starlette.config import Config

from . import models

config = Config(".env")

DEBUG = config("DEBUG", cast=bool, default=False)

engine = create_engine(
    config("DATABASE_URL"), connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class ProxyConfig(BaseURLProxyConfigMixin, ProxyConfig):
    upstream_base_url = config("FRONTEND_URL", default=None)
    rewrite_host_header = config("API_HOST", default=None)


context = ProxyContext(config=ProxyConfig())


async def frontend_proxy(scope, receive, send):
    return await proxy_http(context=context, scope=scope, receive=receive, send=send)


app = FastAPI()


class GuestSchema(BaseModel):
    name: str
    diet: models.DietChoices


class ResponseSchema(BaseModel):
    phone: int
    email: str
    comment: Optional[str] = None
    guests: List[GuestSchema]


@app.get("/_create_tables")
def _create_tables():
    models.Base.metadata.create_all(bind=engine)
    return ""


@app.get("/responses", response_model=List[ResponseSchema])
def get_responses(db: Session = Depends(get_db)):
    return db.query(models.Response).all()


@app.get("/responses/{phone}", response_model=ResponseSchema)
def read_response(phone: int, db: Session = Depends(get_db)):
    return {"name": "Laptop", "price": 1.0}


@app.post("/responses", response_model=ResponseSchema)
def create_response(response: ResponseSchema, db: Session = Depends(get_db)):
    db_response = models.Response(**response.dict())
    db.add(db_response)
    db.commit()
    return db_response


if DEBUG:
    app.mount("/", frontend_proxy)
else:
    app.mount("/", StaticFiles(directory="__sapper__/export", html=True), name="static")

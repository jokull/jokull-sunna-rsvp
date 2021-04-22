from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from . import models, schemas
from .database import engine, get_db

app = FastAPI()


async def _get_response(db: AsyncSession, email: str) -> Optional[models.Response]:
    stmt = select(models.Response).where(models.Response == email)
    return (await db.execute(stmt)).scalars().first()


@app.get("/responses", response_model=List[schemas.DatabaseResponse])
async def get_responses(db: AsyncSession = Depends(get_db)):
    stmt = (
        select(models.Response)
        .order_by(models.Response.created.desc())
        .options(selectinload(models.Response.guests))
    )
    result = await db.execute(stmt)
    return result.scalars().all()


@app.get("/responses/{email}", response_model=schemas.DatabaseResponse)
async def read_response(email: str, db: AsyncSession = Depends(get_db)):
    db_response = await _get_response(db, email)
    if db_response is None:
        return HTTPException(404)
    return db_response


@app.post("/responses", response_model=schemas.DatabaseResponse)
async def create_response(
    response: schemas.Response, db: AsyncSession = Depends(get_db)
):
    email = response.email.strip().lower()
    db_response = await _get_response(db, email)
    if db_response is None:
        db_response = models.Response(email=email, comment=response.comment or None)
    else:
        db_response.comment = response.comment or None
        for guest in db_response.guests or []:
            db.delete(guest)
    db.add(db_response)
    for guest in response.guests:
        db.add(models.Guest(name=guest.name, diet=guest.diet, response_email=email))
    await db.commit()
    await db.refresh(db_response)
    return db_response


@app.get("/_reset")
def reset(db: AsyncSession = Depends(get_db)):
    with engine.begin() as conn:
        conn.run_sync(models.Base.metadata.drop_all)
        conn.run_sync(models.Base.metadata.create_all)

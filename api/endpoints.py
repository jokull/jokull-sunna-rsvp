from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from . import models, schemas
from .database import get_db

app = FastAPI()


async def _get_response(db: AsyncSession, email: str) -> Optional[models.Response]:
    stmt = (
        select(models.Response)
        .where(models.Response.email == email)
        .options(selectinload(models.Response.guests))
    )
    return (await db.execute(stmt)).scalars().first()


@app.get("/responses", response_model=List[schemas.DatabaseResponse])
async def get_responses(db: AsyncSession = Depends(get_db)):
    stmt = (
        select(models.Response)
        .order_by(models.Response.deleted, models.Response.created.desc())
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


@app.post("/responses/{email}", response_model=schemas.DatabaseResponse)
async def update_response(
    email: str, response: schemas.ResponseUpdate, db: AsyncSession = Depends(get_db)
):
    db_response = await _get_response(db, email)
    if db_response is None:
        return HTTPException(404)
    if response.deleted:
        db_response.deleted = func.now()  # type: ignore
    else:
        db_response.deleted = None
    db.add(db_response)
    await db.commit()
    await db.refresh(db_response)
    return db_response


async def _delete_guests(db: AsyncSession, response: models.Response) -> None:
    for guest in response.guests or []:
        await db.delete(guest)


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
        await _delete_guests(db, db_response)
    db.add(db_response)
    for guest in response.guests:
        db.add(models.Guest(name=guest.name, diet=guest.diet, response_email=email))
    await db.commit()
    await db.refresh(db_response)
    return db_response

from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from . import models, schemas
from .database import get_db, engine


app = FastAPI()


@app.get("/responses", response_model=List[schemas.DatabaseResponse])
def get_responses(db: Session = Depends(get_db)):
    return db.execute(select(models.Response)).scalars().all()


@app.get("/responses/{email}", response_model=schemas.DatabaseResponse)
def read_response(email: str, db: Session = Depends(get_db)):
    db_response = db.query(models.Response).get(email)
    if db_response is None:
        return HTTPException(404)
    return db_response


@app.post("/responses", response_model=schemas.DatabaseResponse)
def create_response(response: schemas.Response, db: Session = Depends(get_db)):
    email = response.email.strip().lower()
    db_response = db.query(models.Response).get(email)
    if db_response is None:
        db_response = models.Response(email=email, comment=response.comment or None)
    else:
        db_response.comment = response.comment or None
        for guest in db_response.guests or []:
            db.delete(guest)
    db.add(db_response)
    for guest in response.guests:
        db.add(models.Guest(name=guest.name, diet=guest.diet, response_email=email))
    db.commit()
    db.refresh(db_response)
    return db_response


@app.get("/_reset")
def reset(db: Session = Depends(get_db)):
    models.Base.metadata.drop_all(engine)
    models.Base.metadata.create_all(engine)

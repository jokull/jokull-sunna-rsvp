from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import get_db


app = FastAPI()


@app.get("/responses", response_model=List[schemas.DatabaseResponse])
def get_responses(db: Session = Depends(get_db)):
    return db.query(models.Response).all()


@app.get("/responses/{phone}", response_model=schemas.DatabaseResponse)
def read_response(phone: int, db: Session = Depends(get_db)):
    db_response = db.query(models.Response).get(phone)
    if db_response is None:
        return HTTPException(404)
    return db_response


@app.post("/responses", response_model=schemas.DatabaseResponse)
def create_response(response: schemas.Response, db: Session = Depends(get_db)):
    db_response = db.query(models.Response).get(response.phone)
    if db_response is None:
        db_response = models.Response(
            phone=response.phone, email=response.email, comment=response.comment or None
        )
    else:
        db_response.email = response.email
        db_response.comment = response.comment or None
        for guest in db_response.guests or []:
            db.delete(guest)
    db.add(db_response)
    db.add_all(
        [
            models.Guest(name=g.name, diet=g.diet, response_phone=response.phone)
            for g in response.guests
        ]
    )
    db.commit()
    db.refresh(db_response)
    return db_response

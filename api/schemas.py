from typing import Optional, Sequence

from pydantic import BaseModel

from .models import DietChoices


class Guest(BaseModel):
    name: str
    diet: DietChoices


class DatabaseGuest(Guest):
    class Config:
        orm_mode = True


class Response(BaseModel):
    email: str
    comment: Optional[str] = None
    guests: Sequence[Guest] = []


class DatabaseResponse(Response):
    guests: Sequence[DatabaseGuest] = []

    class Config:
        orm_mode = True

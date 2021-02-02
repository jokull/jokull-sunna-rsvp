from typing import List, Optional
from pydantic import BaseModel

from .models import DietChoices


class Guest(BaseModel):
    name: str
    diet: DietChoices


class DatabaseGuest(Guest):
    class Config:
        orm_mode = True


class Response(BaseModel):
    phone: int
    email: str
    comment: Optional[str] = None
    guests: List[Guest] = []


class DatabaseResponse(Response):
    guests: List[DatabaseGuest] = []
    class Config:
        orm_mode = True

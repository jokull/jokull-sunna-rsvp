import datetime as dt
import enum
from typing import List, Optional

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class DietChoices(enum.Enum):
    vegan = "vegan"
    pescatarian = "pescatarian"
    meat = "meat"


class Response(Base):
    __tablename__ = "responses"
    created: dt.datetime = Column(DateTime, server_default=func.now(), nullable=False)
    email: str = Column(String, primary_key=True, unique=True)
    comment: Optional[str] = Column(String)
    deleted: Optional[dt.datetime] = Column(DateTime)

    guests: List["Guest"] = relationship(
        "Guest", lazy="joined", back_populates="response"
    )


class Guest(Base):
    __tablename__ = "guests"
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, nullable=False)
    diet: DietChoices = Column(Enum(DietChoices), nullable=False)
    response_email: str = Column(String, ForeignKey(Response.email), nullable=False)

    response: Response = relationship(Response, lazy="joined", back_populates="guests")

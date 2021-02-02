import enum
from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation


Base = declarative_base()


class DietChoices(enum.Enum):
    vegan = "vegan"
    pescatarian = "pescatarian"
    meat = "meat"


class Response(Base):
    __tablename__ = "responses"
    created = Column(DateTime, server_default=func.now())
    phone = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    comment = Column(String)


class Guest(Base):
    __tablename__ = "guests"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    diet = Column(Enum(DietChoices))
    response_phone = Column(Integer, ForeignKey(Response.phone))

    response = relation(Response, backref="guests")

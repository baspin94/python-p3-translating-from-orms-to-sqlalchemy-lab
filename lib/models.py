#!/usr/bin/env python3

from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Dog(Base):
    __tablename__ = "dogs"

    # The solution includes the line below to pass the test.
    __table_args__ = (PrimaryKeyConstraint('id'),)

    # The lab before this one did not demonstrate this workflow for setting a primary key.
    # Instead, it demonstrated adding the primary_key argument to the column itself, like so, which is how I passed the test.
        # id = Column(Integer(), primary_key = True)
    
    id = Column(Integer())
    name = Column(String())
    breed = Column(String())

    # The following method was not necessary to pass the test, but I added it because it's become a habit and makes debugging easier.
    def __repr__(self):
        return f"Dog {self.id}: {self.name} ({self.breed})"




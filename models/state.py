#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")

    else:
        name = ""

        @property
        def cities(self):
            """FileStorage relationship between State and City:
            cities in the same state"""
            from models.city import City
            from models import storage

            results = []
            for key in storage.all(City).values():
                if self.id == City.state_id:
                    results.append(storage.all(City)[key])
            return results

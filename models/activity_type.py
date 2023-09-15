#!/usr/bin/python
""" holds class Activity type"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Activity_Type(BaseModel, Base):
    """Representation of Activity Type"""
    if models.storage_t == 'db':
        __tablename__ = 'activity_type'
          __table_args__ = (
            {'mysql_default_charset': 'latin1'})
        name = Column(String(128), nullable=True)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Activity"""
        super().__init__(*args, **kwargs)

#!/usr/bin/python3
""" BaseModel Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel:
    """ BaseModel for all models """

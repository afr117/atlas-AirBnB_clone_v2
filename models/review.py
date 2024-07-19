#!/usr/bin/python3
""" Review Module for HBNB project """
from models.base_model import BaseModel

class Review(BaseModel):
    """ The review class, contains place ID, user ID, text """
    place_id = ""
    user_id = ""
    text = ""


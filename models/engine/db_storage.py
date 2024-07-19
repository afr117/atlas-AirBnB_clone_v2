#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

class DBStorage:
    """interacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        logging.debug("Initializing DBStorage")
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine(f'mysql+mysqldb://{HBNB_MYSQL_USER}:{HBNB_MYSQL_PWD}@{HBNB_MYSQL_HOST}/{HBNB_MYSQL_DB}')
        if HBNB_ENV == "test":
            logging.debug("Dropping all tables for test environment")
            Base.metadata.drop_all(self.__engine)
        self.__session = None

    def all(self, cls=None):
        """query on the current database session"""
        logging.debug("Fetching all objects from database")
        new_dict = {}
        if self.__session is None:
            raise Exception("Session is not initialized")
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """add the object to the current database session"""
        if self.__session is None:
            raise Exception("Session is not initialized")
        logging.debug(f"Adding new object {obj}")
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        if self.__session is None:
            raise Exception("Session is not initialized")
        logging.debug("Committing changes to the database")
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            if self.__session is None:
                raise Exception("Session is not initialized")
            logging.debug(f"Deleting object {obj}")
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        logging.debug("Reloading database session")
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """
        Removes private session
        """
        logging.debug("Closing session")
        if self.__session:
            self.__session.remove()
            self.__session = None


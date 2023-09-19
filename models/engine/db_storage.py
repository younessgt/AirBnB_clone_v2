#!/usr/bin/python3
""" Module containing DBStorage class instead of Filestorage"""
from os import getenv
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.city import City
from models.user import User
from models.state import State
# from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """ creating the class """
    __engine = None
    __session = None

    def __init__(self):
        """ constructor method """
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        dbase = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                user,
                password,
                host,
                dbase
            ),
            pool_pre_ping=True
        )

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """  Retrieving data for each class from a database."""
        list_class = [State, City, User, Place, Review]
        temp = {}
        if cls:
            list_obj = self.__session.query(cls).all()
            for obj in list_obj:
                key = "{}.{}".format(cls.__name__, obj.id)
                temp[key] = obj
                
        else:

            for elem in list_class:
                list_obj = self.__session.query(elem).all()
                for obj in list_obj:
                    key = "{}.{}".format(elem.__name__, obj.id)
                    temp[key] = obj
                    
        return temp

    def new(self, obj):
        """ Adding  the object to the session"""
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        self.__session.delete(obj)

    def reload(self):
        """ reloading  database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(Session)
        self.__session = session()
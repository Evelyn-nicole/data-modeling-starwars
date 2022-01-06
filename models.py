import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(30), nullable=False)
    lastname = Column(String(30), nullable=False)
    password = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    category = Column(String(30))
    favorite_name = Column(String(30))
    users_id= Column(Integer, ForeignKey('users.id'))
    users = relationship(Users)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    model = Column(String(30))
    manufacturer = Column(String(30))
    passengers= Column(String(30))
    vehicle_class= Column(String(250))
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    favorites = relationship(Users)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    height = Column(Integer)
    birth_year = Column(String(30))
    gender = Column(String(30))
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    favorites = relationship(Users)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    diameter = Column(Integer)
    climate = Column(String(30))
    terrain = Column(String(30))
    population = Column(String(30))
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    favorites = relationship(Favorites)


    def to_dict(self):
        return {}






render_er(Base, 'diagram.png')
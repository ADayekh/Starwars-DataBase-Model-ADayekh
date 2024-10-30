import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(250), unique=True, nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), unique=True, nullable=False)
    first_name = Column(String(250))
    last_name = Column(String(250))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    favorites = relationship("Favorite", backref="user")
                             
class Favorite(Base):
    __tablename__ = 'favorite'
    #Propiedades (ID por tipología)
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    film_id = Column(Integer, ForeignKey('film.id'), nullable=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=True)
    added_at = Column(DateTime, default=datetime.datetime.utcnow)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    diameter = Column(String(250))
    rotation_period = Column(String(250))
    orbital_period = Column(String(250))
    gravity = Column(String(250))
    population = Column(String(250))
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(String(250))
    
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    height = Column(String(250))
    gender = Column(String(250))
    mass = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    homeworld = Column(Integer, ForeignKey('planet.id'))

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    model = Column(String(250)) 
    vehicle_class = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(String(250))
    lenght = Column(String(250))
    crew = Column(String(250))
    passengers = Column(String(250))
    max_atmosphering_speed = Column(String(250))
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))
    pilots = Column(Integer, ForeignKey('character.id'))
    films = Column(Integer, ForeignKey('film.id'))

class Film(Base):
    __tablename__ = 'film'
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(250), nullable=False) 
    episode_id = Column(Integer, nullable=False)
    director = Column(String(250))
    release_date = Column(String(250))
    opening_crawl = Column(String(250))
    character_id =  Column(Integer, ForeignKey('character.id'))
    vehicle_id =  Column(Integer, ForeignKey('vehicle.id'))
    planet_id =  Column(Integer, ForeignKey('planet.id'))
    characters = relationship("Character")
    vehicles = relationship("Vehicle")
    planets = relationship("Planet")
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

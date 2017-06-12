import os
import sys
from sqlalchemy import Column, Integer, ForeignKey, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
	__tablename__ = 'restaurant'
	id = Column(Integer, primary_key=True) 
	name = Column(String(250), nullable=False)

class MenuItem(Base):
	__tablename__ = 'menuitem'
	id = Column(Integer, primary_key=True)
	name = Column(String(250),nullable=False)
	price = Column(String(10))
	description = Column(String(250))
	restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
	restaurant = relationship(Restaurant)

engine = create_engine('sqlite:///restaurantmenu.db')	
Base.metadata.create_all(engine)
from sqlalchemy import Column, Integer, String
from .database import Base

"""this Base is from database connection that is from database.py"""


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)  # id will be generated automatically
    title = Column(String)
    body = Column(String)


class User(Base):  # base means database
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
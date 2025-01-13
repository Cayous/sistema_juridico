from sqlalchemy import Column, Integer, String
from .base import Base  # Corrigido

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    full_name = Column(String)
    password = Column(String)
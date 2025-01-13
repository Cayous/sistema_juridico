from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base  # Corrigido

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    status = Column(String)
    case_id = Column(Integer, ForeignKey('cases.id'))

    case = relationship("Case", back_populates="tasks")
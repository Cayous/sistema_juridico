from .base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

class Case(Base):
    __tablename__ = 'cases'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    status = Column(String)
    created_at = Column(Date)
    updated_at = Column(Date)
    client_id = Column(Integer, ForeignKey('clients.id'))

    client = relationship("Client", back_populates="cases")
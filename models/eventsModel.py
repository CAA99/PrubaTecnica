from sqlalchemy import Column, Enum, Integer, String, Date, Boolean
from database import Base

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    eventType = Column(String, nullable=False)
    description = Column(String)
    date = Column(Date, nullable=False)
    status = Column(String, nullable=False)
    requireManagement = Column(Boolean, nullable=True) 
    isDeleted = Column(Boolean, nullable=False,default=False)
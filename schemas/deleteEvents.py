from pydantic import BaseModel, validator
from typing import Optional
from datetime import date, datetime
from enum import Enum

class StatusEvent(str, Enum):
    Pendiente = "Pendiente"
    Revisado = "Revisado"

class eventType(str, Enum):
    TypeEvent_1 = "Evento Tipo 1"
    TypeEvent_2 = "Evento Tipo 2"
    TypeEvent_3 = "Evento Tipo 3"

class DeleteEvent(BaseModel):
    id : int
    eventType : eventType
    description : str
    date : date
    status : StatusEvent
    requireManagement : Optional[bool] = None 
    isDeleted: bool
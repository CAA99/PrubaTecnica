from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Optional
from enum import Enum

class statusEvent(str, Enum):
    Pendiente = "Pendiente"
    Revisado = "Revisado"

class eventType(str, Enum):
    TypeEvent_1 = "Evento Tipo 1"
    TypeEvent_2 = "Evento Tipo 2"
    TypeEvent_3 = "Evento Tipo 3"

class Event(BaseModel):
    id : int
    eventType : eventType 
    description : str
    date : date
    status : statusEvent
    requireManagement : Optional[bool] = None # pensar si devolverlo ó no 

    class Config:
        use_enum_values = True
from pydantic import BaseModel, validator
from typing import Optional
from datetime import date, datetime
from enum import Enum

class statusEvent(str, Enum):
    Pendiente = "Pendiente"
    Revisado = "Revisado"

class eventType(str, Enum):
    TypeEvent_1 = "Evento Tipo 1"
    TypeEvent_2 = "Evento Tipo 2"
    TypeEvent_3 = "Evento Tipo 3"

class CreateEvent(BaseModel):
    eventType : eventType
    description : str
    date : date
    status : statusEvent
    requireManagement : Optional[bool] = None 

    class Config:
        use_enum_values = True

    @validator("requireManagement", pre=True, always=True)
    def set_requireManagement(cls, requireManagement, values):
        event_type = values.get("eventType")
        if event_type == eventType.TypeEvent_2:
            return None
        return requireManagement
from models.eventsModel import Event
from fastapi import HTTPException
from schemas.createEvent import CreateEvent
#from schemas.events import Event
import pdb

class EventManagmentService():
    def __init__(self, db) -> None:
        self.db = db

    def getEventsNotManagment(self):
        try:
            events = self.db.query(Event).filter(Event.isDeleted==False,).filter(Event.requireManagement==False).filter(Event.status=="Revisado").order_by(Event.id).all()
            print(events)
            return events
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error {str(e)}")

    def getEventsManagment(self):
        try:
            events = self.db.query(Event).filter(Event.isDeleted==False).filter(Event.requireManagement==True).filter(Event.status=="Revisado").order_by(Event.id).all()
            return events
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error {str(e)}")

    def getEventsByStatus(self, status: str):
        try:
            events = self.db.query(Event).filter(Event.isDeleted==False).filter(Event.status==status).filter(Event.status=="Revisado").order_by(Event.id).all()
            return events
        except:
            pass

    def getAll(self):
        try:
            events = self.db.query(Event).filter(Event.isDeleted==False).filter(Event.requireManagement==True).filter(Event.requireManagement==False).filter(Event.status=="Revisado").order_by(Event.id).all()
            return events
        except:
            pass

    def update(self, id: int, RequireManagement: bool):
    
        _event = self.db.query(Event).filter(Event.id == id,
                                             Event.status=="Revisado").first()
        if _event is None:
            raise HTTPException(status_code=404, detail="Evento no encontrado")
        _event.requireManagement = RequireManagement
        self.db.commit()
        updated_event = {
                "eventType": _event.eventType,
                "description": _event.description,
                "date": _event.date,
                "status": _event.status,
                "requireManagement": _event.requireManagement
            }
        return updated_event
        
    def softDelete(self, id:int):
        try:
            _event = self.db.query(Event).filter(Event.id == id,
                                                 Event.status=="Revisado").first()
            _event.isDeleted = True
            self.db.commit()
            return 
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error {str(e)}")
        
    def orderBydate(self, desc : bool):
        try:
            if desc == True:
                events = self.db.query(Event).filter(Event.isDeleted==False).filter(Event.status=="Revisado").order_by(Event.date.desc()).all()
                return events
            else:
                events = self.db.query(Event).filter(Event.isDeleted==False).filter(Event.status=="Revisado").order_by(Event.date.asc()).all()
                return events
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error {str(e)}")
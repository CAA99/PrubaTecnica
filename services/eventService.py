from models.eventsModel import Event
from fastapi import HTTPException
from schemas.createEvent import CreateEvent
class EventService():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_events(self):
        events = self.db.query(Event).filter(Event.isDeleted==False).order_by(Event.id).all()
        return events
    
    def create_event(self, event : CreateEvent):
        try:
            new_event = Event(**event.__dict__)
            self.db.add(new_event)
            self.db.commit()
            return {"message": "Registro creado satisfactoriamente", "event": new_event}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error {str(e)}")
        
    def getEvent_id(self, id: int):
        try:
            event = self.db.query(Event).filter(Event.id == id).first()
            return event
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error {str(e)}")
        
    def updateEvent(self, id: int, event: CreateEvent):
        try:
            _event = self.db.query(Event).filter(Event.id == id).first()
            if _event is None:
                
                raise HTTPException(status_code=404, detail="Evento no encontrado")

            _event.eventType = event.eventType
            _event.description = event.description
            _event.date = event.date
            _event.status = event.status
            _event.requireManagement = event.requireManagement

            self.db.commit()
            updated_event = {
                "eventType": _event.eventType,
                "description": _event.description,
                "date": _event.date,
                "status": _event.status,
                "requireManagement": _event.requireManagement
            }
            return updated_event 
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error {str(e)}")
        
    def softDestroy(self, id: int):
        try:
            _event = self.db.query(Event).filter(Event.id == id).first()
            _event.isDeleted = True
            self.db.commit()
            return 
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error {str(e)}")
from models.eventsModel import Event
from fastapi import HTTPException
from schemas.createEvent import CreateEvent

class EventDeleteService():
    def __init__(self, db) -> None:
        self.db = db
    
    def getDeleteEvents(self):
        try:
            events = self.db.query(Event).filter(Event.isDeleted==True).order_by(Event.id).all()
            return events
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error {str(e)}")
        
    def restoreEvent(self, id : int):
        _event = self.db.query(Event).filter(Event.id == id).filter(Event.isDeleted==True).first()
        if not _event: 
            raise HTTPException(status_code=404, detail="Evento no encontrado")
        _event.isDeleted = False
        self.db.commit()
        return _event

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemas.deleteEvents import DeleteEvent
from schemas.events import Event
from schemas.createEvent import CreateEvent, StatusEvent
from services.eventDeleteService import EventDeleteService
from database import Session
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
eventDeleted = APIRouter()

@eventDeleted.get('/events/deleted', tags=['Events was deleted'])
async def get_Events() -> list[DeleteEvent]:
    try:
        db = Session()
        result = EventDeleteService(db).getDeleteEvents()
        return jsonable_encoder(result)
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})


@eventDeleted.put('/event/restore/{id}', tags=['Events was deleted'])
async def restore_event(id : int) -> Event:
    try:
        db = Session()
        result = EventDeleteService(db).restoreEvent(id)
        return JSONResponse(status_code=201, content={"mensaje":"se ha restaurado el evento"})
    except HTTPException as http_exc:
        return JSONResponse(status_code=http_exc.status_code, content={"error": http_exc.detail})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

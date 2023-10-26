from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemas.events import Event
from schemas.createEvent import CreateEvent
from services.eventService import EventService 
from database import Session
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import SQLAlchemyError
eventRouter = APIRouter()

@eventRouter.get('/events', tags=['Events'], response_model=list[Event])
async def get_Events() -> list[Event]:
    try:
        db = Session()
        result = EventService(db).get_events()
        return jsonable_encoder(result)
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})

@eventRouter.get('/events/{id}/', tags=['Events'])
async def get_Event_By_Id(id : int) -> Event:
    db = Session()
    event = EventService(db).getEvent_id(id)
    return jsonable_encoder(event)

@eventRouter.post('/events', tags=['Events'])
async def create_Events(event: CreateEvent) -> None:
    try:
        db = Session()
        Newevent = EventService(db).create_event(event)
        return  {'message': 'Se ha creado el registro satisfactoriamente'}
    except SQLAlchemyError as e:
        return JSONResponse(status_code=500, content={'error': f'{str(e)}'})

@eventRouter.put('/events/{id}/', tags=['Events'])
async def update_Events(id : int, event: CreateEvent ) -> CreateEvent:
    db = Session()
    event = EventService(db).updateEvent(id, event)
    print(event)
    return JSONResponse(status_code=201, content=jsonable_encoder(event) )
    

@eventRouter.delete('/events/{id}/', tags=['Events'])
async def soft_Destroy(id : int):
    db = Session()
    EventService(db).softDestroy(id)
    return{'message': 'Se ha eliminado el registro satisfactoriamente'}
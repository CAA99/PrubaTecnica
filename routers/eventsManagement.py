from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemas.events import Event
from schemas.createEvent import CreateEvent
from services.eventService import EventService 
from database import Session
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from services.eventmanagmentService import EventManagmentService
import pdb
eventManagementRouter = APIRouter()


@eventManagementRouter.get('/Events/NotManagement', tags=['Management Events'])#todos los que no necesitan gestion ordebados por ID
async def get_Events_Not_Management() -> list[Event]:
    db = Session()
    events = EventManagmentService(db).getEventsNotManagment()
    return jsonable_encoder(events)
    
@eventManagementRouter.get('/Events/requireManagement', tags=['Management Events'])
def get_Events_require_Management() -> list[Event]: #todos los que requieren gestion ordebnados por ID
    
    db = Session()
    events = EventManagmentService(db).getEventsManagment()
    return jsonable_encoder(events)
    
    


@eventManagementRouter.put('/Events/Management/{id}/', tags=['Management Events'])
def update_Require_Management(id: int, RequireManagement: bool ) -> Event: #Actualizar si requiere gestion o no
    
    try:
        db = Session()
        event = EventManagmentService(db).update(id, RequireManagement)
        return JSONResponse(status_code=201, content=jsonable_encoder(event)) 
    except HTTPException as e:
        if e.status_code == 404:
            return JSONResponse(status_code=404, content={'error': f'{e.detail}'})
        else:
            return JSONResponse(status_code=500, content={'error': f'{e.detail}'})

@eventManagementRouter.delete('/Events/Management/{id}/', tags=['Management Events'])
def delete_Event(id:int): #SoftDestroy cambiar isDeleted == True
    db = Session()
    EventManagmentService(db).softDelete(id)
    return{'message': 'Se ha eliminado el registro satisfactoriamente'}

@eventManagementRouter.get('/Events/Management/OrderByDate', tags=['Management Events'])
def get_By_Date(desc : bool) -> list[Event]: #todos los archivos necesiten o no gestion ordenados por fecha 
    try:
        db = Session()
        events = EventManagmentService(db).orderBydate(desc)
        return events
    except SQLAlchemyError as e:
        return JSONResponse(status_code=500, content={'error': f'{str(e)}'})


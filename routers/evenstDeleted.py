from fastapi import APIRouter
from schemas.events import Event
eventDeleted = APIRouter()

@eventDeleted.get('/events/deleted', tags=['Events was deleted'])
async def get_Events() -> list[Event]:
    pass

@eventDeleted.get('/events/{id}/deleted', tags=['Events was deleted'])
async def get_by_id(id : int) -> Event:
    pass

@eventDeleted.put('/event/restore/{id}/', tags=['Events was deleted'])
async def restore_event(id : int) -> Event:
    pass
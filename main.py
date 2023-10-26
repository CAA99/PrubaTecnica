from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers.events import eventRouter
from routers.eventsManagement import eventManagementRouter
from database import Base, engine 
app = FastAPI()
app.include_router(eventRouter)
app.include_router(eventManagementRouter)
Base.metadata.create_all(bind=engine)

@app.get('/', include_in_schema=False)
def base():
    return RedirectResponse(url='/docs')
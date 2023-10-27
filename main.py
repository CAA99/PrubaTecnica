from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers.events import eventRouter
from routers.eventsManagement import eventManagementRouter
from routers.evenstDeleted import eventDeleted
from database import Base, engine 
from middlewares.error_handler import ErrorHandler

app = FastAPI()
app.add_middleware(ErrorHandler)
app.include_router(eventRouter)
app.include_router(eventManagementRouter)
app.include_router(eventDeleted)
Base.metadata.create_all(bind=engine)

@app.get('/', include_in_schema=False)
def base():
    return RedirectResponse(url='/docs')

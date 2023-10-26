from fastapi import APIRouter
from schemas.events import Event

eventManagementRouter = APIRouter()

@eventManagementRouter.get('/Events/RequireManagement', tags=['Management Events'])
def getEvents_RequireManagement():
    pass

@eventManagementRouter.get('/Events/WithoutManagement', tags=['Management Events'])
def getEvents_WithoutManagement():
    pass

@eventManagementRouter.get('/Events/{status}/OrderByDate', tags=['Management Events'])
def getByStatus(): #recibir parametro para organizar por fecha, ya sea de mayor a menor 
    pass

@eventManagementRouter.put('/Events/{id}/', tags=['Management Events'])
def update_Require_Management(): #Actualizar si requiere gestion o no
    pass

@eventManagementRouter.delete('/Events/{id}/', tags=['Management Events'])
def delete_Event():
    pass

@eventManagementRouter.get('/Events/OrderByDate', tags=['Management Events'])
def get_By_Date(): #recibir parametro para organizar por fecha, ya sea de mayor a menor 
    pass

@eventManagementRouter.get('/Events/allManagementEvents', tags=['Management Events'])
def get_all(): #recibir parametro para organizar por fecha, ya sea de mayor a menor 
    pass

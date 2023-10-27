from database import Session
from models.eventsModel import Event
from schemas.createEvent import CreateEvent,  StatusEvent, eventType
from enum import Enum

# Crea una sesión de SQLAlchemy
session = Session()

# Enumeraciones
status_pendiente = StatusEvent.Pendiente
event_type_1 = eventType.TypeEvent_1
event_type_3 = eventType.TypeEvent_3

# Consulta eventos que cumplan con los criterios
eventos_para_actualizar = session.query(Event).filter(
    Event.eventType.in_([event_type_1, event_type_3]),
    Event.status == status_pendiente,
    Event.requireManagement == False  # Solo aquellos con requireManagement=True
).all()

# Actualiza los eventos encontrados
for evento in eventos_para_actualizar:
    evento.requireManagement = None  # Establece requireManagement en False

# Confirma los cambios en la base de datos
session.commit()

# Cierra la sesión
session.close()

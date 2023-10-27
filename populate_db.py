from database import Session
from models.eventsModel import Event
from schemas.createEvent import CreateEvent
from schemas.deleteSchema import isDeletedEvent
from random import choice, randint
from datetime import date
from enum import Enum

session = Session()
event_types = [value for value in CreateEvent.__annotations__["eventType"].__members__.values()]
status_values = [value for value in CreateEvent.__annotations__["status"].__members__.values()]
def createExamples():
    for _ in range(60):
        random_event = CreateEvent(
            eventType=choice(event_types),
            description=f"Descripción del evento {randint(1, 100)}",
            date=date(randint(2021, 2023), randint(1, 12), randint(1, 28)),
            status=choice(status_values),
            requireManagement=bool(randint(0, 1))
        )

        evento = Event(**random_event.__dict__)
        session.add(evento)
        print(random_event)

    session.commit()
    session.close()

def createExamples_Delete():
    for _ in range(20):
        random_event = isDeletedEvent(
            eventType=choice(event_types),
            description=f"Descripción del evento {randint(1, 100)}",
            date=date(randint(2021, 2023), randint(1, 12), randint(1, 28)),
            status=choice(status_values),
            requireManagement=bool(randint(0, 1)),
            isDeleted=True
        )

        evento = Event(**random_event.__dict__)
        session.add(evento)
        print(random_event)
    
    session.commit()
    session.close()

if __name__ == "__main__":
    createExamples()
    createExamples_Delete()
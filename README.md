# PRUEBA TECNICA BACKEND

[Descripción breve del proyecto]

## Tabla de Contenidos

- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Base de Datos](#base-de-datos)


## Requisitos

Para ejecutar este proyecto, necesitas tener las siguientes herramientas y dependencias instaladas:

- **Python**: 3.11
- **pip** 
- **Base de Datos**: PostgreSQL
- **Git**: 
- **Docker-Compose** :  v2.22.0

## Instalación

Para la instalacion y ejecucion del proyecto se deben serguir los siguientes pasos.

1. **Clonar el repositorio desde GitHub:**
    ```bash
    # Clonar el repositorio
    git clone https://github.com/CAA99/PrubaTecnica

2. **Crear un entonrno virtual y activarlo :**
    ```bash
    # Crear entorno virtual
    python -m venv env
    # Activar entorno virtual linux
    source env/bin/activate
    # Activar windows
    .\env\bin\activate
    
3. **Instalar requirements.txt:**
    ```bash
    # Instalar requirements.txt
    pip install -r requirements.txt
4. **Ejecutar Docker-Compose para la DB:** para ejecutar se debe estar en la raiz del proyecto
    ```bash
        # Ejecutar Docker-Compose
        docker-compose up
5. **Populate DB:** se debe ejecutar el populate para agregar algunos datos a DB, este paso se debe ejecutar una vez este el docker corriendo
    ```bash
        # Populate DB
        python populate_db.py
6. **Correr el backend:**
    ```bash
    # Correr el backend
    uvicorn main:app --reload --port 8000
    # Abrimos en el navegador
    http://127.0.0.1:8000
    # Nos autenticamos con los siguientes datos para obtener el token
    http://localhost:8000/docs#/Autenticacion/login_login_post
      {
    "email": "admin@mail.com",
    "password": "admin"
    }
    # El Token generado lousaremos para autenticarnos en Authorize
    Token : SeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFkbWluQG1haWwuY29tIiwicGFzc3dvcmQiOiJhZG1pbiJ9.N7fxtyg3oChIAzfk4iOnkl98ErROWMXKqi5F3_e5vQc

# Base de Datos
El modelo de eventos es el siguiente 

### Event

| Campo             | Tipo               | Restricciones                          |
|-------------------|--------------------|----------------------------------------|
| id                | Integer            | Clave primaria                          |
| eventType         | String             | No puede ser nulo                      |
| description       | String             |                                        |
| date              | Date               | No puede ser nulo                      |
| status            | String             | No puede ser nulo                      |
| requireManagement | Boolean            | Puede ser nulo                          |
| isDeleted         | Boolean            | Valor predeterminado: `False`         |

#### Campos:

- `id` (Entero): Identificador único del evento (Clave primaria).
- `eventType` (Cadena de texto): Tipo de evento, no puede ser nulo.
- `description` (Cadena de texto): Descripción del evento.
- `date` (Fecha): Fecha del evento, no puede ser nulo.
- `status` (Cadena de texto): Estado del evento, no puede ser nulo.
- `requireManagement` (Booleano): Indicador booleano que representa si se requiere gestión adicional para el evento (puede ser nulo).
- `isDeleted` (Booleano): Indicador booleano que representa si el evento ha sido eliminado, valor predeterminado es `False`.

Este modelo se utiliza para almacenar y gestionar información sobre eventos en la base de datos, el backend se encarga de manejar ciertas condiciones como lo son
### Reglas de Gestión de Eventos

En este proyecto, el backend se encarga de manejar ciertas condiciones específicas para los eventos:

1. **Tipos de Evento**: Solo pueden existir tres tipos de eventos:
   - Evento tipo 1
   - Evento tipo 2
   - Evento tipo 3

2. **Clasificación de Eventos**:
   - Los eventos de tipo 1 y 3 pueden ser clasificados en "se requiere gestión" o "no se requiere gestión" cuando el estado (status) es "revisado", el valor default de requiere gestión es true cuando el evento pasa a revisado.
   - Para el evento tipo 2, el campo de "se requiere gestión" siempre será nulo.

3. **Manejo de Datos Incorrectos**:
   - Si se envía un dato que no cumple con las reglas mencionadas, el backend tiene la lógica para guardar la información como "se requiere gestión" o "no se requiere gestión", reemplazando los campos de `requireManagement` o `status` según corresponda ejemplo si se crea o actualiza un archivo de tipo evento 2 con requireManagement True | False el backend lo pondra Nulo.

4. **Eliminación Suave (Soft Delete)**:
   - Existe un parámetro llamado `isDeleted`, que representa la eliminación suave de los eventos. Los datos eliminados de esta manera solo podrán ser consultados en las rutas con el tag "was deleted".


Estas reglas aseguran que los eventos se gestionen correctamente en función de su tipo y estado. La lógica de manejo en el backend garantiza la coherencia de los datos y su correcta clasificación.

### Rutas de la API

### /login

- **POST `/events`**
  - Valida datos y crea token necesario para realizar ciertas operaciones.
  - Parámetros de solicitud: Datos del evento a crear "email": "string", "password": "string".

#### `/events`

- **GET `/events`**
  - Obtiene una lista de eventos.
  
  
- **POST `/events`**
  - Crea un nuevo evento.
  - Parámetros de solicitud: Datos del evento a crear.
  

#### `/events/{id}/`

- **GET `/events/{id}/`**
  - Obtiene un evento por su ID.
  - Parámetros de solicitud: `id` (ID del evento).
  

- **PUT `/events/{id}/`**
  - Actualiza un evento existente.
  - Parámetros de solicitud: `id` (ID del evento), Datos del evento actualizado.


- **DELETE `/events/{id}/`**
  - Realiza una eliminación suave (soft destroy) de un evento.
  - Parámetros de solicitud: `id` (ID del evento).


#### `/Events/NotManagement`

- **GET `/Events/NotManagement`**
  - Obtiene una lista de eventos no gestionados.
  

#### `/Events/requireManagement`

- **GET `/Events/requireManagement`**
  - Obtiene una lista de eventos que requieren gestión.
 

- **PUT `/Events/Management/{id}/`**
  - Actualiza el estado de requerimiento de gestión de un evento.
  - Parámetros de solicitud: `id` (ID del evento), `RequireManagement` (booleano).
  

- **DELETE `/Events/Management/{id}/`**
  - Elimina un evento de gestión.
  - Parámetros de solicitud: `id` (ID del evento).
  
- **GET `/Events/Management/OrderByDate`**
  - Obtiene eventos gestionados ordenados por fecha.
  - Parámetros de solicitud: `desc` (booleano).
  

#### `/events/deleted`

- **GET `/events/deleted`**
  - Obtiene eventos eliminados (soft destroy).
  

- **PUT `/event/restore/{id}`**
  - Restaura un evento eliminado (soft destroy).
  - Parámetros de solicitud: `id` (ID del evento).
  


### Requisitos y Validaciones

- La API sigue un conjunto de reglas para la gestión de eventos, incluyendo clasificación por tipo y estado, eliminación suave y restauración de eventos eliminados.


### Ejemplos de Uso
1. **Autenticaion**:
   - {
    "email": "admin@mail.com",
    "password": "admin"
  }
2. **Tipos de Evento**:
   - {
    "eventType": "Evento Tipo 2",
    "description": "Descripción del evento 1",
    "date": "2023-10-26",
    "status": "Pendiente",
    "requireManagement": null
    }
   - {
    "eventType": "Evento Tipo 3",
    "description": "Descripción del evento 2",
    "date": "2023-10-27",
    "status": "Pendiente",
    "requireManagement": null
    }
   - {
    "eventType": "Evento Tipo 1",
    "description": "Descripción del evento 3",
    "date": "2023-10-28",
    "status": "Pendiente",
    "requireManagement": null
    }
    - {
    "eventType": "Evento Tipo 3",
    "description": "Descripción del evento 5",
    "date": "2023-10-30",
    "status": "Revisado",
    "requireManagement": false
    }
    - {
    "eventType": "Evento Tipo 1",
    "description": "Descripción del evento 5",
    "date": "2023-10-30",
    "status": "Revisado",
    "requireManagement": true
    }

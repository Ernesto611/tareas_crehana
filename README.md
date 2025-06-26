# FastAPI tareas_crehana
# Tareas Crehana – API REST

API REST construida con FastAPI para la gestión de listas y tareas.  
Incluye pruebas automatizadas, arquitectura limpia y Docker.

## Tecnologías

- Python 3.10
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pytest
- Docker + Docker Compose
- flake8 + black

---

## Estructura

- `/listas`: CRUD de listas
- `/tareas`: CRUD de tareas

---

## Instalación local (opcional, sin Docker)

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual:
# En Linux/macOS:
source venv/bin/activate
# En Windows:
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el servidor
uvicorn app.main:app --reload
```

## Instalación con Docker

```bash
docker-compose up --build
```
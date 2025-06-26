from fastapi import FastAPI
from app.infrastructure.db import init_db
from app.interfaces.routes import router

app = FastAPI(title="Tareas Crehana")

# Inicializa base de datos (solo para desarrollo; en producción usar migraciones)
init_db()

# Rutas principales
app.include_router(router, prefix="/api", tags=["Tareas"])


@app.get("/")
def root():
    return {"message": "App is running"}

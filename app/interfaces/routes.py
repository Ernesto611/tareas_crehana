from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
from sqlalchemy.orm import Session
from app.infrastructure.db import get_db
from app.application import services
from app.interfaces import schemas
from app.domain.models import PrioridadTarea, EstadoTarea

router = APIRouter()


# ---------- Listas ----------


@router.post("/listas", response_model=schemas.ListaRespuesta)
def crear_lista(datos: schemas.ListaBase, db: Session = Depends(get_db)):
    return services.crear_lista_servicio(db, datos.nombre)


@router.get("/listas", response_model=List[schemas.ListaRespuesta])
def listar_listas(db: Session = Depends(get_db)):
    return services.obtener_listas_servicio(db)


@router.get("/listas/{lista_id}", response_model=schemas.ListaRespuesta)
def obtener_lista(lista_id: int, db: Session = Depends(get_db)):
    lista = services.obtener_lista_servicio(db, lista_id)
    if not lista:
        raise HTTPException(status_code=404, detail="Lista no encontrada")
    return lista


@router.put("/listas/{lista_id}", response_model=schemas.ListaRespuesta)
def actualizar_lista(
    lista_id: int, datos: schemas.ListaBase, db: Session = Depends(get_db)
):
    lista = services.actualizar_lista_servicio(db, lista_id, datos.nombre)
    if not lista:
        raise HTTPException(status_code=404, detail="Lista no encontrada")
    return lista


@router.delete("/listas/{lista_id}")
def eliminar_lista(lista_id: int, db: Session = Depends(get_db)):
    exito = services.eliminar_lista_servicio(db, lista_id)
    if not exito:
        raise HTTPException(status_code=404, detail="Lista no encontrada")
    return {"mensaje": "Lista eliminada correctamente"}


# ---------- Tareas ----------


@router.post("/listas/{lista_id}/tareas", response_model=schemas.TareaRespuesta)
def crear_tarea(lista_id: int, datos: schemas.TareaBase, db: Session = Depends(get_db)):
    return services.crear_tarea_servicio(db, lista_id, datos.nombre, datos.prioridad)


@router.get("/tareas/{tarea_id}", response_model=schemas.TareaRespuesta)
def obtener_tarea(tarea_id: int, db: Session = Depends(get_db)):
    tarea = services.obtener_tarea_servicio(db, tarea_id)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea


@router.put("/tareas/{tarea_id}", response_model=schemas.TareaRespuesta)
def actualizar_tarea(
    tarea_id: int, datos: schemas.ActualizarTarea, db: Session = Depends(get_db)
):
    tarea = services.actualizar_tarea_servicio(
        db, tarea_id, datos.nombre, datos.prioridad
    )
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea


@router.delete("/tareas/{tarea_id}")
def eliminar_tarea(tarea_id: int, db: Session = Depends(get_db)):
    exito = services.eliminar_tarea_servicio(db, tarea_id)
    if not exito:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"mensaje": "Tarea eliminada correctamente"}


@router.patch("/tareas/{tarea_id}/estado", response_model=schemas.TareaRespuesta)
def cambiar_estado(
    tarea_id: int, datos: schemas.CambiarEstado, db: Session = Depends(get_db)
):
    tarea = services.cambiar_estado_servicio(db, tarea_id, datos.estado)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea


@router.get("/listas/{lista_id}/tareas", response_model=List[schemas.TareaRespuesta])
def listar_tareas(
    lista_id: int,
    estado: Optional[EstadoTarea] = None,
    prioridad: Optional[PrioridadTarea] = None,
    db: Session = Depends(get_db),
):
    return services.listar_tareas_con_filtros(db, lista_id, estado, prioridad)


@router.get("/listas/{lista_id}/completitud")
def porcentaje_completado(lista_id: int, db: Session = Depends(get_db)):
    porcentaje = services.porcentaje_completado_servicio(db, lista_id)
    return {"porcentaje_completado": porcentaje}

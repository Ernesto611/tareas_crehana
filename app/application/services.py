from sqlalchemy.orm import Session
from typing import List, Optional
from app.infrastructure import repositories
from app.domain.models import TaskList, Task, EstadoTarea, PrioridadTarea


# ----------- Servicios de Listas -----------


def crear_lista_servicio(db: Session, nombre: str) -> TaskList:
    return repositories.crear_lista(db, nombre)


def obtener_listas_servicio(db: Session) -> List[TaskList]:
    return repositories.obtener_listas(db)


def obtener_lista_servicio(db: Session, lista_id: int) -> Optional[TaskList]:
    return repositories.obtener_lista(db, lista_id)


def actualizar_lista_servicio(
    db: Session, lista_id: int, nuevo_nombre: str
) -> Optional[TaskList]:
    lista = repositories.obtener_lista(db, lista_id)
    if not lista:
        return None
    return repositories.actualizar_lista(db, lista, nuevo_nombre)


def eliminar_lista_servicio(db: Session, lista_id: int) -> bool:
    lista = repositories.obtener_lista(db, lista_id)
    if not lista:
        return False
    repositories.eliminar_lista(db, lista)
    return True


# ----------- Servicios de Tareas -----------


def crear_tarea_servicio(
    db: Session, lista_id: int, nombre: str, prioridad: PrioridadTarea
) -> Task:
    return repositories.crear_tarea(db, lista_id, nombre, prioridad)


def obtener_tarea_servicio(db: Session, tarea_id: int) -> Optional[Task]:
    return repositories.obtener_tarea(db, tarea_id)


def actualizar_tarea_servicio(
    db: Session, tarea_id: int, nombre: str, prioridad: PrioridadTarea
) -> Optional[Task]:
    tarea = repositories.obtener_tarea(db, tarea_id)
    if not tarea:
        return None
    return repositories.actualizar_tarea(db, tarea, nombre, prioridad)


def eliminar_tarea_servicio(db: Session, tarea_id: int) -> bool:
    tarea = repositories.obtener_tarea(db, tarea_id)
    if not tarea:
        return False
    repositories.eliminar_tarea(db, tarea)
    return True


def cambiar_estado_servicio(
    db: Session, tarea_id: int, nuevo_estado: EstadoTarea
) -> Optional[Task]:
    tarea = repositories.obtener_tarea(db, tarea_id)
    if not tarea:
        return None
    return repositories.cambiar_estado(db, tarea, nuevo_estado)


def listar_tareas_con_filtros(
    db: Session,
    lista_id: int,
    estado: Optional[EstadoTarea],
    prioridad: Optional[PrioridadTarea],
) -> List[Task]:
    return repositories.listar_tareas_por_lista(db, lista_id, estado, prioridad)


def porcentaje_completado_servicio(db: Session, lista_id: int) -> float:
    return repositories.calcular_porcentaje_completado(db, lista_id)


from sqlalchemy.orm import Session
from typing import List, Optional
from app.infrastructure import repositories
from app.domain.models import TaskList, Task, EstadoTarea, PrioridadTarea


# ----------- Servicios de Listas -----------


def crear_lista_servicio(db: Session, nombre: str) -> TaskList:
    return repositories.crear_lista(db, nombre)


def obtener_listas_servicio(db: Session) -> List[TaskList]:
    return repositories.obtener_listas(db)


def obtener_lista_servicio(db: Session, lista_id: int) -> Optional[TaskList]:
    return repositories.obtener_lista(db, lista_id)


def actualizar_lista_servicio(
    db: Session, lista_id: int, nuevo_nombre: str
) -> Optional[TaskList]:
    lista = repositories.obtener_lista(db, lista_id)
    if not lista:
        return None
    return repositories.actualizar_lista(db, lista, nuevo_nombre)


def eliminar_lista_servicio(db: Session, lista_id: int) -> bool:
    lista = repositories.obtener_lista(db, lista_id)
    if not lista:
        return False
    repositories.eliminar_lista(db, lista)
    return True


# ----------- Servicios de Tareas -----------


def crear_tarea_servicio(
    db: Session, lista_id: int, nombre: str, prioridad: PrioridadTarea
) -> Task:
    return repositories.crear_tarea(db, lista_id, nombre, prioridad)


def obtener_tarea_servicio(db: Session, tarea_id: int) -> Optional[Task]:
    return repositories.obtener_tarea(db, tarea_id)


def actualizar_tarea_servicio(
    db: Session, tarea_id: int, nombre: str, prioridad: PrioridadTarea
) -> Optional[Task]:
    tarea = repositories.obtener_tarea(db, tarea_id)
    if not tarea:
        return None
    return repositories.actualizar_tarea(db, tarea, nombre, prioridad)


def eliminar_tarea_servicio(db: Session, tarea_id: int) -> bool:
    tarea = repositories.obtener_tarea(db, tarea_id)
    if not tarea:
        return False
    repositories.eliminar_tarea(db, tarea)
    return True


def cambiar_estado_servicio(
    db: Session, tarea_id: int, nuevo_estado: EstadoTarea
) -> Optional[Task]:
    tarea = repositories.obtener_tarea(db, tarea_id)
    if not tarea:
        return None
    return repositories.cambiar_estado(db, tarea, nuevo_estado)


def listar_tareas_con_filtros(
    db: Session,
    lista_id: int,
    estado: Optional[EstadoTarea],
    prioridad: Optional[PrioridadTarea],
) -> List[Task]:
    return repositories.listar_tareas_por_lista(db, lista_id, estado, prioridad)


def porcentaje_completado_servicio(db: Session, lista_id: int) -> float:
    return repositories.calcular_porcentaje_completado(db, lista_id)

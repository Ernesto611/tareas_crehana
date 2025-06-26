from sqlalchemy.orm import Session
from app.domain.models import TaskList, Task, EstadoTarea, PrioridadTarea


# ----------- Listas -----------
def crear_lista(db: Session, nombre: str) -> TaskList:
    lista = TaskList(nombre=nombre)
    db.add(lista)
    db.commit()
    db.refresh(lista)
    return lista


def obtener_listas(db: Session):
    return db.query(TaskList).all()


def obtener_lista(db: Session, lista_id: int):
    return db.query(TaskList).filter(TaskList.id == lista_id).first()


def actualizar_lista(db: Session, lista: TaskList, nuevo_nombre: str):
    lista.nombre = nuevo_nombre
    db.commit()
    db.refresh(lista)
    return lista


def eliminar_lista(db: Session, lista: TaskList):
    db.delete(lista)
    db.commit()


# ----------- Tareas -----------
def crear_tarea(
    db: Session, lista_id: int, nombre: str, prioridad: PrioridadTarea
) -> Task:
    tarea = Task(nombre=nombre, id_lista=lista_id, prioridad=prioridad)
    db.add(tarea)
    db.commit()
    db.refresh(tarea)
    return tarea


def obtener_tarea(db: Session, tarea_id: int) -> Task:
    return db.query(Task).filter(Task.id == tarea_id).first()


def actualizar_tarea(db: Session, tarea: Task, nombre: str, prioridad: PrioridadTarea):
    tarea.nombre = nombre
    tarea.prioridad = prioridad
    db.commit()
    db.refresh(tarea)
    return tarea


def eliminar_tarea(db: Session, tarea: Task):
    db.delete(tarea)
    db.commit()


def cambiar_estado(db: Session, tarea: Task, nuevo_estado: EstadoTarea):
    tarea.estado = nuevo_estado
    db.commit()
    db.refresh(tarea)
    return tarea


# ----------- Filtros y porcentaje -----------
def listar_tareas_por_lista(
    db: Session,
    lista_id: int,
    estado: EstadoTarea = None,
    prioridad: PrioridadTarea = None,
):
    query = db.query(Task).filter(Task.id_lista == lista_id)
    if estado:
        query = query.filter(Task.estado == estado)
    if prioridad:
        query = query.filter(Task.prioridad == prioridad)
    return query.all()


def calcular_porcentaje_completado(db: Session, lista_id: int) -> float:
    total = db.query(Task).filter(Task.id_lista == lista_id).count()
    if total == 0:
        return 0.0
    completadas = (
        db.query(Task)
        .filter(Task.id_lista == lista_id, Task.estado == EstadoTarea.completada)
        .count()
    )
    return round((completadas / total) * 100, 2)

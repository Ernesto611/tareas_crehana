from app.application import services
from app.domain.models import PrioridadTarea, EstadoTarea
from app.infrastructure.db import SessionLocal, init_db


def setup_module(module):
    init_db()


def get_test_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_crear_y_obtener_lista():
    db = next(get_test_db())
    lista = services.crear_lista_servicio(db, "Lista de prueba")
    assert lista.id is not None
    assert lista.nombre == "Lista de prueba"

    lista_obtenida = services.obtener_lista_servicio(db, lista.id)
    assert lista_obtenida is not None
    assert lista_obtenida.nombre == "Lista de prueba"


def test_crear_tarea_con_prioridad():
    db = next(get_test_db())
    lista = services.crear_lista_servicio(db, "Otra lista")
    tarea = services.crear_tarea_servicio(db, lista.id, "Tarea 1", PrioridadTarea.alta)
    assert tarea.id is not None
    assert tarea.nombre == "Tarea 1"
    assert tarea.prioridad == PrioridadTarea.alta


def test_actualizar_y_eliminar_lista():
    db = next(get_test_db())
    lista = services.crear_lista_servicio(db, "Temporal")
    actualizada = services.actualizar_lista_servicio(db, lista.id, "Actualizada")
    assert actualizada.nombre == "Actualizada"

    eliminado = services.eliminar_lista_servicio(db, lista.id)
    assert eliminado is True

    inexistente = services.eliminar_lista_servicio(db, 9999)
    assert inexistente is False


def test_crear_actualizar_estado_tarea():
    db = next(get_test_db())
    lista = services.crear_lista_servicio(db, "Con Tareas")
    tarea = services.crear_tarea_servicio(
        db, lista.id, "Tarea Inicial", PrioridadTarea.baja
    )
    tarea = services.cambiar_estado_servicio(db, tarea.id, EstadoTarea.completada)
    assert tarea.estado == EstadoTarea.completada


def test_listar_y_porcentaje_completado():
    db = next(get_test_db())
    lista = services.crear_lista_servicio(db, "Filtro")
    services.crear_tarea_servicio(db, lista.id, "Una", PrioridadTarea.baja)
    services.crear_tarea_servicio(db, lista.id, "Dos", PrioridadTarea.alta)

    tareas = services.listar_tareas_con_filtros(db, lista.id, None, None)
    assert len(tareas) == 2

    porcentaje = services.porcentaje_completado_servicio(db, lista.id)
    assert porcentaje == 0.0

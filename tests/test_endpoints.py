from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_endpoint():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"message": "App is running"}


def test_crear_lista_endpoint():
    res = client.post("/api/listas", json={"nombre": "Mi Lista API"})
    assert res.status_code == 200
    data = res.json()
    assert data["id"] > 0
    assert data["nombre"] == "Mi Lista API"


def test_validacion_nombre_corto():
    res = client.post("/api/listas", json={"nombre": "A"})
    assert res.status_code == 422


def test_actualizar_lista():
    res = client.post("/api/listas", json={"nombre": "Lista para actualizar"})
    lista = res.json()

    res = client.put(f"/api/listas/{lista['id']}", json={"nombre": "Lista actualizada"})
    assert res.status_code == 200
    assert res.json()["nombre"] == "Lista actualizada"


def test_eliminar_lista():
    res = client.post("/api/listas", json={"nombre": "Eliminarme"})
    lista_id = res.json()["id"]

    res = client.delete(f"/api/listas/{lista_id}")
    assert res.status_code == 200
    assert res.json()["mensaje"] == "Lista eliminada correctamente"

    res = client.get(f"/api/listas/{lista_id}")
    assert res.status_code == 404


def test_cambiar_estado_tarea():
    lista_res = client.post("/api/listas", json={"nombre": "Lista con tarea"})
    lista_id = lista_res.json()["id"]
    tarea_res = client.post(
        f"/api/listas/{lista_id}/tareas",
        json={"nombre": "Tarea X", "prioridad": "media"},
    )
    tarea_id = tarea_res.json()["id"]

    res = client.patch(f"/api/tareas/{tarea_id}/estado", json={"estado": "completada"})
    assert res.status_code == 200
    assert res.json()["estado"] == "completada"


def test_porcentaje_completado():
    res = client.post("/api/listas", json={"nombre": "Completitud"})
    lista_id = res.json()["id"]
    client.post(
        f"/api/listas/{lista_id}/tareas",
        json={"nombre": "Tarea 1", "prioridad": "media"},
    )
    client.post(
        f"/api/listas/{lista_id}/tareas",
        json={"nombre": "Tarea 2", "prioridad": "media"},
    )

    res = client.get(f"/api/listas/{lista_id}/completitud")
    assert res.status_code == 200
    assert "porcentaje_completado" in res.json()
    assert res.json()["porcentaje_completado"] == 0.0


def test_filtrar_tareas_por_estado_y_prioridad():
    res = client.post("/api/listas", json={"nombre": "Con Filtros"})
    lista_id = res.json()["id"]

    tarea1 = client.post(
        f"/api/listas/{lista_id}/tareas",
        json={"nombre": "Tarea A", "prioridad": "alta"},
    ).json()
    tarea2 = client.post(
        f"/api/listas/{lista_id}/tareas",
        json={"nombre": "Tarea B", "prioridad": "baja"},
    ).json()
    client.patch(f"/api/tareas/{tarea2['id']}/estado", json={"estado": "completada"})

    res = client.get(f"/api/listas/{lista_id}/tareas?estado=completada")
    assert res.status_code == 200
    assert all(t["estado"] == "completada" for t in res.json())

    res = client.get(f"/api/listas/{lista_id}/tareas?prioridad=alta")
    assert res.status_code == 200
    assert all(t["prioridad"] == "alta" for t in res.json())


def test_tarea_no_encontrada():
    res = client.get("/api/tareas/999999")
    assert res.status_code == 404


def test_cambiar_estado_tarea_inexistente():
    res = client.patch("/api/tareas/999999/estado", json={"estado": "completada"})
    assert res.status_code == 404

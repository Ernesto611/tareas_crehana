from typing import Optional
from pydantic import BaseModel, field_validator
from enum import Enum


class EstadoTarea(str, Enum):
    pendiente = "pendiente"
    completada = "completada"


class PrioridadTarea(str, Enum):
    baja = "baja"
    media = "media"
    alta = "alta"


# ----------- Listas -----------


class ListaBase(BaseModel):
    nombre: str

    @field_validator("nombre")
    @classmethod
    def nombre_no_vacio(cls, v: str):
        if not v or not v.strip():
            raise ValueError("El nombre de la lista no puede estar vacío")
        if len(v.strip()) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres")
        return v


class ListaRespuesta(ListaBase):
    id: int

    model_config = {"from_attributes": True}


# ----------- Tareas -----------


class TareaBase(BaseModel):
    nombre: str
    prioridad: PrioridadTarea = PrioridadTarea.media

    @field_validator("nombre")
    @classmethod
    def nombre_no_vacio(cls, v: str):
        if not v or not v.strip():
            raise ValueError("El nombre de la tarea no puede estar vacío")
        if len(v.strip()) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres")
        return v


class TareaRespuesta(TareaBase):
    id: int
    estado: EstadoTarea
    id_lista: int

    model_config = {"from_attributes": True}


class ActualizarTarea(BaseModel):
    nombre: str
    prioridad: PrioridadTarea

    @field_validator("nombre")
    @classmethod
    def nombre_no_vacio(cls, v: str):
        if not v or not v.strip():
            raise ValueError("El nombre de la tarea no puede estar vacío")
        if len(v.strip()) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres")
        return v


class CambiarEstado(BaseModel):
    estado: EstadoTarea

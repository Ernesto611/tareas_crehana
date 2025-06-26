from enum import Enum
from sqlalchemy import Column, Integer, String, Enum as SqlEnum, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class EstadoTarea(str, Enum):
    pendiente = "pendiente"
    completada = "completada"


class PrioridadTarea(str, Enum):
    baja = "baja"
    media = "media"
    alta = "alta"


class TaskList(Base):
    __tablename__ = "task_lists"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)

    tareas = relationship("Task", back_populates="lista", cascade="all, delete")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    estado = Column(SqlEnum(EstadoTarea), default=EstadoTarea.pendiente)
    prioridad = Column(SqlEnum(PrioridadTarea), default=PrioridadTarea.media)

    id_lista = Column(
        Integer, ForeignKey("task_lists.id", ondelete="CASCADE"), nullable=False
    )
    lista = relationship("TaskList", back_populates="tareas")

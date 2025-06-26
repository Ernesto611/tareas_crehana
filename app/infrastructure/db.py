from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.domain.models import Base

DATABASE_URL = "postgresql://crehana_user:586247931@db:5432/tareas_crehana"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def init_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import (
    DATABASE_URL,
    DB_POOL_SIZE,
    DB_MAX_OVERFLOW,
    DB_POOL_RECYCLE,
)

engine = create_engine(
    DATABASE_URL,
    pool_size=DB_POOL_SIZE,  # Configurable pool size
    max_overflow=DB_MAX_OVERFLOW,  # Configurable overflow
    pool_recycle=DB_POOL_RECYCLE,  # Configurable connection recycling
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def init_db():
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

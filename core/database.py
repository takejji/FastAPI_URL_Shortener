from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeMeta, declarative_base
from sqlalchemy.orm import Session


def dsn_url(user: str, password: str, host: str, port: int, database_name: str):
    return f"postgresql://{user}:{password}@{host}:{port}/{database_name}"


dsn = dsn_url('postgres', 'sova', 'localhost', 5432, 'storage_url')
engine = create_engine(dsn, connect_args={"check_same_thread": False})
Base = declarative_base()
session = Session(bind=engine)



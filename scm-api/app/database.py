from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
import os

#DATABASE_URL = os.getenv("DATABASE_URL", "mysql+mysqlconnector://user:password@localhost/dbname")
DATABASE_URL = "mysql+pymysql://scm:1234@localhost/scm"

# Crear el motor de SQLAlchemy
engine = create_engine(DATABASE_URL, poolclass=NullPool)

# Crear la base para los modelos de datos
Base = declarative_base()

# Crear la sesión de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependencia que proporcionará la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

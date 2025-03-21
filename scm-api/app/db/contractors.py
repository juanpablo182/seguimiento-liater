from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base

# Definir la base declarativa de SQLAlchemy
Base = declarative_base()

class ContractorDB(Base):
    __tablename__ = "contratistas"  # Nombre de la tabla en la base de datos

    # Definición de las columnas
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), index=True)  # Especificamos el tamaño de la columna como VARCHAR(255)
    carrera = Column(String(255))  # También especificamos el tamaño para esta columna
    servicio = Column(String(255))  # Y para esta también
    tarifa_hora = Column(Float)
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ProjectDB(Base):
    __tablename__ = "proyectos_extension"

    codigo = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    ingreso = Column(Float, nullable=False)
    egreso = Column(Float, nullable=False)
    presupuesto = Column(Float, nullable=False)
    estado = Column(String, nullable=False)  # Puede ser "Activo" o "Inactivo"
    fecha_inicio = Column(String, nullable=False)  # Guardado como string (ISO 8601)
    fecha_fin = Column(String, nullable=True)
    sares = Column(String, nullable=True)

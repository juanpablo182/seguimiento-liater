from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.database import Base  # Importamos la clase Base de nuestro archivo de configuración de base de datos

class MaterialDB(Base):
    __tablename__ = "materiales"  # Nombre de la tabla en la base de datos

    id = Column(Integer, primary_key=True, index=True)  # Identificador único
    nombre = Column(String(255), index=True)  # Nombre del material
    cantidad = Column(Integer)  # Cantidad de material disponible
    descripcion = Column(String(255))  # Descripción del material
    precio_unitario = Column(Float)  # Precio por unidad del material
    total = Column(Float)  # Total calculado (cantidad * precio_unitario)

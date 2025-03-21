from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base

class ProjectDB(Base):
    __tablename__ = "proyectos"

    codigo = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), index=True)  # 🔹 Agregamos longitud (ej: 100 caracteres)
    descripcion = Column(String(255))  # 🔹 Máximo 255 caracteres
    ingreso = Column(Float)
    egreso = Column(Float)
    presupuesto = Column(Float)
    estado = Column(String(50))  # 🔹 Estado con hasta 50 caracteres
    fecha_inicio = Column(String(10), nullable=False)
    fecha_fin = Column(String(10), nullable=False)


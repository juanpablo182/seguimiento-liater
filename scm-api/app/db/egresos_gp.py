from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class EgresosGP(Base):
    __tablename__ = "egresos_gp"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255))
    dedicacion_horas = Column(Integer)
    unidad = Column(String(50))
    valor_unitario = Column(Float)
    cantidad = Column(Integer)
    valor = Column(Float)
    cuatro_por_mil = Column(Float)
    total = Column(Float)
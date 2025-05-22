from sqlalchemy import Column, Integer, String
from app.database import Base

class IngresosDB(Base):
    __tablename__ = "ingresos"

    id = Column(Integer, primary_key=True, index=True)
    tipo_acuerdo = Column(String(100))
    conoce_monto = Column(String(10))  # Sí o No
    aporte_entidad = Column(Integer)
    contrapartida = Column(Integer)
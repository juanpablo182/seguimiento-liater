from sqlalchemy import Column, Integer, String
from app.database import Base  # ¡Ojo! importa Base desde tu archivo, no la declares otra vez

class InfoBasicDB(Base):
    __tablename__ = "informacion_basica"

    id = Column(Integer, primary_key=True, index=True)
    nombre_proyecto = Column(String(255), index=True)
    facultad = Column(String(255))
    unidad_academica = Column(String(255))
    duracion = Column(String(100))
    modalidad = Column(String(100))
    submodalidad = Column(String(100))

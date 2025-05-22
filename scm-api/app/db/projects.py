# from sqlalchemy import Column, Integer, String, Float, Date
# from app.database import Base

# class ProjectDB(Base):
#     __tablename__ = "proyectos"

#     codigo = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     dependencia = Column(Integer, nullable=False)
#     unidad_academica = Column(Integer, nullable=False)
#     modalidad = Column(Integer, nullable=False)
#     sub_modalidad = Column(Integer, nullable=False)
#     nombre = Column(String, nullable=False)
#     duracion_dias = Column(Integer, nullable=False)
#     duracion_meses = Column(Integer, nullable=False)
#     descripcion = Column(String, nullable=False)
#     presupuesto = Column(Integer, nullable=False)
#     estado = Column(Integer, nullable=False)
#     fecha_inicio = Column(Date, nullable=False)
#     fecha_fin = Column(Date, nullable=False)

# from sqlalchemy import Column, Integer, String, Date
# from app.database import Base

# class ProjectDB(Base):
#     __tablename__ = "proyectos"

#     codigo = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     dependencia = Column(Integer, nullable=False)
#     unidad_academica = Column(Integer, nullable=False)
#     modalidad = Column(Integer, nullable=False)
#     sub_modalidad = Column(Integer, nullable=False)
#     nombre = Column(String(255), nullable=False)  # 👈 longitud definida
#     duracion_dias = Column(Integer, nullable=False)
#     duracion_meses = Column(Integer, nullable=False)
#     descripcion = Column(String(500), nullable=False)  # 👈 longitud definida
#     presupuesto = Column(Integer, nullable=False)
#     estado = Column(Integer, nullable=False)
#     fecha_inicio = Column(Date, nullable=False)
#     fecha_fin = Column(Date, nullable=False)

from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class ProjectDB(Base):
    __tablename__ = "proyectos"

    codigo = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # Ahora tipo String para recibir nombres de enums descriptivos
    dependencia = Column(String(100), nullable=False)
    unidad_academica = Column(String(100), nullable=False)
    modalidad = Column(String(100), nullable=False)
    sub_modalidad = Column(String(100), nullable=False)
    
    nombre = Column(String(255), nullable=False)
    duracion_dias = Column(Integer, nullable=False)
    duracion_meses = Column(Integer, nullable=False)
    descripcion = Column(String(500), nullable=False)
    presupuesto = Column(Integer, nullable=False)
    estado = Column(Integer, nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)

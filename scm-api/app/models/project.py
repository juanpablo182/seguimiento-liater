# from pydantic import BaseModel
# from datetime import date
# from typing import Optional

# class Project(BaseModel):
#     codigo: Optional[int] = None
#     dependencia: int
#     unidad_academica: int
#     modalidad: int
#     sub_modalidad: int 
#     nombre: str
#     duracion_dias: int
#     duracion_meses: int
#     #descripcion: str
#     presupuesto: int
#     estado: int
#     fecha_inicio: date
#     fecha_fin: date

#     class Config:
#         from_attributes = True

from pydantic import BaseModel
from datetime import date
from typing import Optional

class Project(BaseModel):
    codigo: Optional[int] = None
    dependencia: str              # ← cambiado de int a str
    unidad_academica: str         # ← cambiado de int a str
    modalidad: str                # ← cambiado de int a str
    sub_modalidad: str            # ← cambiado de int a str
    nombre: str
    duracion_dias: int
    duracion_meses: int
    descripcion: str              # ← descomentado
    presupuesto: int
    estado: int
    fecha_inicio: date
    fecha_fin: date

    class Config:
        from_attributes = True

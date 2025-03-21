from pydantic import BaseModel
from datetime import date

class Project(BaseModel):
    codigo: int
    nombre: str
    descripcion: str
    ingreso: float
    egreso: float
    presupuesto: float
    estado: str
    fecha_inicio: str
    fecha_fin: str
    

    class Config:
        from_attributes = True




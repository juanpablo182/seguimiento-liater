from pydantic import BaseModel

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
    sares: str

    class Config:
        from_attributes = True



from pydantic import BaseModel

class Contractor(BaseModel):
    id: int
    nombre: str
    carrera: str
    servicio: str
    tarifa_hora: float
    fecha_inicio: str
    fecha_fin: str 

    class Config:
        from_attributes = True

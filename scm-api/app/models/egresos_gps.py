from pydantic import BaseModel

class EgresosGPS(BaseModel):
    id: int
    nombre: str
    dedicacion_horas: int
    unidad: str
    valor_unitario: float
    cantidad: int
    valor: float
    cuatro_por_mil: float
    total: float

    class Config:
        from_attributes = True

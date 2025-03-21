from pydantic import BaseModel

class Material(BaseModel):
    id: int
    nombre: str
    cantidad: int
    descripcion: str
    precio_unitario: float
    total: float 

    class Config:
        from_attributes = True

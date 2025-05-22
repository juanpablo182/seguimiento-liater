from pydantic import BaseModel

class Ingreso(BaseModel):
    id: int
    tipo_acuerdo: str
    conoce_monto: str
    aporte_entidad: int
    contrapartida: int

    class Config:
        from_attributes = True
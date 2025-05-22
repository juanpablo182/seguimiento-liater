from pydantic import BaseModel
from datetime import datetime

class Student(BaseModel):
    id: int
    nombre: str
    edad: int
    curso: str
    carrera: str
    fecha_inicio: datetime
    fecha_fin: datetime

    class Config:
        from_attributes = True
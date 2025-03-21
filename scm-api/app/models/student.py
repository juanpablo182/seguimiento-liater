from pydantic import BaseModel

class Student(BaseModel):
    id: int
    nombre: str
    edad: int
    curso: str
    carrera: str
    fecha_inicio: str
    fecha_fin: str 

    class Config:
        from_attributes = True
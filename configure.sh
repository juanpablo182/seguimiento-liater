#!/bin/bash

# Nombre del proyecto
PROJECT_NAME="scm-api"

echo "Creando el proyecto: $PROJECT_NAME"

# Crear el directorio del proyecto
mkdir -p $PROJECT_NAME/app
mkdir -p $PROJECT_NAME/app/routes
mkdir -p $PROJECT_NAME/app/models
mkdir -p $PROJECT_NAME/app/db

cd $PROJECT_NAME || exit

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install fastapi uvicorn

# Crear archivos base
echo "from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from app.routes import students, contractors, materials, projects

app = FastAPI(title='Gestión de Estudiantes, Contratistas, Materiales y Proyectos',
              description='API para manejar estudiantes, contratistas, materiales y proyectos.',
              version='1.1')

app.include_router(students.router)
app.include_router(contractors.router)
app.include_router(materials.router)
app.include_router(projects.router)" > main.py

# Rutas
echo "from fastapi import APIRouter
from typing import List
from app.models.student import Student

router = APIRouter(prefix='/estudiantes', tags=['Estudiantes'])

students = []

@router.get('/', response_model=List[Student])
def obtener_estudiantes():
    return students

@router.post('/')
def agregar_estudiante(estudiante: Student):
    students.append(estudiante)
    return {'mensaje': 'Estudiante agregado'}" > app/routes/students.py

echo "from fastapi import APIRouter
from typing import List
from app.models.contractor import Contractor

router = APIRouter(prefix='/contratistas', tags=['Contratistas'])

contractors = []

@router.get('/', response_model=List[Contractor])
def obtener_contratistas():
    return contractors

@router.post('/')
def agregar_contratista(contratista: Contractor):
    contractors.append(contratista)
    return {'mensaje': 'Contratista agregado'}" > app/routes/contractors.py

echo "from fastapi import APIRouter
from typing import List
from app.models.material import Material

router = APIRouter(prefix='/materiales', tags=['Materiales'])

materials = []

@router.get('/', response_model=List[Material])
def obtener_materiales():
    return materials

@router.post('/')
def agregar_material(material: Material):
    materials.append(material)
    return {'mensaje': 'Material agregado'}" > app/routes/materials.py

echo "from fastapi import APIRouter
from typing import List
from app.models.project import Project

router = APIRouter(prefix='/proyectos', tags=['Proyectos'])

projects = []

@router.get('/', response_model=List[Project])
def obtener_proyectos():
    return projects

@router.post('/')
def agregar_proyecto(proyecto: Project):
    projects.append(proyecto)
    return {'mensaje': 'Proyecto agregado'}" > app/routes/projects.py

# Modelos
echo "from pydantic import BaseModel

class Student(BaseModel):
    id: int
    nombre: str
    edad: int
    curso: str" > app/models/student.py

echo "from pydantic import BaseModel

class Contractor(BaseModel):
    id: int
    nombre: str
    servicio: str
    tarifa_hora: float" > app/models/contractor.py

echo "from pydantic import BaseModel

class Material(BaseModel):
    id: int
    nombre: str
    cantidad: int
    precio_unitario: float" > app/models/material.py

echo "from pydantic import BaseModel

class Project(BaseModel):
    id: int
    nombre: str
    descripcion: str
    presupuesto: float" > app/models/project.py

# Archivo de dependencias
echo "fastapi
uvicorn" > requirements.txt

# Mensaje de finalización
echo "Proyecto $PROJECT_NAME creado exitosamente."
echo "Ejecuta el servidor con:"
echo "source venv/bin/activate && uvicorn main:app --reload"

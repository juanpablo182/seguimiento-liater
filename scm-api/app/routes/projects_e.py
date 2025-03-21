from fastapi import FastAPI, Depends, HTTPException
from fastapi import APIRouter
from typing import List
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.project_e import Project  # Importamos el modelo Pydantic
from app.db.projects import ProjectDB  # Importamos el modelo de BD

# Creamos un router para los proyectos de extensión
router = APIRouter(prefix='/api/proyectos_extension', tags=['Proyectos de Extensión'])

# Obtener todos los proyectos
@router.get("/", response_model=List[Project])
def obtener_proyectos(db: Session = Depends(get_db)):
    return db.query(ProjectDB).all()

# Agregar un nuevo proyecto
@router.post("/", response_model=Project)
def agregar_proyecto(proyecto: Project, db: Session = Depends(get_db)):
    nuevo_proyecto = ProjectDB(**proyecto.dict())  
    db.add(nuevo_proyecto)
    db.commit()
    db.refresh(nuevo_proyecto)
    return nuevo_proyecto  

# Obtener un proyecto por código
@router.get("/{codigo}", response_model=Project)
def obtener_proyecto(codigo: int, db: Session = Depends(get_db)):
    proyecto = db.query(ProjectDB).filter(ProjectDB.codigo == codigo).first()
    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return proyecto

# Actualizar un proyecto existente
@router.put("/{codigo}", response_model=Project)
def actualizar_proyecto(codigo: int, proyecto: Project, db: Session = Depends(get_db)):
    proyecto_db = db.query(ProjectDB).filter(ProjectDB.codigo == codigo).first()
    if not proyecto_db:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    for key, value in proyecto.dict(exclude_unset=True).items():
        setattr(proyecto_db, key, value)

    db.commit()
    db.refresh(proyecto_db)
    return proyecto_db

# Eliminar un proyecto
@router.delete("/{codigo}")
def eliminar_proyecto(codigo: int, db: Session = Depends(get_db)):
    proyecto = db.query(ProjectDB).filter(ProjectDB.codigo == codigo).first()
    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    db.delete(proyecto)
    db.commit()
    return {"mensaje": "Proyecto eliminado correctamente"}


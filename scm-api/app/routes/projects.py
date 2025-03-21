from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.projects import ProjectDB
from app.models.project import Project
from app.database import get_db

router = APIRouter(prefix='/api/proyectos', tags=['Proyectos'])

@router.get("/", response_model=List[Project])
def obtener_proyectos(db: Session = Depends(get_db)):
    return db.query(ProjectDB).all()  # Corrección aquí

@router.get("/{codigo}", response_model=Project)
def obtener_proyecto(codigo: int, db: Session = Depends(get_db)):
    proyecto = db.query(ProjectDB).filter(ProjectDB.codigo == codigo).first()  # Corrección aquí
    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return proyecto

@router.post("/", response_model=Project)
def agregar_proyecto(proyecto: Project, db: Session = Depends(get_db)):
    nuevo_proyecto = ProjectDB(**proyecto.dict())
    db.add(nuevo_proyecto)
    db.commit()
    db.refresh(nuevo_proyecto)
    return nuevo_proyecto

@router.put("/{codigo}", response_model=Project)
def actualizar_proyecto(codigo: int, proyecto: Project, db: Session = Depends(get_db)):
    proyecto_db = db.query(ProjectDB).filter(ProjectDB.codigo == codigo).first()  # Corrección aquí
    if not proyecto_db:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    for key, value in proyecto.dict(exclude_unset=True).items():
        setattr(proyecto_db, key, value)

    db.commit()
    db.refresh(proyecto_db)
    return proyecto_db

@router.delete("/{codigo}")
def eliminar_proyecto(codigo: int, db: Session = Depends(get_db)):
    proyecto = db.query(ProjectDB).filter(ProjectDB.codigo == codigo).first()  # Corrección aquí
    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    db.delete(proyecto)
    db.commit()
    return {"mensaje": "Proyecto eliminado correctamente"}

from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi import APIRouter, Depends
from typing import List
from app.models.student import Student
from app.db.students import StudentDB
from sqlalchemy.orm import Session
from app.database import get_db


router = APIRouter(prefix='/api/estudiantes', tags=['Estudiantes'])

@router.get('/', response_model=List[Student])
def obtener_estudiantes(db: Session = Depends(get_db)):
    return db.query(StudentDB).all()    
    

@router.post('/', response_model=Student)
def agregar_estudiante(estudiante: Student, db: Session = Depends(get_db)):
    nuevo_estudiante = StudentDB(**estudiante.dict())  
    db.add(nuevo_estudiante)
    db.commit()
    db.refresh(nuevo_estudiante) 
    return nuevo_estudiante  

@router.get("/{id}", response_model=Student)
def obtener_estudiante(id: int, db: Session = Depends(get_db)):
    estudiante = db.query(StudentDB).filter(StudentDB.id == id).first()
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return estudiante
from fastapi import APIRouter


@router.get("/", response_model=List[Student])
def obtener_estudiantes(db: Session = Depends(get_db)):
    return db.query(StudentDB).all()


@router.post("/", response_model=Student)
def agregar_estudiante(estudiante: Student, db: Session = Depends(get_db)):
    nuevo_estudiante = StudentDB(**estudiante.dict())
    db.add(nuevo_estudiante)
    db.commit()
    db.refresh(nuevo_estudiante)
    return nuevo_estudiante

@router.put("/{id}", response_model=Student)
def actualizar_estudiante(id: int, estudiante: Student, db: Session = Depends(get_db)):
    estudiante_db = db.query(StudentDB).filter(StudentDB.id == id).first()
    if not estudiante_db:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")

    for key, value in estudiante.dict(exclude_unset=True).items():
        setattr(estudiante_db, key, value)

    db.commit()
    db.refresh(estudiante_db)
    return estudiante_db

@router.delete("/{id}")
def eliminar_estudiante(id: int, db: Session = Depends(get_db)):
    estudiante = db.query(StudentDB).filter(StudentDB.id == id).first()
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")

    db.delete(estudiante)
    db.commit()
    return {"mensaje": "Estudiante eliminado correctamente"}




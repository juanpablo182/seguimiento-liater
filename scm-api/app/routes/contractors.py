from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.models.contractor import Contractor  # Asegúrate de que tu modelo de Contractor esté en app/models
from app.db.contractors import ContractorDB  # Asegúrate de que tu modelo en la base de datos sea ContractorDB
from app.database import get_db  # Asegúrate de tener esta función para obtener la sesión de la base de datos

router = APIRouter(prefix='/api/contratistas', tags=['Contratistas'])

@router.get('/', response_model=List[Contractor])
def obtener_contratistas(db: Session = Depends(get_db)):
    # Devuelve todos los contratistas desde la base de datos
    return db.query(ContractorDB).all()    

@router.post('/', response_model=Contractor)
def agregar_contratista(contratista: Contractor, db: Session = Depends(get_db)):
    # Crea un nuevo contratista y lo agrega a la base de datos
    nuevo_contratista = ContractorDB(**contratista.dict())  
    db.add(nuevo_contratista)
    db.commit()
    db.refresh(nuevo_contratista) 
    return nuevo_contratista  

@router.get("/{id}", response_model=Contractor)
def obtener_contratista(id: int, db: Session = Depends(get_db)):
    # Busca un contratista por su ID
    contratista = db.query(ContractorDB).filter(ContractorDB.id == id).first()
    if not contratista:
        raise HTTPException(status_code=404, detail="Contratista no encontrado")
    return contratista

@router.put("/{id}", response_model=Contractor)
def actualizar_contratista(id: int, contratista: Contractor, db: Session = Depends(get_db)):
    # Actualiza los datos de un contratista según el ID
    contratista_db = db.query(ContractorDB).filter(ContractorDB.id == id).first()
    if not contratista_db:
        raise HTTPException(status_code=404, detail="Contratista no encontrado")

    # Actualiza los campos que no estén vacíos
    for key, value in contratista.dict(exclude_unset=True).items():
        setattr(contratista_db, key, value)

    db.commit()
    db.refresh(contratista_db)
    return contratista_db

@router.delete("/{id}")
def eliminar_contratista(id: int, db: Session = Depends(get_db)):
    # Elimina un contratista por su ID
    contratista = db.query(ContractorDB).filter(ContractorDB.id == id).first()
    if not contratista:
        raise HTTPException(status_code=404, detail="Contratista no encontrado")

    db.delete(contratista)
    db.commit()
    return {"mensaje": "Contratista eliminado correctamente"}
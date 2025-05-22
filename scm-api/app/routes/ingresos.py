from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from typing import List
from sqlalchemy.orm import Session
from app.models.ingresos_1 import Ingreso
from app.db.ingresos import IngresosDB
from app.database import get_db
import os
from pathlib import Path

router = APIRouter(prefix='/api/ingresos', tags=['Ingresos'])

BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@router.get("/vista")
def mostrar_vista_ingresos(request: Request):
    return templates.TemplateResponse("ingresos.html", {"request": request})

@router.get('/', response_model=List[Ingreso])
def obtener_ingresos(db: Session = Depends(get_db)):
    return db.query(IngresosDB).all()

@router.post('/', response_model=Ingreso)
def agregar_ingreso(ingreso: Ingreso, db: Session = Depends(get_db)):
    nuevo = IngresosDB(**ingreso.dict(exclude={"id"}))
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/{id}", response_model=Ingreso)
def obtener_ingreso(id: int, db: Session = Depends(get_db)):
    ingreso = db.query(IngresosDB).filter(IngresosDB.id == id).first()
    if not ingreso:
        raise HTTPException(status_code=404, detail="Ingreso no encontrado")
    return ingreso

@router.put("/{id}", response_model=Ingreso)
def actualizar_ingreso(id: int, ingreso: Ingreso, db: Session = Depends(get_db)):
    ingreso_db = db.query(IngresosDB).filter(IngresosDB.id == id).first()
    if not ingreso_db:
        raise HTTPException(status_code=404, detail="Ingreso no encontrado")

    for key, value in ingreso.dict(exclude_unset=True, exclude={"id"}).items():
        setattr(ingreso_db, key, value)

    db.commit()
    db.refresh(ingreso_db)
    return ingreso_db

@router.delete("/{id}")
def eliminar_ingreso(id: int, db: Session = Depends(get_db)):
    ingreso = db.query(IngresosDB).filter(IngresosDB.id == id).first()
    if not ingreso:
        raise HTTPException(status_code=404, detail="Ingreso no encontrado")
    db.delete(ingreso)
    db.commit()
    return {"mensaje": "Ingreso eliminado correctamente"}

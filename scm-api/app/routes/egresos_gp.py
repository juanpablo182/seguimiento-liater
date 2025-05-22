from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.egresos_gps import EgresosGPS
from app.db.egresos_gp import EgresosGP
from fastapi.templating import Jinja2Templates
import os
from pathlib import Path

router = APIRouter(prefix='/api/egresos_gp', tags=['Egresos - Gastos de Personal'])

BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@router.get("/vista")
def mostrar_egresos_gp(request: Request):
    return templates.TemplateResponse("egresos_gp.html", {"request": request})

@router.get("/", response_model=List[EgresosGPS])
def listar_egresos_gp(db: Session = Depends(get_db)):
    return db.query(EgresosGP).all()

@router.post("/", response_model=EgresosGPS)
def crear_egreso_gp(egreso: EgresosGPS, db: Session = Depends(get_db)):
    nuevo = EgresosGP(**egreso.dict(exclude={"id"}))
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/{id}", response_model=EgresosGPS)
def obtener_egreso_gp(id: int, db: Session = Depends(get_db)):
    egreso = db.query(EgresosGP).filter(EgresosGP.id == id).first()
    if not egreso:
        raise HTTPException(status_code=404, detail="Egreso no encontrado")
    return egreso

@router.put("/{id}", response_model=EgresosGPS)
def actualizar_egreso_gp(id: int, egreso: EgresosGPS, db: Session = Depends(get_db)):
    egreso_db = db.query(EgresosGP).filter(EgresosGP.id == id).first()
    if not egreso_db:
        raise HTTPException(status_code=404, detail="Egreso no encontrado")
    
    for key, value in egreso.dict(exclude={"id"}).items():
        setattr(egreso_db, key, value)

    db.commit()
    db.refresh(egreso_db)
    return egreso_db

@router.delete("/{id}")
def eliminar_egreso_gp(id: int, db: Session = Depends(get_db)):
    egreso = db.query(EgresosGP).filter(EgresosGP.id == id).first()
    if not egreso:
        raise HTTPException(status_code=404, detail="Egreso no encontrado")
    db.delete(egreso)
    db.commit()
    return {"mensaje": "Egreso eliminado correctamente"}

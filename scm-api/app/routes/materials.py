from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi import APIRouter, Depends
from typing import List
from app.models.material import Material  # Cambiado el modelo a Material
from app.db.materials import MaterialDB  # Cambiado la base de datos a MaterialDB
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter(prefix='/api/materiales', tags=['Materiales'])  # Ruta adaptada

# Obtener lista de materiales
@router.get('/', response_model=List[Material])
def obtener_materiales(db: Session = Depends(get_db)):
    return db.query(MaterialDB).all()

# Agregar un material
@router.post('/', response_model=Material)
def agregar_material(material: Material, db: Session = Depends(get_db)):
    nuevo_material = MaterialDB(**material.dict())  # Crear el nuevo material
    db.add(nuevo_material)
    db.commit()
    db.refresh(nuevo_material)  # Refrescar los datos del material
    return nuevo_material

# Obtener un material por ID
@router.get("/{id}", response_model=Material)
def obtener_material(id: int, db: Session = Depends(get_db)):
    material = db.query(MaterialDB).filter(MaterialDB.id == id).first()  # Buscar material por ID
    if not material:
        raise HTTPException(status_code=404, detail="Material no encontrado")
    return material

# Actualizar un material por ID
@router.put("/{id}", response_model=Material)
def actualizar_material(id: int, material: Material, db: Session = Depends(get_db)):
    material_db = db.query(MaterialDB).filter(MaterialDB.id == id).first()  # Buscar el material
    if not material_db:
        raise HTTPException(status_code=404, detail="Material no encontrado")

    for key, value in material.dict(exclude_unset=True).items():  # Actualizar campos
        setattr(material_db, key, value)

    db.commit()  # Guardar cambios
    db.refresh(material_db)  # Refrescar datos del material
    return material_db

# Eliminar un material por ID
@router.delete("/{id}")
def eliminar_material(id: int, db: Session = Depends(get_db)):
    material = db.query(MaterialDB).filter(MaterialDB.id == id).first()  # Buscar el material
    if not material:
        raise HTTPException(status_code=404, detail="Material no encontrado")

    db.delete(material)  # Eliminar material
    db.commit()  # Confirmar eliminación
    return {"mensaje": "Material eliminado correctamente"}

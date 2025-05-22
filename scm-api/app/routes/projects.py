# from fastapi import APIRouter, Depends, HTTPException, Request
# from fastapi.templating import Jinja2Templates
# from typing import List
# from sqlalchemy.orm import Session
# from app.models.project import Project  # Pydantic
# from app.db.projects import ProjectDB    # SQLAlchemy
# from app.database import get_db             # Session DB
# from app.enums.dependencies import Dependencies
# from app.enums.modalities import Modalities
# from app.enums.sub_modalities import SubModalities
# from app.enums.basic_unities import BasicUnities
# import os
# from pathlib import Path

# router = APIRouter(prefix='/api/projects', tags=['Información básica'])

# BASE_DIR = Path(__file__).resolve().parent.parent
# templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# @router.get("/vista")
# def mostrar_plantilla_info_basica(request: Request):
#     return templates.TemplateResponse("infobasica.html", {
#         "request": request,
#         "dependencies": list(Dependencies),
#         "modalities": list(Modalities),
#         "sub_modalities": list(SubModalities),
#         "basic_unities": list(BasicUnities)
#     })


# @router.get('/', response_model=List[Project])
# def obtener_info_basica(db: Session = Depends(get_db)):
#     return db.query(Project).all()

# @router.post('/', response_model=Project)
# def agregar_info_basica(info: Project, db: Session = Depends(get_db)):
#     nueva_info = Project(**info.dict(exclude={"id"}))
#     db.add(nueva_info)
#     db.commit()
#     db.refresh(nueva_info)
#     return nueva_info

# @router.get("/{id}", response_model=Project)
# def obtener_info_por_id(id: int, db: Session = Depends(get_db)):
#     info = db.query(Project).filter(Project.id == id).first()
#     if not info:
#         raise HTTPException(status_code=404, detail="Información básica no encontrada")
#     return info

# @router.put("/{id}", response_model=Project)
# def actualizar_info_basica(id: int, info: Project, db: Session = Depends(get_db)):
#     info_db = db.query(Project).filter(Project.id == id).first()
#     if not info_db:
#         raise HTTPException(status_code=404, detail="Información básica no encontrada")

#     for key, value in info.dict(exclude={"id"}, exclude_unset=True).items():
#         setattr(info_db, key, value)

#     db.commit()
#     db.refresh(info_db)
#     return info_db
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from typing import List
from sqlalchemy.orm import Session
from app.models.project import Project  # Pydantic
from app.db.projects import ProjectDB    # SQLAlchemy
from app.database import get_db
from app.enums.dependencies import Dependencies
from app.enums.modalities import Modalities
from app.enums.sub_modalities import SubModalities
from app.enums.basic_unities import BasicUnities
import os
from pathlib import Path

router = APIRouter(prefix='/api/projects', tags=['Información básica'])

BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# @router.get("/vista")
# def mostrar_plantilla_info_basica(request: Request):
#     return templates.TemplateResponse("infobasica.html", {
#         "request": request,
#         "dependencies": list(Dependencies),
#         "modalities": list(Modalities),
#         "sub_modalities": list(SubModalities),
#         "basic_unities": list(BasicUnities)
#     })

@router.get("/vista")
def mostrar_plantilla_info_basica(request: Request):
    return templates.TemplateResponse("projects.html", {
        "request": request,
        "dependencies": list(Dependencies),
        "modalities": list(Modalities),
        "sub_modalities": list(SubModalities),
        "basic_unities": list(BasicUnities)
    })


@router.get('/', response_model=List[Project])
def obtener_info_basica(db: Session = Depends(get_db)):
    return db.query(ProjectDB).all()  # ✅ CORREGIDO

@router.post('/', response_model=Project)
def agregar_info_basica(info: Project, db: Session = Depends(get_db)):
    nueva_info = ProjectDB(**info.dict(exclude={"codigo"}))  # ✅ CORREGIDO
    db.add(nueva_info)
    db.commit()
    db.refresh(nueva_info)
    return nueva_info

@router.get("/{codigo}", response_model=Project)  # ✅ CAMBIADO A "codigo"
def obtener_info_por_id(codigo: int, db: Session = Depends(get_db)):
    info = db.query(ProjectDB).filter(ProjectDB.codigo == codigo).first()
    if not info:
        raise HTTPException(status_code=404, detail="Información básica no encontrada")
    return info

@router.put("/{codigo}", response_model=Project)  # ✅ CAMBIADO A "codigo"
def actualizar_info_basica(codigo: int, info: Project, db: Session = Depends(get_db)):
    info_db = db.query(ProjectDB).filter(ProjectDB.codigo == codigo).first()
    if not info_db:
        raise HTTPException(status_code=404, detail="Información básica no encontrada")

    for key, value in info.dict(exclude={"codigo"}, exclude_unset=True).items():
        setattr(info_db, key, value)

    db.commit()
    db.refresh(info_db)
    return info_db

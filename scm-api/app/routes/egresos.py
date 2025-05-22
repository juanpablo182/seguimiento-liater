from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
import os
from pathlib import Path

router = APIRouter(prefix="/egresos", tags=["Egresos"])

BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@router.get("/")
def vista_egresos(request: Request):
    return templates.TemplateResponse("egresos.html", {"request": request})

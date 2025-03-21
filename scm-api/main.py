from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.database import engine, Base
from app.routes import contractors, materials, projects, students,projects_e

app = FastAPI(
    title='Gestión de Estudiantes, Contratistas, Materiales y Proyectos',
    description='API para manejar estudiantes, contratistas, materiales y proyectos.',
    version='1.2'
)

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Configurar Jinja2 para la renderización de plantillas HTML
templates = Jinja2Templates(directory="app/templates")

# Servir archivos estáticos (CSS, JS, imágenes)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# 🚀 Rutas del frontend 🚀
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/estadisticas")
def estadisticas(request: Request):
    return templates.TemplateResponse("estadisticas.html", {"request": request})

@app.get("/ejecucion")
def ejecucion(request: Request):
    return templates.TemplateResponse("ejecucion.html", {"request": request})

@app.get("/student")
def student_page(request: Request):
    return templates.TemplateResponse("student.html", {"request": request})

@app.get("/materials")
def materials_page(request: Request):
    return templates.TemplateResponse("materials.html", {"request": request})

@app.get("/proyecto_liater")
def proyecto_liater_page(request: Request):
    return templates.TemplateResponse("proyecto_liater.html", {"request": request})

@app.get("/contratistas")
def contratistas_page(request: Request):
    return templates.TemplateResponse("contratistas.html", {"request": request})

@app.get("/proyectos_extension")
def proyectos_extension_page(request: Request):
    return templates.TemplateResponse("proyectos_extension.html", {"request": request})

# Incluir los routers de las distintas entidades
app.include_router(contractors.router)
app.include_router(materials.router)
app.include_router(projects.router)
app.include_router(students.router)  
app.include_router(projects_e.router)  

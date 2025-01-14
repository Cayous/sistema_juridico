from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.models import Base
from src.core.database import engine
from src.api.auth import router as auth_router

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Configura o FastAPI
app = FastAPI()

# Monta arquivos estáticos e configura templates
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="backend/src/templates")

# Registra o router de autenticação
app.include_router(auth_router)

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})

@app.get("/register", response_class=HTMLResponse)
def show_register_form(request: Request):
    return templates.TemplateResponse("auth/register.html", {"request": request})

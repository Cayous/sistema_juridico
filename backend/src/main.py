from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from .core.database import engine, Base
from .models import User, Client, Case, Task

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema Jurídico")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
from .api import auth, clients, cases, tasks
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(clients.router, prefix="/api/clients", tags=["clients"])
app.include_router(cases.router, prefix="/api/cases", tags=["cases"])
app.include_router(tasks.router, prefix="/api/tasks", tags=["tasks"])
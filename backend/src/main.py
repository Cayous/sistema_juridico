from fastapi import FastAPI
from .models import Base, User, Client, Case, Task
from .core.database import engine

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Sistema Jurídico está funcionando!"}
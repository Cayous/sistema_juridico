from fastapi import FastAPI
from .models import Base, User, Client, Case, Task
from .core.database import engine
from .api.auth import router as auth_router  # Importe o router de autenticação


# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Registre o router de autenticação
app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"message": "Sistema Jurídico está funcionando!"}
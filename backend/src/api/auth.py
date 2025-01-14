from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from ..core.database import get_db
from ..models.user import User
from ..schemas.user import UserCreate, UserInDB
from ..core.security import get_password_hash
from datetime import datetime

router = APIRouter()

@router.post("/register", response_class=HTMLResponse)
async def register(
    email: str = Form(...),
    full_name: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    # Criar objeto UserCreate para validação
    user_create = UserCreate(email=email, full_name=full_name, password=password)
    
    # Verificar se o email já existe
    db_user = db.query(User).filter(User.email == user_create.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Criptografa a senha
    hashed_password = get_password_hash(user_create.password)
    
    # Criar novo usuário
    new_user = User(
        email=user_create.email,
        full_name=user_create.full_name,
        hashed_password=hashed_password,
        is_active=True,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # Criar UserInDB para garantir que todos os campos estão corretos
    user_in_db = UserInDB(
        id=new_user.id,
        email=new_user.email,
        full_name=new_user.full_name,
        is_active=new_user.is_active,
        created_at=new_user.created_at,
        updated_at=new_user.updated_at,
        hashed_password=new_user.hashed_password
    )
    
    return f'<p class="text-green-500">User registered successfully! Welcome {user_in_db.full_name}</p>'
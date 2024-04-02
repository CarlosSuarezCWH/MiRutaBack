from fastapi import APIRouter, HTTPException
from models.user import UserModel
from config.database import conn
from schemas.user import LoginSchemas
from typing import List
from sqlalchemy import select
from passlib.context import CryptContext
import jwt
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

login_router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@login_router.post("/login")
def login(login: LoginSchemas) -> dict:
    try:
        query = select(UserModel).where(UserModel.c.email == login.email)
        user = conn.execute(query).first()
        if not user:
            raise HTTPException(status_code=401, detail="Credenciales inválidas")
        if not pwd_context.verify(login.password, user.password):
            raise HTTPException(status_code=401, detail="Credenciales inválidas")
        
        access_token = create_access_token(data={"email": user.email, "rol_id": user.rol_id})
        return {"access_token": access_token, "token_type": "bearer"}
    except jwt.PyJWTError as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor al generar token")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor al iniciar sesión")
# Compare this snippet from models/user.py:
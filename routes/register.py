from fastapi import FastAPI, HTTPException, APIRouter
from models.user import UserModel
from config.database import conn
from schemas.user import RegisterSchema
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
import logging

app = FastAPI()

register_router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Configuración básica de logging para capturar errores
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

@register_router.post("/register", response_model=RegisterSchema)
def register(user: RegisterSchema):
    try:
        # Verificar si el correo ya está registrado
        existing_user = conn.execute(select(UserModel).where(UserModel.c.email == user.email)).first()
        if existing_user:
            print(f"Correo electrónico ya registrado: {user.email}")
            raise HTTPException(status_code=400, detail="El correo electrónico ya está registrado")
        
        # Hash de la contraseña
        hashed_password = pwd_context.hash(user.password)
        
        # Crear diccionario para el nuevo usuario
        new_user = {
            "full_name": user.full_name,
            "email": user.email,
            "password": hashed_password,
            "rol_id": user.rol_id
        }
        
        # Insertar usuario en la base de datos
        result = conn.execute(UserModel.insert().values(new_user))
        conn.commit()
        inserted_user_id = result.lastrowid
        
        # Consultar el usuario recién creado
        query = select(UserModel).where(UserModel.c.id == inserted_user_id)
        created_user = conn.execute(query).first()
        
        print(f"Usuario registrado exitosamente: {created_user}")
        return created_user
    except SQLAlchemyError as e:
        # Registra detalles del error de SQLAlchemy
        logger.error(f"Error de SQLAlchemy: {e}")
        print(f"Error de SQLAlchemy: {e}")
        # Lanza una excepción HTTP con un mensaje genérico
        raise HTTPException(status_code=500, detail="Error interno del servidor al registrar usuario")
    except HTTPException:
        # Captura las excepciones HTTP y las relanza
        raise
    except Exception as e:
        # Registra detalles del error
        logger.error(f"Error en la función de registro: {e}")
        print(f"Error en la función de registro: {e}")
        # Lanza una excepción HTTP con un mensaje genérico
        raise HTTPException(status_code=500, detail="Error interno del servidor al registrar usuario")

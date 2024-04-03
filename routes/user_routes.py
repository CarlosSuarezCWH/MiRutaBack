from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session,sessionmaker
from passlib.context import CryptContext
from datetime import datetime, timedelta
from schemas.UserSchema import UserLoginSchema, UserResponseSchema, UserCreateSchema, UserUpdateSchema, UserDeleteSchema
from models.User import User as UserModel
from config.database import engine
from config.database import conn
import logging
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
import jwt

router = APIRouter()
SessionLocal = sessionmaker(bind=engine)


# Configuración del algoritmo de hash para las contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Configuración del token JWT
SECRET_KEY = "your_secret_key"  # Deberías cambiar esto en producción
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Función para obtener la conexión a la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Función para generar un token JWT
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post("/login")
def login(user: UserLoginSchema):
    try:
        # Verificar si el usuario existe en la base de datos
        db_user = conn.execute(select(UserModel).where(UserModel.c.email == user.email)).first()
        if not db_user:
            print(f"Usuario no encontrado: {user.email}")
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        # Verificar si la contraseña es correcta
        if not pwd_context.verify(user.password, db_user.password):
            print(f"Contraseña incorrecta para el usuario: {user.email}")
            raise HTTPException(status_code=400, detail="Contraseña incorrecta")
        
        # Generar un token de acceso
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": db_user.email}, expires_delta=access_token_expires
        )
        
        # Devolver el token de acceso
        return {"access_token": access_token, "token_type": "bearer"}
    except SQLAlchemyError as e:
        # Registra detalles del error de SQLAlchemy
        #logger.error(f"Error de SQLAlchemy: {e}")
        print(f"Error de SQLAlchemy: {e}")
        # Lanza una excepción HTTP con un mensaje genérico
        raise HTTPException(status_code=500, detail="Error interno del servidor al iniciar sesión")
    except HTTPException:
        # Captura las excepciones HTTP y las relanza
        raise
    except Exception as e:
        # Registra detalles del error
        #logger.error(f"Error en la función de inicio de sesión: {e}")
        print(f"Error en la función de inicio de sesión: {e}")
        # Lanza una excepción HTTP con un mensaje genérico
        raise HTTPException(status_code=500, detail="Error interno del servidor al iniciar sesión")





@router.post("/register", response_model=UserCreateSchema)
def register(user: UserCreateSchema):
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
        #logger.error(f"Error de SQLAlchemy: {e}")
        print(f"Error de SQLAlchemy: {e}")
        # Lanza una excepción HTTP con un mensaje genérico
        raise HTTPException(status_code=500, detail="Error interno del servidor al registrar usuario")
    except HTTPException:
        # Captura las excepciones HTTP y las relanza
        raise
    except Exception as e:
        # Registra detalles del error
        #logger.error(f"Error en la función de registro: {e}")
        print(f"Error en la función de registro: {e}")
        # Lanza una excepción HTTP con un mensaje genérico
        raise HTTPException(status_code=500, detail="Error interno del servidor al registrar usuario")


@router.get("/users/{user_id}", response_model=UserResponseSchema)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    # Obtener un usuario por su ID de la base de datos
    db_user = db.query(UserModel).filter(UserModel.c.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user




@router.delete("/users/{user_id}")
async def delete_user(user: UserDeleteSchema):
    try:
        # Eliminar un usuario de la base de datos
        result = conn.execute(UserModel.delete().where(UserModel.c.id == user.id))
        conn.commit()
        if result.rowcount == 0:
            print(f"Usuario no encontrado: {user.id}")
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        print(f"Usuario eliminado exitosamente: {user.id}")
        return {"message": "Usuario eliminado exitosamente"}
    except SQLAlchemyError as e:
        # Registra detalles del error de SQLAlchemy
        #logger.error(f"Error de SQLAlchemy: {e}")
        print(f"Error de SQLAlchemy: {e}")
        # Lanza una excepción HTTP con un mensaje genérico
        raise HTTPException(status_code=500, detail="Error interno del servidor al eliminar usuario")
    except HTTPException:
        # Captura las excepciones HTTP y las relanza
        raise
    except Exception as e:
        # Registra detalles del error
        #logger.error(f"Error en la función de eliminación de usuario: {e}")
        print(f"Error en la función de eliminación de usuario: {e}")
        # Lanza una excepción HTTP con un mensaje genérico
        raise HTTPException(status_code=500, detail="Error interno del servidor al eliminar usuario")
    


from fastapi import FastAPI, HTTPException, APIRouter
from models.terminales import TerminalModel
from config.database import conn
from schemas.terminal import TerminalSchema
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
import logging

app = FastAPI()

terminal_router = APIRouter()

# Configuración básica de logging para capturar errores
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

def terminal_to_dict(terminal):
    return {
        "id": terminal.id,
        "name": terminal.name,
        # Agrega más atributos si es necesario
    }

@terminal_router.get("/terminals")
def get_terminales():
    try:
        terminales = conn.execute(select(TerminalModel)).fetchall()
        # Convertir los objetos TerminalModel en diccionarios
        terminales_dict = [terminal_to_dict(terminal) for terminal in terminales]
        return terminales_dict
    except SQLAlchemyError as e:
        # Registra detalles del error de SQLAlchemy
        logger.error(f"Error de SQLAlchemy: {e}")
        print(f"Error de SQLAlchemy: {e}")
        # Lanza una excepción HTTP con un mensaje genérico
        raise HTTPException(status_code=500, detail="Error interno del servidor al obtener terminales")
    except HTTPException:
        # Captura las excepciones HTTP y las relanza
        raise
    except Exception as e:
        # Registra detalles del error
        logger.error(f"Error: {e}")
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor al obtener terminales")

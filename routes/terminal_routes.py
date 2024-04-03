from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.TerminalSchema import TerminalCreateSchema, TerminalUpdateSchema, TerminalResponseSchema
from models.Terminal import Terminal as TerminalModel
from config.database import  engine,conn
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

router = APIRouter()

# Función para obtener la instancia de la sesión de la base de datos
def get_db():
    db = engine.connect()
    try:
        yield db
    finally:
        db.close()

def terminal_to_dict(terminal):
    return {
        "id": terminal.id,
        "name": terminal.name,
        # Agrega más atributos si es necesario
    }

@router.post("/terminals/", response_model=TerminalResponseSchema)
async def create_terminal(terminal: TerminalCreateSchema, db: Session = Depends(get_db)):
    # Lógica para crear una nueva terminal en la base de datos
    db_terminal = TerminalModel(**terminal.dict())
    db.add(db_terminal)
    db.commit()
    db.refresh(db_terminal)
    return db_terminal


@router.get("/terminals")
def get_terminales():
    try:
        terminales = conn.execute(select(TerminalModel)).fetchall()
        # Convertir los objetos TerminalModel en diccionarios
        terminales_dict = [terminal_to_dict(terminal) for terminal in terminales]
        return terminales_dict
    except SQLAlchemyError as e:
        # Registra detalles del error de SQLAlchemy
        #logger.error(f"Error de SQLAlchemy: {e}")
        #print(f"Error de SQLAlchemy: {e}")
        # Lanza una excepción HTTP con un mensaje genérico
        raise HTTPException(status_code=500, detail="Error interno del servidor al obtener terminales")
    except HTTPException:
        # Captura las excepciones HTTP y las relanza
        raise
    except Exception as e:
        # Registra detalles del error
        #logger.error(f"Error: {e}")
        #print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor al obtener terminales")


@router.put("/terminals/{terminal_id}", response_model=TerminalResponseSchema)
async def update_terminal(terminal_id: int, terminal: TerminalUpdateSchema, db: Session = Depends(get_db)):
    # Lógica para actualizar la información de una terminal por su ID
    db_terminal = db.query(TerminalModel).filter(TerminalModel.id == terminal_id).first()
    if not db_terminal:
        raise HTTPException(status_code=404, detail="Terminal not found")
    for var, value in vars(terminal).items():
        setattr(db_terminal, var, value) if value else None
    db.commit()
    db.refresh(db_terminal)
    return db_terminal

@router.delete("/terminals/{terminal_id}")
async def delete_terminal(terminal_id: int, db: Session = Depends(get_db)):
    # Lógica para eliminar una terminal por su ID
    db_terminal = db.query(TerminalModel).filter(TerminalModel.id == terminal_id).first()
    if not db_terminal:
        raise HTTPException(status_code=404, detail="Terminal not found")
    db.delete(db_terminal)
    db.commit()
    return {"message": "Terminal deleted successfully"}

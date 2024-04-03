from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.TransactionSchema import TransactionCreateSchema, TransactionResponseSchema
from models.Transaction import Transaction as TransactionModel
from config.database import  engine

router = APIRouter()

# Función para obtener la instancia de la sesión de la base de datos
def get_db():
    db = engine.connect()
    try:
        yield db
    finally:
        db.close()

@router.post("/transactions/", response_model=TransactionResponseSchema)
async def create_transaction(transaction: TransactionCreateSchema, db: Session = Depends(get_db)):
    # Lógica para crear una nueva transacción en la base de datos
    db_transaction = TransactionModel(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@router.get("/transactions/{transaction_id}", response_model=TransactionResponseSchema)
async def get_transaction(transaction_id: int, db: Session = Depends(get_db)):
    # Lógica para obtener información de una transacción por su ID
    db_transaction = db.query(TransactionModel).filter(TransactionModel.id == transaction_id).first()
    if not db_transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return db_transaction

# Puedes agregar rutas adicionales para actualizar, eliminar, etc., según sea necesario

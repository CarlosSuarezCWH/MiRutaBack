from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.TicketTypeSchema import TicketTypeCreateSchema, TicketTypeUpdateSchema, TicketTypeResponseSchema
from models.TicketType import TicketType as TicketTypeModel
from config.database import engine

router = APIRouter()

# Función para obtener la instancia de la sesión de la base de datos
def get_db():
    db = engine.connect()
    try:
        yield db
    finally:
        db.close()

@router.post("/ticket-types/", response_model=TicketTypeResponseSchema)
async def create_ticket_type(ticket_type: TicketTypeCreateSchema, db: Session = Depends(get_db)):
    # Lógica para crear un nuevo tipo de boleto en la base de datos
    db_ticket_type = TicketTypeModel(**ticket_type.dict())
    db.add(db_ticket_type)
    db.commit()
    db.refresh(db_ticket_type)
    return db_ticket_type

@router.get("/ticket-types/{ticket_type_id}", response_model=TicketTypeResponseSchema)
async def get_ticket_type(ticket_type_id: int, db: Session = Depends(get_db)):
    # Lógica para obtener información de un tipo de boleto por su ID
    db_ticket_type = db.query(TicketTypeModel).filter(TicketTypeModel.id == ticket_type_id).first()
    if not db_ticket_type:
        raise HTTPException(status_code=404, detail="Ticket Type not found")
    return db_ticket_type

@router.put("/ticket-types/{ticket_type_id}", response_model=TicketTypeResponseSchema)
async def update_ticket_type(ticket_type_id: int, ticket_type: TicketTypeUpdateSchema, db: Session = Depends(get_db)):
    # Lógica para actualizar la información de un tipo de boleto por su ID
    db_ticket_type = db.query(TicketTypeModel).filter(TicketTypeModel.id == ticket_type_id).first()
    if not db_ticket_type:
        raise HTTPException(status_code=404, detail="Ticket Type not found")
    for var, value in vars(ticket_type).items():
        setattr(db_ticket_type, var, value) if value else None
    db.commit()
    db.refresh(db_ticket_type)
    return db_ticket_type

@router.delete("/ticket-types/{ticket_type_id}")
async def delete_ticket_type(ticket_type_id: int, db: Session = Depends(get_db)):
    # Lógica para eliminar un tipo de boleto por su ID
    db_ticket_type = db.query(TicketTypeModel).filter(TicketTypeModel.id == ticket_type_id).first()
    if not db_ticket_type:
        raise HTTPException(status_code=404, detail="Ticket Type not found")
    db.delete(db_ticket_type)
    db.commit()
    return {"message": "Ticket Type deleted successfully"}

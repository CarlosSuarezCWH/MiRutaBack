from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.TicketSchema import TicketCreateSchema, TicketUpdateSchema, TicketResponseSchema
from models.Ticket import Ticket as TicketModel
from config.database import  engine, conn
from sqlalchemy.orm import sessionmaker

router = APIRouter()
SessionLocal = sessionmaker(bind=engine)


# Función para obtener la conexión a la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/tickets/", response_model=TicketResponseSchema)
async def create_ticket(ticket: TicketCreateSchema, db: Session = Depends(get_db)):
    # Lógica para crear un nuevo ticket en la base de datos
    db_ticket = TicketModel(**ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

@router.get("/tickets/{ticket_id}", response_model=TicketResponseSchema)
async def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    # Obtener un usuario por su ID de la base de datos
    db_ticket = db.query(TicketModel).filter(TicketModel.c.id == ticket_id).first()
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket


@router.put("/tickets/{ticket_id}", response_model=TicketResponseSchema)
async def update_ticket(ticket_id: int, ticket: TicketUpdateSchema, db: Session = Depends(get_db)):
    # Lógica para actualizar la información de un ticket por su ID
    db_ticket = db.query(TicketModel).filter(TicketModel.c.id == ticket_id).first()
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    for var, value in vars(ticket).items():
        setattr(db_ticket, var, value) if value else None
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

@router.delete("/tickets/{ticket_id}")
async def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    # Lógica para eliminar un ticket por su ID
    db_ticket = db.query(TicketModel).filter(TicketModel.id == ticket_id).first()
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    db.delete(db_ticket)
    db.commit()
    return {"message": "Ticket deleted successfully"}

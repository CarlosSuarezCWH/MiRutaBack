from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.BusSchema import BusCreateSchema, BusUpdateSchema, BusResponseSchema
from models.Bus import Bus as BusModel
from config.database import engine

router = APIRouter()

# Función para obtener la instancia de la sesión de la base de datos
def get_db():
    db = engine.connect()
    try:
        yield db
    finally:
        db.close()


@router.post("/buses/", response_model=BusResponseSchema)
async def create_bus(bus: BusCreateSchema, db: Session = Depends(get_db)):
    # Lógica para crear un nuevo autobús en la base de datos
    db_bus = BusModel(**bus.dict())
    db.add(db_bus)
    db.commit()
    db.refresh(db_bus)
    return db_bus

@router.get("/buses/{bus_id}", response_model=BusResponseSchema)
async def get_bus(bus_id: int, db: Session = Depends(get_db)):
    # Lógica para obtener información de un autobús por su ID
    db_bus = db.query(BusModel).filter(BusModel.id == bus_id).first()
    if not db_bus:
        raise HTTPException(status_code=404, detail="Bus not found")
    return db_bus

@router.put("/buses/{bus_id}", response_model=BusResponseSchema)
async def update_bus(bus_id: int, bus: BusUpdateSchema, db: Session = Depends(get_db)):
    # Lógica para actualizar la información de un autobús por su ID
    db_bus = db.query(BusModel).filter(BusModel.id == bus_id).first()
    if not db_bus:
        raise HTTPException(status_code=404, detail="Bus not found")
    for var, value in vars(bus).items():
        setattr(db_bus, var, value) if value else None
    db.commit()
    db.refresh(db_bus)
    return db_bus

@router.delete("/buses/{bus_id}")
async def delete_bus(bus_id: int, db: Session = Depends(get_db)):
    # Lógica para eliminar un autobús por su ID
    db_bus = db.query(BusModel).filter(BusModel.id == bus_id).first()
    if not db_bus:
        raise HTTPException(status_code=404, detail="Bus not found")
    db.delete(db_bus)
    db.commit()
    return {"message": "Bus deleted successfully"}

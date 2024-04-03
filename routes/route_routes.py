from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.RouteSchema import RouteCreateSchema, RouteUpdateSchema, RouteResponseSchema
from models.Route import Route as RouteModel
from config.database import  engine

router = APIRouter()

# Función para obtener la instancia de la sesión de la base de datos
def get_db():
    db = engine.connect()
    try:
        yield db
    finally:
        db.close()

@router.post("/routes/", response_model=RouteResponseSchema)
async def create_route(route: RouteCreateSchema, db: Session = Depends(get_db)):
    # Lógica para crear una nueva ruta en la base de datos
    db_route = RouteModel(**route.dict())
    db.add(db_route)
    db.commit()
    db.refresh(db_route)
    return db_route

@router.get("/routes/{route_id}", response_model=RouteResponseSchema)
async def get_route(route_id: int, db: Session = Depends(get_db)):
    # Lógica para obtener información de una ruta por su ID
    db_route = db.query(RouteModel).filter(RouteModel.id == route_id).first()
    if not db_route:
        raise HTTPException(status_code=404, detail="Route not found")
    return db_route

@router.put("/routes/{route_id}", response_model=RouteResponseSchema)
async def update_route(route_id: int, route: RouteUpdateSchema, db: Session = Depends(get_db)):
    # Lógica para actualizar la información de una ruta por su ID
    db_route = db.query(RouteModel).filter(RouteModel.id == route_id).first()
    if not db_route:
        raise HTTPException(status_code=404, detail="Route not found")
    for var, value in vars(route).items():
        setattr(db_route, var, value) if value else None
    db.commit()
    db.refresh(db_route)
    return db_route

@router.delete("/routes/{route_id}")
async def delete_route(route_id: int, db: Session = Depends(get_db)):
    # Lógica para eliminar una ruta por su ID
    db_route = db.query(RouteModel).filter(RouteModel.id == route_id).first()
    if not db_route:
        raise HTTPException(status_code=404, detail="Route not found")
    db.delete(db_route)
    db.commit()
    return {"message": "Route deleted successfully"}

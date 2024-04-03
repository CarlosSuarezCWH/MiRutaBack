from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.RoleSchema import RoleCreateSchema, RoleUpdateSchema, RoleResponseSchema
from models.Role import Role as RoleModel
from config.database import  engine

router = APIRouter()

# Función para obtener la instancia de la sesión de la base de datos
def get_db():
    db = engine.connect()
    try:
        yield db
    finally:
        db.close()

@router.post("/roles/", response_model=RoleResponseSchema)
async def create_role(role: RoleCreateSchema, db: Session = Depends(get_db)):
    # Lógica para crear un nuevo rol en la base de datos
    db_role = RoleModel(**role.dict())
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

@router.get("/roles/{role_id}", response_model=RoleResponseSchema)
async def get_role(role_id: int, db: Session = Depends(get_db)):
    # Lógica para obtener información de un rol por su ID
    db_role = db.query(RoleModel).filter(RoleModel.id == role_id).first()
    if not db_role:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

@router.put("/roles/{role_id}", response_model=RoleResponseSchema)
async def update_role(role_id: int, role: RoleUpdateSchema, db: Session = Depends(get_db)):
    # Lógica para actualizar la información de un rol por su ID
    db_role = db.query(RoleModel).filter(RoleModel.id == role_id).first()
    if not db_role:
        raise HTTPException(status_code=404, detail="Role not found")
    for var, value in vars(role).items():
        setattr(db_role, var, value) if value else None
    db.commit()
    db.refresh(db_role)
    return db_role

# Puedes agregar rutas adicionales para eliminar, etc., según sea necesario

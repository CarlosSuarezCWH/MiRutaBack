from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.PermissionSchema import PermissionCreateSchema, PermissionUpdateSchema, PermissionResponseSchema
from models.Permission import Permission as PermissionModel
from config.database import  engine

router = APIRouter()

# Función para obtener la instancia de la sesión de la base de datos
def get_db():
    db = engine.connect()
    try:
        yield db
    finally:
        db.close()

@router.post("/permissions/", response_model=PermissionResponseSchema)
async def create_permission(permission: PermissionCreateSchema, db: Session = Depends(get_db)):
    # Lógica para crear un nuevo permiso en la base de datos
    db_permission = PermissionModel(**permission.dict())
    db.add(db_permission)
    db.commit()
    db.refresh(db_permission)
    return db_permission

@router.get("/permissions/{permission_id}", response_model=PermissionResponseSchema)
async def get_permission(permission_id: int, db: Session = Depends(get_db)):
    # Lógica para obtener información de un permiso por su ID
    db_permission = db.query(PermissionModel).filter(PermissionModel.id == permission_id).first()
    if not db_permission:
        raise HTTPException(status_code=404, detail="Permission not found")
    return db_permission

@router.put("/permissions/{permission_id}", response_model=PermissionResponseSchema)
async def update_permission(permission_id: int, permission: PermissionUpdateSchema, db: Session = Depends(get_db)):
    # Lógica para actualizar la información de un permiso por su ID
    db_permission = db.query(PermissionModel).filter(PermissionModel.id == permission_id).first()
    if not db_permission:
        raise HTTPException(status_code=404, detail="Permission not found")
    for var, value in vars(permission).items():
        setattr(db_permission, var, value) if value else None
    db.commit()
    db.refresh(db_permission)
    return db_permission

# Puedes agregar rutas adicionales para eliminar, etc., según sea necesario

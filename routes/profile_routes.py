from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.ProfileSchema import ProfileCreateSchema, ProfileUpdateSchema, ProfileResponseSchema
from models.Profile import Profile as ProfileModel
from config.database import engine

router = APIRouter()

# Función para obtener la instancia de la sesión de la base de datos
def get_db():
    db = engine.connect()
    try:
        yield db
    finally:
        db.close()


@router.post("/profiles/", response_model=ProfileResponseSchema)
async def create_profile(profile: ProfileCreateSchema, db: Session = Depends(get_db)):
    # Lógica para crear un nuevo perfil de usuario en la base de datos
    db_profile = ProfileModel(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

@router.get("/profiles/{user_id}", response_model=ProfileResponseSchema)
async def get_profile(user_id: int, db: Session = Depends(get_db)):
    # Lógica para obtener información del perfil de un usuario por su ID
    db_profile = db.query(ProfileModel).filter(ProfileModel.user_id == user_id).first()
    if not db_profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return db_profile

@router.put("/profiles/{user_id}", response_model=ProfileResponseSchema)
async def update_profile(user_id: int, profile: ProfileUpdateSchema, db: Session = Depends(get_db)):
    # Lógica para actualizar la información del perfil de un usuario por su ID
    db_profile = db.query(ProfileModel).filter(ProfileModel.user_id == user_id).first()
    if not db_profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    for var, value in vars(profile).items():
        setattr(db_profile, var, value) if value else None
    db.commit()
    db.refresh(db_profile)
    return db_profile

# Puedes agregar rutas adicionales para eliminar, etc., según sea necesario

from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError


class LoginSchemas(BaseModel):
    email: str
    password: str

class RegisterSchema(BaseModel):
    full_name: str
    email: str
    password: str
    rol_id: int

class UserResponse(BaseModel):
    id: int
    full_name: str
    email: str
    rol_id: int
    created_at: Optional[datetime]

class RegisterResponse(BaseModel):
    message: str
    user: UserResponse

class LoginResponse(BaseModel): 
    message: str
    token: str



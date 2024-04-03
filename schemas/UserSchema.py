from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserCreateSchema(BaseModel):
    full_name: str
    email: str
    password: str
    rol_id: int
    registration_date: Optional[datetime]

class UserDeleteSchema(BaseModel):
    id: int


class UserUpdateSchema(BaseModel):
    id: int
    full_name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    rol_id: Optional[int]


class UserResponseSchema(BaseModel):
    id: int
    full_name: str
    email: str
    rol_id: int
    registration_date: datetime

class UserLoginSchema(BaseModel):
    email: str
    password: str

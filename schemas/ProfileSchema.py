from pydantic import BaseModel
from typing import Optional

class ProfileCreateSchema(BaseModel):
    user_id: int
    identification_route: Optional[str]
    phone: Optional[str]
    address: Optional[str]

class ProfileUpdateSchema(BaseModel):
    identification_route: Optional[str]
    phone: Optional[str]
    address: Optional[str]

class ProfileResponseSchema(BaseModel):
    user_id: int
    identification_route: Optional[str]
    phone: Optional[str]
    address: Optional[str]

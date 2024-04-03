from pydantic import BaseModel

class PermissionCreateSchema(BaseModel):
    name: str

class PermissionUpdateSchema(BaseModel):
    name: str

class PermissionResponseSchema(BaseModel):
    id: int
    name: str

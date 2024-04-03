from pydantic import BaseModel

class RoleCreateSchema(BaseModel):
    name: str

class RoleUpdateSchema(BaseModel):
    name: str

class RoleResponseSchema(BaseModel):
    id: int
    name: str
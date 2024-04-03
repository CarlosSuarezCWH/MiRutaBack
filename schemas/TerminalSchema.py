from pydantic import BaseModel

class TerminalCreateSchema(BaseModel):
    id: int
    name: str
    location: str

class TerminalUpdateSchema(BaseModel):
    id: int
    name: str
    location: str

class TerminalResponseSchema(BaseModel):
    id: int
    name: str
    location: str
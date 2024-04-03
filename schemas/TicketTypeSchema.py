from pydantic import BaseModel

class TicketTypeCreateSchema(BaseModel):
    name: str
    discount: float

class TicketTypeUpdateSchema(BaseModel):
    name: str
    discount: float

class TicketTypeResponseSchema(BaseModel):
    id: int
    name: str
    discount: float


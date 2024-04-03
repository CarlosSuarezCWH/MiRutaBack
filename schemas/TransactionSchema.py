from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TransactionCreateSchema(BaseModel):
    user_id: int
    ticket_id: Optional[int]
    amount: float
    date: Optional[datetime]

class TransactionResponseSchema(BaseModel):
    id: int
    user_id: int
    ticket_id: Optional[int]
    amount: float
    date: Optional[datetime]

from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError

class  TerminalModel(BaseModel):
    id: int
    name: str
    location: str

class TerminalSchema(BaseModel):
    name: str
    location: str
    full_name: str

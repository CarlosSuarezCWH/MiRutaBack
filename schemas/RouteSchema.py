from pydantic import BaseModel
from datetime import date, time
from typing import Optional

class RouteCreateSchema(BaseModel):
    origin: str
    destination: str
    schedule: time
    date: date
    base_price: float
    bus_type: str
    origin_terminal_id: Optional[int]
    destination_terminal_id: Optional[int]
    bus_id: Optional[int]

class RouteUpdateSchema(BaseModel):
    origin: Optional[str]
    destination: Optional[str]
    schedule: Optional[time]
    date: Optional[date]
    base_price: Optional[float]
    bus_type: Optional[str]
    origin_terminal_id: Optional[int]
    destination_terminal_id: Optional[int]
    bus_id: Optional[int]

class RouteResponseSchema(BaseModel):
    id: int
    origin: str
    destination: str
    schedule: time
    date: date
    base_price: float
    bus_type: str
    origin_terminal_id: Optional[int]
    destination_terminal_id: Optional[int]
    bus_id: Optional[int]

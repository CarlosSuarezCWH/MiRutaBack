from pydantic import BaseModel
from datetime import date
from typing import Optional

class TicketCreateSchema(BaseModel):
    user_id: int
    route_id: int
    ticket_type_id: int
    departure_date: date
    payment_status: str
    usage_status: str
    cost: float
    seat_number: Optional[int]
    trip_coverage: Optional[str]
    transaction_id: Optional[int]

class TicketUpdateSchema(BaseModel):
    user_id: Optional[int]
    route_id: Optional[int]
    ticket_type_id: Optional[int]
    departure_date: Optional[date]
    payment_status: Optional[str]
    usage_status: Optional[str]
    cost: Optional[float]
    seat_number: Optional[int]
    trip_coverage: Optional[str]
    transaction_id: Optional[int]

class TicketResponseSchema(BaseModel):
    id: int
    user_id: int
    route_id: int
    ticket_type_id: int
    departure_date: date
    payment_status: str
    usage_status: str
    cost: float
    seat_number: Optional[int]
    trip_coverage: Optional[str]
    transaction_id: Optional[int]
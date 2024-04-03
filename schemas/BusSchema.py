from pydantic import BaseModel
from typing import Optional

class BusCreateSchema(BaseModel):
    model: str
    capacity: int
    manufacturer: Optional[str]
    manufacture_year: Optional[int]
    engine_type: Optional[str]
    length: Optional[float]
    width: Optional[float]
    height: Optional[float]
    seat_count: Optional[int]
    door_count: Optional[int]
    window_count: Optional[int]
    air_conditioning: Optional[str]
    seat_type: Optional[str]
    entertainment_system: Optional[str]
    other_features: Optional[str]

class BusUpdateSchema(BaseModel):
    model: Optional[str]
    capacity: Optional[int]
    manufacturer: Optional[str]
    manufacture_year: Optional[int]
    engine_type: Optional[str]
    length: Optional[float]
    width: Optional[float]
    height: Optional[float]
    seat_count: Optional[int]
    door_count: Optional[int]
    window_count: Optional[int]
    air_conditioning: Optional[str]
    seat_type: Optional[str]
    entertainment_system: Optional[str]
    other_features: Optional[str]

class BusResponseSchema(BaseModel):
    id: int
    model: str
    capacity: int
    manufacturer: Optional[str]
    manufacture_year: Optional[int]
    engine_type: Optional[str]
    length: Optional[float]
    width: Optional[float]
    height: Optional[float]
    seat_count: Optional[int]
    door_count: Optional[int]
    window_count: Optional[int]
    air_conditioning: Optional[str]
    seat_type: Optional[str]
    entertainment_system: Optional[str]
    other_features: Optional[str]

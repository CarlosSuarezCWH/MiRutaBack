from sqlalchemy import Table,Column, Integer, String, DECIMAL, Enum
from config.database import meta

Bus = Table(
    "buses",
    meta,
    Column("id", Integer, primary_key=True),
    Column("model", String(255), nullable=False),
    Column("capacity", Integer, nullable=False),
    Column("manufacturer", String(255)),
    Column("manufacture_year", Integer),
    Column("engine_type", String(100)),
    Column("length", DECIMAL(10, 2)),
    Column("width", DECIMAL(10, 2)),
    Column("height", DECIMAL(10, 2)),
    Column("seat_count", Integer),
    Column("door_count", Integer),
    Column("window_count", Integer),
    Column("air_conditioning", Enum('Yes', 'No', name='air_conditioning_enum')),
    Column("seat_type", String(100)),
    Column("entertainment_system", Enum('Yes', 'No', name='entertainment_system_enum')),
    Column("other_features", String)
)

from sqlalchemy import Table, Column, Integer, String, Date, Time, DECIMAL, Enum
from config.database import meta

Route = Table(
    "routes",
    meta,
    Column("id", Integer, primary_key=True),
    Column("origin", String(255), nullable=False),
    Column("destination", String(255), nullable=False),
    Column("schedule", Time, nullable=False),
    Column("date", Date, nullable=False),
    Column("base_price", DECIMAL(10, 2), nullable=False),
    Column("bus_type", Enum('economy', 'executive', 'premium', name='bus_type_enum'), nullable=False),
    Column("origin_terminal_id", Integer),
    Column("destination_terminal_id", Integer),
    Column("bus_id", Integer)
)

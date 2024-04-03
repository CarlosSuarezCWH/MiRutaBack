from sqlalchemy import Table, Column, Integer, String, Date, Enum, DECIMAL
from config.database import meta

Ticket = Table(
    "tickets",
    meta,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer),
    Column("route_id", Integer),
    Column("ticket_type_id", Integer),
    Column("departure_date", Date),
    Column("payment_status", Enum('pending', 'paid', name='payment_status_enum'), default='pending'),
    Column("usage_status", Enum('not used', 'used', name='usage_status_enum'), default='not used'),
    Column("cost", DECIMAL(10, 2), nullable=False),
    Column("seat_number", Integer),
    Column("trip_coverage", String(255)),
    Column("transaction_id", Integer)
)

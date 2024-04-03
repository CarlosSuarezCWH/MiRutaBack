from sqlalchemy import Table, Column, Integer, String, DECIMAL
from config.database import meta

TicketType = Table(
    "ticket_types",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("discount", DECIMAL(10, 2), nullable=False)
)

from sqlalchemy import Table, Column, Integer, DECIMAL, TIMESTAMP
from config.database import meta
from sqlalchemy.sql import func

Transaction = Table(
    "transactions",
    meta,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, nullable=False),
    Column("ticket_id", Integer),
    Column("amount", DECIMAL(10, 2), nullable=False),
    Column("date", TIMESTAMP, nullable=False, server_default=func.current_timestamp())
)

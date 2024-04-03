from sqlalchemy import Table, Column, Integer, String
from config.database import meta

Terminal = Table(
    "terminals",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255), nullable=False),
    Column("location", String(255), nullable=False),
    Column("full_name", String(255), nullable=False)
)

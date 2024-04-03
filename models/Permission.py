from sqlalchemy import Table, Column, Integer, String
from config.database import meta

Permission = Table(
    "permissions",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False)
)

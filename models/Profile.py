from sqlalchemy import Table, Column, String, Integer, ForeignKey
from config.database import meta

Profile = Table(
    "profiles",
    meta,
    Column("user_id", Integer, ForeignKey('users.id'), primary_key=True),
    Column("identification_route", String(255)),
    Column("phone", String(255)),
    Column("address", String(255))
)

from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from config.database import meta

User = Table("user",meta,
    Column("id", Integer, primary_key=True ,autoincrement=True),
    Column("email",String(255),nullable=False),
    Column("password", String(255), nullable=False),
    Column("full_name", String(255), nullable=False),
    Column("rol_id", Integer, nullable=False),
    Column("registration_date", DateTime, nullable=True)
)



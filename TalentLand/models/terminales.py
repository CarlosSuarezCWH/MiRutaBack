from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from config.database import meta, engine
from sqlalchemy.sql import func

TerminalModel = Table("terminal",meta,
    Column("id", Integer, primary_key=True ,autoincrement=True),
    Column("name",String(255),nullable=False),
    Column("location", String(255), nullable=False)
)

meta.create_all(engine)

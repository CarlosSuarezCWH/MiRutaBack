from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import SQLAlchemyError

#prod
engine = create_engine("mysql+pymysql://muud_flecha:elemental1302@107.161.75.132:3306/muud_flechadev")

#dev
#engine = create_engine("sqlite:///test.db")

meta = MetaData()
conn = engine.connect()

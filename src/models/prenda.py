from config.database import Base
from sqlalchemy import Column, Integer, String

class Prenda(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    img = Column(String)
    tipo = Column(String)

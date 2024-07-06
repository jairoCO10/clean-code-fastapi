from sqlalchemy.sql.sqltypes import DateTime
# from ..Connection.Connection import Base
from App.infrastructure.database import Connection
from sqlalchemy import Column, Integer, String, Boolean, BigInteger
import datetime


class User(Connection.Base):
    __tablename__ = 'usuarios'
    id = Column(BigInteger , primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=True)
    users= Column(String(255), nullable=True)
    password = Column(String(255), nullable=True) # Especifica el nombre de la columna en la base de datos
    cellphone = Column(String(20), nullable=True, unique= True)
    email = Column(String(255), nullable=True, unique= True)
    is_admin = Column(Boolean, nullable=True, default=False)
    is_staff = Column(Boolean, nullable=True, default=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.datetime.now)

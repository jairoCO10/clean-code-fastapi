from sqlalchemy.sql.sqltypes import DateTime
# from ..Connection.Connection import Base
from App.infrastructure.database import Connection
from sqlalchemy import Column, Integer, String, Boolean, BigInteger, Text
import datetime


class AuthGroup(Connection.Base):
    __tablename__ = 'auth_group'
    id = Column(BigInteger , primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=True, unique=True)
    description= Column(Text, nullable=True, default=False)
    deactivated_at = Column(DateTime, onupdate=datetime.datetime.now)
    deactivate = Column(Boolean, nullable=True, unique= True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.datetime.now)
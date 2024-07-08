from App.infrastructure.database import Connection
from sqlalchemy import Column, Integer,  BigInteger



class AuthUserGroup(Connection.Base):
    __tablename__ = 'auth_user_groups'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    group_id= Column(Integer)
   
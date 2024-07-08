from App.infrastructure.database import Connection
from sqlalchemy import Column, Integer,  BigInteger



class AuthGroupPermissions(Connection.Base):

    __tablename__ = 'auth_group_permissions'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    group_id= Column(Integer)





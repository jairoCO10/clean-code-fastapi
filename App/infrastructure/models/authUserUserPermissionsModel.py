


from App.infrastructure.database import Connection
from sqlalchemy import Column, Integer,  BigInteger,String



class AuthUserPermissions(Connection.Base):

    __tablename__ = 'auth_user_user_permissions'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    permission_id= Column(Integer)








from App.infrastructure.database import Connection
from sqlalchemy import Column, Integer,  BigInteger,String



class AuthPermissions(Connection.Base):

    __tablename__ = 'auth_permission'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=True)
    content_type_id= Column(Integer, nullable=True)
    codename= Column(String(100), nullable=True)





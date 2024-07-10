


from App.infrastructure.database import Connection
from sqlalchemy import Column, Integer,  BigInteger,String



class ContentType(Connection.Base):

    __tablename__ = 'content_type'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    app_label = Column(String(255), nullable=True)
    model= Column(String(255), nullable=True)
   
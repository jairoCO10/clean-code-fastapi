from sqlalchemy.orm import Session
from App.infrastructure.models.usersModel import User as ORMUser
from sqlalchemy.future import select
from typing import List
from App.infrastructure.models.contentTypeModel import ContentType as ORMContenType


class ContenTypeService:
    def __init__(self, db:Session):
        self.connection = db


    async def reads_contentype(self)->List[ORMContenType]:
        result = self.connection.execute(select(ORMContenType))
        content_types = result.scalars().all()
        return content_types
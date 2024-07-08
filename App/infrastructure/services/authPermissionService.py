from sqlalchemy.orm import Session
from App.infrastructure.models.usersModel import User as ORMUser
from sqlalchemy.future import select
from typing import List
from App.infrastructure.models.authGroupModel import AuthGroup as ORMAuthgroup
from App.infrastructure.models.authPermissionModel import AuthPermissions as ORMPermissions


class PermissionService:
    def __init__(self, db:Session):
        self.connection = db


    async def read_auth_permissions(self) -> List[ORMPermissions]:
        result = self.connection.execute(select(ORMPermissions))
        orm_auth_permissions = result.scalars().all()

        for orm_auth in orm_auth_permissions:
            print(f"Fetched auth group: {orm_auth}")

        return orm_auth_permissions


    async def read_auth_permission(self, permission_id: int) -> ORMPermissions:
        result = self.connection.execute(select(ORMPermissions).filter(ORMPermissions.id == permission_id))
        return result.scalars().first()

    async def create_auth_permission(self, name:str, content_type_id:int, codename:str)->ORMPermissions:
        auth_permission= ORMPermissions(
            name=name,
            content_type_id=content_type_id,
            codename = codename
        )
        self.connection.add(auth_permission)
        self.connection.commit()
        self.connection.refresh(auth_permission)
        return auth_permission


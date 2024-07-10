from sqlalchemy.orm import Session
from App.infrastructure.models.usersModel import User as ORMUser
from sqlalchemy.future import select
from typing import List
from App.infrastructure.models.authGroupModel import AuthGroup as ORMAuthgroup
from App.infrastructure.models.authPermissionModel import AuthPermissions as ORMPermissions
from App.infrastructure.models.authUserUserPermissionsModel import AuthUserPermissions as ORMUserPermission
from App.infrastructure.models.authGroupPermissionsModel import AuthGroupPermissions as ORMGroupPermission


class PermissionService:
    def __init__(self, db:Session):
        self.connection = db


    async def read_auth_permissions(self) -> List[ORMPermissions]:
        result = self.connection.execute(select(ORMPermissions))
        orm_auth_permissions = result.scalars().all()
        return orm_auth_permissions


    async def read_auth_permission(self, permission_id: int) -> ORMPermissions:
        result = self.connection.execute(select(ORMPermissions).filter(ORMPermissions.id == permission_id))
        return result.scalars().first()
    
    async def read_auth_permission_content_type(self, content_type_id: int) -> List[ORMPermissions]:
        result = self.connection.execute(select(ORMPermissions).filter(ORMPermissions.content_type_id == content_type_id))
        orm_auth_permissions = result.scalars().all()
        return orm_auth_permissions


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
    
    async def list_user_permission(self,users_id:int, permission_id:int)->ORMUserPermission:
        result = self.connection.execute(select(ORMUserPermission).filter(ORMUserPermission.user_id == users_id, ORMUserPermission.permission_id==permission_id))
        return  result.scalars().first()
    

    async def list_group_permission(self,group_id:int, permission_id:int)->ORMGroupPermission:
        result = self.connection.execute(select(ORMGroupPermission).filter(ORMGroupPermission.group_id == group_id, ORMUserPermission.permission_id==permission_id))
        return  result.scalars().first()
        
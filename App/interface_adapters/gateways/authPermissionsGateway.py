# app/interface_adapters/gateways/db_gateway.py
from typing import List
from sqlalchemy.orm import Session
from fastapi import  HTTPException, status
from App.core.entities.authPermissionEntities import CreateAuthPermissions,AuthPermissions
from App.infrastructure.services.authPermissionService import PermissionService




class AuthPermissionGateway:


    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.permission_repository = PermissionService(self.db_session)
        self.detail="register no found"


    async def create_auth_permission(self,  name: str, content_type_id:str, codename:str) -> AuthPermissions:
        
        orm_permission = await self.permission_repository.create_auth_permission(name, content_type_id, codename)
        return AuthPermissions(id=orm_permission.id,
                        name=orm_permission.name,
                        content_type_id=orm_permission.content_type_id,
                        codename= orm_permission.codename,
        )



    async def read_auth_permissions(self) -> List[AuthPermissions]:
        orm_permissions = await self.permission_repository.read_auth_permissions()
        auth_groups = []
        for orm_permission in orm_permissions:

            auth_groups.append(
                AuthPermissions(id=orm_permission.id,
                        name=orm_permission.name,
                        content_type_id=orm_permission.content_type_id,
                        codename= orm_permission.codename,
        ))
        return auth_groups


    async def read_auth_permission(self, auth_id: int) -> AuthPermissions:
        orm_permission = await self.permission_repository.read_auth_permission(auth_id)
        if orm_permission:
            return AuthPermissions(id=orm_permission.id,
                        name=orm_permission.name,
                        content_type_id=orm_permission.content_type_id,
                        codename= orm_permission.codename,
        )
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail= self.detail
            )

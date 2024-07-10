# app/interface_adapters/gateways/db_gateway.py
from typing import List
from sqlalchemy.orm import Session
from fastapi import  HTTPException, status
from App.core.entities.authPermissionEntities import CreateAuthPermissions,AuthPermissions, UserPermission, ContentType,AuthPermissions2, GroupPermission
from App.infrastructure.services.authPermissionService import PermissionService
from App.infrastructure.services.usersServices import UserRepository
from App.infrastructure.services.authService import AuthService
from App.infrastructure.services.authContentTypeService import ContenTypeService




class AuthPermissionGateway:


    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.permission_repository = PermissionService(self.db_session)
        self.use_repository = UserRepository(self.db_session)
        self.group_repository = AuthService(self.db_session)
        self.content_type_repository = ContenTypeService(self.db_session)
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
    
    async def read_user_permissions(self, users_id:int)->UserPermission:
        orm_user = await self.use_repository.get_user(users_id)
        if orm_user:
            content_type = []
            orm_contenttypes = await self.content_type_repository.reads_contentype()
            for orm_contenttype in orm_contenttypes:
                orm_permissions = await self.permission_repository.read_auth_permission_content_type(orm_contenttype.id)
                permissions=[]

                for orm_permission in orm_permissions:
                    list_permission = await self.permission_repository.list_user_permission(orm_user.id, orm_permission.id)
                    status_permission = False if not list_permission else True
                    permissions.append(AuthPermissions2(id=orm_permission.id,
                        name=orm_permission.name,
                        content_type_id=orm_permission.content_type_id,
                        codename= orm_permission.codename,
                        status_permission = status_permission
                ))

                content_type.append(ContentType(id = orm_contenttype.id,
                                                app_label= orm_contenttype.app_label,
                                                model= orm_contenttype.model,
                                                permission =permissions
                                                ))
            return UserPermission(id= orm_user.id,
                            name= orm_user.name,
                              content_type=content_type
                            )
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail= self.detail
            )
    
    async def read_group_permissions(self, group_id:int)->GroupPermission:
        orm_group = await self.group_repository.get_auth_group(group_id)
        if orm_group:
            content_type = []
            orm_contenttypes = await self.content_type_repository.reads_contentype()
            for orm_contenttype in orm_contenttypes:
                orm_permissions = await self.permission_repository.read_auth_permission_content_type(orm_contenttype.id)
                permissions=[]

                for orm_permission in orm_permissions:
                    list_permission = await self.permission_repository.list_group_permission(orm_group.id, orm_permission.id)
                    status_permission = False if not list_permission else True
                    permissions.append(AuthPermissions2(id=orm_permission.id,
                        name=orm_permission.name,
                        content_type_id=orm_permission.content_type_id,
                        codename= orm_permission.codename,
                        status_permission = status_permission
                ))

                content_type.append(ContentType(id = orm_contenttype.id,
                                                app_label= orm_contenttype.app_label,
                                                model= orm_contenttype.model,
                                                permission = permissions
                                                ))
            return GroupPermission(id= orm_group.id,
                            name= orm_group.name,
                            content_type=content_type
                            )
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail= self.detail
            )

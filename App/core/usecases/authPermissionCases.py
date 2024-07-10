# app/core/usecases/user_usecase.py
from typing import List
from App.core.entities.authGroupEntities import AuthGroup, CreateAuthGroup
from App.core.entities.authPermissionEntities import AuthPermissions, CreateAuthPermissions
from App.interface_adapters.gateways.authGroupGateways import AuthGroupGateway
from App.interface_adapters.gateways.authPermissionsGateway import AuthPermissionGateway

class AuthPermissionUseCase:
    def __init__(self, authpermission_gateway: AuthPermissionGateway):
        self.authpermission_gateway = authpermission_gateway

    async def create_auth_permission(self, name: str, description:str) -> CreateAuthPermissions:
        return await self.authpermission_gateway.create_auth_permission(name, description)


    async def read_auth_permission(self, authroup_id: int) -> AuthPermissions:
        return await self.authpermission_gateway.read_auth_permission(authroup_id)
    
    async def read_auth_permissions(self,) -> AuthPermissions:
        return await self.authpermission_gateway.read_auth_permissions()
    
    async def read_user_permissions(self, users_id:int):
        return await self.authpermission_gateway.read_user_permissions(users_id)
    
    async def read_group_permissions(self, group_id:int):
        return await self.authpermission_gateway.read_group_permissions(group_id)

    
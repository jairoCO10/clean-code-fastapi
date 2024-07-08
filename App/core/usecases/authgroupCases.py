# app/core/usecases/user_usecase.py
from typing import List
from App.core.entities.authGroupEntities import AuthGroup, CreateAuthGroup
from App.interface_adapters.gateways.authGroupGateways import AuthGroupGateway

class AuthGroupUseCase:
    def __init__(self, authgroup_gateway: AuthGroupGateway):
        self.authgroup_gateway = authgroup_gateway

    async def create_auth_group(self, name: str, description:str) -> CreateAuthGroup:
        return await self.authgroup_gateway.create_auth_group(name, description)

    async def get_auth_group(self, authroup_id: int) -> AuthGroup:
        return await self.authgroup_gateway.get_auth_group(authroup_id)
    
    async def get_auth_groups(self,) -> AuthGroup:
        return await self.authgroup_gateway.get_auth_groups()

    async def update_auth_group(self, authroup_id: int, name: str, description: str, deactivate:bool) -> AuthGroup:
        return await self.authgroup_gateway.update_auth_group(authroup_id, name, description, deactivate)

    async def delete_auth_group(self, user_id: int) -> AuthGroup:
        return await self.authgroup_gateway.delete_auth_group(user_id)
    
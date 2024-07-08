# app/interface_adapters/gateways/db_gateway.py
from typing import List
from sqlalchemy.orm import Session
from fastapi import  HTTPException, status
from App.core.entities.authGroupEntities import AuthGroup

from App.infrastructure.services.usersServices import UserRepository
from App.infrastructure.services.authService import AuthService



class AuthGroupGateway:


    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.repository = UserRepository(self.db_session)
        self.auth_repository = AuthService(self.db_session)
        self.detail="register no found"


    async def create_auth_group(self,  name: str,description:str) -> AuthGroup:
        orm_auth_by_name = await self.auth_repository.get_auth_group_name(name)

        if not orm_auth_by_name:


            orm_auth = await self.auth_repository.create_auth_group(name, description)
            return AuthGroup(id=orm_auth.id,
                            name=orm_auth.name,
                            description=orm_auth.description,
                            deactivated_at= orm_auth.deactivated_at,
                            created_at = orm_auth.created_at,
                            updated_at= orm_auth.updated_at,
                            deactivate= orm_auth.deactivate )


        return AuthGroup(id=orm_auth_by_name.id,
                            name=orm_auth_by_name.name,
                            description=orm_auth_by_name.description,
                            deactivated_at= orm_auth_by_name.deactivated_at,
                            created_at = orm_auth_by_name.created_at,
                            updated_at= orm_auth_by_name.updated_at,
                            deactivate= orm_auth_by_name.deactivate )


    async def get_auth_groups(self) -> List[AuthGroup]:
        orm_auths = await self.auth_repository.get_auth_groups()
        auth_groups = []
        for orm_auth in orm_auths:

            auth_groups.append(
                AuthGroup(id=orm_auth.id,
                        name=orm_auth.name,
                        description=orm_auth.description,
                        deactivated_at= orm_auth.deactivated_at,
                        created_at = orm_auth.created_at,
                        updated_at= orm_auth.updated_at,
                        deactivate= orm_auth.deactivate ))
        return auth_groups


    async def get_auth_group(self, auth_id: int) -> AuthGroup:
        orm_auth = await self.auth_repository.get_auth_group(auth_id)
        if orm_auth:
            return AuthGroup(id=orm_auth.id,
                            name=orm_auth.name,
                            description=orm_auth.description,
                            deactivated_at= orm_auth.deactivated_at,
                            created_at = orm_auth.created_at,
                            updated_at= orm_auth.updated_at,
                            deactivate= orm_auth.deactivate )
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail= self.detail
            )


    async def update_auth_group(self, auth_id:int, name:str, description:str, deactivate:bool)->AuthGroup:
        orm_auth = await self.auth_repository.get_auth_group(auth_id)
        if orm_auth:
            orm_auth.name  = name if orm_auth.name != name else orm_auth.name
            orm_auth.description  = description if orm_auth.description != name else orm_auth.description
            orm_auth.deactivate  = name if orm_auth.deactivate != deactivate else orm_auth.deactivate

            self.db_session.commit()
            self.db_session.refresh(orm_auth)
            return AuthGroup(id=orm_auth.id,
                        name=orm_auth.name,
                        description=orm_auth.description,
                        deactivated_at= orm_auth.deactivated_at,
                        created_at = orm_auth.created_at,
                        updated_at= orm_auth.updated_at,
                        deactivate= orm_auth.deactivate )
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail= self.detail
            )
    
    async def delete_auth_group(self, auth_id)->AuthGroup:
        orm_auth = await self.auth_repository.delete_auth_group(auth_id)
        return AuthGroup(id=orm_auth.id,
                        name=orm_auth.name,
                        description=orm_auth.description,
                        deactivated_at= orm_auth.deactivated_at,
                        created_at = orm_auth.created_at,
                        updated_at= orm_auth.updated_at,
                        deactivate= orm_auth.deactivate )




# app/interface_adapters/gateways/db_gateway.py
from typing import List
from sqlalchemy.orm import Session
from App.core.entities.usersEntities import Users, CreateUser, UserGroup


from App.infrastructure.models.usersModel import User as ORMUser
from App.infrastructure.services.usersServices import UserRepository
from App.infrastructure.services.authService import AuthService





class UserGateway:
    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.repository = UserRepository(self.db_session)
        self.authrepository = AuthService(self.db_session)
        
    async def create_user(self,  name: str, email: str, username:str, cellphone: str, password:str, group_id:int) -> CreateUser:
        orm_user = await self.repository.create_user(name, email, username, cellphone, password)
        response = {}
        if group_id not in  [None, 0]:
            user_id = orm_user.id
            
            group = await self.repository.agg_user_group(user_id, group_id)
            if group:
                data = await self.authrepository.get_auth_group(group_id)
                response = UserGroup(
                    group_id=data.id,
                    name= data.name
                )
                
        return CreateUser(id=orm_user.id, name=orm_user.name, email=orm_user.email, username= orm_user.users, 
                          cellphone= orm_user.cellphone, password=orm_user.password)
    

    async def get_users(self, skip: int, limit: int) -> List[Users]:
        orm_users = await self.repository.get_users(skip, limit)
        users = []
        for orm_user in orm_users:
            users.append(Users(id=orm_user.id, name=orm_user.name, email=orm_user.email,password=orm_user.password,cellphone=orm_user.cellphone, is_admin=orm_user.is_admin, is_staff=orm_user.is_staff ))
        return users
    
    async def get_user(self, user_id: int) -> Users:
        orm_user = await self.repository.get_user(user_id)
        if orm_user:
            return Users(id=orm_user.id, name=orm_user.name, email=orm_user.email,password=orm_user.password,cellphone=orm_user.cellphone, is_admin=orm_user.is_admin, is_staff=orm_user.is_staff )
        return None
    
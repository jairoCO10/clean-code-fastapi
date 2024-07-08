from sqlalchemy.orm import Session
from App.infrastructure.models.usersModel import User as ORMUser
from sqlalchemy.future import select
from typing import List
from App.entrypoints.schemas.userSchema import Login
from App.infrastructure.models.authGroupModel import AuthGroup as ORMAuthgroup


class AuthService:
    def __init__(self, db:Session):
        self.connection = db


    
    def login(self, user:Login)-> ORMUser:
        result = self.connection.execute(select(ORMUser).filter(ORMUser.users== user.username))
        return result.scalar_one_or_none()
    

    async def get_auth_groups(self) -> List[ORMAuthgroup]:
        result = self.connection.execute(select(ORMAuthgroup).filter(ORMAuthgroup.deactivate == False))
        orm_auth_groups = result.scalars().all()
        
        # Debugging output to check the fetched results
        for orm_auth in orm_auth_groups:
            print(f"Fetched auth group: {orm_auth}")
        
        return orm_auth_groups
    

    async def get_auth_group(self, user_id: int) -> ORMAuthgroup:
        result = self.connection.execute(select(ORMAuthgroup).filter(ORMAuthgroup.id == user_id))
        return result.scalars().first()
    
    async def get_auth_group_name(self, name: str) -> ORMAuthgroup:
        result = self.connection.execute(select(ORMAuthgroup).filter(ORMAuthgroup.name == name))
        return result.scalars().first()
    
    async def create_auth_group(self, name:str, description:str)->ORMAuthgroup:
        auth_group = ORMAuthgroup(
            name=name,
            description=description,
            deactivate = False
        )
        self.connection.add(auth_group)
        self.connection.commit()
        self.connection.refresh(auth_group)
        return auth_group
    
    async def update_auth_group(self, user_id: int, name: str, email: str) -> ORMUser:
        user = await self.get_user(user_id)
        if user:
            user.name = name
            user.email = email
            self.db.commit()
            self.db.refresh(user)
        return user
    
    

    
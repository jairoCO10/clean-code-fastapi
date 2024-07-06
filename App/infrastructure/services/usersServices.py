from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from App.infrastructure.models.usersModel import User as ORMUser
import bcrypt  


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    username:str
    async def create_user(self, name: str, email: str, username:str, cellphone:str, password:str) -> ORMUser:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = ORMUser(name=name, email=email, users=username, cellphone =cellphone,  password = hashed_password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    async def get_user(self, user_id: int) -> ORMUser:
        result = self.db.execute(select(ORMUser).filter(ORMUser.id == user_id))
        return result.scalars().first()

    async def get_users(self, skip: int, limit: int) -> List[ORMUser]:
        result = self.db.execute(select(ORMUser).offset(skip).limit(limit))
        return result.scalars().all()

    async def update_user(self, user_id: int, name: str, email: str) -> ORMUser:
        user = await self.get_user(user_id)
        if user:
            user.name = name
            user.email = email
            self.db.commit()
            self.db.refresh(user)
        return user

    async def delete_user(self, user_id: int) -> ORMUser:
        user = await self.get_user(user_id)
        if user:
            self.db.delete(user)
            self.db.commit()
        return user
    
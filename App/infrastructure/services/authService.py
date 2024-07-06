from sqlalchemy.orm import Session
from App.infrastructure.models.usersModel import User as ORMUser
from sqlalchemy.future import select
from App.entrypoints.schemas.userSchema import Login


class AuthService:
    def __init__(self, db:Session) -> None:
        self.connection = db


    
    def login(self, user:Login)-> ORMUser:
        result = self.connection.execute(select(ORMUser).filter(ORMUser.users== user.username))
        return result.scalar_one_or_none()
    
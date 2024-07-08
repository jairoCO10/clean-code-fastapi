# app/entrypoints/api/schemas.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class UserBase(BaseModel):
    name: str
    email: str
    
class AuthToken(BaseModel):
    access_token: str
    token_type:str


class Login(BaseModel):
    username:str 
    password:str


class CreateUser(UserBase):
    username:str
    cellphone: str
    password: str



class UserRead(UserBase):
    id: int
    cellphone: str
    is_admin: bool
    is_staff: bool
    password:str

    class Config:
        from_attributes = True

    
class AuthGroupRead(BaseModel):
    id: int
    name: str
    description: str
    # deactivated_at: Optional[datetime]
    deactivate: Optional[bool]
    created_at: datetime
    # updated_at: Optional[datetime]
    class Config:
        from_attributes = True


class CreateAuthGroup(BaseModel):
    name: str
    description: Optional[str]



class UpdateAuthGroup(BaseModel):
    name: Optional[str]
    description: Optional[str]
    deactivate: Optional[bool]


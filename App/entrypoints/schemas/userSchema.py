# app/entrypoints/api/schemas.py
from pydantic import BaseModel
from typing import List, Optional


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


from dataclasses import dataclass
from typing import List
from datetime import datetime



@dataclass
class Users:
    id: int
    name: str
    email: str
    password: str
    cellphone: str
    is_admin: bool
    is_staff: bool


@dataclass
class UserGroup:
    group_id:str
    name:str


@dataclass
class CreateUser:
    id:str
    name: str
    email: str
    username:str
    cellphone: str
    password: str



@dataclass
class AuthToken:
    access_token: str
    token_type:str





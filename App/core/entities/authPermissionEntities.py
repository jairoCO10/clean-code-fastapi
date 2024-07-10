from dataclasses import dataclass
from typing import List, Optional

@dataclass
class AuthPermissions:
    id: int
    name: str
    content_type_id:int
    codename:str

@dataclass
class AuthPermissions2:
    id: int
    name: str
    content_type_id:int
    codename:str
    status_permission:bool


@dataclass
class ContentType:
    id:int
    app_label:str
    model:str
    permission:List[AuthPermissions2]



@dataclass
class CreateAuthPermissions:
    name:str
    content_type_id:int

@dataclass
class UserPermission:
    id:int
    name:str
    content_type:List[ContentType]

@dataclass
class GroupPermission:
    id:int
    name:str
    content_type:List[ContentType]


    # permissions:List[AuthPermissions]






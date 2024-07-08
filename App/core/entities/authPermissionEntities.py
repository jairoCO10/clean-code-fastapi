from dataclasses import dataclass


@dataclass
class AuthPermissions:
    id: int
    name: str
    content_type_id:int
    codename:str


@dataclass
class CreateAuthPermissions:
    name:str
    content_type_id:int



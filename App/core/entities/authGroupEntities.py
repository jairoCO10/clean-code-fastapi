from dataclasses import dataclass
from typing import List
from datetime import datetime



@dataclass
class AuthGroup:
    id: int
    name: str
    description: str
    deactivated_at: datetime
    deactivate: bool
    created_at: datetime
    updated_at: datetime

@dataclass
class CreateAuthGroup:
    name:str
    description:str
    


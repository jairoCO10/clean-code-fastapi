# app/interface_adapters/controllers/user_controller.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from App.entrypoints.schemas.userSchema import CreateUser, UserRead
from App.infrastructure.database import Connect
from App.interface_adapters.gateways.usersGateways import UserGateway
from App.core.usecases.usersCases import UserUseCase
from App.interface_adapters.dependencies import  jwt

router = APIRouter()

@router.post("/users/", response_model=UserRead)
async def create_user(user: CreateUser, db: Session = Depends(Connect.get_db)):
    user_gateway = UserGateway(db)
    user_usecase = UserUseCase(user_gateway)
    return await user_usecase.create_user(user.name, user.email, user.username, user.cellphone, user.password)



@router.get("/users/", response_model=List[UserRead])
async def read_users(skip: int = 0, limit: int = 10,  db: Session = Depends(Connect.get_db),  current_user: UserRead = Depends(jwt.get_current_user)):
    user_gateway = UserGateway(db)
    user_usecase = UserUseCase(user_gateway)
    return await user_usecase.get_users(skip, limit)

@router.get("/user/{iduser}")
async def read_user(iduser:str, db:Session= Depends(Connect.get_db),  current_user: UserRead = Depends(jwt.get_current_user)):
    user_gateway = UserGateway(db)
    user_usercase = UserUseCase(user_gateway)
    user = await user_usercase.get_user(iduser)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

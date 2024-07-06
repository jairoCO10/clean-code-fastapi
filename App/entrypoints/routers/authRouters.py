from typing import List
from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from App.entrypoints.schemas.userSchema import Login, AuthToken
from App.infrastructure.database import Connect
from App.interface_adapters.controllers.authController import AuthController


router = APIRouter(prefix='/web', tags=['AUTH'])


@router.post('/login',response_model= AuthToken,  status_code=status.HTTP_200_OK)
async def login(user: Login, db:Session=Depends(Connect.get_db)):
    auth_token = AuthController(db)
    response = await auth_token.auth_login(user)
    return response
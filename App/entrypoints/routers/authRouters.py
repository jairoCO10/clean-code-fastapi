from typing import List
from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from App.entrypoints.schemas.userSchema import Login, AuthToken, AuthGroupRead, CreateAuthGroup, UpdateAuthGroup
from App.infrastructure.database import Connect
from App.interface_adapters.controllers.authController import AuthController
from App.interface_adapters.gateways.authGroupGateways import AuthGroupGateway
from App.core.usecases.authgroupCases import AuthGroupUseCase

router = APIRouter()


@router.post('/login',response_model= AuthToken,  status_code=status.HTTP_200_OK)
async def login(user: Login, db:Session=Depends(Connect.get_db)):
    auth_token = AuthController(db)
    response = await auth_token.auth_login(user)
    return response



@router.get("/authgroups", response_model=List[AuthGroupRead], status_code=status.HTTP_200_OK)
async def read_auth_groups(db:Session= Depends(Connect.get_db)):
    authgroup_gateway =  AuthGroupGateway(db)
    authgroup_usecase= AuthGroupUseCase(authgroup_gateway)
    return await authgroup_usecase.get_auth_groups()


@router.get("/authgroup/{id}", response_model=AuthGroupRead, status_code=status.HTTP_200_OK)
async def read_auth_groups(id:int, db:Session= Depends(Connect.get_db)):
    authgroup_gateway =  AuthGroupGateway(db)
    authgroup_usecase= AuthGroupUseCase(authgroup_gateway)
    return await authgroup_usecase.get_auth_group(id)



@router.post("/authgroups/", response_model=AuthGroupRead, status_code=status.HTTP_200_OK)
async def create_auth_group(auth_group:CreateAuthGroup, db:Session= Depends(Connect.get_db)):
    authgroup_gateway =  AuthGroupGateway(db)
    authgroup_usecase= AuthGroupUseCase(authgroup_gateway)
    return await authgroup_usecase.create_auth_group(auth_group.name, auth_group.description)



@router.put("/authgroup/{id}", response_model=AuthGroupRead, status_code=status.HTTP_200_OK)
async def update_auth_group(id:int, auth_group:UpdateAuthGroup, db:Session= Depends(Connect.get_db)):
    authgroup_gateway =  AuthGroupGateway(db)
    authgroup_usecase= AuthGroupUseCase(authgroup_gateway)
    return await authgroup_usecase.update_auth_group(id, auth_group.name, auth_group.description, auth_group.deactivate)




@router.delete("/authgroup/{id}", status_code=status.HTTP_200_OK)
async def update_auth_group(id:int, db:Session= Depends(Connect.get_db)):
    authgroup_gateway =  AuthGroupGateway(db)
    authgroup_usecase= AuthGroupUseCase(authgroup_gateway)
    return await authgroup_usecase.delete_auth_group(id)







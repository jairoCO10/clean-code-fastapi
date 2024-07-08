from typing import List
from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from App.entrypoints.schemas.userSchema import Login, AuthToken, AuthGroupRead, CreateAuthGroup, UpdateAuthGroup
from App.infrastructure.database import Connect
from App.interface_adapters.controllers.authController import AuthController
from App.interface_adapters.gateways.authGroupGateways import AuthGroupGateway
from App.core.usecases.authgroupCases import AuthGroupUseCase
from App.core.usecases.authPermissionCases import AuthPermissionUseCase
from App.interface_adapters.gateways.authPermissionsGateway import AuthPermissionGateway


router = APIRouter()

@router.get("/authpermissions", status_code=status.HTTP_200_OK)
async def read_auth_permissions(db:Session= Depends(Connect.get_db)):
    authpermissions_gateway =  AuthPermissionGateway(db)
    authpermission_usecase= AuthPermissionUseCase(authpermissions_gateway)
    return await authpermission_usecase.read_auth_permissions()


@router.get("/authpermission/{id}", status_code=status.HTTP_200_OK)
async def read_auth_permission(id:int, db:Session= Depends(Connect.get_db)):
    authpermissions_gateway =  AuthPermissionGateway(db)
    authpermission_usecase= AuthPermissionUseCase(authpermissions_gateway)
    return await authpermission_usecase.read_auth_permission(id)



# @router.post("/authpermissions/", response_model=AuthGroupRead, status_code=status.HTTP_200_OK)
# async def create_auth_permission(auth_group:CreateAuthGroup, db:Session= Depends(Connect.get_db)):
#     authgroup_gateway =  AuthGroupGateway(db)
#     authgroup_usecase= AuthGroupUseCase(authgroup_gateway)
#     return await authgroup_usecase.create_auth_permission(auth_group.name, auth_group.description)







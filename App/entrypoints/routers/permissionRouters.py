from typing import List
from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from App.infrastructure.database import Connect
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

@router.get("/userpermision/{users_id}", status_code=status.HTTP_200_OK)
async def read_user_permission(users_id:int, db:Session=Depends(Connect.get_db)):
    authpermissions_gateway =  AuthPermissionGateway(db)
    authpermission_usecase= AuthPermissionUseCase(authpermissions_gateway)
    return await authpermission_usecase.read_user_permissions(users_id)


@router.get("/grouppermision/{group_id}", status_code=status.HTTP_200_OK)
async def read_group_permission(group_id:int, db:Session=Depends(Connect.get_db)):
    authpermissions_gateway =  AuthPermissionGateway(db)
    authpermission_usecase= AuthPermissionUseCase(authpermissions_gateway)
    return await authpermission_usecase.read_group_permissions(group_id)



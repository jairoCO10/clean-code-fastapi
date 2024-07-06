# app/entrypoints/api/main.py
from fastapi import FastAPI
from App.infrastructure.database import Connection
from App.entrypoints.routers import authRouters
from App.entrypoints.routers import usersRouters
# from app.entrypoints.api.middleware import ErrorHandlerMiddleware
# from app.interface_adapters.controllers import task_controller
# from app.interface_adapters.controllers import user_controller
import os

Connection.Base.metadata.create_all(bind=Connection.engine)

version = f"{os.getenv('VERSION')} - {os.getenv('ENVIRONMENT')}"
title= "Clean Architecture"
description="This is a custom API built with FastAPI."


app = FastAPI(
    title=title,
    description=description,
    version=version
    
)

# Registra el middleware de manejo de errores
# app.add_middleware(ErrorHandlerMiddleware)



app.include_router(authRouters.router, prefix="/api/login", tags=["AUTH"])
app.include_router(usersRouters.router, prefix="/api/v1/users", tags=["users"])


# app/entrypoints/api/main.py
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from App.infrastructure.database import Connection
from App.entrypoints.routers import authRouters
from App.entrypoints.routers import usersRouters
from App.entrypoints.routers import permissionRouters
from fastapi.exceptions import RequestValidationError, HTTPException
import os
import logging
from App.entrypoints.api.logging_config import initialize_logger  # Import the logging setup function
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path



Connection.Base.metadata.create_all(bind=Connection.engine)

# Initialize the logger
logger = initialize_logger()



version = f"{os.getenv('VERSION')} - {os.getenv('ENVIRONMENT')}"
title= "Clean Architecture"
description="This is a custom API built with FastAPI."


app = FastAPI(
    title=title,
    description=description,
    version=version
    
)
# Montar archivos estáticos
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")


origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Configurar GZipMiddleware con un tamaño mínimo de 100 MB para comprimir respuestas
app.add_middleware(GZipMiddleware, minimum_size=1000000)
app.max_request_size = 100000000  # 100 MB en bytes

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        errors.append( 
            {
                "loc": error["loc"],
                "msg": error["msg"],
                "type": error["type"],
            }
        )
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content={"detail": errors})


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"details": exc.detail})

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    # Log detailed error information for debugging
    logger.error(f"Unexpected error occurred: {exc}", exc_info=True)

    return JSONResponse(
        status_code=500,
        content={
            "detail": "An unexpected error has occurred. Please try again later.",
            "error": str(exc)  # Include the exception message for debugging purposes
        }
    )

# Servir archivo HTML de bienvenida
@app.get("/", response_class=HTMLResponse)
async def get_index():
    html_content = Path("frontend/templates/index.html").read_text()
    return HTMLResponse(content=html_content)

@app.get("/login", response_class=HTMLResponse)
async def get_login():
    html_content = Path("frontend/templates/login.html").read_text(encoding="utf-8")
    return HTMLResponse(content=html_content)

@app.get("/home", response_class=HTMLResponse)
async def get_login():
    html_content = Path("frontend/templates/home.html").read_text(encoding="utf-8")
    return HTMLResponse(content=html_content)



app.include_router(authRouters.router, prefix="/api/auth", tags=["AUTH"])
app.include_router(usersRouters.router, prefix="/api/v1/users", tags=["users"])
app.include_router(permissionRouters.router, prefix="/api/v1/permissions", tags=["permission"])


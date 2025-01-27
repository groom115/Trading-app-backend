from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import create_app
from app.routes import auth_routes, file_routes, random_number_routes
from app.core.db import engine
from app.models.user_model import Base 
from app.models.random_number_model import Base
from app.services.random_number_service import start_random_number_generator

app = create_app()
Base.metadata.create_all(bind=engine)

start_random_number_generator()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_routes.router, prefix="/auth", tags=["Authentication"])
app.include_router(file_routes.router, prefix="/table", tags=["File"])
app.include_router(random_number_routes.router, prefix="/numbers", tags=["Numbers"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Backend!"}

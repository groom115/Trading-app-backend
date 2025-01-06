# app/main.py
from fastapi import FastAPI
# from app.routes import user_routes

app = FastAPI()

# Registering the routes
# app.include_router(user_routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Backend!"}

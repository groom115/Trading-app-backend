from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from app.services.auth_service import signup_user, login_user, verify_token
from app.models.user_model import SignupRequest, LoginRequest
from sqlalchemy.orm import Session
from app.core.db import get_db

router = APIRouter()



@router.post("/signup")
def signup(request: SignupRequest, db: Session = Depends(get_db)):
    if not request.email or not request.password:
        raise HTTPException(status_code=400, detail="Email and password are required.")
    return signup_user(request, db)

@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    if not request.email or not request.password:
        raise HTTPException(status_code=400, detail="Email and password are required.")
    return login_user(request, db)

@router.get("/verify")
def verify(token: str):
    return verify_token(token)
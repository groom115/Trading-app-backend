from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, EmailStr


Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    
    user_id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    token = Column(String)


class SignupRequest(BaseModel):
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str

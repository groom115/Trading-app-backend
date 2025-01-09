from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.models.user_model import SignupRequest, User, LoginRequest
from app.core.db import get_db
from jose import jwt, JWTError
from fastapi import HTTPException
from app.core.db import get_db
import uuid

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def signup_user(request: SignupRequest, db: Session):

    user_id = str(uuid.uuid4())
    token = create_access_token({"sub": user_id})
    password_hash = request.password
    new_user = User(user_id=user_id, email=request.email, password_hash=password_hash, token=token)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"user_id": new_user.user_id, "email": new_user.email, "access_token": token, "token_type": "bearer"}


def login_user(request: LoginRequest, db: Session):

    user = db.query(User).filter(User.email == request.email).first()
    
    if user is None:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    if request.password != user.password_hash:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    token = create_access_token({"sub": user.user_id})

    return {"user_id": user.user_id, "email": user.email, "access_token": token, "token_type": "bearer"}


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if not email:
            raise HTTPException(status_code=401, detail="Invalid token")
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT user_id FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        if not user:
            raise HTTPException(status_code=401, detail="User not found")
        return {"user_id": user[0]}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import HTTPException
# from app.core.db import get_db
import uuid

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# def verify_token(token: str):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         email = payload.get("sub")
#         if not email:
#             raise HTTPException(status_code=401, detail="Invalid token")
#         db = get_db()
#         cursor = db.cursor()
#         cursor.execute("SELECT user_id FROM users WHERE email = ?", (email,))
#         user = cursor.fetchone()
#         if not user:
#             raise HTTPException(status_code=401, detail="User not found")
#         return {"user_id": user[0]}
#     except JWTError:
#         raise HTTPException(status_code=401, detail="Invalid token")

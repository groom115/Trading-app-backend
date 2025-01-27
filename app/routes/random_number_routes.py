from fastapi import APIRouter, FastAPI, Depends
import asyncio
from sqlalchemy.orm import Session
from app.services.random_number_service import (
    add_random_number,
    get_latest_random_numbers,
)
from app.core.db import get_db

router = APIRouter()

@router.post("/")
def add_random_numbers(db: Session = Depends(get_db)):
    random_numbers = add_random_number(db)
    return {"random_numbers": random_numbers}


@router.get("/")
def get_random_numbers(db: Session = Depends(get_db)):
    random_numbers = get_latest_random_numbers(db)
    return {"random_numbers": random_numbers}


from fastapi import APIRouter, FastAPI, Depends
import asyncio
from sqlalchemy.orm import Session
from app.services.random_number_service import (
    add_random_number,
    get_latest_random_numbers,
)
from app.core.db import get_db
from app.models.random_number_model import RandomNumber
router = APIRouter()

@router.post("/")
def add_random_numbers(db: Session = Depends(get_db)):
    random_numbers = add_random_number(db)
    return {"random_numbers": random_numbers}


@router.get("/")
def get_random_numbers(db: Session = Depends(get_db)):
    random_numbers = get_latest_random_numbers(db)
    return {"random_numbers": random_numbers}

@router.delete("/")
def delete_large_numbers(db: Session = Depends(get_db)):
    try:
        
        large_numbers = db.query(RandomNumber).filter(RandomNumber.number > 1000000)
        count = large_numbers.count()
        if count == 0:
            return {"message": "No numbers greater than 1000000 found."}

        large_numbers.delete(synchronize_session=False)
        db.commit()

        return {"message": f"Successfully deleted {count} numbers greater than 1000000."}
    except Exception as e:
        db.rollback()



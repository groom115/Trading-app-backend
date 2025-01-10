from fastapi import APIRouter, FastAPI, Depends
import asyncio
from sqlalchemy.orm import Session
from app.services.random_number_service import (
    add_random_number,
    get_latest_random_numbers,
    start_generating_random_numbers
)
from app.core.db import get_db
from contextlib import asynccontextmanager


router = APIRouter()

@asynccontextmanager
async def lifespan():
    print("Starting random number generator...")

    # Get a database session and start generating random numbers
    db_session = next(get_db())
    task = asyncio.create_task(start_generating_random_numbers(db_session))

    # yield

    # print("Stopping random number generator...")
    # task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Random number generator stopped.")

@router.post("/")
def add_random_numbers(db: Session = Depends(get_db)):
    random_numbers = add_random_number(db)
    return {"random_numbers": random_numbers}


@router.get("/")
def get_random_numbers(db: Session = Depends(get_db)):
    random_numbers = get_latest_random_numbers(db)
    return {"random_numbers": random_numbers}


from datetime import datetime
import random
import asyncio
from sqlalchemy.orm import Session
from app.models.random_number_model import RandomNumber  # Import your RandomNumber model

def add_random_number(db: Session):
  
    random_number = random.randint(1, 1000)
    timestamp = datetime.now()
    new_random_number = RandomNumber(timestamp=timestamp, number=random_number)
    db.add(new_random_number)
    db.commit()


async def start_generating_random_numbers(db: Session):
    """Generate a random number and store it in the database every second."""
    while True:
        print('okayiiish')
        random_number = random.randint(1, 1000)
        timestamp = datetime.now()

        new_random_number = RandomNumber(timestamp=timestamp, number=random_number)
        db.add(new_random_number)
        db.commit()
        await asyncio.sleep(1)

        

def get_latest_random_numbers(db: Session):
    latest_random_numbers = db.query(RandomNumber).order_by(RandomNumber.timestamp.desc()).limit(50).all()
    return latest_random_numbers

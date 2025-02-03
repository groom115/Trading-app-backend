from datetime import datetime
import random
import asyncio
from sqlalchemy.orm import Session
from app.models.random_number_model import RandomNumber  # Import your RandomNumber model
from app.core.db import get_db
import threading
import time

def add_random_number(db: Session):
    
    print('called')
    random_number = random.randint(1, 1000000)
    timestamp = datetime.now()
    new_random_number = RandomNumber(timestamp=timestamp, number=random_number)
    db.add(new_random_number)
    db.commit()


def generate_random_numbers_continuously():
    db = next(get_db())
    while True:
        add_random_number(db)
        time.sleep(10)

def start_random_number_generator():
    thread = threading.Thread(target=generate_random_numbers_continuously, daemon=True)
    thread.start()
        

def get_latest_random_numbers(db: Session):
    latest_random_numbers = db.query(RandomNumber).order_by(RandomNumber.timestamp.desc()).all()
    return latest_random_numbers

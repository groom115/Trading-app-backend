import csv
import os
from threading import Lock
from fastapi import HTTPException
from app.models.file_model import File
import shutil
from dotenv import load_dotenv

lock = Lock()

load_dotenv()


CSV_FILE = os.getenv("CSV_FILE", "default_table.csv")
BACKUP_FILE = os.getenv("BACKUP_FILE", "default_backup.csv")


def fetch_csv():
    if not os.path.exists(CSV_FILE):
        return []
    with open(CSV_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

def add_csv_row(row: File):
    with lock:
        backup_csv()
        row_dict = row.model_dump() 
        fieldnames = row_dict.keys()
        file_exists = os.path.exists(CSV_FILE)
        with open(CSV_FILE, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow(row_dict)
        return {"message": "Row added successfully."}

def update_csv_row(row_id: int, row: File):
    with lock:
        backup_csv()
        rows = fetch_csv()
        if row_id < 1 or row_id > len(rows):
            raise HTTPException(status_code=404, detail="Row not found.")
        rows[row_id - 1].update(row.model_dump())
        with open(CSV_FILE, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
        return {"message": "Row updated successfully."}


def delete_csv_row(row_id: int):
    with lock:
        backup_csv()
        rows = fetch_csv()
        if row_id < 1 or row_id > len(rows):
            return {"message": "Invalid row index."}
        rows.pop(row_id-1)
        with open(CSV_FILE, mode="w", newline="") as file:
            if rows:
                writer = csv.DictWriter(file, fieldnames=rows[0].keys())
                writer.writeheader()
                writer.writerows(rows)
            else:
                file.truncate(0)
        return {"message": f"Row at index {row_id} deleted successfully."}


def restore_csv():
    with lock:
        if not os.path.exists(BACKUP_FILE):
            return []
        if os.path.exists(CSV_FILE):
            shutil.copy(BACKUP_FILE, CSV_FILE)
        with open(BACKUP_FILE, mode="r") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

def backup_csv():
    if os.path.exists(CSV_FILE):
        shutil.copy(CSV_FILE, BACKUP_FILE)

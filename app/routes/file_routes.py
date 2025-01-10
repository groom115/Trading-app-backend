
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.services.file_services import fetch_csv, add_csv_row, update_csv_row, delete_csv_row, restore_csv
from app.models.file_model import File

router = APIRouter()

@router.get("/", response_model=List[File])
def fetch():
    return fetch_csv()

@router.post("/", response_model=dict)
def add(row: File):
    return add_csv_row(row)

@router.put("/")
def update(row_id: int, row: File):
    return update_csv_row(row_id, row)

@router.delete("/", response_model=dict)
def delete(row_id: int):
    return delete_csv_row(row_id)

@router.get("/restore", response_model=List[File])
def restore():
    return restore_csv()

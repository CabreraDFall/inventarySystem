from fastapi import APIRouter
from app import fake_data

router = APIRouter(prefix="/batches", tags=["Batches"]) 

@router.get("/")
def get_users():
    
    return fake_data["batches"]
# items.py
from fastapi import APIRouter
from app import fake_data

router = APIRouter(prefix="/users", tags=["Users"]) 

@router.get("/")
def get_users():
    
    return fake_data["users"]

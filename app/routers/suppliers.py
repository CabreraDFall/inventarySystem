from fastapi import APIRouter
from app import fake_data

router = APIRouter(prefix="/suppliers",tags=["Suppliers"])

@router.get("")
async def get_suppliers():
    return fake_data["suppliers"]
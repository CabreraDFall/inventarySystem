from fastapi import APIRouter
from app import fake_data

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.get("")
async def get_transactions():
    return fake_data["transactions"]
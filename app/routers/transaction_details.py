from fastapi import APIRouter
from app import fake_data

router = APIRouter(prefix="/transaction-details", tags=["Transaction details"])

@router.get("")
async def get_transaction_details():
    return fake_data["transaction_details"]
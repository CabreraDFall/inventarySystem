from fastapi import APIRouter
from app import fake_data

router = APIRouter(prefix="/stock-history", tags=["Stock history"])

@router.get("")
async def get_stock_history():
    return fake_data["stock_histories"]
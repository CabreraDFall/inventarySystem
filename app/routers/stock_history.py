from fastapi import APIRouter

router = APIRouter(prefix="/stock-history", tags=["Stock history"])

@router.get("")
async def get_stock_history():
    return "get_stock_history"
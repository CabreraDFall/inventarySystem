from fastapi import APIRouter

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.get("")
async def get_transactions():
    return "transactions"
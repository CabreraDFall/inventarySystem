from fastapi import APIRouter

router = APIRouter(prefix="/transaction-details", tags=["Transaction details"])

@router.get("")
async def get_transaction_details():
    return "transaction_details"
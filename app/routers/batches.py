from fastapi import APIRouter

router = APIRouter(prefix="/batches", tags=["Batches"])

@router.get("")
async def get_batches():
    return "batches"
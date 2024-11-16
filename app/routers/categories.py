from fastapi import APIRouter
from app import fake_data


router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("")
async def get_categories():
    return fake_data["categories"]